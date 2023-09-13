from generator.design.design_generator import DesignGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.design.core.frame_generator import FrameGenerator
from generator.utils import indent


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
        enabled_name = f'self.{self.name}_enabled'

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
{enabled_name} = True""".splitlines()

        # Mouse over
        yield from f"""def __{self.name}_mouse_over(*args, **kwargs):
    if {enabled_name} :""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('True'), n=2)
        yield from indent(self.hide_show_pressed_generator.generate_set('False'), n=2)
        yield from indent(self.hide_show_disabled_generator.generate_set('False'), n=2)

        # Mouse leave
        yield from f"""def __{self.name}_mouse_leave(*args, **kwargs):
    if {enabled_name} :""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'), n=2)
        yield from indent(self.hide_show_pressed_generator.generate_set('False'), n=2)
        yield from indent(self.hide_show_disabled_generator.generate_set('False'), n=2)

        # Mouse press
        yield from f"""def __{self.name}_mouse_press(*args, **kwargs):
    if {enabled_name} :""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'), n=2)
        yield from indent(self.hide_show_pressed_generator.generate_set('True'), n=2)
        yield from indent(self.hide_show_disabled_generator.generate_set('False'), n=2)

        # Mouse release
        yield from f"""def __{self.name}_mouse_release(*args, **kwargs):
    if {enabled_name} :""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('True'), n=2)
        yield from indent(self.hide_show_pressed_generator.generate_set('False'), n=2)
        yield from indent(self.hide_show_disabled_generator.generate_set('False'), n=2)
        yield from indent(f'{self.name}.clicked.emit()', n=2)

        # Disable

        yield from f"""def __{self.name}_disable(*args, **kwargs):
    {enabled_name} = False""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('True'))
        # disable capture mouse events
        yield from indent(f'{self.name}.setMouseTracking(False)')
        yield from indent(f'{self.name}.setFocusPolicy(Qt.NoFocus)')
        yield from indent(f'{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0);")')

        # Enable
        yield from f"""def __{self.name}_enable(*args, **kwargs):
    {enabled_name} = True""".splitlines()
        yield from indent(self.hide_show_mouse_over_generator.generate_set('False'))
        yield from indent(self.hide_show_pressed_generator.generate_set('False'))
        yield from indent(self.hide_show_disabled_generator.generate_set('False'))
        # enable capture mouse events
        yield from indent(f'{self.name}.setMouseTracking(True)')

        # Click handler
        yield from f"""
def __{self.handler_click_function_name}(*args, **kwargs):
    try :
        GuiHandler.{self.handler_class_path}.{self.handler_click_function_name}()
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
    GuiController.{self.controller_class_path}.{self.controller_enable_function_name} = {self.name}.enable
    GuiController.{self.controller_class_path}.{self.controller_disable_function_name} = {self.name}.disable
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
