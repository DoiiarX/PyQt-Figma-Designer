from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.design.core.frame_generator import FrameGenerator
from utils import indent


class CheckboxGenerator(DesignGenerator):
    handler_function_name: str

    def __init__(self, fig_node, parent, group_generator: GroupGenerator):
        super().__init__(fig_node, parent)
        self.hide_show_checked_generator = VisibilityGenerator(group_generator)

    def generate_design(self):
        self.handler_function_name = f'{self.name}_check_changed'
        frame = FrameGenerator.get_current_frame(self)
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
        GuiHandler.{frame.handler_class_name}.{self.handler_function_name}({visible_get})""".splitlines()
        yield from indent(self.hide_show_checked_generator.generate_set(f'not {visible_get}'), n=2)
        yield from f"""
    except :
        print("No function {self.handler_function_name} defined. Checked = " + str({visible_get}))
{self.name}.clicked.connect(__{self.handler_function_name})""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_function_name}(cls, checked:bool) :
    print("Checkbox {self.name} checked = " + str(checked))""".splitlines()
