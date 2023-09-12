from generator.design.components.custom_button_generator import CustomButtonGenerator
from generator.design.components.custom_text_field_generator import CustomTextFieldGenerator
from generator.design.components.progress_bar_generator import ProgressBarGenerator
from generator.design.components.button_generator import ButtonGenerator
from generator.design.components.checkbox_generator import CheckboxGenerator
from generator.design.components.slider_generator import SliderGenerator
from generator.design.components.text_field_generator import TextFieldGenerator
from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.core.text_generator import TextGenerator
from generator.design.core.vector_generator import VectorGenerator
from generator.properties.visibility_generator import VisibilityGenerator


class FactoryGenerator(DesignGenerator):
    def generate_design(self):
        yield f'{self.name} = QLabel(central_widget)'
        if not self.fig_node.get('visible', True):
            return

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
        name = self.fig_node['name'].lower().replace(' ', '').replace('-', '').replace('_', '')

        if name.startswith('button'):
            yield from ButtonGenerator(self.fig_node, self).generate_design()

        elif name.startswith('textfield'):
            yield from TextFieldGenerator(self.fig_node, self).generate_design()

        # those components need a group generator
        elif group_generator is not None:
            if name.startswith('checkbox'):
                yield from CheckboxGenerator(self.fig_node, self, group_generator).generate_design()

            elif name.startswith('customtextfield'):
                yield from CustomTextFieldGenerator(self.fig_node, self, group_generator).generate_design()

            elif name.startswith('progressbar'):
                yield from ProgressBarGenerator(self.fig_node, self, group_generator).generate_design()

            elif name.startswith('custombutton'):
                yield from CustomButtonGenerator(self.fig_node, self, group_generator).generate_design()

            elif name.startswith('slider'):
                yield from SliderGenerator(self.fig_node, self, group_generator).generate_design()

        # hide the component if it is not visible
        if not self.fig_node.get('visible', True):
            yield from VisibilityGenerator(self).generate_set('False')
