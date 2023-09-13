from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import indent, generate_activate_handler, generate_link_controller


class CheckboxGenerator(DesignGenerator):
    handler_check_changed_function_name: str
    controller_set_checked_function_name: str

    def __init__(self, figma_node, parent, group_generator: GroupGenerator):
        super().__init__(figma_node, parent)
        checked_generator = group_generator.children[-1]
        self.hide_show_checked_generator = VisibilityGenerator(checked_generator)

    def generate_design(self):
        self.handler_check_changed_function_name = f'{self.q_widget_name}_check_changed'
        self.controller_set_checked_function_name = f'{self.q_widget_name}_set_checked'
        checked_name = f'{self.q_widget_name}_checked'

        yield from f"""
self.{checked_name} = False
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

def __{self.handler_check_changed_function_name}():
    self.{checked_name} = not self.{checked_name}""".splitlines()
        yield from indent(self.hide_show_checked_generator.generate_set(f'self.{checked_name}'), n=1)
        yield from indent(generate_activate_handler(self, self.handler_check_changed_function_name,
                                                    f'self.{checked_name}'), n=1)
        yield from f"""
def __{self.controller_set_checked_function_name}(checked:bool):
    self.{checked_name} = checked""".splitlines()
        yield from indent(self.hide_show_checked_generator.generate_set(f'self.{checked_name}'), n=1)
        yield f'self.{self.q_widget_name}.clicked.connect(__{self.handler_check_changed_function_name})'
        yield from generate_link_controller(self, f'__{self.controller_set_checked_function_name}',
                                       self.controller_set_checked_function_name)
        # hide the checked image
        yield from self.hide_show_checked_generator.generate_set('False')

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_check_changed_function_name}(cls, checked:bool) :
    print("Checkbox {self.q_widget_name} checked = " + str(checked))""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_checked_function_name}(cls, checked:bool) :
    print("The function {self.controller_set_checked_function_name} is unfortunately not linked to the controller")""".splitlines()
