from abc import abstractmethod
from typing import List, Iterator

from config import scale


class DesignGenerator:
    used_names: set = set()

    parent: 'DesignGenerator|None' = None
    fig_node: dict
    start_coordinates: (float, float) = (0, 0)
    children: List['DesignGenerator']
    name: str
    pyqt_bounds: str

    def __init__(self, figma_node: dict, parent: 'DesignGenerator|None'):
        if parent is not None:
            self.parent = parent
            self.parent.children.append(self)
            self.start_coordinates = parent.start_coordinates
        self.fig_node = figma_node
        self.children = []
        self.name = self.create_name(figma_node)

        bounds = figma_node.get('absoluteBoundingBox', {'x': 0, 'y': 0, 'width': 0, 'height': 0})
        x, y = bounds['x'] - self.start_coordinates[0], bounds['y'] - self.start_coordinates[1]
        width, height = bounds['width'], bounds['height']
        x, y, width, height = x * scale, y * scale, width * scale, height * scale
        self.pyqt_bounds = f'QRect({int(x)}, {int(y)}, {int(width)}, {int(height)})'

    @classmethod
    def create_name(cls, figma_node: dict) -> str:
        view_name = figma_node['name'].replace(' ', '_').lower()
        while '__' in view_name:
            view_name = view_name.replace('__', '_')
        while view_name.startswith('_'):
            view_name = view_name[1:]
        while view_name.endswith('_'):
            view_name = view_name[:-1]
        view_name = 'view_' + ''.join(c for c in view_name if c.isalnum() or c == '_')
        i = 0
        new_name = view_name
        while new_name in cls.used_names:
            new_name = f'{view_name}_{i}'
            i += 1
        view_name = new_name
        cls.used_names.add(view_name)
        return view_name

    @abstractmethod
    def generate_design(self) -> Iterator[str]:
        pass

    def generate_handler(self):
        for child in self.children:
            yield from child.generate_handler()

    def generate_controller(self):
        for child in self.children:
            yield from child.generate_controller()
