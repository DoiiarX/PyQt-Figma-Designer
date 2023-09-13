from typing import Iterator


def indent(c: str | Iterator[str], n: int = 1) -> Iterator[str]:
    if isinstance(c, str):
        for line in c.splitlines():
            yield '    ' * n + line
        return

    for line in c:
        yield '    ' * n + line


def generate_link_controller(generator, lambda_function_name: str, controller_function_name: str):
    yield from f"""try :
    GuiController.{generator.controller_class_path}.{controller_function_name} = {lambda_function_name}
except NameError:
    print("No function {controller_function_name} defined in class {generator.controller_class_path}")
except Exception as e:
    print("Caught exception while trying to set the function {generator.controller_class_path}.{controller_function_name} : " + str(e))""".splitlines()


def generate_activate_handler(generator, handler_function_name: str, value: str | None = None):
    value = '' if value is None else value
    yield from f"""try :
    GuiHandler.{generator.handler_class_path}.{handler_function_name}({value})
except NameError:
    print("No function {handler_function_name} defined in class {generator.handler_class_path}")
except Exception as e:
    print("Caught exception while trying to call {generator.handler_class_path}.{handler_function_name} : " + str(e))""".splitlines()


def generate_q_widget(generator):
    yield from f"""self.{generator.q_widget_name} = QWidget(self.{generator.parent.q_widget_name})
self.{generator.q_widget_name}.setGeometry({generator.pyqt_bounds})
self.{generator.q_widget_name}.setObjectName("{generator.q_widget_name}")""".splitlines()
