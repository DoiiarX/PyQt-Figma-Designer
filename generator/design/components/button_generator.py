from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator


class ButtonGenerator(DesignGenerator):
    handler_click_function_name: str

    def generate_design(self):
        self.handler_click_function_name = f'{self.name}_clicked'
        yield from f"""
{self.name} = QPushButton(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setFlat(True)
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
def __{self.handler_click_function_name}(*args, **kwargs):
    try : 
        GuiHandler.{self.handler_class_path}.{self.handler_click_function_name}()
    except :
        print("No function {self.handler_click_function_name} defined")
{self.name}.clicked.connect(__{self.handler_click_function_name})
{self.name}.setFocusPolicy(Qt.NoFocus)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_click_function_name}(cls) : 
    print("Button {self.name} clicked")""".splitlines()
