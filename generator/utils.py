"""
Utility functions for the generator.
"""
import importlib.util
import inspect
import os
from typing import Iterator

import config
import logging

logging.basicConfig(level=logging.DEBUG)


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


def generate_get_component_config(generator: 'DesignGenerator', component_config_key: str) -> str:
    """
    Generate the code to get the value of the given component config key.
    Args:
        generator: The generator that will generate the code.
        component_config_key: The key of the component config to get.
    returns:
        A string containing the code to get the value of the given component config key.
    """
    return f'{generator.config_class_path}.{component_config_key}'


def generate_handler_function(handler_function_name: str, *args) -> Iterator[str]:
    """
    Generate the code for the given handler function with the given args.
    Args:
        handler_function_name: The name of the handler function to generate.
        args: The arguments to pass to the handler function.
    returns:
        An iterator of strings containing the code for the given handler function with the given args.
    """
    args = 'cls' + (', ' + ', '.join(args) if args else '')
    yield from f"""@classmethod
def {handler_function_name}({args}) : 
    {generate_print(f"'Handler {handler_function_name} called with args ' + str(list(locals().items())[1:])")}""".splitlines()


def generate_controller_function(controller_function_name: str, *args) -> Iterator[str]:
    """
    Generate the code for the given controller function with the given args.
    Args:
        controller_function_name: The name of the controller function to generate.
        args: The arguments to pass to the controller function.
    returns:
        An iterator of strings containing the code for the given controller function with the given args.
    """
    args = 'cls' + (', ' + ', '.join(args) if args else '')
    yield from f"""@classmethod
def {controller_function_name}({args}) : 
    {generate_print(f"'Controller {controller_function_name} is unfortunately not linked.'")}""".splitlines()


def generate_controller_setup(generator, lambda_function_name: str, controller_function_name: str) -> Iterator[str]:
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
    {generator.controller_class_path}.{controller_function_name} = {lambda_function_name}
except NameError:
    {generate_print(f"'No function {controller_function_name} defined in class {generator.controller_class_path}'")}
except Exception as e:
    {generate_print(f"'Caught exception while trying to set the function {generator.controller_class_path}.{controller_function_name} : ' + str(e)")}""".splitlines()


def generate_handler_call(generator: 'DesignGenerator', handler_function_name: str, *args) -> Iterator[str]:
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
    {generator.handler_class_path}.{handler_function_name}({value})
except NameError:
    {generate_print(f"'No function {handler_function_name} defined in class {generator.handler_class_path}'")}
except Exception as e:
    {generate_print(f"'Caught exception while trying to call {generator.handler_class_path}.{handler_function_name} : ' + str(e)")}""".splitlines()


def generate_q_widget_create(generator: 'DesignGenerator') -> Iterator[str]:
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


def generate_q_push_button_create(generator: 'ComponentGenerator') -> Iterator[str]:
    """
    Generate the code to create a QPushButton for the given generator (correct bounds). This QPushButton will be used
    as a source of events.
    Args:
        generator: The generator that will generate the code.
    returns:
        An iterator of strings containing the code to create a QPushButton for the given generator.
    """
    generator.component_config['pressed_color'] = generator.component_config.get('pressed_color', "'rgba(0, 0, 0, 0)'")
    generator.component_config['enabled'] = generator.component_config.get('enabled', True)
    background_color = generate_get_component_config(generator, 'pressed_color')
    enabled = generate_get_component_config(generator, 'enabled')
    yield from f"""try:
    __temp = self.{generator.q_widget_name}
except AttributeError:
    __temp = None
self.{generator.q_widget_name} = QPushButton(self.{generator.parent.q_widget_name})
self.{generator.q_widget_name}.setGeometry({generator.pyqt_bounds})
if __temp is not None:
    __temp.setParent(self.{generator.q_widget_name})
self.{generator.q_widget_name}.setFlat(True)
self.{generator.q_widget_name}.setAutoFillBackground(False)
self.{generator.q_widget_name}.setObjectName("{generator.q_widget_name}")
self.{generator.q_widget_name}.setMouseTracking(True)
self.{generator.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{generator.q_widget_name}.setAcceptDrops(False)
self.{generator.q_widget_name}.setEnabled({enabled})
self.{generator.q_widget_name}.setFocusPolicy(Qt.NoFocus)
self.{generator.q_widget_name}.setStyleSheet(f"background-color:" + {background_color})""".splitlines()


def generate_q_line_edit_create(generator: 'ComponentGenerator') -> Iterator[str]:
    """
    Generate the code to create a QLineEdit for the given generator (correct bounds). This QLineEdit will be used as
    a source of events.
    Args:
        generator: The generator that will generate the code.
    returns:
        An iterator of strings containing the code to create a QLineEdit for the given generator.
    """
    generator.component_config['text_color'] = generator.component_config.get('text_color',
                                                                              "'rgba(255, 255, 255, 255)'")
    generator.component_config['hint'] = generator.component_config.get('hint', "''")
    text_color = generate_get_component_config(generator, 'text_color')
    hint = generate_get_component_config(generator, 'hint')
    yield from f"""try:
    __temp = self.{generator.q_widget_name}
except AttributeError:
    __temp = None    
self.{generator.q_widget_name} = QLineEdit(self.{generator.parent.q_widget_name})
self.{generator.q_widget_name}.setGeometry({generator.pyqt_bounds})
if __temp is not None:
    self.{generator.q_widget_name}.setParent(__temp)
self.{generator.q_widget_name}.setAutoFillBackground(False)
self.{generator.q_widget_name}.setObjectName("{generator.q_widget_name}")
self.{generator.q_widget_name}.setMouseTracking(True)
self.{generator.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
self.{generator.q_widget_name}.setAcceptDrops(False)
self.{generator.q_widget_name}.setFont(QFont("Arial", 20 * {config.scale * config.text_scale}))
# set text color, hint color and hint
self.{generator.q_widget_name}.setStyleSheet("color: " + {text_color} + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
self.{generator.q_widget_name}.setPlaceholderText({hint})""".splitlines()


def generate_open_window(window_node_id: str) -> Iterator[str]:
    from generator.design.core.frame_generator import FrameGenerator
    window_name = FrameGenerator.get_window_name(window_node_id)
    yield from f"""window = {window_name}()
# close current window
MainWindow.close()
# open new window
self.MainWindow = QMainWindow()        
window.setupUi(self.MainWindow)
self.MainWindow.show()
app.exec()""".splitlines()


def generate_print(msg, level='logging.DEBUG') -> str:
    """
    Generate the code to print the given message.
    Args:
        msg: The message to print.
        level: The level of the message.
    returns:
        A string containing the code to print the given message.
    """
    return f'logging.log({level}, {msg})'


def get_generic_components() -> 'Iterator[ComponentGenerator]':
    """
    Get all the generic components from the generic_components_directory.
    returns:
        An iterator of classes that are generic components (subclasses of ComponentGenerator).
    """
    from generator.design.component_generator import ComponentGenerator
    module_files = [f for f in os.listdir(config.generic_components_directory) if f.endswith('.py')]
    # Remove the file extension to get module names.
    module_names = [os.path.splitext(f)[0] for f in module_files]
    for module_name in module_names:
        spec = importlib.util.spec_from_file_location(module_name,
                                                      os.path.join(config.generic_components_directory,
                                                                   module_name + '.py'))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, ComponentGenerator) and cls != ComponentGenerator:
                yield cls
