from overrides import override
from config import scale

from generator.python_generator.vector_generator import VectorGenerator
from utils import indent

from generator.python_generator.base_generator import BaseGenerator


class FrameGenerator(BaseGenerator):
    class_name: str

    def __int__(self, fig_node, start_coordinates, parent):
        super().__init__(fig_node, start_coordinates, parent)
        self.class_name = 'QWindow'

    def generate_design(self):
        # import it here to avoid circular import
        from generator.python_generator.factory_generator import FactoryGenerator
        bounds = self.fig_node['absoluteBoundingBox']
        width, height = bounds['width'], bounds['height']
        start_x, start_y = bounds['x'], bounds['y']
        self.class_name = f'QWindow_{self.name}'
        yield from f"""


class {self.class_name}(object):
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
            child_generator = FactoryGenerator(child, (start_x, start_y), self)
            yield from indent(child_generator.generate_design(), n=2)
        yield from indent('MainWindow.setCentralWidget(central_widget)', n=2)

    def generate_handler(self):
        yield from f"""

class {self.name}Handler:
    pass
""".splitlines()
        for child in self.children:
            yield from indent(child.generate_handler(), n=1)

    def generate_controller(self):
        yield from f"""

class {self.name}Controller:
    pass
""".splitlines()
        for child in self.children:
            yield from indent(child.generate_controller(), n=1)

    @classmethod
    def get_current_frame(cls, generator: 'BaseGenerator'):
        while generator.parent is not None:
            if isinstance(generator, FrameGenerator):
                return generator
            generator = generator.parent
