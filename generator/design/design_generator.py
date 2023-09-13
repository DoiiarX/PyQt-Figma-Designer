from abc import abstractmethod
from typing import List, Iterator
import config


class DesignGenerator:
    used_names: set = set()

    parent: 'DesignGenerator|None' = None
    figma_node: dict
    start_coordinates: (float, float) = (0, 0)
    children: List['DesignGenerator']
    q_widget_name: str

    handler_class_path: str = ''
    controller_class_path: str = ''

    def __init__(self, figma_node: dict, parent: 'DesignGenerator|None'):
        self.figma_node = figma_node
        self.children = []
        self.q_widget_name = self.create_name(figma_node)
        self.short_class_name = self.q_widget_name.replace('_', ' ').title().replace(' ', '')
        if parent is not None:
            self.parent = parent
            self.parent.children.append(self)
            self.controller_class_path = parent.controller_class_path
            self.handler_class_path = parent.handler_class_path

    @property
    def bounds(self):
        parent_start_x, parent_start_y = 0, 0
        if self.parent is not None:
            parent_bounds = self.parent.figma_node.get('absoluteBoundingBox', {'x': 0, 'y': 0, 'width': 0, 'height': 0})
            parent_start_x, parent_start_y = parent_bounds['x'], parent_bounds['y']
        bounds = self.figma_node.get('absoluteBoundingBox', {'x': 0, 'y': 0, 'width': 0, 'height': 0})
        x, y = bounds['x'] - parent_start_x, bounds['y'] - parent_start_y
        width, height = bounds['width'], bounds['height']
        x, y, width, height = x * config.scale, y * config.scale, width * config.scale, height * config.scale
        return x, y, width, height

    @property
    def pyqt_bounds(self):
        x, y, width, height = self.bounds
        return f'QRect({int(x)}, {int(y)}, {int(width)}, {int(height)})'

    @classmethod
    def create_name(cls, figma_node: dict) -> str:
        view_name = figma_node['name'].replace(' ', '_').lower()
        view_name = ''.join(c for c in view_name if c.isalnum() or c == '_')
        while '__' in view_name:
            view_name = view_name.replace('__', '_')
        while view_name.startswith('_'):
            view_name = view_name[1:]
        while view_name.endswith('_'):
            view_name = view_name[:-1]
        if view_name == '':
            view_name = 'view'
        if view_name[0].isdigit():
            view_name = '_' + view_name
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
