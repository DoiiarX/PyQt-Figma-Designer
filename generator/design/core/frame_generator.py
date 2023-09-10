from config import scale

from generator.design.core.vector_generator import VectorGenerator
from utils import indent

from generator.design.design_generator import DesignGenerator


class FrameGenerator(DesignGenerator):
    short_class_name: str
    window_class_name: str
    handler_class_name: str
    controller_class_name: str

    def generate_design(self):
        # import it here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        bounds = self.fig_node['absoluteBoundingBox']
        width, height = bounds['width'], bounds['height']
        start_x, start_y = bounds['x'], bounds['y']
        self.start_coordinates = (start_x, start_y)
        self.short_class_name = self.name.replace('_', ' ').title().replace(' ', '')
        self.window_class_name = f'QWindow{self.short_class_name}'
        self.handler_class_name = f'{self.short_class_name}Handler'
        self.controller_class_name = f'{self.short_class_name}Controller'

        yield from f"""


class {self.window_class_name}(object):
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
        yield from indent(f'GuiHandler.{self.handler_class_name}.window_started()', n=2)

    def generate_handler(self):
        yield from f"""

class {self.handler_class_name}:

    @classmethod
    def window_started(cls):
        pass""".splitlines()
        has_handler = False
        for child in self.children:
            for handler in child.generate_handler():
                yield from indent(handler, n=1)
                has_handler = True
        if not has_handler:
            yield from indent('pass', n=1)

    def generate_controller(self):
        yield from f"""

class {self.controller_class_name}:""".splitlines()
        has_controller = False
        for child in self.children:
            for controller in child.generate_controller():
                yield from indent(controller, n=1)
                has_controller = True
        if not has_controller:
            yield from indent('pass', n=1)

    @classmethod
    def get_current_frame(cls, generator: 'DesignGenerator'):
        while generator.parent is not None:
            if isinstance(generator, FrameGenerator):
                return generator
            generator = generator.parent
