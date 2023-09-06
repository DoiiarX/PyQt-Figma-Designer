from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QStatusBar, QTableView, QWidget)


class UI_Mainwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(661.0, 411.0)
        centralWidget = QWidget(MainWindow)
        label = QLabel(centralWidget)
        label.setText("Create project")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(185.00000417232513, 185.00000417232513, 185.00000417232513);")
        label.setGeometry(QRect(-344.0, -216.0, 90.0, 20.0));
        label = QLabel(centralWidget)
        label.setText("Overrides")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(184.52083468437195, 184.52083468437195, 184.52083468437195);")
        label.setGeometry(QRect(-344.0, -42.0, 61.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-116.0, -17.0, 116.0, 20.06382942199707));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Type")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(-113.40121459960938, -12.661874771118164, 109.62117767333984, 10.84531307220459));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(0.0, -17.0, 160.0, 20.06382942199707));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Override")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(3.584531545639038, -12.661874771118164, 151.20162963867188, 10.84531307220459));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-232.0, -17.0, 116.0, 20.06382942199707));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Method")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(-229.40121459960938, -12.661874771118164, 109.62117767333984, 10.84531307220459));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-344.0, -17.0, 116.0, 20.06382942199707));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Class")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(-341.4012145996094, -12.661874771118164, 109.62118530273438, 10.84531307220459));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-344.0, -143.0, 504.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-344.0, -188.0, 504.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-344.0, 7.0, 504.0, 164.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(180.0, 134.0, 107.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Build")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(218.0, 142.0, 33.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(173.0, 28.0, 45.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("-")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(194.0, 37.0, 5.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(173.0, -17.0, 45.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("+")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(192.0, -8.0, 8.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(-85.0, -98.0, 107.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Start")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(-47.0, -90.0, 32.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(173.0, -142.0, 107.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Browse")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(203.0, -134.0, 48.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(173.0, -184.0, 107.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Browse")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(203.0, -176.0, 48.0, 20.0));
        label = QLabel(centralWidget)
        label.setText("Project directory")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(-332.7087707519531, -135.0, 476.2851257324219, 20.0));
        label = QLabel(centralWidget)
        label.setText("APK input file")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(-332.7087707519531, -180.0, 476.2851257324219, 20.0));
        MainWindow.setCentralWidget(centralWidget)


class UI_Overridewindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364.0, 387.0)
        centralWidget = QWidget(MainWindow)
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(454.0, 111.0, 107.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("OK")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(255.0, 255.0, 255.0);")
        label.setGeometry(QRect(499.0, 119.0, 19.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(342.0, -165.0, 332.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        label = QLabel(centralWidget)
        label.setText("Class name (leave empty for any)")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(115.45833975076675, 115.45833975076675, 115.45833975076675);")
        label.setGeometry(QRect(342.0, -185.0, 213.0, 20.0));
        label = QLabel(centralWidget)
        label.setText("Type")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(115.45833975076675, 115.45833975076675, 115.45833975076675);")
        label.setGeometry(QRect(342.0, -54.0, 31.0, 20.0));
        label = QLabel(centralWidget)
        label.setText("Filter")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(185.00000417232513, 185.00000417232513, 185.00000417232513);")
        label.setGeometry(QRect(342.0, -214.0, 33.0, 20.0));
        label = QLabel(centralWidget)
        label.setText("Action")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(185.00000417232513, 185.00000417232513, 185.00000417232513);")
        label.setGeometry(QRect(342.0, 25.0, 42.0, 20.0));
        label = QLabel(centralWidget)
        label.setText("Method name (leave empty for any)")
        label.setFont(QFont("Roboto", 14.0))
        label.setStyleSheet("color: rgb(115.45833975076675, 115.45833975076675, 115.45833975076675);")
        label.setGeometry(QRect(342.0, -119.0, 226.0, 20.0));
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(342.0, -99.0, 332.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(342.0, -34.0, 332.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame = QFrame(centralWidget)
        frame.setStyleSheet("background-color: rgb(68.7083387374878, 68.7083387374878, 68.7083387374878);")
        frame.setGeometry(QRect(342.0, 45.0, 332.0, 37.0));
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(centralWidget)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    ui = UI_Mainwindow()
    ui.setupUi(ui)
    ui.show()

    ui = UI_Overridewindow()
    ui.setupUi(ui)
    ui.show()

    sys.exit(app.exec_())
