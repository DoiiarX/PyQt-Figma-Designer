from overrides import override

from config import text_scale, scale
from generator.python_generator.base_generator import BaseGenerator
from generator.python_generator.frame_generator import FrameGenerator


class TextFieldGenerator(BaseGenerator):
    handler_functions: list
    controller_functions: list

    def __init__(self, figma_node, start_coordinates, parent):
        super().__init__(figma_node, start_coordinates, parent)
        self.handler_functions = []
        self.controller_functions = []

    def generate_design(self):
        yield f'{self.name} = QLineEdit(central_widget)'
        yield f'{self.name}.setGeometry({self.pyqt_bounds})'
        yield f'{self.name}.setAutoFillBackground(False)'
        yield f'{self.name}.setObjectName("{self.name}")'
        yield f'{self.name}.setMouseTracking(True)'
        yield f'{self.name}.setContextMenuPolicy(Qt.NoContextMenu)'
        yield f'{self.name}.setAcceptDrops(False)'
        handler_function_name = f'{self.name}_text_changed'
        controller_function_name = f'{self.name}_set_text'
        frame_name = FrameGenerator.get_current_frame(self).name
        yield f'{controller_function_name} = {self.name}.setText'
        yield f'GuiController.{frame_name}Controller.{controller_function_name} = {controller_function_name}'
        self.controller_functions.append(f"""
@classmethod
def {controller_function_name}(cls, text:str) :
    print("The function {controller_function_name} is unfortunately not linked. text : " + text)""")
        self.handler_functions.append(f"""
@classmethod
def {handler_function_name}(cls, current_text:str) :
            print("Text field {self.name} text changed to " + current_text)""")
        yield from f"""def __{self.name}_text_changed(self):
    try : 
        current_text = {self.name}.text()
        GuiHandler.{frame_name}Handler.{handler_function_name}(current_text)
    except :
        print("No function {self.name}_clicked defined. Current text : " + current_text)""".splitlines()
        yield f'{self.name}.textChanged.connect(__{self.name}_text_changed)'
        yield (f'{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0); '
               # cursor color
               f'border: 0px solid rgba(255, 255, 255, 255);'
               f'color: rgba(255, 255, 255, 255); ")')

    def generate_handler(self):
        for fun in self.handler_functions:
            yield from fun.splitlines()

    def generate_controller(self):
        for fun in self.controller_functions:
            yield from fun.splitlines()
