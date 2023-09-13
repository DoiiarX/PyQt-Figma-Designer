from typing import Iterator

from generator.properties.property_generator import PropertyGenerator


class VisibilityGenerator(PropertyGenerator):

    def generate_get(self) -> str:
        return f'{self.target_generator.q_widget_name}.isVisible()'

    def generate_set(self, value: bool | str) -> Iterator[str]:

        yield f'{self.target_generator.q_widget_name}.setVisible({value})'
