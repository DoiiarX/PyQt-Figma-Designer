import importlib.util
import inspect
import os

from generator.design.component_generator import ComponentGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.core.text_generator import TextGenerator
from generator.design.core.vector_generator import VectorGenerator
from generator.design.design_generator import DesignGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.utils import generate_q_widget


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
        module_directory = 'generator/design/components'
        module_files = [f for f in os.listdir(module_directory) if f.endswith('.py')]
        # Remove the file extension to get module names.
        module_names = [os.path.splitext(f)[0] for f in module_files]
        # Import the modules and list them.
        for module_name in module_names:
            spec = importlib.util.spec_from_file_location(module_name,
                                                          os.path.join(module_directory, module_name + '.py'))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for _, cls in inspect.getmembers(module, inspect.isclass):
                if issubclass(cls, ComponentGenerator) and cls != ComponentGenerator:
                    prefix_rule = cls.prefix_rule.lower().replace(' ', '').replace('-', '').replace('_', '')
                    if name.startswith(prefix_rule):
                        yield from cls(self.figma_node, self, group_generator).generate_design()
