from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.core.text_generator import TextGenerator
from generator.design.core.vector_generator import VectorGenerator
from generator.design.components.button_generator import ButtonGenerator
from generator.design.components.checkbox_generator import CheckboxGenerator
from generator.design.components.text_field_generator import TextFieldGenerator


class FactoryGenerator(DesignGenerator):
    def generate_design(self):
        if not self.fig_node.get('visible', True):
            return []

        # generate visuals
        if ('fillGeometry' in self.fig_node and len(self.fig_node['fillGeometry']) > 0) \
                or ('strokeGeometry' in self.fig_node and len(self.fig_node['strokeGeometry']) > 0):
            yield from VectorGenerator(self.fig_node, self).generate_design()

        if self.fig_node['type'] == 'TEXT':
            yield from TextGenerator(self.fig_node, self).generate_design()

        # generate children
        group_generator = None
        if 'children' in self.fig_node and len(self.fig_node['children']) > 0:
            group_generator = GroupGenerator(self.fig_node, self)
            yield from group_generator.generate_design()

        # generate inputs
        if self.fig_node['name'].lower().strip().startswith('button'):
            yield from ButtonGenerator(self.fig_node, self).generate_design()

        if self.fig_node['name'].lower().replace(' ', '').replace('-', '').startswith('textfield'):
            yield from TextFieldGenerator(self.fig_node, self).generate_design()

        if self.fig_node['name'].lower().replace(' ', '').replace('-', '').startswith('checkbox'):
            if group_generator is not None:
                yield from CheckboxGenerator(self.fig_node, self, group_generator).generate_design()

        yield f'{self.name} = QLabel(central_widget)'
