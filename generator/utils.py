"""
Utility functions for the generator.
"""
import importlib.util
import inspect
import os
from typing import Iterator

from config import generic_components_directory


def indent(c: str | Iterator[str], n: int = 1) -> Iterator[str]:
    """
    Indent the given string or iterator of strings by n tabs.
    Args:
        c: The string or iterator of strings to indent.
        n: The number of tabs to indent by.
    returns:
        An iterator of strings with n tabs prepended to each string.
    """
    if isinstance(c, str):
        for line in c.splitlines():
            yield '    ' * n + line
        return

    for line in c:
        yield '    ' * n + line


def generate_link_controller(generator, lambda_function_name: str, controller_function_name: str):
    """
    Generate the code to link the given lambda function to the given controller function.
    Args:
        generator: The generator that will generate the code.
        lambda_function_name: The name of the lambda function to link.
        controller_function_name: The name of the controller function to link to.
    returns:
        An iterator of strings containing the code to link the given lambda function to the given controller function.
    """
    yield from f"""try :
    GuiController.{generator.controller_class_path}.{controller_function_name} = {lambda_function_name}
except NameError:
    print("No function {controller_function_name} defined in class {generator.controller_class_path}")
except Exception as e:
    print("Caught exception while trying to set the function {generator.controller_class_path}.{controller_function_name} : " + str(e))""".splitlines()


def generate_activate_handler(generator, handler_function_name: str, *args):
    """
    Generate the code to call the given handler function with the given value.
    Args:
        generator: The generator that will generate the code.
        handler_function_name: The name of the handler function to call.
        args: The arguments to pass to the handler function.
    returns:
        An iterator of strings containing the code to call the given handler function with the given args.
    """
    value = ', '.join(args)
    yield from f"""try :
    GuiHandler.{generator.handler_class_path}.{handler_function_name}({value})
except NameError:
    print("No function {handler_function_name} defined in class {generator.handler_class_path}")
except Exception as e:
    print("Caught exception while trying to call {generator.handler_class_path}.{handler_function_name} : " + str(e))""".splitlines()


def generate_q_widget(generator):
    """
    Generate the code to create an empty QWidget for the given generator (correct bounds). This QWidget will be used as
    the parent of the generated subcomponents.
    Args:
        generator: The generator that will generate the code.
    returns:
        An iterator of strings containing the code to create an empty QWidget for the given generator.
    """
    yield from f"""self.{generator.q_widget_name} = QWidget(self.{generator.parent.q_widget_name})
self.{generator.q_widget_name}.setGeometry({generator.pyqt_bounds})
self.{generator.q_widget_name}.setObjectName("{generator.q_widget_name}")""".splitlines()


def get_generic_components():
    """
    Get all the generic components from the generic_components_directory.
    returns:
        An iterator of classes that are generic components (subclasses of ComponentGenerator).
    """
    from generator.design.component_generator import ComponentGenerator
    module_files = [f for f in os.listdir(generic_components_directory) if f.endswith('.py')]
    # Remove the file extension to get module names.
    module_names = [os.path.splitext(f)[0] for f in module_files]
    for module_name in module_names:
        spec = importlib.util.spec_from_file_location(module_name,
                                                      os.path.join(generic_components_directory, module_name + '.py'))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, ComponentGenerator) and cls != ComponentGenerator:
                yield cls
