from config import text_scale, scale
from generator.design.design_generator import DesignGenerator


class TextGenerator(DesignGenerator):
    def generate_design(self):

        text = self.fig_node['characters'].replace('"', '\\"')
        font = self.fig_node['style']['fontFamily']
        font_size = self.fig_node['style']['fontSize'] * text_scale * scale
        color = 'rgba(0, 0, 0, 0)'
        if len(self.fig_node['fills']) > 0 and 'color' in self.fig_node['fills'][0]:
            color = self.fig_node['fills'][0]['color']
            color = f'rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {color.get("a", 1) * 255})'

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

        yield from f"""{self.name} = QLabel(central_widget)
{self.name}.setText("{text}")
font = QFont()
font.setFamilies([u"{font}"])
font.setPointSize({int(font_size)})
{self.name}.setFont(font)
{self.name}.setStyleSheet("color: {color}")
{self.name}.setGeometry({self.pyqt_bounds})
{self.name}.setAlignment({vertical_alignment} | {horizontal_alignment})
{self.name}.setMouseTracking(False)
{self.name}.setContextMenuPolicy(Qt.NoContextMenu)""".splitlines()
