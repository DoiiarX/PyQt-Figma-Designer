from generator.core.base_generator import BaseGenerator
from generator.ui.frame_generator import FrameGenerator


class ButtonGenerator(BaseGenerator):
    handler_functions: list

    def __init__(self, figma_node, parent):
        super().__init__(figma_node, parent)
        self.handler_functions = []

    def generate_design(self):
        frame_name = FrameGenerator.get_current_frame(self).name
        handler_function_name = f'{self.name}_clicked'
        handler_class_name = f'{frame_name}Handler'
        yield from f"""
{self.name} = QPushButton(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setFlat(True)
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
def __{handler_function_name}(self):
    try : 
        GuiHandler.{handler_class_name}.{handler_function_name}()
    except :
        print("No function {handler_function_name} defined")
{self.name}.clicked.connect(__{handler_function_name})
{self.name}.setFocusPolicy(Qt.NoFocus)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")""".splitlines()

        self.handler_functions.append(f"""
@classmethod
def {handler_function_name}(cls) : 
    print("Button {self.name} clicked")""")
        yield from f"""""".splitlines()
        yield from f"""
""".splitlines()

    def generate_handler(self):
        for fun in self.handler_functions:
            yield from fun.splitlines()
