from typing import Iterator

from generator.properties.property_generator import PropertyGenerator


class VisibilityGenerator(PropertyGenerator):

    def generate_get(self) -> str:
        return f'{self.target_generator.name}.isVisible()'

    def generate_set(self, value: bool | str) -> Iterator[str]:
        def generate_set_visible(generator):
            yield f'{generator.name}.setVisible({value})'
            for child in generator.children:
                yield from generate_set_visible(child)

        return generate_set_visible(self.target_generator)
