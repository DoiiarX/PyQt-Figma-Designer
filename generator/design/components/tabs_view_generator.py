from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import indent


class TabsViewGenerator(DesignGenerator):
    handler_tab_changed_function_name: str
    controller_set_tab_function_name: str

    def __init__(self, fig_node, parent, group_generator: GroupGenerator):
        super().__init__(fig_node, parent)
        if len(group_generator.children) < 2:
            raise Exception(f'Tabs view {self.name} should have at least 2 children')

        tab_bar = group_generator.children[-1].children[0].children
        tabs_content = group_generator.children[-2].children[0].children
        self.tabs = list(reversed(list(zip(tab_bar, tabs_content))))

    def generate_design(self):
        self.handler_tab_changed_function_name = f'{self.name}_tab_changed'
        self.controller_set_tab_function_name = f'{self.name}_set_tab'
        for i, (_, _) in enumerate(self.tabs):
            yield f'def __select_tab_{i}(*args, **kwargs):'
            for j, (tab_bar_button, tab_content) in enumerate(self.tabs):
                yield from indent(VisibilityGenerator(tab_content).generate_set(str(i == j)), n=1)
                yield from indent(VisibilityGenerator(tab_bar_button).generate_set(str(i == j)), n=1)
            yield from f"""
    try :
        GuiHandler.{self.handler_class_path}.{self.handler_tab_changed_function_name}({i})
    except :
        print("No function {self.handler_tab_changed_function_name} defined. Tab = {i}")""".splitlines()

        yield from f"""
{self.name} = QLabel(central_widget)
""".splitlines()
        for i, (tab_bar_button, tab_content) in enumerate(self.tabs):
            button_name = f'{tab_bar_button.name}_button'
            yield from f"""
{button_name} = QPushButton(central_widget)
{button_name}.setGeometry({tab_bar_button.pyqt_bounds})
{button_name}.setFlat(True)
{button_name}.setObjectName("{button_name}")
{button_name}.setMouseTracking(True)
{button_name}.setContextMenuPolicy(Qt.NoContextMenu)
{button_name}.setAcceptDrops(False)
{button_name}.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
{button_name}.clicked.connect(__select_tab_{i})""".splitlines()
            yield from VisibilityGenerator(tab_content).generate_set(str(i == 0))
            yield from VisibilityGenerator(tab_bar_button).generate_set(str(i == 0))
