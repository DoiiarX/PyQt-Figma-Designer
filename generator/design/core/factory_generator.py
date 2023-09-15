from generator.design.core.group_generator import GroupGenerator
from generator.design.core.text_generator import TextGenerator
from generator.design.core.vector_generator import VectorGenerator
from generator.design.design_generator import DesignGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.utils import generate_q_widget, get_generic_components


class FactoryGenerator(DesignGenerator):
    def generate_design(self):
        yield from generate_q_widget(self)

        if not self.figma_node.get('visible', True):
            return

        # generate visuals
        if ('fillGeometry' in self.figma_node and len(self.figma_node['fillGeometry']) > 0) \
                or ('strokeGeometry' in self.figma_node and len(self.figma_node['strokeGeometry']) > 0):
            yield from VectorGenerator(self.figma_node, self).generate_design()

        if self.figma_node['type'] == 'TEXT':
            yield from TextGenerator(self.figma_node, self).generate_design()

        # generate children
        group_generator = None
        if 'children' in self.figma_node and len(self.figma_node['children']) > 0:
            group_generator = GroupGenerator(self.figma_node, self)
            yield from group_generator.generate_design()

        # generate inputs

        if group_generator is not None:
            yield from self.generate_generic_components(group_generator)

        # hide the component if it is not visible
        if not self.figma_node.get('visible', True):
            yield from VisibilityGenerator(self).generate_set('False')

    def generate_generic_components(self, group_generator):
        name = self.figma_node['name'].lower().replace(' ', '').replace('-', '').replace('_', '')
        for cls in get_generic_components():
            prefix_rule = cls.component_name.lower().replace(' ', '').replace('-', '').replace('_', '')
            if name.startswith(prefix_rule):
                yield from cls(self.figma_node, self, group_generator).generate_design()
