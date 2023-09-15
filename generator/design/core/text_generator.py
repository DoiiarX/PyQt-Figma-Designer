"""
This module contains the class TextGenerator that is used to generate every text in the design.
"""
from typing import Iterator

import config
from generator.design.design_generator import DesignGenerator


class TextGenerator(DesignGenerator):
    """
    Class used to generate every text in the design.
    """
    # The name of the function used to set the text of the text in the GuiController.
    controller_set_text_function_name: str

    @property
    def string(self):
        """
        Get the content of the text.
        returns:
            The content of the text.
        """
        return self.figma_node['characters'].replace('"', '\\"')

    @property
    def string_name(self):
        """
        Get the name of the string variable.
        returns:
            The name of the string variable.
        """
        return f'text_{self.q_widget_name}'.upper()

    def generate_design(self):
        __doc__ = super().generate_design().__doc__
        self.controller_set_text_function_name = f'{self.q_widget_name}_set_text'

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

        yield from f"""self.{self.q_widget_name} = QLabel(self.{self.parent.q_widget_name})
self.{self.q_widget_name}.setText(Strings.{self.strings_class_path}.{self.string_name})
font = QFont()
font.setFamilies([u"{font}"])
font.setPointSize({int(font_size)})
self.{self.q_widget_name}.setFont(font)
self.{self.q_widget_name}.setStyleSheet("color: {color}")
self.{self.q_widget_name}.setGeometry({self.pyqt_bounds})
self.{self.q_widget_name}.setAlignment({vertical_alignment} | {horizontal_alignment})
self.{self.q_widget_name}.setMouseTracking(False)
self.{self.q_widget_name}.setContextMenuPolicy(Qt.NoContextMenu)
def {self.controller_set_text_function_name}(text:str):
    self.{self.q_widget_name}.setText(text)

try :
    GuiController.{self.controller_class_path}.{self.controller_set_text_function_name} = {self.controller_set_text_function_name}
except NameError:
    print("No function {self.controller_set_text_function_name} defined. Current text : " + self.{self.q_widget_name}.text())
except Exception as e:
    print("Caught exception while trying to call {self.controller_set_text_function_name} : " + str(e))
""".splitlines()

    def generate_controller(self):
        __doc__ = super().generate_controller().__doc__
        yield from f"""
@classmethod
def {self.controller_set_text_function_name}(cls, text:str):
    print("The function {self.controller_set_text_function_name} is unfortunately not linked to the controller")""".splitlines()

    def generate_strings(self) -> Iterator[str]:
        __doc__ = super().generate_strings().__doc__
        yield f'{self.string_name} = \'{self.string}\''
