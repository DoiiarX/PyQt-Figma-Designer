from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.design.core.frame_generator import FrameGenerator
from utils import indent


class CustomButtonGenerator(DesignGenerator):
    handler_click_function_name: str
    controller_enable_function_name: str
    controller_disable_function_name: str

    def __init__(self, fig_node, parent, group_generator: GroupGenerator):
        super().__init__(fig_node, parent)
        if len(group_generator.children) < 4:
            raise Exception(f'Custom button {self.name} should have at least 4 children')
        self.hide_show_mouse_over_generator = VisibilityGenerator(group_generator.children[-1])
        self.hide_show_pressed_generator = VisibilityGenerator(group_generator.children[-2])
        self.hide_show_disabled_generator = VisibilityGenerator(group_generator.children[-3])

    def generate_design(self):
        self.handler_click_function_name = f'{self.name}_clicked'
        self.controller_enable_function_name = f'{self.name}_enable'
        self.controller_disable_function_name = f'{self.name}_disable'
        frame = FrameGenerator.get_current_frame(self)

        yield from f"""
{self.name} = QPushButton(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setFlat(True)
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
{self.name}.setFocusPolicy(Qt.NoFocus)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0);")""".splitlines()

        # Mouse over
        yield f'def __{self.name}_mouse_over(*args, **kwargs):'
        yield from indent(self.hide_show_mouse_over_generator.generate_set('True'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('False'))

        # Mouse leave
        yield f'def __{self.name}_mouse_leave(*args, **kwargs):'
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('False'))

        # Mouse press
        yield f'def __{self.name}_mouse_press(*args, **kwargs):'
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'))
        yield from indent(self.hide_show_pressed_generator.generate_set('True'))
        yield from indent(self.hide_show_disabled_generator.generate_set('False'))

        # Mouse release
        yield f'def __{self.name}_mouse_release(*args, **kwargs):'
        yield from indent(self.hide_show_mouse_over_generator.generate_set('True'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('False'))

        # Disable
        # create rectangle to cover the button to avoid mouse events
        disable_rectangle_name = f'{self.name}_disabled_rectangle'
        yield from f"""{disable_rectangle_name}= QLabel(central_widget)
{disable_rectangle_name}.setGeometry({self.pyqt_bounds})
{disable_rectangle_name}.setObjectName("{disable_rectangle_name}")
{disable_rectangle_name}.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
{disable_rectangle_name}.setVisible(False)""".splitlines()

        yield from f"""def __{self.name}_disable(*args, **kwargs):
    {disable_rectangle_name}.setVisible(True)""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('True'))
        # disable capture mouse events
        yield from indent(f'{self.name}.setMouseTracking(False)')
        yield from indent(f'{self.name}.setFocusPolicy(Qt.NoFocus)')
        yield from indent(f'{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0);")')

        # Enable
        yield from f"""def __{self.name}_enable(*args, **kwargs):
    {disable_rectangle_name}.setVisible(False)""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('False'))
        # enable capture mouse events
        yield from indent(f'{self.name}.setMouseTracking(True)')

        # Click handler
        yield from f"""
def __{self.handler_click_function_name}():
    try :
        GuiHandler.{frame.handler_class_name}.{self.handler_click_function_name}()
    except :
        print("No function {self.handler_click_function_name} defined")""".splitlines()

        # Connect signals
        yield from f"""
{self.name}.clicked.connect(__{self.handler_click_function_name})
{self.name}.enterEvent = __{self.name}_mouse_over
{self.name}.leaveEvent = __{self.name}_mouse_leave
{self.name}.mousePressEvent = __{self.name}_mouse_press
{self.name}.mouseReleaseEvent = __{self.name}_mouse_release
{self.name}.disable = __{self.name}_disable
{self.name}.enable = __{self.name}_enable""".splitlines()

        # Connect controller
        yield from f"""
try :
    GuiController.{frame.controller_class_name}.{self.controller_enable_function_name} = {self.name}.enable
    GuiController.{frame.controller_class_name}.{self.controller_disable_function_name} = {self.name}.disable
except :
    print("No function {self.controller_enable_function_name} defined")
    print("No function {self.controller_disable_function_name} defined")""".splitlines()

        # hide the mouse over, pressed and disabled children
        yield from self.hide_show_mouse_over_generator.generate_set('False')
        yield from self.hide_show_pressed_generator.generate_set('False')
        yield from self.hide_show_disabled_generator.generate_set('False')

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_click_function_name}(cls):
    print("CustomButton {self.name} clicked")
""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_enable_function_name}(cls):
     print("The function {self.controller_enable_function_name} is unfortunately not linked to the controller")
 
@classmethod
def {self.controller_disable_function_name}(cls):
        print("The function {self.controller_disable_function_name} is unfortunately not linked to the controller")
""".splitlines()
