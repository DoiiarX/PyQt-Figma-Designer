from generator.core.base_generator import BaseGenerator
from generator.ui.frame_generator import FrameGenerator


class TextFieldGenerator(BaseGenerator):
    handler_functions: list
    controller_functions: list

    def __init__(self, figma_node, parent):
        super().__init__(figma_node, parent)
        self.handler_functions = []
        self.controller_functions = []

    def generate_design(self):

        handler_function_name = f'{self.name}_text_changed'
        controller_function_name = f'{self.name}_set_text'
        frame_name = FrameGenerator.get_current_frame(self).name

        yield from f"""
{self.name} = QLineEdit(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
{controller_function_name} = {self.name}.setText
try :
    GuiController.{frame_name}Controller.{controller_function_name} = {controller_function_name}
except :
    print("No function {controller_function_name} defined. Current text : " + {self.name}.text())

def __{self.name}_text_changed(self):
    try : 
        current_text = {self.name}.text()
        GuiHandler.{frame_name}Handler.{handler_function_name}(current_text)
    except :
        print("No function {self.name}_clicked defined. Current text : " + current_text)

{self.name}.textChanged.connect(__{self.name}_text_changed)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 255); color: rgba(255, 255, 255, 255); ")""".splitlines()

        self.controller_functions.append(f"""
@classmethod
def {controller_function_name}(cls, text:str) :
    print("The function {controller_function_name} is unfortunately not linked. text : " + text)""")

        self.handler_functions.append(f"""
@classmethod
def {handler_function_name}(cls, current_text:str) :
            print("Text field {self.name} text changed to " + current_text)""")

    def generate_handler(self):
        for fun in self.handler_functions:
            yield from fun.splitlines()

    def generate_controller(self):
        for fun in self.controller_functions:
            yield from fun.splitlines()
