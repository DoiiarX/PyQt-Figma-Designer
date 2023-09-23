from generator.design.component_generator import ComponentGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import *


class ButtonGenerator(ComponentGenerator):
    handler_click_function_name: str

    component_name = 'button'
    component_config = {
        'pressed_color': "'rgba(255, 255, 255, 30)'",
        'enabled': True
    }

    def generate_design(self):
        self.handler_click_function_name = f'{self.q_widget_name}_clicked'
        yield f'def __{self.handler_click_function_name}(*args, **kwargs):'
        yield from indent(generate_handler_call(self, self.handler_click_function_name))
        yield from indent(generate_transitions(self))
        yield from generate_q_push_button_create(self)
        yield f'self.{self.q_widget_name}.clicked.connect(__{self.handler_click_function_name})'

    def generate_handler(self):
        yield from generate_handler_function(self.handler_click_function_name)
