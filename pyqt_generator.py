from typing import Iterator
from config import scale

image_counter = 0


def indent(s: str): return '    ' + s


def get_color(element: dict):
    if len(element['fills']) == 0:
        return 'rgba(0, 0, 0, 0)'
    elif 'color' in element['fills'][0]:
        for fill in element['fills']:
            a, r, g, b = 0, 0, 0, 0
            if 'color' in fill:
                color = fill['color']
                opacity = fill.get('opacity', 1)

                def mix(v1, v2, o): return v1 * (1 - o) + v2 * o

                a = mix(a, color['a'], opacity)
                r = mix(r, color['r'], opacity)
                g = mix(g, color['g'], opacity)
                b = mix(b, color['b'], opacity)

        color = {'a': a, 'r': r, 'g': g, 'b': b}
        return f'rgba({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255}, {color["a"] * 255})'
    else:
        return None


def get_style_sheet(element: dict) -> str:
    color = get_color(element)
    if color is None:
        image_ref = element['fills'][0]['imageRef']
        image = f'url("../resources/images/{image_ref}.png")'
        scale_mode = element['fills'][0]['scaleMode'].lower()
        return f'border-image: {image} 0 0 0 0 stretch {scale_mode}; border: 0px solid black ;'
    if len(element['strokes']) == 0 or 'color' not in element['strokes'][0]:
        stroke_color, stroke_size = 'rgba(0, 0, 0, 0)', 0
    else:
        stroke_color, stroke_size = element['strokes'][0]['color'], element['strokeWeight'] * scale
        stroke_color = f'rgb({stroke_color["r"] * 255}, {stroke_color["g"] * 255}, {stroke_color["b"] * 255})'
    if color is not None:
        return (f'color: {color}; '
                f'background-color: {color}; '
                f'border: {stroke_size}px solid {stroke_color};')


def generate_pyqt_design(figma_file: dict) -> Iterator[str]:
    yield from """from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)""".splitlines()
    canvas = figma_file['document']['children'][0]
    frames = canvas['children']
    classes = []
    for frame in frames:
        frame_name = frame['name']
        # ensure class name is valid
        class_name = 'UI_' + ''.join(c for c in frame_name if c.isalnum()).title()
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
    """.splitlines()
    yield '    sys.exit(app.exec())'


def generate_frame(frame: dict, class_name: str) -> Iterator[str]:
    bounds = frame['absoluteBoundingBox']

    width, height = bounds['width'], bounds['height']
    start_x, start_y = bounds['x'], bounds['y']
    yield from f"""class {class_name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width * scale}, {height * scale})
        centralWidget = QWidget(MainWindow)""".splitlines()
    for child in frame['children']:
        yield from map(indent, map(indent, generate_ui_element(child, (start_x, start_y))))
    yield indent(indent('MainWindow.setCentralWidget(centralWidget)'))


def generate_bounds(child, start_coordinates=(0, 0)):
    bounds = child['absoluteBoundingBox']
    x, y = bounds['x'] - start_coordinates[0], bounds['y'] - start_coordinates[1]
    width, height = bounds['width'], bounds['height']
    x, y, width, height = x * scale, y * scale, width * scale, height * scale
    return f'QRect({int(x)}, {int(y)}, {int(width)}, {int(height)})'


def generate_ui_element(child, start_coordinates=(0, 0)):
    match child['type']:
        case 'RECTANGLE':
            yield from generate_rectangle(child, start_coordinates)
        case 'TEXT':
            yield from generate_text(child, start_coordinates)
        case 'GROUP':
            yield from generate_group(child, start_coordinates)
        case 'VECTOR':
            yield from generate_vector(child, start_coordinates)
        case 'LINE':
            yield from generate_line(child, start_coordinates)
        case 'COMPONENT_SET' | 'COMPONENT' | 'FRAME' | 'INSTANCE':
            # TODO handle these cases properly
            yield from generate_rectangle(child, start_coordinates)
            yield from generate_group(child, start_coordinates)
        case _:
            print(f'Unknown type: {child["type"]}')


def generate_group(group: dict, start_coordinates=(0, 0)) -> Iterator[str]:
    for child in group['children']:
        yield from generate_ui_element(child, start_coordinates)


def generate_text(child, start_coordinates=(0, 0)):
    text = child['characters']
    font = child['style']['fontFamily']
    font_size = child['style']['fontSize'] / 1.5 * scale
    yield 'label = QLabel(centralWidget)'
    yield f'label.setText("{text}")'
    yield from f"""font = QFont()
font.setFamilies([u"{font}"])
font.setPointSize({int(font_size)})
label.setFont(font)""".splitlines()
    yield f'label.setStyleSheet(\'color: {get_color(child)}\')'
    yield f'label.setGeometry({generate_bounds(child, start_coordinates)})'


def generate_rectangle(child, start_coordinates=(0, 0)):
    yield 'frame = QFrame(centralWidget)'
    yield f'frame.setStyleSheet(\'{get_style_sheet(child)}\')'
    yield f'frame.setGeometry({generate_bounds(child, start_coordinates)})'
    yield 'frame.setFrameShape(QFrame.StyledPanel)'


def generate_vector(child, start_coordinates=(0, 0)):
    yield 'frame = QFrame(centralWidget)'
    yield f'frame.setStyleSheet(\'{get_style_sheet(child)}\')'
    yield f'frame.setGeometry({generate_bounds(child, start_coordinates)})'
    yield 'frame.setFrameShape(QFrame.StyledPanel)'
    yield 'frame.setFrameShadow(QFrame.Raised)'


def generate_line(child, start_coordinates=(0, 0)):
    yield 'frame = QFrame(centralWidget)'
    yield f'frame.setStyleSheet(\'{get_style_sheet(child)}\')'
    yield f'frame.setGeometry({generate_bounds(child, start_coordinates)})'
    yield 'frame.setFrameShape(QFrame.HLine)'
    yield 'frame.setFrameShadow(QFrame.Sunken)'
