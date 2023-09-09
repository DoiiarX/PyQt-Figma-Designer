from config import text_scale, scale
from generator.core.base_generator import BaseGenerator


class TextGenerator(BaseGenerator):
    def generate_design(self):

        text = self.fig_node['characters'].replace('"', '\\"')
        font = self.fig_node['style']['fontFamily']
        font_size = self.fig_node['style']['fontSize'] * text_scale * scale
        yield from f"""{self.name} = QLabel(central_widget)
{self.name}.setText("{text}")
font = QFont()
font.setFamilies([u"{font}"])
font.setPointSize({int(font_size)})
{self.name}.setFont(font)""".splitlines()

        color = 'rgba(0, 0, 0, 0)'
        if len(self.fig_node['fills']) > 0 and 'color' in self.fig_node['fills'][0]:
            color = self.fig_node['fills'][0]['color']
            color = f'rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {color.get("a", 1) * 255})'

        yield f'{self.name}.setStyleSheet("color: {color}")'
        yield f'{self.name}.setGeometry({self.pyqt_bounds})'

        vertical_alignment_figma = self.fig_node['style']['textAlignVertical']
        horizontal_alignment_figma = self.fig_node['style']['textAlignHorizontal']
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

        yield f'{self.name}.setAlignment({vertical_alignment} | {horizontal_alignment})'
        yield f'{self.name}.setMouseTracking(False)'
        yield f'{self.name}.setContextMenuPolicy(Qt.NoContextMenu)'
