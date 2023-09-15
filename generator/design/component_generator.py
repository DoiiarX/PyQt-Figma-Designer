from abc import abstractmethod
from typing import Iterator

from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.utils import indent


class ComponentGenerator(DesignGenerator):
    # The group generator corresponding to the figma node that generated this component.
    group_generator: GroupGenerator
    # Abstract property to be defined in subclasses to specify the default component config.
    # This config will be saved as json together with the design. It can be used to edit the style of the component.
    component_config: dict = {}
    # Abstract property to be defined in subclasses to specify the component name (prefix of the figma node name).
    component_name: str

    def __init__(self, figma_node, parent, group_generator: GroupGenerator):
        super().__init__(figma_node, parent)
        self.group_generator = group_generator
        self.config_class_path = f'{self.group_generator.parent.config_class_path}.{self.short_class_name}Config'

    @abstractmethod
    def generate_design(self):
        pass

    def generate_config(self) -> Iterator[str]:
        if len(self.component_config) > 0:
            yield f'class {self.config_class_path.split(".")[-1]}:'
            for key, value in self.component_config.items():
                yield from indent(f'{key} = {value}')
        yield from super().generate_config()
