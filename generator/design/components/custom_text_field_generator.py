from generator.design.component_generator import ComponentGenerator
from generator.design.components.text_field_generator import TextFieldGenerator
from generator.design.core.text_generator import TextGenerator
from generator.utils import *


class CustomTextFieldGenerator(ComponentGenerator):

    component_name = 'custom_text_field'
    component_config = {}

    def generate_design(self):
        text_field_text = self.group_generator.children[-1]
        while not isinstance(text_field_text, TextGenerator):
            text_field_text = text_field_text.children[-1]

        text_field_hint = self.group_generator.children[-2]
        while not isinstance(text_field_hint, TextGenerator):
            text_field_hint = text_field_hint.children[-1]
        text_field_hint = text_field_hint

        text_field_generator = TextFieldGenerator(self.group_generator.children[-3])  # type: ignore
        yield from text_field_generator.generate_design()
        yield from f"""self.{text_field_generator.q_widget_name}.setFont(self.{text_field_text.q_widget_name}.font())
text_color = self.{text_field_text.q_widget_name}.styleSheet().split("color: ")[1].split(";")[0]
self.{text_field_generator.q_widget_name}.setStyleSheet("color: rgba(255, 255, 255, 0);")
self.{text_field_text.q_widget_name}.hide()
self.{text_field_generator.q_widget_name}.setStyleSheet("color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")""".splitlines()
        yield from generate_decorate_handler(text_field_generator, text_field_generator.handler_text_changed_function_name,
                                             f"""if text == '' :
    self.{text_field_hint.q_widget_name}.show()
else :
    self.{text_field_hint.q_widget_name}.hide()""".splitlines().__iter__(),
                                             'text')
