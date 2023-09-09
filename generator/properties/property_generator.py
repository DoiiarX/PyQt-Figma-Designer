from abc import abstractmethod
from typing import List, Iterator, Any

from config import scale
from generator.core.base_generator import BaseGenerator


class PropertyGenerator:
    target_generator: BaseGenerator

    def __init__(self, target_generator: BaseGenerator):
        self.target_generator = target_generator

    @abstractmethod
    def generate_get(self) -> str:
        pass

    @abstractmethod
    def generate_set(self, value: str) -> Iterator[str]:
        pass
