from generator.design.component_generator import ComponentGenerator
from generator.utils import *


class TextFieldGenerator(ComponentGenerator):
    handler_text_changed_function_name: str
    controller_set_text_function_name: str

    component_name = 'text_field'
    component_config = {
        'text_color': "'rgba(255, 255, 255, 255)'",
        'hint': "''"
    }

    def generate_design(self):
        self.handler_text_changed_function_name = f'{self.q_widget_name}_text_changed'
        self.controller_set_text_function_name = f'{self.q_widget_name}_set_text'
        text_color = generate_get_component_config(self, 'text_color')
        hint = generate_get_component_config(self, 'hint')

        yield from f"""
self.{self.q_widget_name} = QLineEdit(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setGeometry({self.pyqt_bounds})
self.{self.q_widget_name}.setAutoFillBackground(False)
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{self.q_widget_name}.setAcceptDrops(False)
self.{self.q_widget_name}.setFont(QFont("Arial", 20 * {config.scale * config.text_scale}))
self.{self.controller_set_text_function_name} = self.{self.q_widget_name}.setText
# set text color, hint color and hint
self.{self.q_widget_name}.setStyleSheet("color: " + {text_color} + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
self.{self.q_widget_name}.setPlaceholderText({hint})
def __{self.handler_text_changed_function_name}(text):
    current_text = self.{self.q_widget_name}.text()""".splitlines()
        yield from indent(generate_activate_handler(self, self.handler_text_changed_function_name, 'current_text'))
        yield f'self.{self.q_widget_name}.textChanged.connect(__{self.handler_text_changed_function_name})'
        yield from generate_link_controller(self, f'self.{self.q_widget_name}.setText',
                                            self.controller_set_text_function_name)

    def generate_handler(self):
        yield from generate_handler(self.handler_text_changed_function_name, 'text:str')

    def generate_controller(self):
        yield from generate_controller(self.controller_set_text_function_name, 'text:str')
