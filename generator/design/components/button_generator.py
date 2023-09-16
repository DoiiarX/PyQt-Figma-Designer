from generator.design.component_generator import ComponentGenerator
from generator.utils import generate_activate_handler, indent, generate_print


class ButtonGenerator(ComponentGenerator):
    handler_click_function_name: str

    component_name = 'button'
    component_config = {
        'pressed_color': "'rgba(255, 255, 255, 30)'",
        'enabled': True
    }

    def generate_design(self):
        self.handler_click_function_name = f'{self.q_widget_name}_clicked'
        background_color = f'ComponentsConfig.{self.config_class_path}.pressed_color'
        yield from f"""
self.{self.q_widget_name} = QPushButton(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setGeometry({self.pyqt_bounds})
self.{self.q_widget_name}.setFlat(True)
self.{self.q_widget_name}.setAutoFillBackground(False)
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{self.q_widget_name}.setAcceptDrops(False)
self.{self.q_widget_name}.setEnabled(ComponentsConfig.{self.config_class_path}.enabled)
def __{self.handler_click_function_name}(*args, **kwargs):""".splitlines()
        yield from indent(generate_activate_handler(self, self.handler_click_function_name))
        yield from f"""
self.{self.q_widget_name}.clicked.connect(__{self.handler_click_function_name})
self.{self.q_widget_name}.setFocusPolicy(Qt.NoFocus)
self.{self.q_widget_name}.setStyleSheet(f"background-color:" + {background_color})""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_click_function_name}(cls) : 
    {generate_print(f"'Button {self.q_widget_name} clicked'")}""".splitlines()
