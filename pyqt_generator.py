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
    for frame in frames:
        yield from generate_frame(frame)


def generate_frame(frame: dict) -> Iterator[str]:
    bounds = frame['absoluteBoundingBox']
    width, height = bounds['width'], bounds['height']
    yield from f"""class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize({width}, {height})""".splitlines()
    for child in frame['children']:
        yield from map(indent, map(indent, generate_ui_element(child)))


def generate_ui_element(child):
    match child['type']:
        case 'VECTOR':
            yield from generate_vector(child)
        case 'TEXT':
            yield from generate_text(child)
        case 'GROUP':
            yield from generate_group(child)


def generate_group(group: dict) -> Iterator[str]:
    for child in group['children']:
        yield from generate_ui_element(child)


def generate_text(child):
    pass


def generate_vector(child):
    bounds = child['absoluteBoundingBox']
    yield f'QRect({bounds["x"]}, {bounds["y"]}, {bounds["width"]}, {bounds["height"]})'
    color = child['fills'][0]['color']
    yield f'QColor({color["r"]}, {color["g"]}, {color["b"]}, {color["a"]})'
