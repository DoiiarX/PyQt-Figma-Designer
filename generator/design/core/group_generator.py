from typing import Iterator, Tuple

from generator.design.design_generator import DesignGenerator
from generator.utils import indent, generate_q_widget


class GroupGenerator(DesignGenerator):
    def generate_design(self):
        if self.parent is None:
            return []
        if 'children' not in self.figma_node:
            return []
        self.controller_class_path = f'{self.controller_class_path}.{self.short_class_name}Controller'
        self.handler_class_path = f'{self.handler_class_path}.{self.short_class_name}Handler'
        self.strings_class_path = f'{self.strings_class_path}.{self.short_class_name}Strings'
        # import here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        yield from generate_q_widget(self)
        for child in self.figma_node['children']:
            yield from FactoryGenerator(child, self).generate_design()

    def generate_handler(self):
        sub_handlers = []
        for child in self.children:
            sub_handlers.extend(child.generate_handler())
        if len(sub_handlers) == 0:
            return []

        yield f'class {self.handler_class_path.split(".")[-1]}:'
        yield from indent(sub_handlers.__iter__(), n=1)

    def generate_controller(self):
        sub_controllers = []
        for child in self.children:
            sub_controllers.extend(child.generate_controller())
        if len(sub_controllers) == 0:
            return []

        yield f'class {self.controller_class_path.split(".")[-1]}:'
        yield from indent(sub_controllers.__iter__(), n=1)

    def generate_strings(self) -> Iterator[Tuple[str, str]]:
        sub_strings = []
        for child in self.children:
            sub_strings.extend(child.generate_strings())
        if len(sub_strings) == 0:
            return []

        yield f'class {self.strings_class_path.split(".")[-1]}:'
        yield from indent(sub_strings.__iter__(), n=1)
