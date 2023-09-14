import inspect

from generator.design.component_generator import ComponentGenerator
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
from generator.utils import generate_q_widget
import generator.design.components as components


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
        name = self.figma_node['name'].lower().replace(' ', '').replace('-', '').replace('_', '')

        if group_generator is not None:
            # enumerate classes in module design.components
            for _, obj in inspect.getmembers(components, inspect.ismodule):
                for _, cls in inspect.getmembers(obj, inspect.isclass):
                    # if cls inherits ComponentGenerator
                    if issubclass(cls, ComponentGenerator) and cls != ComponentGenerator:
                        prefix_rule = cls.prefix_rule.lower().replace(' ', '').replace('-', '').replace('_', '')
                        if name.startswith(prefix_rule):
                            yield from cls(self.figma_node, self, group_generator).generate_design()

        # hide the component if it is not visible
        if not self.figma_node.get('visible', True):
            yield from VisibilityGenerator(self).generate_set('False')
