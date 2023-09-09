from config import scale

from generator.ui.vector_generator import VectorGenerator
from utils import indent

from generator.core.base_generator import BaseGenerator


class FrameGenerator(BaseGenerator):
    class_name: str

    def __int__(self, fig_node, parent):
        super().__init__(fig_node, parent)
        self.class_name = 'QWindow'

    def generate_design(self):
        # import it here to avoid circular import
        from generator.core.factory_generator import FactoryGenerator
        bounds = self.fig_node['absoluteBoundingBox']
        width, height = bounds['width'], bounds['height']
        start_x, start_y = bounds['x'], bounds['y']
        self.start_coordinates = (start_x, start_y)
        class_name_short = self.name.replace('_', ' ').title().replace(' ', '')
        self.class_name = f'QWindow{class_name_short}'
        yield from f"""


class {self.class_name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width * scale}, {height * scale})
        central_widget = QWidget(MainWindow)
        MainWindow.setFixedSize({width * scale}, {height * scale})
        MainWindow.setWindowTitle("{self.fig_node['name']}")""".splitlines()
        yield from indent(VectorGenerator(self.fig_node, self).generate_design(), n=2)
        for child in self.fig_node['children']:
            yield from indent(FactoryGenerator(child, self).generate_design(), n=2)
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
