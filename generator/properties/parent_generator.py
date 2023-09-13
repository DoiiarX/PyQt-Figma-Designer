from typing import Iterator

from generator.properties.property_generator import PropertyGenerator


class ParentGenerator(PropertyGenerator):

    def generate_get(self) -> str:
        return f'self.{self.target_generator.q_widget_name}.parent()'

    def generate_set(self, value: str) -> Iterator[str]:
        yield f'self.{self.target_generator.q_widget_name}.setParent({value})'
        for child in self.target_generator.children:
            yield from ParentGenerator(child).generate_set(value)
