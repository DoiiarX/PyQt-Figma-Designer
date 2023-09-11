from generator.design.core.group_generator import GroupGenerator
from generator.design.core.text_generator import TextGenerator
from generator.design.design_generator import DesignGenerator
from generator.design.core.frame_generator import FrameGenerator


class CustomTextFieldGenerator(DesignGenerator):
    handler_text_changed_function_name: str
    controller_set_text_function_name: str
    text_field_text: TextGenerator | None
    text_field_hint: TextGenerator | None
    text_field_bounds: str

    def __init__(self, fig_node, parent, group_generator: GroupGenerator):
        super().__init__(fig_node, parent)
        text_field_text = group_generator.children[-1]
        while not isinstance(text_field_text, TextGenerator):
            text_field_text = text_field_text.children[-1]
        self.text_field_text = text_field_text

        text_field_hint = group_generator.children[-2]
        while not isinstance(text_field_hint, TextGenerator):
            text_field_hint = text_field_hint.children[-1]
        self.text_field_hint = text_field_hint

        self.text_field_bounds = group_generator.children[-3].pyqt_bounds

    def generate_design(self):
        frame = FrameGenerator.get_current_frame(self)
        self.handler_text_changed_function_name = f'{self.name}_text_changed'
        self.controller_set_text_function_name = f'{self.name}_set_text'

        yield from f"""
{self.name} = QLineEdit(central_widget)
{self.name}.setGeometry({self.text_field_bounds})
{self.name}.setAutoFillBackground(False)
{self.name}.setObjectName("{self.name}")
{self.name}.setMouseTracking(True)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)
{self.name}.setAcceptDrops(False)
{self.name}.setFont({self.text_field_text.name}.font())
text_color = {self.text_field_text.name}.styleSheet().split("color: ")[1].split(";")[0]
{self.text_field_text.name}.setStyleSheet("color: rgba(255, 255, 255, 0);")
{self.text_field_text.name}.hide()
{self.name}.setStyleSheet("color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
try :
    GuiController.{frame.controller_class_name}.{self.controller_set_text_function_name} = {self.name}.setText
except :
    print("No function {self.controller_set_text_function_name} defined. Current text : " + {self.name}.text())

def __{self.handler_text_changed_function_name}(*args, **kwargs):    
    if {self.name}.text() == "" :
        {self.text_field_hint.name}.show()
    else :
        {self.text_field_hint.name}.hide()
        {self.text_field_text.controller_set_text_function_name}({self.name}.text())              
           
    try : 
        current_text = {self.name}.text()
        GuiHandler.{frame.handler_class_name}.{self.handler_text_changed_function_name}(current_text)
    except :
        print("No function {self.handler_text_changed_function_name} defined. Current text : " + current_text)

__{self.handler_text_changed_function_name}()   
{self.name}.textChanged.connect(__{self.handler_text_changed_function_name})""".splitlines()

    def generate_handler(self):
        yield from f"""
@classmethod
def {self.handler_text_changed_function_name}(cls, text:str) :
    print("Text field {self.handler_text_changed_function_name} text changed to text : " + text)""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_text_function_name}(cls, text:str):
    print("The function {self.controller_set_text_function_name} is unfortunately not linked to the controller")
    return ''""".splitlines()
