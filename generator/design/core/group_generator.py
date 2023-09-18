"""
This module contains GroupGenerator class responsible for generating
children of a figma group.
"""
from typing import Iterator, Tuple

from generator.design.design_generator import DesignGenerator
from generator.utils import indent, generate_q_widget_create


class GroupGenerator(DesignGenerator):
    """
    Responsible for generating children of a figma group.
    Also, responsible for increasing the hierarchy level of the Handler, Controller, Strings and Config classes.
    """

    def generate_design(self):
        __doc__ = super().generate_design().__doc__
        if self.parent is None:
            return []
        if 'children' not in self.figma_node:
            return []
        self.controller_class_path = f'{self.controller_class_path}.{self.short_class_name}Controller'
        self.handler_class_path = f'{self.handler_class_path}.{self.short_class_name}Handler'
        self.strings_class_path = f'{self.strings_class_path}.{self.short_class_name}Strings'
        self.config_class_path = f'{self.config_class_path}.{self.short_class_name}Config'
        # import here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        yield from generate_q_widget_create(self)
        for child in self.figma_node['children']:
            yield from FactoryGenerator(child, self).generate_design()

    def generate_handler(self):
        __doc__ = super().generate_handler().__doc__
        sub_handlers = []
        for child in self.children:
            sub_handlers.extend(child.generate_handler())
        if len(sub_handlers) == 0:
            return []

        yield f'class {self.handler_class_path.split(".")[-1]}:'
        yield from indent(sub_handlers.__iter__(), n=1)

    def generate_controller(self):
        __doc__ = super().generate_controller().__doc__
        sub_controllers = []
        for child in self.children:
            sub_controllers.extend(child.generate_controller())
        if len(sub_controllers) == 0:
            return []

        yield f'class {self.controller_class_path.split(".")[-1]}:'
        yield from indent(sub_controllers.__iter__(), n=1)

    def generate_strings(self) -> Iterator[Tuple[str, str]]:
        __doc__ = super().generate_strings().__doc__
        sub_strings = []
        for child in self.children:
            sub_strings.extend(child.generate_strings())
        if len(sub_strings) == 0:
            return []

        yield f'class {self.strings_class_path.split(".")[-1]}:'
        yield from indent(sub_strings.__iter__(), n=1)

    def generate_config(self) -> Iterator[Tuple[str, str]]:
        __doc__ = super().generate_config().__doc__
        sub_config = []
        for child in self.children:
            sub_config.extend(child.generate_config())
        if len(sub_config) == 0:
            return []

        yield f'class {self.config_class_path.split(".")[-1]}:'
        yield from indent(sub_config.__iter__(), n=1)
