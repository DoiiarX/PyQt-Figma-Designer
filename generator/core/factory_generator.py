from generator.core.base_generator import BaseGenerator
from generator.ui.button_generator import ButtonGenerator
from generator.ui.checkbox_generator import CheckboxGenerator
from generator.core.group_generator import GroupGenerator
from generator.ui.text_field_generator import TextFieldGenerator
from generator.ui.text_generator import TextGenerator
from generator.ui.vector_generator import VectorGenerator


class FactoryGenerator(BaseGenerator):
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
        if 'children' in self.fig_node and len(self.fig_node['children']) > 0:
            yield from GroupGenerator(self.fig_node, self).generate_design()

        # generate inputs
        if self.fig_node['name'].lower().strip().startswith('button'):
            yield from ButtonGenerator(self.fig_node, self).generate_design()

        if self.fig_node['name'].lower().replace(' ', '').replace('-', '').startswith('textfield'):
            yield from TextFieldGenerator(self.fig_node, self).generate_design()

        if self.fig_node['name'].lower().replace(' ', '').replace('-', '').startswith('checkbox'):
            yield from CheckboxGenerator(self.fig_node, self,
                                         self.children[0].children[-1]).generate_design()
        yield f'{self.name} = QLabel(central_widget)'
