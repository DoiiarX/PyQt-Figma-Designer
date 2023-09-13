from generator.design.design_generator import DesignGenerator
from generator.utils import indent


class GroupGenerator(DesignGenerator):
    def generate_design(self):
        if self.parent is None:
            return []
        if 'children' not in self.figma_node:
            return []
        self.controller_class_path = f'{self.controller_class_path}.{self.short_class_name}Controller'
        self.handler_class_path = f'{self.handler_class_path}.{self.short_class_name}Handler'
        # import here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        yield from self.generate_q_widget()
        for child in self.figma_node['children']:
            yield from FactoryGenerator(child, self).generate_design()

    def generate_handler(self):
        sub_handlers = []
        for child in self.children:
            sub_handlers.extend(child.generate_handler())
        if len(sub_handlers) == 0:
            return []

        yield f'class {self.handler_class_path.split(".")[-1]}:'
        yield from indent(sub_handlers, n=1)

    def generate_controller(self):
        sub_controllers = []
        for child in self.children:
            sub_controllers.extend(child.generate_controller())
        if len(sub_controllers) == 0:
            return []

        yield f'class {self.controller_class_path.split(".")[-1]}:'
        yield from indent(sub_controllers, n=1)
