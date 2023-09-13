import config
from generator.design.core.vector_generator import VectorGenerator
from generator.utils import indent

from generator.design.design_generator import DesignGenerator


class FrameGenerator(DesignGenerator):
    short_class_name: str
    window_class_name: str

    def generate_design(self):
        # import it here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        bounds = self.figma_node['absoluteBoundingBox']
        width, height = bounds['width'], bounds['height']
        self.window_class_name = f'QWindow{self.short_class_name}'
        self.handler_class_path = f'{self.short_class_name}Handler'
        self.controller_class_path = f'{self.short_class_name}Controller'

        yield from f"""


class {self.window_class_name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width * config.scale}, {height * config.scale})
        self.{self.q_widget_name} = QWidget(MainWindow)
        MainWindow.setFixedSize({width * config.scale}, {height * config.scale})
        MainWindow.setWindowTitle("{self.figma_node['name']}")""".splitlines()
        yield from indent(VectorGenerator(self.figma_node, self).generate_design(), n=2)
        for child in self.figma_node['children']:
            yield from indent(FactoryGenerator(child, self).generate_design(), n=2)

        yield from indent(f'MainWindow.setCentralWidget(self.{self.q_widget_name})', n=2)
        yield from f"""
        try : 
            GuiHandler.{self.handler_class_path}.window_started()            
        except NameError:
            print("No function {self.handler_class_path}.window_started defined.")
        except Exception as e:
            print("Caught exception while trying to call {self.handler_class_path}.window_started : " + str(e))
        def __window_closed(*args, **kwargs):
            try :
                GuiHandler.{self.handler_class_path}.window_closed()
            except NameError:
                print("No function {self.handler_class_path}.window_closed defined.")
            except Exception as e:
                print("Caught exception while trying to call {self.handler_class_path}.window_closed : " + str(e))
        MainWindow.closeEvent = __window_closed
        
""".splitlines()

    def generate_handler(self):
        yield from f"""

class {self.handler_class_path.split(".")[-1]}:

    @classmethod
    def window_started(cls):
        pass
        
    @classmethod
    def window_closed(cls):
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

class {self.controller_class_path.split(".")[-1]}:""".splitlines()
        has_controller = False
        for child in self.children:
            for controller in child.generate_controller():
                yield from indent(controller, n=1)
                has_controller = True
        if not has_controller:
            yield from indent('pass', n=1)
