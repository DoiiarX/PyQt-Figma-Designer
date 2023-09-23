from generator.design.component_generator import ComponentGenerator
from generator.design.components.slider_generator import SliderGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.properties.parent_generator import ParentGenerator
from generator.utils import generate_q_widget_create, indent


class ScrollViewGenerator(ComponentGenerator):
    component_name = 'v_scroll_view'

    def generate_design(self):
        scroll_bar_group: GroupGenerator = self.group_generator.children[-1].children[0]  # type: ignore
        content = self.group_generator.children[-2]
        content_geometry_generator = GeometryGenerator(content)
        slider_generator = SliderGenerator(scroll_bar_group)
        slider_generator.component_config['default_value'] = 0
        cx, cy, cw, ch = content.bounds
        sx, sy, sw, sh = self.bounds
        tx, ty, tw, th = scroll_bar_group.bounds
        y = f'{cy} - ({ch} - {sh}) * value'
        content_new_bounds = (cx, y, cw, ch)
        # generate empty button to capture mouse wheel events
        yield from generate_q_widget_create(self)
        yield from f"""self.{self.q_widget_name}.setFocusPolicy(Qt.NoFocus)
self.{self.q_widget_name}.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)""".splitlines()
        yield from slider_generator.generate_design(orientation='vertical')
        yield f'def __{self.q_widget_name}_update_content_bounds(value):'
        yield from indent(content_geometry_generator.generate_set(content_new_bounds))
        yield from f"""def __{self.q_widget_name}_wheel_event(event):
    value = {slider_generator.value_name}
    value -= event.angleDelta().y() / 120 / 10
    if value < 0 :
        value = 0
    if value > 1 :
        value = 1
    {slider_generator.controller_class_path}.{slider_generator.controller_set_value_function_name}(value)
    __{self.q_widget_name}_update_content_bounds(value)
self.{self.q_widget_name}.wheelEvent = __{self.q_widget_name}_wheel_event
def {self.q_widget_name}_link_slider():
    f = {slider_generator.handler_class_path}.{slider_generator.handler_value_changed_function_name}
    def decorator(value) : 
        __{self.q_widget_name}_update_content_bounds(value)
        f(value)
    {slider_generator.handler_class_path}.{slider_generator.handler_value_changed_function_name} = decorator
{self.q_widget_name}_link_slider()
""".splitlines()
        yield from ParentGenerator(self).generate_set(f'self.{self.group_generator.q_widget_name}')
        yield from ParentGenerator(slider_generator).generate_set(f'self.{self.group_generator.q_widget_name}')
        yield from GeometryGenerator(slider_generator).generate_set((sx + sw - tw, sy, tw, sh))
