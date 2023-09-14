from abc import abstractmethod

from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator


class ComponentGenerator(DesignGenerator):
    group_generator: GroupGenerator

    def __init__(self, figma_node, parent, group_generator: GroupGenerator):
        super().__init__(figma_node, parent)
        self.group_generator = group_generator

    @abstractmethod
    def generate_design(self):
        pass

    @property
    @abstractmethod
    def prefix_rule(self):
        pass
