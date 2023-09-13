from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import generate_activate_handler, indent


class ButtonGenerator(DesignGenerator):
    handler_click_function_name: str

    def generate_design(self):
        self.handler_click_function_name = f'{self.q_widget_name}_clicked'
        yield from f"""
self.{self.q_widget_name} = QPushButton(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setGeometry({self.pyqt_bounds})
self.{self.q_widget_name}.setFlat(True)
self.{self.q_widget_name}.setAutoFillBackground(False)
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{self.q_widget_name}.setAcceptDrops(False)
def __{self.handler_click_function_name}(*args, **kwargs):""".splitlines()
        yield from indent(generate_activate_handler(self, self.handler_click_function_name))
        yield from f"""
self.{self.q_widget_name}.clicked.connect(__{self.handler_click_function_name})
self.{self.q_widget_name}.setFocusPolicy(Qt.NoFocus)
self.{self.q_widget_name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_click_function_name}(cls) : 
    print("Button {self.q_widget_name} clicked")""".splitlines()
