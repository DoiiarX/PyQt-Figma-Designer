from typing import Iterator

from generator.properties.property_generator import PropertyGenerator


class GeometryGenerator(PropertyGenerator):

    def generate_get(self) -> str:
        return f'self.{self.target_generator.q_widget_name}.getGeometry()'

    def generate_set(self, value: '(str, str, str, str) | str') -> Iterator[str]:
        def generate_set_visible(generator):
            yield f'self.{generator.q_widget_name}.setGeometry({value})'
            for child in generator.children:
                yield from generate_set_visible(child)

        match value:
            case (x, y, width, height):
                value = f'QRect({x}, {y}, {width}, {height})'
            case _:
                pass
        return generate_set_visible(self.target_generator)
