from typing import Iterator


def indent(s: str): return '    ' + s


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
    yield '    sys.exit(app.exec_())'


def generate_frame(frame: dict, class_name: str) -> Iterator[str]:
    bounds = frame['absoluteBoundingBox']

    width, height = bounds['width'], bounds['height']
    start_x, start_y = bounds['x'], bounds['y']
    yield from f"""class {class_name}(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width}, {height})
        centralWidget = QWidget(MainWindow)""".splitlines()
    for child in frame['children']:
        yield from map(indent, map(indent, generate_ui_element(child, (start_x, start_y))))
    yield indent(indent('MainWindow.setCentralWidget(centralWidget)'))


def generate_rect(child, start_coordinates=(0, 0)):
    bounds = child['absoluteBoundingBox']
    x, y = bounds['x'] - start_coordinates[0], bounds['y'] - start_coordinates[1]
    width, height = bounds['width'], bounds['height']
    return f'QRect({x}, {y}, {width}, {height})'


def generate_ui_element(child, start_coordinates=(0, 0)):
    match child['type']:
        case 'RECTANGLE':
            yield from generate_rectangle(child, start_coordinates)
        case 'TEXT':
            yield from generate_text(child, start_coordinates)
        case 'GROUP':
            yield from generate_group(child, start_coordinates)
        case _:
            print(f'Unknown type: {child["type"]}')


def generate_group(group: dict, start_coordinates=(0, 0)) -> Iterator[str]:
    for child in group['children']:
        yield from generate_ui_element(child, start_coordinates)


def generate_text(child, start_coordinates=(0, 0)):
    color = child['fills'][0]['color']
    text = child['characters']
    font = child['style']['fontFamily']
    fontSize = child['style']['fontSize']
    yield 'label = QLabel(centralWidget)'
    yield f'label.setText("{text}")'
    yield f'label.setFont(QFont("{font}", {fontSize}))'
    yield f'label.setStyleSheet("color: rgb({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255});")'
    yield f'label.setGeometry({generate_rect(child, start_coordinates)});'


def generate_rectangle(child, start_coordinates=(0, 0)):
    color = child['fills'][0]['color']
    yield 'frame = QFrame(centralWidget)'
    yield f'frame.setStyleSheet("background-color: rgb({color["r"] * 255}, {color["g"] * 255}, {color["b"] * 255});")'
    yield f'frame.setGeometry({generate_rect(child, start_coordinates)});'
    yield 'frame.setFrameShape(QFrame.StyledPanel)'
    yield 'frame.setFrameShadow(QFrame.Raised)'
