from generator.core.factory_generator import FactoryGenerator
from generator.properties.property_generator import PropertyGenerator
from generator.ui.vector_generator import VectorGenerator


class VisibilityGenerator(PropertyGenerator):

    def generate_design(self):
        yield from VectorGenerator(self.fig_node, self.start_coordinates, self)
        for child in self.fig_node.get('children', []):
            yield from FactoryGenerator(child, self.start_coordinates, self).generate_design()

    def generate_get(self):
        yield f'{self.name}.isVisible()'

    def generate_set(self, value: bool | str):

        def generate_show(generator):
            yield f'{generator.name}.setVisible({value})'
            for child in generator.children:
                yield from generate_show(child.fig_node)

        return generate_show(self)
