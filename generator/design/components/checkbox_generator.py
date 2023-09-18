from generator.design.component_generator import ComponentGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.utils import *


class CheckboxGenerator(ComponentGenerator):
    handler_check_changed_function_name: str
    controller_set_checked_function_name: str

    component_name = 'checkbox'
    component_config = {
        'default_checked': False,
        'enabled': True
    }

    def generate_design(self):
        checked_generator = self.group_generator.children[-1]
        hide_show_checked_generator = VisibilityGenerator(checked_generator)
        self.handler_check_changed_function_name = f'{self.q_widget_name}_check_changed'
        self.controller_set_checked_function_name = f'{self.q_widget_name}_set_checked'
        checked_name = f'{self.q_widget_name}_checked'
        default_checked = generate_get_component_config(self, 'default_checked')
        enabled = generate_get_component_config(self, 'enabled')
        yield from f"""
self.{checked_name} = {default_checked}
self.{self.q_widget_name} = QPushButton(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setGeometry({self.pyqt_bounds})
self.{self.q_widget_name}.setFlat(True)
self.{self.q_widget_name}.setAutoFillBackground(False)
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{self.q_widget_name}.setAcceptDrops(False)
self.{self.q_widget_name}.setFocusPolicy(Qt.NoFocus)
self.{self.q_widget_name}.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
self.{self.q_widget_name}.setEnabled({enabled})
def __{self.handler_check_changed_function_name}():
    self.{checked_name} = not self.{checked_name}""".splitlines()
        yield from indent(hide_show_checked_generator.generate_set(f'self.{checked_name}'), n=1)
        yield from indent(generate_activate_handler(self, self.handler_check_changed_function_name,
                                                    f'self.{checked_name}'), n=1)
        yield from f"""
def __{self.controller_set_checked_function_name}(checked:bool):
    self.{checked_name} = checked""".splitlines()
        yield from indent(hide_show_checked_generator.generate_set(f'self.{checked_name}'), n=1)
        yield f'self.{self.q_widget_name}.clicked.connect(__{self.handler_check_changed_function_name})'
        yield from generate_link_controller(self, f'__{self.controller_set_checked_function_name}',
                                            self.controller_set_checked_function_name)
        # hide the checked image if needed
        yield from hide_show_checked_generator.generate_set(f'self.{checked_name}')

    def generate_handler(self):
        yield from generate_handler(self.handler_check_changed_function_name, 'checked:bool')

    def generate_controller(self):
        yield from generate_controller(self.controller_set_checked_function_name, 'checked:bool')
