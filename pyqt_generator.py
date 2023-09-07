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
        central_widget = QWidget(MainWindow)""".splitlines()
    for child in frame['children']:
        yield from map(indent, map(indent, generate_ui_element(child, (start_x, start_y))))
    yield indent(indent('MainWindow.setCentralWidget(central_widget)'))


def generate_fills(element: dict, start_coordinates=(0, 0)) -> Iterator[str]:
    for i, fill in enumerate(element['fills']):
        frame_name = 'frame_' + get_legal_name(element) + f'_fill{i}'
        match fill['type']:
            case 'IMAGE':
                image_ref = fill['imageRef']
                image = f'url("../resources/images/{image_ref}.png")'
                scale_mode = fill['scaleMode'].lower()
                stylesheet = f'border-image: {image} 0 0 0 0 stretch {scale_mode}; border: 0px solid black ;'
                yield f'{frame_name} = QFrame(central_widget)'
                yield f'{frame_name}.setStyleSheet(\'{stylesheet}\')'
                yield f'{frame_name}.setGeometry({get_bounds(element, start_coordinates)})'
                yield f'{frame_name}.setFrameShape(QFrame.StyledPanel)'
                yield f'{frame_name}.setFrameShadow(QFrame.Raised)'
            case 'SOLID':
                color = fill['color']
                opacity = fill.get('opacity', 1)
                yield f'{frame_name} = QFrame(central_widget)'
                color = f'rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {color.get("a", 1) * 255 * opacity})'
                yield f'{frame_name}.setStyleSheet(\'background-color: {color}; color: {color}\')'
                yield f'{frame_name}.setGeometry({get_bounds(element, start_coordinates)})'
                yield f'{frame_name}.setFrameShape(QFrame.StyledPanel)'
                yield f'{frame_name}.setFrameShadow(QFrame.Raised)'
            case _:
                print(f'Unknown fill type: {fill["type"]} for element {element["name"]}')


def generate_strokes(element: dict, start_coordinates=(0, 0)) -> Iterator[str]:
    for i, stroke in enumerate(element['strokes']):
        frame_name = 'frame_' + get_legal_name(element) + f'_stroke{i}'
        match stroke['type']:
            case 'SOLID':
                color = stroke['color']
                opacity = stroke.get('opacity', 1)
                yield f'{frame_name} = QFrame(central_widget)'
                yield f'{frame_name}.setStyleSheet(\'border: {element["strokeWeight"] * scale}px solid rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {opacity * 255});\')'
                yield f'{frame_name}.setGeometry({get_bounds(element, start_coordinates)})'
                yield f'{frame_name}.setFrameShape(QFrame.StyledPanel)'
                yield f'{frame_name}.setFrameShadow(QFrame.Raised)'
            case _:
                print(f'Unknown stroke type: {stroke["type"]} for element {element["name"]}')


def generate_ui_element(child, start_coordinates=(0, 0)) -> Iterator[str]:
    match child['type']:
        case 'TEXT':
            yield from generate_text(child, start_coordinates)
        case 'GROUP':
            yield from generate_group(child, start_coordinates)
        case 'VECTOR':
            yield from generate_vector(child, start_coordinates)
        case 'COMPONENT_SET' | 'COMPONENT' | 'FRAME' | 'INSTANCE' | 'RECTANGLE' | 'STAR' | 'LINE' | 'ELLIPSE' | 'REGULAR_POLYGON' | 'SLICE' | 'BOOLEAN_OPERATION' | 'STICKY_GUIDES':
            # TODO handle these cases properly
            yield from generate_fills(child, start_coordinates)
            yield from generate_strokes(child, start_coordinates)
            yield from generate_group(child, start_coordinates)
        case _:
            print(f'Unknown type: {child["type"]}')

        # generate inputs and touchzones for buttons
    if child['name'].lower().strip().startswith('button'):
        yield from generate_button(child, start_coordinates)


def generate_group(group: dict, start_coordinates=(0, 0)) -> Iterator[str]:
    if 'children' not in group:
        return []
    for child in group['children']:
        yield from generate_ui_element(child, start_coordinates)


def generate_text(child, start_coordinates=(0, 0)) -> Iterator[str]:
    text = child['characters']
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
    yield f'{label_name}.setStyleSheet(\'color: {color}\')'
    yield f'{label_name}.setGeometry({get_bounds(child, start_coordinates)})'


def generate_vector(child, start_coordinates=(0, 0)) -> Iterator[str]:
    global svg_counter
    svg_counter += 1

    svg_filename = '../resources/svg/' + f'file{svg_counter}.svg'

    def create_svg_file():
        svg_file_data = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="100%" height="100%" viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg">"""
        for i, (geometry, fill) in enumerate(zip(child.get('fillGeometry', []), child.get('fills', []))):
            svg_data = geometry['path']
            color = 0, 0, 0, 1
            if 'color' in fill:
                color = fill['color']
                color = color['r'], color['g'], color['b'], color.get('a', 1)
            color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: int(x * 255), color))
            svg_file_data += f'\n\t<path d="{svg_data}" stroke="{color}" stroke-width="5" fill="{color}" />'
        svg_file_data += '\n</svg>'
        with open(svg_filename, 'w') as file:
            file.write(svg_file_data)

    create_svg_file()

    svg_widget_name = 'svg_' + get_legal_name(child)
    yield f'{svg_widget_name} = QSvgWidget(central_widget)'
    yield f'{svg_widget_name}.setGeometry({get_bounds(child, start_coordinates)})'
    yield f'{svg_widget_name}.load("{svg_filename}")'
    yield f'{svg_widget_name}.setFixedSize({int(child["absoluteBoundingBox"]["width"] * scale)}, {int(child["absoluteBoundingBox"]["height"] * scale)})'


def generate_button(child, start_coordinates):
    button_name = get_legal_name(child)
    yield f'{button_name} = QPushButton(central_widget)'
    yield f'{button_name}.setGeometry({get_bounds(child, start_coordinates)})'
    yield f'{button_name}.setStyleSheet(\'background-color: rgba(0, 0, 0, 0);\')'
    yield f'{button_name}.setFlat(True)'
    yield f'{button_name}.setAutoFillBackground(False)'
    yield f'{button_name}.setObjectName("{button_name}")'
    yield f'{button_name}.setMouseTracking(True)'
    yield f'{button_name}.setFocusPolicy(Qt.NoFocus)'
    yield f'{button_name}.setContextMenuPolicy(Qt.NoContextMenu)'
    yield f'{button_name}.setAcceptDrops(False)'
    yield from f"""def __{button_name}_clicked(self):
    try : 
        GuiHandler.{button_name}_clicked()
    except :
        print("No function {button_name}_clicked defined")""".splitlines()
    yield f'{button_name}.clicked.connect(__{button_name}_clicked)'
