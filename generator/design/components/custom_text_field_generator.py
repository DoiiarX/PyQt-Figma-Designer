from generator.design.component_generator import ComponentGenerator
from generator.design.core.text_generator import TextGenerator
from generator.utils import generate_link_controller, indent, generate_activate_handler, generate_print


class CustomTextFieldGenerator(ComponentGenerator):
    handler_text_changed_function_name: str
    controller_set_text_function_name: str

    component_name = 'custom_text_field'
    component_config = {}

    def generate_design(self):
        text_field_text = self.group_generator.children[-1]
        while not isinstance(text_field_text, TextGenerator):
            text_field_text = text_field_text.children[-1]
        text_field_text = text_field_text

        text_field_hint = self.group_generator.children[-2]
        while not isinstance(text_field_hint, TextGenerator):
            text_field_hint = text_field_hint.children[-1]
        text_field_hint = text_field_hint

        text_field_bounds = self.group_generator.children[-3].pyqt_bounds

        self.handler_text_changed_function_name = f'{self.q_widget_name}_text_changed'
        self.controller_set_text_function_name = f'{self.q_widget_name}_set_text'

        yield from f"""
self.{self.q_widget_name} = QLineEdit(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setGeometry({text_field_bounds})
self.{self.q_widget_name}.setAutoFillBackground(False)
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{self.q_widget_name}.setAcceptDrops(False)
self.{self.q_widget_name}.setFont(self.{text_field_text.q_widget_name}.font())
text_color = self.{text_field_text.q_widget_name}.styleSheet().split("color: ")[1].split(";")[0]
self.{text_field_text.q_widget_name}.setStyleSheet("color: rgba(255, 255, 255, 0);")
self.{text_field_text.q_widget_name}.hide()
self.{self.q_widget_name}.setStyleSheet("color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")

def __{self.handler_text_changed_function_name}(*args, **kwargs):    
    if self.{self.q_widget_name}.text() == "" :
        self.{text_field_hint.q_widget_name}.show()
    else :
        self.{text_field_hint.q_widget_name}.hide()
        {text_field_text.controller_set_text_function_name}(self.{self.q_widget_name}.text())              
           
    current_text = self.{self.q_widget_name}.text()""".splitlines()
        yield from indent(generate_activate_handler(self, self.handler_text_changed_function_name, f'current_text'),
                          n=1)

        yield from f"""
__{self.handler_text_changed_function_name}()   
self.{self.q_widget_name}.textChanged.connect(__{self.handler_text_changed_function_name})""".splitlines()
        yield from generate_link_controller(self, f'self.{self.q_widget_name}.setText',
                                            self.controller_set_text_function_name)

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_text_changed_function_name}(cls, text:str) :
    {generate_print(f"'Text field {self.handler_text_changed_function_name} text changed to text : ' + text")}""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_text_function_name}(cls, text:str):
    {generate_print(f"'The function {self.controller_set_text_function_name} is unfortunately not linked to the controller'")}
    return ''""".splitlines()
