from generator.design.component_generator import ComponentGenerator
from generator.design.components.slider_generator import SliderGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.utils import generate_q_widget_create, indent


class ScrollViewGenerator(ComponentGenerator):
    component_name = 'v_scroll_view'

    def generate_design(self):
        scroll_bar_group: GroupGenerator = self.group_generator.children[-1].children[0]  # type: ignore
        content = self.group_generator.children[-2]
        content_geometry_generator = GeometryGenerator(content)
        slider_generator = SliderGenerator(scroll_bar_group.figma_node, scroll_bar_group.parent, scroll_bar_group)
        slider_generator.component_config['default_value'] = 0
        cx, cy, cw, ch = content.bounds
        sx, sy, sw, sh = self.bounds
        y = f'{cy} - ({ch} - {sh}) * value'
        content_new_bounds = (cx, y, cw, ch)

        yield from slider_generator.generate_design(orientation='vertical')
        yield f'def __{self.q_widget_name}_update_content_bounds(value):'
        yield from indent(content_geometry_generator.generate_set(content_new_bounds))
        yield from f"""def {self.q_widget_name}_link_slider():
    f = {slider_generator.handler_class_path}.{slider_generator.handler_value_changed_function_name}
    def decorator(value) : 
        __{self.q_widget_name}_update_content_bounds(value)
        f(value)
    {slider_generator.handler_class_path}.{slider_generator.handler_value_changed_function_name} = decorator
{self.q_widget_name}_link_slider()
""".splitlines()
        yield f''
