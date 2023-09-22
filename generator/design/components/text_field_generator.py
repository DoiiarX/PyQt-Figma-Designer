from generator.design.component_generator import ComponentGenerator
from generator.utils import *


class TextFieldGenerator(ComponentGenerator):
    handler_text_changed_function_name: str
    controller_set_text_function_name: str

    component_name = 'text_field'
    component_config = {
        'text_color': "'rgba(255, 255, 255, 255)'",
        'hint': "''"
    }

    def generate_design(self):
        self.handler_text_changed_function_name = f'{self.q_widget_name}_text_changed'
        self.controller_set_text_function_name = f'{self.q_widget_name}_set_text'
        yield from generate_q_line_edit_create(self)
        yield from f"""def __{self.handler_text_changed_function_name}(text):
    current_text = self.{self.q_widget_name}.text()""".splitlines()
        yield from indent(generate_handler_call(self, self.handler_text_changed_function_name, 'current_text'))
        yield f'self.{self.q_widget_name}.textChanged.connect(__{self.handler_text_changed_function_name})'
        yield from generate_controller_setup(self, f'self.{self.q_widget_name}.setText',
                                             self.controller_set_text_function_name)

    def generate_handler(self):
        yield from generate_handler_function(self.handler_text_changed_function_name, 'text:str')

    def generate_controller(self):
        yield from generate_controller_function(self.controller_set_text_function_name, 'text:str')
