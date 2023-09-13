from generator.design.components.custom_button_generator import CustomButtonGenerator
from generator.design.components.custom_text_field_generator import CustomTextFieldGenerator
from generator.design.components.progress_bar_generator import ProgressBarGenerator
from generator.design.components.button_generator import ButtonGenerator
from generator.design.components.checkbox_generator import CheckboxGenerator
from generator.design.components.slider_generator import SliderGenerator
from generator.design.components.tabs_view_generator import TabsViewGenerator
from generator.design.components.text_field_generator import TextFieldGenerator
from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.core.text_generator import TextGenerator
from generator.design.core.vector_generator import VectorGenerator
from generator.properties.visibility_generator import VisibilityGenerator


class FactoryGenerator(DesignGenerator):
    def generate_design(self):
        yield from self.generate_q_widget()

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
        name = self.figma_node['name'].lower().replace(' ', '').replace('-', '').replace('_', '')

        if name.startswith('button'):
            yield from ButtonGenerator(self.figma_node, self).generate_design()

        elif name.startswith('textfield'):
            yield from TextFieldGenerator(self.figma_node, self).generate_design()

        # those components need a group generator
        elif group_generator is not None:
            if name.startswith('checkbox'):
                yield from CheckboxGenerator(self.figma_node, self, group_generator).generate_design()

            elif name.startswith('customtextfield'):
                yield from CustomTextFieldGenerator(self.figma_node, self, group_generator).generate_design()

            elif name.startswith('progressbar'):
                yield from ProgressBarGenerator(self.figma_node, self, group_generator).generate_design()

            elif name.startswith('custombutton'):
                yield from CustomButtonGenerator(self.figma_node, self, group_generator).generate_design()

            elif name.startswith('slider'):
                yield from SliderGenerator(self.figma_node, self, group_generator).generate_design()

            elif name.startswith('tabsview'):
                yield from TabsViewGenerator(self.figma_node, self, group_generator).generate_design()

        # hide the component if it is not visible
        if not self.figma_node.get('visible', True):
            yield from VisibilityGenerator(self).generate_set('False')
