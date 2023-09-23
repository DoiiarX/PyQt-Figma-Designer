"""
This module contains the abstract class ComponentGenerator that is the base class for all component generators.
"""
from abc import abstractmethod
from typing import Iterator

from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.utils import indent


class ComponentGenerator(DesignGenerator):
    """
    Abstract class for all generic component generators.
    """
    # The group generator corresponding to the figma node that generated this component.
    group_generator: GroupGenerator
    # Abstract property to be defined in subclasses to specify the component name (prefix of the figma node name).
    component_name: str
    # Abstract property to be defined in subclasses to specify if the component is orientable (horizontal or vertical).
    # This affects the way its name is matched with the figma node name. (adds v_ or h_ optional prefix)
    orientable: bool = False

    # Abstract property to be defined in subclasses to specify the default component config.
    # This config will be saved as json together with the design. It can be used to edit the style of the component.
    component_config: dict = {}

    def __init__(self, group_generator: GroupGenerator):
        """
        Create a new component generator.
        Args:
            group_generator: The group generator corresponding to the figma node that generated this component.
        """
        super().__init__(group_generator.figma_node, group_generator.parent)
        self.group_generator = group_generator
        self.config_class_path = f'{self.group_generator.parent.config_class_path}.{self.short_class_name}Config'

    @abstractmethod
    def generate_design(self):
        __doc__ = super().generate_design().__doc__
        pass

    def generate_config(self) -> Iterator[str]:
        """
        Generates the code to create the config class for this component if it has a config (non empty component_config).
        returns:
            An iterator of strings containing the code to generate the config class for this component.
        """
        if len(self.component_config) > 0:
            yield f'class {self.config_class_path.split(".")[-1]}:'
            for key, value in self.component_config.items():
                yield from indent(f'{key} = {value}')
        yield from super().generate_config()
