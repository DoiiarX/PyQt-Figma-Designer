from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator


class TextFieldGenerator(DesignGenerator):
    handler_function_name: str
    controller_function_name: str

    def generate_design(self):
        frame = FrameGenerator.get_current_frame(self)
        self.handler_function_name = f'{self.name}_text_changed'
        self.controller_function_name = f'{self.name}_set_text'

        yield from f"""
{self.name} = QLineEdit(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
{self.controller_function_name} = {self.name}.setText
try :
    GuiController.{frame.controller_class_name}.{self.controller_function_name} = {self.controller_function_name}
except :
    print("No function {self.controller_function_name} defined. Current text : " + {self.name}.text())

def __{self.name}_text_changed(self):
    try : 
        current_text = {self.name}.text()
        GuiHandler.{frame.handler_class_name}Handler.{self.handler_function_name}(current_text)
    except :
        print("No function {self.name}_clicked defined. Current text : " + current_text)

{self.name}.textChanged.connect(__{self.name}_text_changed)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 255); color: rgba(255, 255, 255, 255); ")""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.controller_function_name}(cls, text:str) :
    print("The function {self.controller_function_name} is unfortunately not linked. text : " + text)""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.handler_function_name}(cls, text:str) :
    print("Text field {self.name} text changed to text : " + text)""".splitlines()
