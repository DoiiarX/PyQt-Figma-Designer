import random
from typing import Iterator
from config import scale

TEXT_SCALE = 1 / 1.5

svg_counter = 0


def indent(s: str): return '    ' + s


def get_legal_name(element: dict) -> str:
    object_name = element.get('name', '').strip()
    if object_name == '':
        object_name = element['id']
    object_name = ''.join(c for c in object_name if c.isalnum() or c == ' ').strip().replace(' ', '_')
    while '__' in object_name:
        object_name = object_name.replace('__', '_')
    return object_name.lower()


def get_bounds(element: dict, start_coordinates: (float, float)) -> str:
    bounds = element['absoluteBoundingBox']
    x, y = bounds['x'] - start_coordinates[0], bounds['y'] - start_coordinates[1]
    width, height = bounds['width'], bounds['height']
    x, y, width, height = x * scale, y * scale, width * scale, height * scale
    return f'QRect({int(x)}, {int(y)}, {int(width)}, {int(height)})'


def generate_pyqt_design(figma_file: dict) -> Iterator[str]:
    yield from """try:
    import GuiHandler
except:
    print("No GuiHandler found, events will not be handled.")
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform, QPen, QPainterPath)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)""".splitlines()
    canvas = figma_file['document']['children'][0]
    frames = canvas['children']
    classes = []
    for frame in frames:
        class_name = 'UI_' + get_legal_name(frame).replace('_', ' ').title().replace(' ', '')
        yield from generate_frame(frame, class_name)
        classes.append(class_name)
    yield from f"""
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)    
    MainWindow = QMainWindow()
    ui = {classes[0]}()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())""".splitlines()


def generate_frame(frame: dict, class_name: str) -> Iterator[str]:
    bounds = frame['absoluteBoundingBox']
    width, height = bounds['width'], bounds['height']
    start_x, start_y = bounds['x'], bounds['y']
    yield from f"""class {class_name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width * scale}, {height * scale})
        central_widget = QWidget(MainWindow)
        MainWindow.setFixedSize({width * scale}, {height * scale})
        MainWindow.setWindowTitle("{frame['name']}")
        
        """.splitlines()
    yield from map(indent, map(indent, generate_vector(frame, (start_x, start_y))))
    for child in frame['children']:
        yield from map(indent, map(indent, generate_ui_element(child, (start_x, start_y))))
    yield indent(indent('MainWindow.setCentralWidget(central_widget)'))


def generate_ui_element(child, start_coordinates=(0, 0)) -> Iterator[str]:
    if not child.get('visible', True):
        return []
    # generate visuals
    if ('fillGeometry' in child and len(child['fillGeometry']) > 0) \
            or ('strokeGeometry' in child and len(child['strokeGeometry']) > 0):
        yield from generate_vector(child, start_coordinates)

    if child['type'] == 'TEXT':
        yield from generate_text(child, start_coordinates)

    # generate children
    if 'children' in child and len(child['children']) > 0:
        yield from generate_group(child, start_coordinates)

    # generate inputs
    if child['name'].lower().strip().startswith('button'):
        yield from generate_button(child, start_coordinates)

    if child['name'].lower().replace(' ', '').replace('-', '').startswith('textfield'):
        yield from generate_text_field(child, start_coordinates)

    if child['name'].lower().replace(' ', '').replace('-', '').startswith('checkbox'):
        children = {c['name']: c for c in child['children']}
        checked = children.get('Checked', None)
        if checked is not None:
            yield from generate_checkbox(child, checked, start_coordinates)


def generate_group(group: dict, start_coordinates=(0, 0)) -> Iterator[str]:
    if 'children' not in group:
        return []
    for child in group['children']:
        yield from generate_ui_element(child, start_coordinates)


def generate_text(child, start_coordinates=(0, 0)) -> Iterator[str]:
    text = child['characters'].replace('"', '\\"')
    font = child['style']['fontFamily']
    font_size = child['style']['fontSize'] * TEXT_SCALE * scale
    label_name = 'label_' + get_legal_name(child)
    yield f'{label_name} = QLabel(central_widget)'
    yield f'{label_name}.setText("{text}")'
    yield from f"""font = QFont()
font.setFamilies([u"{font}"])
font.setPointSize({int(font_size)})
{label_name}.setFont(font)""".splitlines()
    color = 'rgba(0, 0, 0, 0)'

    if len(child['fills']) > 0 and 'color' in child['fills'][0]:
        color = child['fills'][0]['color']
        color = f'rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {color.get("a", 1) * 255})'
    yield f'{label_name}.setStyleSheet("color: {color}")'
    yield f'{label_name}.setGeometry({get_bounds(child, start_coordinates)})'
    # align horizontally
    alignment = child['style']['textAlignHorizontal']
    match alignment:
        case 'LEFT':
            yield f'{label_name}.setAlignment(Qt.AlignLeft)'
        case 'RIGHT':
            yield f'{label_name}.setAlignment(Qt.AlignRight)'
        case 'CENTER':
            yield f'{label_name}.setAlignment(Qt.AlignCenter)'
        case 'JUSTIFIED':
            yield f'{label_name}.setAlignment(Qt.AlignJustify)'
        case _:
            yield f'{label_name}.setAlignment(Qt.AlignCenter)'
    # align vertically
    alignment = child['style']['textAlignVertical']
    match alignment:
        case 'TOP':
            yield f'{label_name}.setAlignment(Qt.AlignTop)'
        case 'BOTTOM':
            yield f'{label_name}.setAlignment(Qt.AlignBottom)'
        case 'CENTER':
            yield f'{label_name}.setAlignment(Qt.AlignVCenter)'
        case _:
            yield f'{label_name}.setAlignment(Qt.AlignVCenter)'

    yield f'{label_name}.setMouseTracking(False)'
    yield f'{label_name}.setContextMenuPolicy(Qt.NoContextMenu)'


def generate_vector(child, start_coordinates=(0, 0)) -> Iterator[str]:
    global svg_counter
    svg_counter += 1

    svg_filename = '../resources/svg/' + f'file{svg_counter}.svg'

    image_counter = 0

    def generate_path(path_data: str, graphic: dict, stroke=True) -> Iterator[str]:
        stroke_width = child.get('strokeWeight', 0)
        opacity = graphic.get('opacity', 1)

        match graphic['type']:
            case 'SOLID':
                color = graphic['color']
                opacity *= color.get('a', 0)
                color = color['r'], color['g'], color['b']
                color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: int(x * 255), color))
                yield (f'<path '
                       f'fill="{color}" stroke-width="{stroke_width}" '
                       f'fill-opacity="{opacity}" stroke-opacity="{opacity}" '
                       f'd="{path_data}"/>')
            case 'IMAGE':
                image_ref = graphic['imageRef']
                image = f'../images/{image_ref}.png'
                width, height = child['absoluteBoundingBox']['width'], child['absoluteBoundingBox']['height']
                img_ref = f'img{image_counter}'
                yield f'<image x="0" y="0" width="{width}" height="{height}" xlink:href="{image}" id="{img_ref}" opacity="{opacity}"/>'
            case 'GRADIENT_LINEAR':
                gradient = graphic['gradientHandlePositions']
                gradient = f'x1="{gradient[0]["x"]}" y1="{gradient[0]["y"]}" x2="{gradient[1]["x"]}" y2="{gradient[1]["y"]}"'
                stops = graphic['gradientStops']
                yield f'<linearGradient id="gradient{image_counter}" {gradient}>'
                for stop in stops:
                    color = stop['color']
                    opacity = color.get('a', 1)
                    color = color['r'], color['g'], color['b']
                    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: int(x * 255), color))
                    yield f'\t<stop offset="{stop["position"]}" stop-color="{color}" stop-opacity="{opacity}"/>'
                yield f'</linearGradient>'
                yield f'<path fill="url(#gradient{image_counter})" stroke-width="{stroke_width}" fill-opacity="{opacity}" stroke-opacity="{opacity}" d="{path_data}"/>'
            case 'GRADIENT_RADIAL':
                gradient = graphic['gradientHandlePositions']
                p0, p1 = gradient[0], gradient[-1]
                radius = ((p0['x'] - p1['x']) ** 2 + (p0['y'] - p1['y']) ** 2) ** .5
                gradient = f'cx="{p0["x"]}" cy="{p0["y"]}" r="{radius}"'
                stops = graphic['gradientStops']
                yield f'<radialGradient id="gradient{image_counter}" {gradient}>'
                for stop in stops:
                    color = stop['color']
                    opacity = color.get('a', 1)
                    color = color['r'], color['g'], color['b']
                    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: int(x * 255), color))
                    yield f'\t<stop offset="{stop["position"]}" stop-color="{color}" stop-opacity="{opacity}"/>'
                yield f'</radialGradient>'
                yield f'<path fill="url(#gradient{image_counter})" stroke-width="{stroke_width}" fill-opacity="{opacity}" stroke-opacity="{opacity}" d="{path_data}"/>'
            case _:
                print(f'Unknown graphic type: {graphic["type"]}')
                return []

    def create_svg_file():
        bounds = f'0 0 {int(child["absoluteBoundingBox"]["width"])} {int(child["absoluteBoundingBox"]["height"])}'
        svg_file_data = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg version="1.2" baseProfile="tiny" viewBox="{bounds}" xmlns="http://www.w3.org/2000/svg">"""
        for i, (geometry, fill) in enumerate(zip(child.get('fillGeometry', []), child.get('fills', []))):
            for line in generate_path(geometry['path'], fill, stroke=False):
                svg_file_data += '\n\t' + line

        for i, (geometry, stroke) in enumerate(zip(child.get('strokeGeometry', []), child.get('strokes', []))):
            for line in generate_path(geometry['path'], stroke):
                svg_file_data += '\n\t' + line

        svg_file_data += '\n</svg>'
        with open(svg_filename, 'w') as file:
            file.write(svg_file_data)

    create_svg_file()
    label_name = 'label_' + get_legal_name(child)
    svg_widget_name = 'svg_' + get_legal_name(child)
    yield f'{label_name} = QLabel(central_widget)'
    yield f'{label_name}.setGeometry({get_bounds(child, start_coordinates)})'
    yield f'{svg_widget_name} = QSvgWidget({label_name})'
    width, height = child['absoluteBoundingBox']['width'], child['absoluteBoundingBox']['height']
    yield f'{svg_widget_name}.setGeometry(QRect(0, 0, {int(width * scale)}, {int(height * scale)}))'
    yield f'{svg_widget_name}.load("{svg_filename}")'


def generate_button(child, start_coordinates):
    button_name = get_legal_name(child)
    yield f'{button_name} = QPushButton(central_widget)'
    yield f'{button_name}.setGeometry({get_bounds(child, start_coordinates)})'
    yield f'{button_name}.setFlat(True)'
    yield f'{button_name}.setAutoFillBackground(False)'
    yield f'{button_name}.setObjectName("{button_name}")'
    yield f'{button_name}.setMouseTracking(True)'
    yield f'{button_name}.setContextMenuPolicy(Qt.NoContextMenu)'
    yield f'{button_name}.setAcceptDrops(False)'
    yield from f"""def __{button_name}_clicked(self):
    try : 
        GuiHandler.{button_name}_clicked()
    except :
        print("No function {button_name}_clicked defined")""".splitlines()
    yield f'{button_name}.clicked.connect(__{button_name}_clicked)'
    yield f'{button_name}.setFocusPolicy(Qt.NoFocus)'
    yield f'{button_name}.setStyleSheet("background-color: rgba(255, 255, 255, 30);")'


def generate_text_field(child, start_coordinates):
    text_field_name = get_legal_name(child)
    yield f'{text_field_name} = QLineEdit(central_widget)'
    yield f'{text_field_name}.setGeometry({get_bounds(child, start_coordinates)})'
    yield f'{text_field_name}.setAutoFillBackground(False)'
    yield f'{text_field_name}.setObjectName("{text_field_name}")'
    yield f'{text_field_name}.setMouseTracking(True)'
    yield f'{text_field_name}.setContextMenuPolicy(Qt.NoContextMenu)'
    yield f'{text_field_name}.setAcceptDrops(False)'
    yield from f"""def __{text_field_name}_text_changed(self):
    try : 
        GuiHandler.{text_field_name}_text_changed()
    except :
        print("No function {text_field_name}_clicked defined")""".splitlines()
    yield f'{text_field_name}.textChanged.connect(__{text_field_name}_text_changed)'
    yield (f'{text_field_name}.setStyleSheet("background-color: rgba(255, 255, 255, 0); '
           # cursor color
           f'border: 0px solid rgba(255, 255, 255, 255);'
           f'color: rgba(255, 255, 255, 255); ")')
    yield f'{text_field_name}.setPlaceholderText("{child["name"]}")'


def generate_checkbox(child, checked, start_coordinates):
    checkbox_name = get_legal_name(child)
    checked_name = 'label_' + get_legal_name(checked)
    yield f'{checkbox_name} = QPushButton(central_widget)'
    yield f'{checkbox_name}.setGeometry({get_bounds(child, start_coordinates)})'
    yield f'{checkbox_name}.setFlat(True)'
    yield f'{checkbox_name}.setAutoFillBackground(False)'
    yield f'{checkbox_name}.setObjectName("{checkbox_name}")'
    yield f'{checkbox_name}.setMouseTracking(True)'
    yield f'{checkbox_name}.setContextMenuPolicy(Qt.NoContextMenu)'
    yield f'{checkbox_name}.setAcceptDrops(False)'
    yield from f"""def __{checkbox_name}_check_changed(self):
    try : 
        # hide the checked element
        {checked_name}.setVisible(not {checked_name}.isVisible())        
        GuiHandler.{checkbox_name}_check_changed({checked_name}.isVisible())
    except :
        print("No function {checkbox_name}_check_changed defined. Checked = " + str({checked_name}.isVisible()))""".splitlines()
    yield f'{checkbox_name}.clicked.connect(__{checkbox_name}_check_changed)'
