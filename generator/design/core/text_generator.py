import config
from generator.design.core.frame_generator import FrameGenerator
from generator.design.design_generator import DesignGenerator


class TextGenerator(DesignGenerator):
    controller_set_text_function_name: str

    def generate_design(self):
        self.controller_set_text_function_name = f'{self.q_widget_name}_set_text'
        text = self.figma_node['characters'].replace('"', '\\"')
        font = self.figma_node['style']['fontFamily']
        font_size = self.figma_node['style']['fontSize'] * config.text_scale * config.scale
        color = 'rgba(0, 0, 0, 0)'
        if len(self.figma_node['fills']) > 0 and 'color' in self.figma_node['fills'][0]:
            color = self.figma_node['fills'][0]['color']
            color = f'rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {color.get("a", 1) * 255})'

        vertical_alignment_figma = self.figma_node['style']['textAlignVertical']
        horizontal_alignment_figma = self.figma_node['style']['textAlignHorizontal']
        match vertical_alignment_figma:
            case 'TOP':
                vertical_alignment = 'Qt.AlignTop'
            case 'BOTTOM':
                vertical_alignment = 'Qt.AlignBottom'
            case 'CENTER':
                vertical_alignment = 'Qt.AlignVCenter'
            case _:
                vertical_alignment = 'Qt.AlignVCenter'
        match horizontal_alignment_figma:
            case 'LEFT':
                horizontal_alignment = 'Qt.AlignLeft'
            case 'RIGHT':
                horizontal_alignment = 'Qt.AlignRight'
            case 'CENTER':
                horizontal_alignment = 'Qt.AlignHCenter'
            case 'JUSTIFIED':
                horizontal_alignment = 'Qt.AlignJustify'
            case _:
                horizontal_alignment = 'Qt.AlignHCenter'

        yield from f"""{self.q_widget_name} = QLabel(central_widget)
{self.q_widget_name}.setText("{text}")
font = QFont()
font.setFamilies([u"{font}"])
font.setPointSize({int(font_size)})
{self.q_widget_name}.setFont(font)
{self.q_widget_name}.setStyleSheet("color: {color}")
{self.q_widget_name}.setGeometry({self.pyqt_bounds})
{self.q_widget_name}.setAlignment({vertical_alignment} | {horizontal_alignment})
{self.q_widget_name}.setMouseTracking(False)
{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
def {self.controller_set_text_function_name}(text:str):
    {self.q_widget_name}.setText(text)

try :
    GuiController.{self.controller_class_path}.{self.controller_set_text_function_name} = {self.controller_set_text_function_name}
except :
    print("No function {self.controller_set_text_function_name} defined. Current text : " + {self.q_widget_name}.text())
""".splitlines()

    def generate_controller(self):
        yield from f"""
@classmethod
def {self.controller_set_text_function_name}(cls, text:str):
    print("The function {self.controller_set_text_function_name} is unfortunately not linked to the controller")""".splitlines()
