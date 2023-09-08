from overrides import override

from generator.python_generator.base_generator import BaseGenerator


class ButtonGenerator(BaseGenerator):
    handler_functions: list

    def __init__(self, name, bounds, parent):
        super().__init__(name, bounds, parent)
        self.handler_functions = []

    def generate_design(self):
        yield f'{self.name} = QPushButton(central_widget)'
        yield f'{self.name}.setGeometry({self.pyqt_bounds})'
        yield f'{self.name}.setFlat(True)'
        yield f'{self.name}.setAutoFillBackground(False)'
        yield f'{self.name}.setObjectName("{self.name}")'
        yield f'{self.name}.setMouseTracking(True)'
        yield f'{self.name}.setContextMenuPolicy(Qt.NoContextMenu)'
        yield f'{self.name}.setAcceptDrops(False)'
        handler_function_name = f'{self.name}_clicked'
        self.handler_functions.append(f"""
@classmethod
def {handler_function_name}(cls) : 
    print("Button {self.name} clicked")""")
        yield from f"""def __{handler_function_name}(self):
    try : 
        GuiHandler.{handler_function_name}()
    except :
        print("No function {handler_function_name} defined")""".splitlines()
        yield f'{self.name}.clicked.connect(__{handler_function_name})'
        yield f'{self.name}.setFocusPolicy(Qt.NoFocus)'
        yield f'{self.name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")'

    def generate_handler(self):
        for fun in self.handler_functions:
            yield from fun.splitlines()
