from generator.design.component_generator import ComponentGenerator
from generator.design.components.button_generator import ButtonGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.utils import indent, generate_controller_setup, generate_handler_call, generate_print, \
    generate_controller_function, generate_handler_function, generate_get_component_config, \
    generate_q_push_button_create, generate_q_widget_create


class TabsViewGenerator(ComponentGenerator):
    handler_tab_changed_function_name: str
    controller_set_tab_function_name: str

    prefix_rule = 'tabs_view'
    component_name = 'tabs_view'
    component_config = {'default_tab': 0}

    def generate_design(self):
        self.handler_tab_changed_function_name = f'{self.q_widget_name}_tab_changed'
        self.controller_set_tab_function_name = f'{self.q_widget_name}_set_tab'

        if len(self.group_generator.children) < 2:
            raise Exception(f'Tabs view {self.q_widget_name} should have at least 2 children')

        tab_bar = self.group_generator.children[-1].children[0].children
        tabs_content = self.group_generator.children[-2].children[0].children
        tabs = list(reversed(list(zip(tab_bar, tabs_content))))
        default_tab = generate_get_component_config(self, 'default_tab')

        yield f'def __select_tab(i):'
        for j, (tab_bar_button, tab_content) in enumerate(tabs):
            yield from indent(VisibilityGenerator(tab_content).generate_set(f'i == {j}'), n=1)
            yield from indent(VisibilityGenerator(tab_bar_button).generate_set(f'i == {j}'), n=1)
        yield from indent(generate_handler_call(self, self.handler_tab_changed_function_name, 'i'), n=1)

        for i, _ in enumerate(tabs):
            yield f'__select_tab_{i} = lambda: __select_tab({i})'

        yield from generate_q_widget_create(self)
        for i, (tab_bar_button, tab_content) in enumerate(tabs):
            tab_button_generator = ButtonGenerator(tab_bar_button)
            yield from tab_button_generator.generate_design()
            yield f'self.{tab_button_generator.q_widget_name}.setParent(self.{self.q_widget_name})'
            yield f'self.{tab_button_generator.q_widget_name}.clicked.connect(__select_tab_{i})'
        yield f'__select_tab({default_tab})'
        yield from generate_controller_setup(self, f'__select_tab', self.controller_set_tab_function_name)

    def generate_handler(self):
        yield from generate_handler_function(self.handler_tab_changed_function_name, 'tab:int')

    def generate_controller(self):
        yield from generate_controller_function(self.controller_set_tab_function_name, 'tab:int')
