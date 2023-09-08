from overrides import override
from config import scale
from generator.python_generator.figma_node_generator import FigmaNodeGenerator
from generator.python_generator.vector_generator import VectorGenerator
from utils import indent

from generator.python_generator.base_generator import BaseGenerator


class FrameGenerator(BaseGenerator):
    @override
    def generate_design(self):
        bounds = self.fig_node['absoluteBoundingBox']
        width, height = bounds['width'], bounds['height']
        start_x, start_y = bounds['x'], bounds['y']
        yield from f"""


class {self.name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width * scale}, {height * scale})
        central_widget = QWidget(MainWindow)
        MainWindow.setFixedSize({width * scale}, {height * scale})
        MainWindow.setWindowTitle("{self.fig_node['name']}")""".splitlines()
        vector_generator = VectorGenerator(self.fig_node, (start_x, start_y), self)
        yield from indent(vector_generator.generate_design(), n=2)
        for child in self.fig_node['children']:
            child_generator = FigmaNodeGenerator(child, (start_x, start_y), self)
            yield from indent(child_generator.generate_design(), n=2)
        yield indent('MainWindow.setCentralWidget(central_widget)', n=2)

    @override
    def generate_handler(self):
        yield from f"""
class {self.name}Handler:
""".splitlines()
        for child in self.children:
            yield from indent(child.generate_handler(), n=1)

    @override
    def generate_controller(self):
        yield from f"""
class {self.name}Controller:
""".splitlines()
        for child in self.children:
            yield from indent(child.generate_controller(), n=1)
