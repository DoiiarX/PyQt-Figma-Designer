from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator


class ButtonGenerator(DesignGenerator):
    handler_click_function_name: str

    def generate_design(self):
        self.handler_click_function_name = f'{self.q_widget_name}_clicked'
        yield from f"""
{self.q_widget_name} = QPushButton({self.parent.q_widget_name})
{self.q_widget_name}.setGeometry({self.pyqt_bounds})
{self.q_widget_name}.setFlat(True)
{self.q_widget_name}.setAutoFillBackground(False)
{self.q_widget_name}.setObjectName("{self.q_widget_name}")
{self.q_widget_name}.setMouseTracking(True)
{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.q_widget_name}.setAcceptDrops(False)
def __{self.handler_click_function_name}(*args, **kwargs):
    try : 
        GuiHandler.{self.handler_class_path}.{self.handler_click_function_name}()
    except :
        print("No function {self.handler_click_function_name} defined")
{self.q_widget_name}.clicked.connect(__{self.handler_click_function_name})
{self.q_widget_name}.setFocusPolicy(Qt.NoFocus)
{self.q_widget_name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_click_function_name}(cls) : 
    print("Button {self.q_widget_name} clicked")""".splitlines()
