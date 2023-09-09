from abc import abstractmethod
from typing import List, Iterator, Any

from config import scale
from generator.core.base_generator import BaseGenerator


class PropertyGenerator(BaseGenerator):

    @abstractmethod
    def generate_get(self) -> Any:
        pass

    @abstractmethod
    def generate_set(self, value: Any) -> None:
        pass
