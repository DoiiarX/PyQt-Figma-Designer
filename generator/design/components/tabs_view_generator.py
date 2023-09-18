from generator.design.component_generator import ComponentGenerator
from generator.properties.visibility_generator import VisibilityGenerator
from generator.utils import indent, generate_link_controller, generate_activate_handler, generate_print, \
    generate_controller, generate_handler, generate_get_component_config


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
        yield from indent(generate_activate_handler(self, self.handler_tab_changed_function_name, 'i'), n=1)

        for i, _ in enumerate(tabs):
            yield f'__select_tab_{i} = lambda: __select_tab({i})'

        yield f'self.{self.q_widget_name} = QLabel(self.{self.parent.q_widget_name})'
        for i, (tab_bar_button, tab_content) in enumerate(tabs):
            button_name = f'{tab_bar_button.q_widget_name}_button'
            yield from f"""
{button_name} = QPushButton(self.{tab_bar_button.parent.q_widget_name})
{button_name}.setGeometry({tab_bar_button.pyqt_bounds})
{button_name}.setFlat(True)
{button_name}.setObjectName("{button_name}")
{button_name}.setMouseTracking(True)
{button_name}.setContextMenuPolicy(Qt.NoContextMenu)
{button_name}.setAcceptDrops(False)
{button_name}.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
{button_name}.clicked.connect(__select_tab_{i})
__select_tab({default_tab})
""".splitlines()
            yield from generate_link_controller(self, f'__select_tab', self.controller_set_tab_function_name)

    def generate_handler(self):
        yield from generate_handler(self.handler_tab_changed_function_name, 'tab:int')

    def generate_controller(self):
        yield from generate_controller(self.controller_set_tab_function_name, 'tab:int')
