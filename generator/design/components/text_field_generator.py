from generator.design.component_generator import ComponentGenerator
from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import generate_link_controller


class TextFieldGenerator(ComponentGenerator):
    handler_text_changed_function_name: str
    controller_set_text_function_name: str

    prefix_rule = 'text_field'

    def generate_design(self):
        self.handler_text_changed_function_name = f'{self.q_widget_name}_text_changed'
        self.controller_set_text_function_name = f'{self.q_widget_name}_set_text'

        yield from f"""
self.{self.q_widget_name} = QLineEdit(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setGeometry({self.pyqt_bounds})
self.{self.q_widget_name}.setAutoFillBackground(False)
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{self.q_widget_name}.setAcceptDrops(False)
self.{self.controller_set_text_function_name} = self.{self.q_widget_name}.setText

def __{self.handler_text_changed_function_name}(text):
    current_text = self.{self.q_widget_name}.text()
    try : 
        GuiHandler.{self.handler_class_path}.{self.handler_text_changed_function_name}(current_text)
    except NameError:
        print("No function {self.handler_text_changed_function_name} defined. Current text : " + current_text)
    except Exception as e:
        print("Caught exception while trying to call {self.handler_text_changed_function_name} : " + str(e))

self.{self.q_widget_name}.textChanged.connect(__{self.handler_text_changed_function_name})
self.{self.q_widget_name}.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 255); color: rgba(255, 255, 255, 255); ")""".splitlines()
        yield from generate_link_controller(self, f'self.{self.q_widget_name}.setText',
                                            self.controller_set_text_function_name)

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_text_changed_function_name}(cls, text:str) :
    print("Text field {self.handler_text_changed_function_name} text changed to text : " + text)""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_text_function_name}(cls, text:str):
    print("The function {self.controller_set_text_function_name} is unfortunately not linked to the controller")""".splitlines()
