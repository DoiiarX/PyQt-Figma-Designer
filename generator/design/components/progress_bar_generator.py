from generator.design.component_generator import ComponentGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.utils import indent, generate_link_controller


class ProgressBarGenerator(ComponentGenerator):
    controller_set_progress_function_name: str

    prefix_rule = 'progress_bar'

    def generate_design(self):
        fill_generator = self.group_generator.children[-1]
        geometry_generator = GeometryGenerator(fill_generator)
        self.controller_set_progress_function_name = f'{self.q_widget_name}_set_progress'

        yield f'def __{self.controller_set_progress_function_name}(progress:float) :'
        x, y, width, height = self.bounds
        new_bounds = (x, y, f'{width} * progress', height)
        yield from indent(geometry_generator.generate_set(new_bounds), n=1)
        yield from generate_link_controller(self, f'__{self.controller_set_progress_function_name}',
                                            self.controller_set_progress_function_name)

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_progress_function_name}(cls, progress:float) :
    print("Progress bar {self.q_widget_name} progress = " + str(progress))""".splitlines()
