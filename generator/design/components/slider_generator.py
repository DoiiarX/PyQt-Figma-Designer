from generator.design.component_generator import ComponentGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.properties.parent_generator import ParentGenerator
from generator.utils import indent, generate_controller_setup, generate_handler_call, generate_print, \
    generate_controller_function, generate_handler_function, generate_get_component_config


class SliderGenerator(ComponentGenerator):
    controller_set_value_function_name: str
    handler_value_changed_function_name: str

    value_name : str

    component_name = 'slider'
    component_config = {'default_value': 0.5}

    def generate_design(self, orientation='horizontal'):
        function_update_thumb_position_name = f'__{self.q_widget_name}_update_thumb_position'
        self.controller_set_value_function_name = f'{self.q_widget_name}_set_value'
        self.handler_value_changed_function_name = f'{self.q_widget_name}_value_changed'
        thumb_generator = self.group_generator.children[-1]
        thumb_parent_generator = ParentGenerator(thumb_generator)
        thumb_geometry_generator = GeometryGenerator(thumb_generator)

        self.value_name = f'self.{self.q_widget_name}_value'
        captured_name = f'self.{self.q_widget_name}_captured'
        slider_x, slider_y, slider_width, slider_height = self.bounds
        thumb_x, thumb_y, thumb_width, thumb_height = thumb_generator.bounds
        # place the thumb at the value position between the slider bounds
        if orientation == 'horizontal':
            new_thumb_bounds = (f'{slider_x} + {slider_width - thumb_width} * {self.value_name}',
                                thumb_y, thumb_width * 2, thumb_height * 2)
        else:
            new_thumb_bounds = (thumb_x, f'{slider_y} + {slider_height - thumb_height} * {self.value_name}',
                                thumb_width * 2, thumb_height * 2)
        default_value = generate_get_component_config(self, 'default_value')
        # capture mouse and deploy the thumb at the mouse position when clicked
        yield from f"""
{captured_name} = False
{self.value_name} = {default_value}
def {function_update_thumb_position_name}(*args, **kwargs):
    if {captured_name} and len(args) > 0 :
        x, y, width, height = {self.bounds}
        event = args[0]
        mouse_x, mouse_y = event.x(), event.y()
        {self.value_name} = {'mouse_x / width' if orientation == 'horizontal' else 'mouse_y / height'}
        if {self.value_name} < 0 :
            {self.value_name} = 0
        if {self.value_name} > 1 :
            {self.value_name} = 1""".splitlines()
        yield from indent(generate_handler_call(self, self.handler_value_changed_function_name, f'{self.value_name}'),
                          n=2)
        yield from indent(thumb_geometry_generator.generate_set(new_thumb_bounds), n=1)
        yield from f"""
def __{self.q_widget_name}_mouse_press(*args, **kwargs):
    {captured_name} = True
    {function_update_thumb_position_name}(*args, **kwargs)

def __{self.q_widget_name}_mouse_release(*args, **kwargs):
    {captured_name} = False

def __{self.q_widget_name}_mouse_move(*args, **kwargs):          
    {function_update_thumb_position_name}(*args, **kwargs)

def __{self.controller_set_value_function_name}(value:float) :
    {self.value_name} = value
    {function_update_thumb_position_name}()

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
self.{self.q_widget_name}.mouseMoveEvent = __{self.q_widget_name}_mouse_move""".splitlines()
        yield from generate_controller_setup(self, f'__{self.controller_set_value_function_name}',
                                             self.controller_set_value_function_name)
        yield f'__{self.q_widget_name}_update_thumb_position()'
        yield from thumb_parent_generator.generate_set(f'self.{self.q_widget_name}')

    def generate_controller(self):
        yield from generate_controller_function(self.controller_set_value_function_name, 'value:float')

    def generate_handler(self):
        yield from generate_handler_function(self.handler_value_changed_function_name, 'value:float')
