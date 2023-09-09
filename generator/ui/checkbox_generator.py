from generator.core.base_generator import BaseGenerator
from generator.ui.frame_generator import FrameGenerator
from utils import indent


class CheckboxGenerator(BaseGenerator):
    checked_generator: 'BaseGenerator'

    def __init__(self, fig_node, parent, checked_generator: 'BaseGenerator'):
        super().__init__(fig_node, parent)
        self.checked_generator = checked_generator
        self.handler_functions = []

    def generate_recursive_hide_show(self, generator: 'BaseGenerator'):
        for child in generator.children:
            yield from self.generate_recursive_hide_show(child)
        yield f'{generator.name}.setVisible(not {generator.name}.isVisible())'

    def generate_design(self):
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
    try :""".splitlines()
        yield from indent(self.generate_recursive_hide_show(self.checked_generator), n=2)

        handler_function_name = f'{self.name}_check_changed'
        self.handler_functions.append(f"""
@classmethod
def {handler_function_name}(cls, checked:bool) :
    print("Checkbox {self.name} checked = " + str(checked))""")

        frame_name = FrameGenerator.get_current_frame(self).name
        yield from f"""
        GuiHandler.{frame_name}Handler.{handler_function_name}({self.checked_generator.name}.isVisible())
    except :
        print("No function {handler_function_name} defined. Checked = " + str({self.checked_generator.name}.isVisible()))
        {self.name}.clicked.connect(__{handler_function_name})""".splitlines()

    def generate_handler(self):
        for fun in self.handler_functions:
            yield from fun.splitlines()
