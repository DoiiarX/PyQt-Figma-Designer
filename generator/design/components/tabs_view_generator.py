from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import indent


class TabsViewGenerator(DesignGenerator):
    handler_tab_changed_function_name: str
    controller_set_tab_function_name: str

    def __init__(self, figma_node, parent, group_generator: GroupGenerator):
        super().__init__(figma_node, parent)
        if len(group_generator.children) < 2:
            raise Exception(f'Tabs view {self.q_widget_name} should have at least 2 children')

        tab_bar = group_generator.children[-1].children[0].children
        tabs_content = group_generator.children[-2].children[0].children
        self.tabs = list(reversed(list(zip(tab_bar, tabs_content))))

    def generate_design(self):
        self.handler_tab_changed_function_name = f'{self.q_widget_name}_tab_changed'
        self.controller_set_tab_function_name = f'{self.q_widget_name}_set_tab'

        yield f'def __select_tab(i):'
        for j, (tab_bar_button, tab_content) in enumerate(self.tabs):
            yield from indent(VisibilityGenerator(tab_content).generate_set(f'i == {j}'), n=1)
            yield from indent(VisibilityGenerator(tab_bar_button).generate_set(f'i == {j}'), n=1)
        yield from f"""
    try :
        GuiHandler.{self.handler_class_path}.{self.handler_tab_changed_function_name}(i)
    except NameError:
        print("No function {self.handler_tab_changed_function_name} defined. Tab = " + str(i))
    except Exception as e:
        print("Caught exception while trying to call {self.handler_tab_changed_function_name} : " + str(e))
""".splitlines()

        for i, (tab_bar_button, tab_content) in enumerate(self.tabs):
            yield f'__select_tab_{i} = lambda: __select_tab({i})'
        yield from f"""
self.{self.q_widget_name} = QLabel(self.{self.parent.q_widget_name})
""".splitlines()
        for i, (tab_bar_button, tab_content) in enumerate(self.tabs):
            button_name = f'{tab_bar_button.q_widget_name}_button'
            yield from f"""
{button_name} = QPushButton(self.{tab_bar_button.parent.q_widget_name})
{button_name}.setGeometry({tab_bar_button.pyqt_bounds})
{button_name}.setFlat(True)
{button_name}.setObjectName("{button_name}")
{button_name}.setMouseTracking(True)
{button_name}.setContextMenuPolicy(Qt.NoContextMenu)
{button_name}.setAcceptDrops(False)
{button_name}.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
{button_name}.clicked.connect(__select_tab_{i})
try :
    GuiController.{self.controller_class_path}.{self.controller_set_tab_function_name} = __select_tab
except NameError:
    print("No function {self.controller_set_tab_function_name} defined. Current tab : {i}")
except Exception as e:
    print("Caught exception while trying to set the function {self.controller_set_tab_function_name} : " + str(e))
""".splitlines()
            yield from VisibilityGenerator(tab_content).generate_set(str(i == 0))
            yield from VisibilityGenerator(tab_bar_button).generate_set(str(i == 0))

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_tab_changed_function_name}(cls, tab:int) :
    print("Tabs view {self.q_widget_name} tab changed to tab : " + str(tab))""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_tab_function_name}(cls, tab:int):
    print("The function {self.controller_set_tab_function_name} is unfortunately not linked to the controller")""".splitlines()
