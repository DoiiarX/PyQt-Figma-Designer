from generator.design.component_generator import ComponentGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.utils import *


class ProgressBarGenerator(ComponentGenerator):
    controller_set_progress_function_name: str

    component_name = 'progress_bar'
    orientable = True
    component_config = {'default_progress': 0.5}

    def generate_design(self, orientation='horizontal'):
        fill_generator = self.group_generator.children[-1]
        geometry_generator = GeometryGenerator(fill_generator)
        self.controller_set_progress_function_name = f'{self.q_widget_name}_set_progress'
        progress = generate_get_component_config(self, 'default_progress')
        x, y, width, height = self.bounds
        if orientation == 'horizontal':
            new_bounds = (x, y, f'{width} * progress', height)
        else:
            new_bounds = (x, y, width, f'{height} * progress')

        yield f'def __{self.controller_set_progress_function_name}(progress:float) :'
        yield from indent(geometry_generator.generate_set(new_bounds), n=1)
        yield from generate_controller_setup(self, f'__{self.controller_set_progress_function_name}',
                                             self.controller_set_progress_function_name)
        yield f'__{self.controller_set_progress_function_name}({progress})'

    def generate_controller(self):
        yield from generate_controller_function(self.controller_set_progress_function_name, 'progress:float')
