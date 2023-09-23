from generator.design.component_generator import ComponentGenerator
from generator.design.components.slider_generator import SliderGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.properties.parent_generator import ParentGenerator
from generator.utils import *


class ScrollViewGenerator(ComponentGenerator):
    component_name = 'scroll_view'
    orientable = True

    def generate_design(self, orientation='vertical'):
        scroll_bar_group: GroupGenerator = self.group_generator.children[-1].children[0]  # type: ignore
        content = self.group_generator.children[-2]
        content_geometry_generator = GeometryGenerator(content)
        slider_generator = SliderGenerator(scroll_bar_group)
        slider_generator.component_config['default_value'] = 0
        cx, cy, cw, ch = content.bounds
        sx, sy, sw, sh = self.bounds
        tx, ty, tw, th = scroll_bar_group.bounds
        if orientation == 'vertical':
            y = f'{cy} - ({ch} - {sh}) * value'
            content_new_bounds = (cx, y, cw, ch)
        else:
            x = f'{cx} - ({cw} - {sw}) * value'
            content_new_bounds = (x, cy, cw, ch)
        # generate empty button to capture mouse wheel events
        yield from generate_q_widget_create(self)
        yield from f"""self.{self.q_widget_name}.setFocusPolicy(Qt.NoFocus)
self.{self.q_widget_name}.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
self.{self.q_widget_name}.setObjectName("{self.q_widget_name}")
self.{self.q_widget_name}.setMouseTracking(True)""".splitlines()
        yield from slider_generator.generate_design(orientation=f'{orientation}')
        yield f'def __{self.q_widget_name}_update_content_bounds(value):'
        yield from indent(content_geometry_generator.generate_set(content_new_bounds))
        axis = 'y' if orientation == 'vertical' else 'x'
        yield from f"""def __{self.q_widget_name}_wheel_event(event):
    value = {slider_generator.value_name}
    value -= event.angleDelta().{axis}() / 120 / 10
    if value < 0 :
        value = 0
    if value > 1 :
        value = 1
    {slider_generator.controller_class_path}.{slider_generator.controller_set_value_function_name}(value)
    __{self.q_widget_name}_update_content_bounds(value)
self.{self.q_widget_name}.wheelEvent = __{self.q_widget_name}_wheel_event""".splitlines()
        yield from generate_decorate_handler(slider_generator,
                                             slider_generator.handler_value_changed_function_name,
                                             [f'__{self.q_widget_name}_update_content_bounds(value)'].__iter__(),
                                             'value')
        yield from ParentGenerator(self).generate_set(f'self.{self.group_generator.q_widget_name}')
        yield from ParentGenerator(slider_generator).generate_set(f'self.{self.group_generator.q_widget_name}')
        yield from GeometryGenerator(slider_generator).generate_set((sx + sw - tw, sy + sh - th, tw, sh))
        yield from generate_handler_call(slider_generator, slider_generator.handler_value_changed_function_name, '0')
