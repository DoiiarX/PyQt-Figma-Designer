from generator.design.design_generator import DesignGenerator
from generator.utils import indent


class GroupGenerator(DesignGenerator):
    def generate_design(self):
        self.controller_class_path = f'{self.controller_class_path}.{self.short_class_name}Controller'
        self.handler_class_path = f'{self.handler_class_path}.{self.short_class_name}Handler'
        # import here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        if 'children' not in self.figma_node:
            return []
        for child in self.figma_node['children']:
            yield from FactoryGenerator(child, self).generate_design()
        yield f'{self.q_widget_name} = QLabel(central_widget)'

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
