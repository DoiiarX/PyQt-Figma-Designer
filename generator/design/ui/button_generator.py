from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator


class ButtonGenerator(DesignGenerator):
    handler_function_name: str

    def generate_design(self):
        frame = FrameGenerator.get_current_frame(self)
        self.handler_function_name = f'{self.name}_clicked'
        yield from f"""
{self.name} = QPushButton(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setFlat(True)
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
def __{self.handler_function_name}(self):
    try : 
        GuiHandler.{frame.handler_class_name}.{self.handler_function_name}()
    except :
        print("No function {self.handler_function_name} defined")
{self.name}.clicked.connect(__{self.handler_function_name})
{self.name}.setFocusPolicy(Qt.NoFocus)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_function_name}(cls) : 
    print("Button {self.name} clicked")""".splitlines()
