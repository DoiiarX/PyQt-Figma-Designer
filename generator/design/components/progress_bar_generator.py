from generator.design.core.frame_generator import FrameGenerator
from generator.design.core.group_generator import GroupGenerator
from generator.design.design_generator import DesignGenerator
from generator.properties.geometry_generator import GeometryGenerator
from generator.utils import indent


class ProgressBarGenerator(DesignGenerator):
    fill_geometry_generator: GeometryGenerator
    controller_set_progress_function_name: str

    def __init__(self, figma_node, parent, group_generator: GroupGenerator):
        super().__init__(figma_node, parent)
        fill_generator = group_generator.children[-1]
        self.geometry_generator = GeometryGenerator(fill_generator)
        self.controller_set_progress_function_name = f'{self.q_widget_name}_set_progress'

    def generate_design(self):

        yield f'def __{self.controller_set_progress_function_name}(progress:float) :'
        x, y, width, height = self.bounds
        new_bounds = (x, y, f'{width} * progress', height)
        yield from indent(self.geometry_generator.generate_set(new_bounds), n=1)
        yield from f"""
try :
    GuiController.{self.controller_class_path}.{self.controller_set_progress_function_name} = __{self.controller_set_progress_function_name}    
except NameError:
    print("No function {self.controller_set_progress_function_name} defined.")
except Exception as e:
    print("Caught exception while trying to call {self.controller_set_progress_function_name} : " + str(e))
""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_progress_function_name}(cls, progress:float) :
    print("Progress bar {self.q_widget_name} progress = " + str(progress))""".splitlines()
