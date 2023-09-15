from typing import Iterator

import config
from generator.utils import indent, generate_activate_handler

from generator.design.design_generator import DesignGenerator


class FrameGenerator(DesignGenerator):
    short_class_name: str
    window_class_name: str

    def generate_design(self) -> Iterator[str]:
        # import it here to avoid circular import
        from generator.design.core.factory_generator import FactoryGenerator
        bounds = self.figma_node['absoluteBoundingBox']
        width, height = bounds['width'], bounds['height']
        self.window_class_name = f'QWindow{self.short_class_name}'
        self.handler_class_path = f'{self.short_class_name}Handler'
        self.controller_class_path = f'{self.short_class_name}Controller'
        self.strings_class_path = f'{self.short_class_name}Strings'
        self.config_class_path = f'{self.short_class_name}Config'
        yield from f"""


class {self.window_class_name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width * config.scale}, {height * config.scale})
        self.{self.q_widget_name} = QWidget(MainWindow)
        MainWindow.setFixedSize({width * config.scale}, {height * config.scale})
        MainWindow.setWindowTitle("{self.figma_node['name']}")""".splitlines()
        yield from indent(FactoryGenerator(self.figma_node, self).generate_design(), n=2)
        yield from indent(f'MainWindow.setCentralWidget(self.{self.q_widget_name})', n=2)
        yield from indent(generate_activate_handler(self, 'window_started'), n=2)
        yield from indent('def __window_closed(*args, **kwargs):', n=2)
        yield from indent(generate_activate_handler(self, 'window_closed'), n=3)
        yield from indent('MainWindow.closeEvent = __window_closed', n=2)

    def generate_handler(self) -> Iterator[str]:
        yield from f"""

class {self.handler_class_path.split(".")[-1]}:

    @classmethod
    def window_started(cls):
        pass
        
    @classmethod
    def window_closed(cls):
        pass""".splitlines()
        yield from indent(super().generate_handler())

    def generate_controller(self) -> Iterator[str]:
        sub_controllers = list(indent(super().generate_controller()))
        if len(sub_controllers) == 0:
            return [].__iter__()
        yield f'class {self.controller_class_path.split(".")[-1]}:'
        yield from sub_controllers

    def generate_strings(self) -> Iterator[str]:
        sub_strings = list(indent(super().generate_strings()))
        if len(sub_strings) == 0:
            return [].__iter__()
        yield f'class {self.strings_class_path.split(".")[-1]}:'
        yield from sub_strings

    def generate_config(self) -> Iterator[str]:
        sub_config = list(indent(super().generate_config()))
        if len(sub_config) == 0:
            return [].__iter__()
        yield f'class {self.config_class_path.split(".")[-1]}:'
        yield from sub_config
