import abc
from dataclasses import dataclass
from typing import List, Tuple, Iterator


@dataclass
class Fill:
    blendMode: str
    type: str


@dataclass
class SolidFill(Fill):
    color: (float, float, float)
    blendMode: str = 'NORMAL'
    type: str = 'SOLID'


class Node:
    """
    Used for parsing Figma API responses.
    """
    children: List["Node"]
    type: str


class GraphicNode(Node):
    """
    Used for displaying graphics.
    """
    children: List["Node"] = []
    type: str
    absoluteBoundingBox: dict
    fills: List[dict]
    strokes: List[dict]
    strokeWeight: int
    strokeAlign: str
    cornerRadius: int
    characters: str
    style: dict


def parse(file: dict):
    pass


def parse_node(node: dict) -> Iterator[GraphicNode]:
    pass
