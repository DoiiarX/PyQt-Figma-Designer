from generator.design.core.frame_generator import FrameGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.design_generator import DesignGenerator
from generator.properties.geometry_generator import GeometryGenerator
from utils import indent


class SliderGenerator(DesignGenerator):
    thumb_generator: GeometryGenerator
    controller_set_value_function_name: str
    handler_value_changed_function_name: str

    def __init__(self, fig_node, parent, group_generator: GroupGenerator):
        super().__init__(fig_node, parent)
        thumb_generator = group_generator.children[-1]
        self.thumb_generator = GeometryGenerator(thumb_generator)
        self.controller_set_value_function_name = f'{self.name}_set_value'
        self.handler_value_changed_function_name = f'{self.name}_value_changed'

    def generate_design(self):
        frame = FrameGenerator.get_current_frame(self)
        value_name = f'self.{self.name}_value'
        captured_name = f'self.{self.name}_captured'
        slider_x, slider_y, slider_width, slider_height = self.bounds
        _, thumb_y, thumb_width, thumb_height = self.thumb_generator.target_generator.bounds
        # place the thumb at the value position between the slider bounds
        new_thumb_bounds = (f'{slider_x} + {slider_width} * {value_name} - {thumb_width / 2}',
                            thumb_y, thumb_width * 2, thumb_height * 2)

        # capture mouse and deploy the thumb at the mouse position when clicked
        yield from f"""
{captured_name} = False
{value_name} = 0.5
def __{self.name}_update_thumb_position(*args, **kwargs):""".splitlines()
        yield from indent(self.thumb_generator.generate_set(new_thumb_bounds), n=1)
        yield from f"""
    if {captured_name} and len(args) > 0 :
        x, y, width, height = {self.bounds}
        event = args[0]
        mouse_x, mouse_y = event.x(), event.y()
        {value_name} = mouse_x / width
        if {value_name} < 0 :
            {value_name} = 0
        if {value_name} > 1 :
            {value_name} = 1
        try :
            GuiHandler.{frame.handler_class_name}.{self.handler_value_changed_function_name}({value_name})
        except : 
            print("No function {self.handler_value_changed_function_name} defined. Value = " + str({value_name}))
def __{self.name}_mouse_press(*args, **kwargs):
    {captured_name} = True
    __{self.name}_update_thumb_position(*args, **kwargs)

def __{self.name}_mouse_release(*args, **kwargs):
    {captured_name} = False

def __{self.name}_mouse_move(*args, **kwargs):          
    __{self.name}_update_thumb_position(*args, **kwargs)

def __{self.controller_set_value_function_name}(cls, value:float) :
    {value_name} = value
    __{self.name}_update_thumb_position()

{self.name} = QPushButton(central_widget)
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setFlat(True)
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
{self.name}.setFocusPolicy(Qt.NoFocus)
{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
{self.name}.mousePressEvent = __{self.name}_mouse_press
{self.name}.mouseReleaseEvent = __{self.name}_mouse_release
{self.name}.mouseMoveEvent = __{self.name}_mouse_move
try :
    GuiController.{frame.controller_class_name}.{self.controller_set_value_function_name} = __{self.controller_set_value_function_name}
except :
    print("No function {self.controller_set_value_function_name} defined. Value = " + str({value_name}))

__{self.name}_update_thumb_position()""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_value_function_name}(cls, value:float) :
    print("Progress bar {self.name} value = " + str(value))
""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_value_changed_function_name}(cls, value:float) :
    print("Progress bar {self.name} value changed = " + str(value))
""".splitlines()
