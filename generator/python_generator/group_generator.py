from overrides import override

from generator.python_generator.base_generator import BaseGenerator


class GroupGenerator(BaseGenerator):
    def generate_design(self):
        # import here to avoid circular import
        from generator.python_generator.factory_generator import FactoryGenerator
        if 'children' not in self.fig_node:
            return []
        for child in self.fig_node['children']:
            yield from FactoryGenerator(child, self.start_coordinates, self).generate_design()
        yield f'{self.name} = QLabel(central_widget)'
