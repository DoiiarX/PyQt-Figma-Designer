from generator.core.base_generator import BaseGenerator
from generator.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.ui.frame_generator import FrameGenerator
from utils import indent


class CheckboxGenerator(BaseGenerator):

    def __init__(self, fig_node, parent, group_generator: GroupGenerator):
        super().__init__(fig_node, parent)
        self.handler_functions = []
        self.hide_show_checked_generator = VisibilityGenerator(group_generator)

    def generate_design(self):
        handler_function_name = f'{self.name}_check_changed'
        frame_name = FrameGenerator.get_current_frame(self).name
        visible_get = self.hide_show_checked_generator.generate_get()

        yield from f"""
{self.name} = QPushButton(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setFlat(True)
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
{self.name}.setFocusPolicy(Qt.NoFocus)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        
def __{self.name}_check_changed():
    try :
        GuiHandler.{frame_name}Handler.{handler_function_name}({visible_get})""".splitlines()
        yield from indent(self.hide_show_checked_generator.generate_set(f'not {visible_get}'), n=2)
        yield from f"""
    except :
        print("No function {handler_function_name} defined. Checked = " + str({visible_get}))
{self.name}.clicked.connect(__{handler_function_name})""".splitlines()

        self.handler_functions.append(f"""
@classmethod
def {handler_function_name}(cls, checked:bool) :
    print("Checkbox {self.name} checked = " + str(checked))""")

    def generate_handler(self):
        for fun in self.handler_functions:
            yield from fun.splitlines()
