from abc import abstractmethod
from typing import Iterator

from generator.design.design_generator import DesignGenerator


class PropertyGenerator:
    target_generator: DesignGenerator

    def __init__(self, target_generator: DesignGenerator):
        self.target_generator = target_generator

    @abstractmethod
    def generate_get(self) -> str:
        pass

    @abstractmethod
    def generate_set(self, value: str) -> Iterator[str]:
        pass
