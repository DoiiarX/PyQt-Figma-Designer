from generator.design.core.frame_generator import FrameGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.design_generator import DesignGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.properties.parent_generator import ParentGenerator
from generator.utils import indent


class SliderGenerator(DesignGenerator):
    controller_set_value_function_name: str
    handler_value_changed_function_name: str

    def __init__(self, figma_node, parent, group_generator: GroupGenerator):
        super().__init__(figma_node, parent)
        thumb_generator = group_generator.children[-1]
        self.thumb_parent_generator = ParentGenerator(thumb_generator)
        self.thumb_geometry_generator = GeometryGenerator(thumb_generator)
        self.controller_set_value_function_name = f'{self.q_widget_name}_set_value'
        self.handler_value_changed_function_name = f'{self.q_widget_name}_value_changed'

    def generate_design(self):
        value_name = f'self.{self.q_widget_name}_value'
        captured_name = f'self.{self.q_widget_name}_captured'
        slider_x, slider_y, slider_width, slider_height = self.bounds
        _, thumb_y, thumb_width, thumb_height = self.thumb_geometry_generator.target_generator.bounds
        # place the thumb at the value position between the slider bounds
        new_thumb_bounds = (f'{slider_x} + {slider_width - thumb_width} * {value_name}',
                            thumb_y, thumb_width * 2, thumb_height * 2)
        # capture mouse and deploy the thumb at the mouse position when clicked
        yield from f"""
{captured_name} = False
{value_name} = 0.5
def __{self.q_widget_name}_update_thumb_position(*args, **kwargs):
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
            GuiHandler.{self.handler_class_path}.{self.handler_value_changed_function_name}({value_name})
        except : 
            print("No function {self.handler_value_changed_function_name} defined. Value = " + str({value_name}))
""".splitlines()
        yield from indent(self.thumb_geometry_generator.generate_set(new_thumb_bounds), n=1)
        yield from f"""
def __{self.q_widget_name}_mouse_press(*args, **kwargs):
    {captured_name} = True
    __{self.q_widget_name}_update_thumb_position(*args, **kwargs)

def __{self.q_widget_name}_mouse_release(*args, **kwargs):
    {captured_name} = False

def __{self.q_widget_name}_mouse_move(*args, **kwargs):          
    __{self.q_widget_name}_update_thumb_position(*args, **kwargs)

def __{self.controller_set_value_function_name}(value:float) :
    {value_name} = value
    __{self.q_widget_name}_update_thumb_position()

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
self.{self.q_widget_name}.mousePressEvent = __{self.q_widget_name}_mouse_press
self.{self.q_widget_name}.mouseReleaseEvent = __{self.q_widget_name}_mouse_release
self.{self.q_widget_name}.mouseMoveEvent = __{self.q_widget_name}_mouse_move
try :
    GuiController.{self.controller_class_path}.{self.controller_set_value_function_name} = __{self.controller_set_value_function_name}    
except NameError:
    print("No function {self.controller_set_value_function_name} defined. Value = " + str({value_name}))
except Exception as e:
    print("Error while linking {self.controller_set_value_function_name} to {self.controller_class_path}.{self.controller_set_value_function_name} : " + str(e))
__{self.q_widget_name}_update_thumb_position()""".splitlines()
        yield from self.thumb_parent_generator.generate_set(f'self.{self.q_widget_name}')

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_value_function_name}(cls, value:float) :
    print("The function {self.controller_set_value_function_name} is unfortunately not linked to the controller")
""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_value_changed_function_name}(cls, value:float) :
    print("Slider {self.q_widget_name} value changed = " + str(value))
""".splitlines()
