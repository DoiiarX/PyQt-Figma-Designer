try:
    import gui_handler as GuiHandler
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
                               QStatusBar, QTableView, QWidget)


class Windowq_PyQt_Figma_Designer(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460.59999999999997, 280.7)
        central_widget = QWidget(MainWindow)
        MainWindow.setFixedSize(460.59999999999997, 280.7)
        MainWindow.setWindowTitle("PyQt Figma Designer")
        q_PyQt_Figma_Designer_ = QLabel(central_widget)
        q_PyQt_Figma_Designer_.setGeometry(QRect(0, 0, 460, 280))
        q_svg_widget_q_PyQt_Figma_Designer__ = QSvgWidget(q_PyQt_Figma_Designer_)
        q_svg_widget_q_PyQt_Figma_Designer__.setGeometry(QRect(0, 0, 460, 280))
        q_svg_widget_q_PyQt_Figma_Designer__.load("svg/file1.svg")
        q_ButtonCreateProject = QLabel(central_widget)
        q_ButtonCreateProject.setGeometry(QRect(20, 224, 420, 42))
        q_svg_widget_q_ButtonCreateProject_ = QSvgWidget(q_ButtonCreateProject)
        q_svg_widget_q_ButtonCreateProject_.setGeometry(QRect(0, 0, 420, 42))
        q_svg_widget_q_ButtonCreateProject_.load("svg/file2.svg")
        q_Title = QLabel(central_widget)
        q_Title.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        q_Title.setFont(font)
        q_Title.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        q_Title.setGeometry(QRect(34, 224, 378, 42))
        q_Title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        q_Title.setMouseTracking(False)
        q_Title.setContextMenuPolicy(Qt.NoContextMenu)
        q_Disclosure = QLabel(central_widget)
        q_Disclosure.setText(">")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        q_Disclosure.setFont(font)
        q_Disclosure.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        q_Disclosure.setGeometry(QRect(418, 239, 7, 12))
        q_Disclosure.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        q_Disclosure.setMouseTracking(False)
        q_Disclosure.setContextMenuPolicy(Qt.NoContextMenu)
        q_ButtonCreateProject__ = QPushButton(central_widget)
        q_ButtonCreateProject__.setGeometry(QRect(20, 224, 420, 42))
        q_ButtonCreateProject__.setFlat(True)
        q_ButtonCreateProject__.setAutoFillBackground(False)
        q_ButtonCreateProject__.setObjectName("q_ButtonCreateProject__")
        q_ButtonCreateProject__.setMouseTracking(True)
        q_ButtonCreateProject__.setContextMenuPolicy(Qt.NoContextMenu)
        q_ButtonCreateProject__.setAcceptDrops(False)

        def __q_ButtonCreateProject___clicked(self):
            GuiHandler.q_ButtonCreateProject___clicked()

        q_ButtonCreateProject__.clicked.connect(__q_ButtonCreateProject___clicked)
        q_ButtonCreateProject__.setFocusPolicy(Qt.NoFocus)
        q_ButtonCreateProject__.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        q_Input_file_URL = QLabel(central_widget)
        q_Input_file_URL.setText("Input file URL")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        q_Input_file_URL.setFont(font)
        q_Input_file_URL.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        q_Input_file_URL.setGeometry(QRect(29, 14, 70, 15))
        q_Input_file_URL.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        q_Input_file_URL.setMouseTracking(False)
        q_Input_file_URL.setContextMenuPolicy(Qt.NoContextMenu)
        q_Figma_API_token = QLabel(central_widget)
        q_Figma_API_token.setText("Figma API token")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        q_Figma_API_token.setFont(font)
        q_Figma_API_token.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        q_Figma_API_token.setGeometry(QRect(29, 74, 87, 15))
        q_Figma_API_token.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        q_Figma_API_token.setMouseTracking(False)
        q_Figma_API_token.setContextMenuPolicy(Qt.NoContextMenu)
        q_Output_directory = QLabel(central_widget)
        q_Output_directory.setText("Output directory")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        q_Output_directory.setFont(font)
        q_Output_directory.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        q_Output_directory.setGeometry(QRect(29, 134, 85, 15))
        q_Output_directory.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        q_Output_directory.setMouseTracking(False)
        q_Output_directory.setContextMenuPolicy(Qt.NoContextMenu)
        q_Overwrite_handler = QLabel(central_widget)
        q_Overwrite_handler.setText("Overwrite handler")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        q_Overwrite_handler.setFont(font)
        q_Overwrite_handler.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        q_Overwrite_handler.setGeometry(QRect(57, 196, 93, 15))
        q_Overwrite_handler.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        q_Overwrite_handler.setMouseTracking(False)
        q_Overwrite_handler.setContextMenuPolicy(Qt.NoContextMenu)
        q_Text_Field_Inut_File_URL = QLabel(central_widget)
        q_Text_Field_Inut_File_URL.setGeometry(QRect(25, 37, 413, 30))
        q_svg_widget_q_Text_Field_Inut_File_URL_ = QSvgWidget(q_Text_Field_Inut_File_URL)
        q_svg_widget_q_Text_Field_Inut_File_URL_.setGeometry(QRect(0, 0, 413, 30))
        q_svg_widget_q_Text_Field_Inut_File_URL_.load("svg/file3.svg")
        q_Text_Field_Inut_File_URL__ = QLineEdit(central_widget)
        q_Text_Field_Inut_File_URL__.setGeometry(QRect(25, 37, 413, 30))
        q_Text_Field_Inut_File_URL__.setAutoFillBackground(False)
        q_Text_Field_Inut_File_URL__.setObjectName("q_Text_Field_Inut_File_URL__")
        q_Text_Field_Inut_File_URL__.setMouseTracking(True)
        q_Text_Field_Inut_File_URL__.setContextMenuPolicy(Qt.NoContextMenu)
        q_Text_Field_Inut_File_URL__.setAcceptDrops(False)

        def __q_Text_Field_Inut_File_URL___text_changed(self):
            try:
                current_text = q_Text_Field_Inut_File_URL__.text()
                GuiHandler.q_Text_Field_Inut_File_URL___text_changed(current_text)
            except:
                print("No function q_Text_Field_Inut_File_URL___clicked defined. Current text : " + current_text)

        q_Text_Field_Inut_File_URL__.textChanged.connect(__q_Text_Field_Inut_File_URL___text_changed)
        q_Text_Field_Inut_File_URL__.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 255);color: rgba(255, 255, 255, 255); ")
        q_Text_Field_Inut_File_URL__.setPlaceholderText("Text Field Inut File URL")
        q_Text_Field_Figma_API_Token = QLabel(central_widget)
        q_Text_Field_Figma_API_Token.setGeometry(QRect(23, 96, 413, 30))
        q_svg_widget_q_Text_Field_Figma_API_Token_ = QSvgWidget(q_Text_Field_Figma_API_Token)
        q_svg_widget_q_Text_Field_Figma_API_Token_.setGeometry(QRect(0, 0, 413, 30))
        q_svg_widget_q_Text_Field_Figma_API_Token_.load("svg/file4.svg")
        q_Text_Field_Figma_API_Token__ = QLineEdit(central_widget)
        q_Text_Field_Figma_API_Token__.setGeometry(QRect(23, 96, 413, 30))
        q_Text_Field_Figma_API_Token__.setAutoFillBackground(False)
        q_Text_Field_Figma_API_Token__.setObjectName("q_Text_Field_Figma_API_Token__")
        q_Text_Field_Figma_API_Token__.setMouseTracking(True)
        q_Text_Field_Figma_API_Token__.setContextMenuPolicy(Qt.NoContextMenu)
        q_Text_Field_Figma_API_Token__.setAcceptDrops(False)

        def __q_Text_Field_Figma_API_Token___text_changed(self):
            try:
                current_text = q_Text_Field_Figma_API_Token__.text()
                GuiHandler.q_Text_Field_Figma_API_Token___text_changed(current_text)
            except:
                print("No function q_Text_Field_Figma_API_Token___clicked defined. Current text : " + current_text)

        q_Text_Field_Figma_API_Token__.textChanged.connect(__q_Text_Field_Figma_API_Token___text_changed)
        q_Text_Field_Figma_API_Token__.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 255);color: rgba(255, 255, 255, 255); ")
        q_Text_Field_Figma_API_Token__.setPlaceholderText("Text Field Figma API Token")
        q_Text_Field_Output_Directory = QLabel(central_widget)
        q_Text_Field_Output_Directory.setGeometry(QRect(23, 156, 413, 30))
        q_svg_widget_q_Text_Field_Output_Directory_ = QSvgWidget(q_Text_Field_Output_Directory)
        q_svg_widget_q_Text_Field_Output_Directory_.setGeometry(QRect(0, 0, 413, 30))
        q_svg_widget_q_Text_Field_Output_Directory_.load("svg/file5.svg")
        q_Text_Field_Output_Directory__ = QLineEdit(central_widget)
        q_Text_Field_Output_Directory__.setGeometry(QRect(23, 156, 413, 30))
        q_Text_Field_Output_Directory__.setAutoFillBackground(False)
        q_Text_Field_Output_Directory__.setObjectName("q_Text_Field_Output_Directory__")
        q_Text_Field_Output_Directory__.setMouseTracking(True)
        q_Text_Field_Output_Directory__.setContextMenuPolicy(Qt.NoContextMenu)
        q_Text_Field_Output_Directory__.setAcceptDrops(False)

        def __q_Text_Field_Output_Directory___text_changed(self):
            try:
                current_text = q_Text_Field_Output_Directory__.text()
                GuiHandler.q_Text_Field_Output_Directory___text_changed(current_text)
            except:
                print("No function q_Text_Field_Output_Directory___clicked defined. Current text : " + current_text)

        q_Text_Field_Output_Directory__.textChanged.connect(__q_Text_Field_Output_Directory___text_changed)
        q_Text_Field_Output_Directory__.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 255);color: rgba(255, 255, 255, 255); ")
        q_Text_Field_Output_Directory__.setPlaceholderText("Text Field Output Directory")
        q_Unchecked = QLabel(central_widget)
        q_Unchecked.setGeometry(QRect(25, 194, 19, 19))
        q_svg_widget_q_Unchecked_ = QSvgWidget(q_Unchecked)
        q_svg_widget_q_Unchecked_.setGeometry(QRect(0, 0, 19, 19))
        q_svg_widget_q_Unchecked_.load("svg/file6.svg")
        q_Checked = QLabel(central_widget)
        q_Checked.setGeometry(QRect(25, 194, 19, 19))
        q_svg_widget_q_Checked_ = QSvgWidget(q_Checked)
        q_svg_widget_q_Checked_.setGeometry(QRect(0, 0, 19, 19))
        q_svg_widget_q_Checked_.load("svg/file7.svg")
        q_ = QLabel(central_widget)
        q_.setText("􀆅")
        font = QFont()
        font.setFamilies([u"SF Pro"])
        font.setPointSize(6)
        q_.setFont(font)
        q_.setStyleSheet("color: rgba(254.00000005960464, 254.00000005960464, 254.00000005960464, 255.0)")
        q_.setGeometry(QRect(25, 194, 19, 19))
        q_.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        q_.setMouseTracking(False)
        q_.setContextMenuPolicy(Qt.NoContextMenu)
        q_CheckboxOverwriteHandler = QPushButton(central_widget)
        q_CheckboxOverwriteHandler.setGeometry(QRect(25, 194, 19, 19))
        q_CheckboxOverwriteHandler.setFlat(True)
        q_CheckboxOverwriteHandler.setAutoFillBackground(False)
        q_CheckboxOverwriteHandler.setObjectName("q_CheckboxOverwriteHandler")
        q_CheckboxOverwriteHandler.setMouseTracking(True)
        q_CheckboxOverwriteHandler.setContextMenuPolicy(Qt.NoContextMenu)
        q_CheckboxOverwriteHandler.setAcceptDrops(False)

        def __q_CheckboxOverwriteHandler_check_changed(self):
            try:
                q_.setVisible(not q_.isVisible())
                q_Checked.setVisible(not q_Checked.isVisible())
                q_Checked_.setVisible(not q_Checked_.isVisible())
                GuiHandler.q_CheckboxOverwriteHandler_check_changed(q_Checked.isVisible())
            except:
                print("No function q_CheckboxOverwriteHandler_check_changed defined. Checked = " + str(
                    q_Checked.isVisible()))

        q_CheckboxOverwriteHandler.clicked.connect(__q_CheckboxOverwriteHandler_check_changed)
        MainWindow.setCentralWidget(central_widget)


class Windowq_Gradients(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(268.79999999999995, 172.2)
        central_widget = QWidget(MainWindow)
        MainWindow.setFixedSize(268.79999999999995, 172.2)
        MainWindow.setWindowTitle("Gradients")
        q_Gradients_ = QLabel(central_widget)
        q_Gradients_.setGeometry(QRect(0, 0, 268, 172))
        q_svg_widget_q_Gradients__ = QSvgWidget(q_Gradients_)
        q_svg_widget_q_Gradients__.setGeometry(QRect(0, 0, 268, 172))
        q_svg_widget_q_Gradients__.load("svg/file8.svg")
        q_Rectangle_1 = QLabel(central_widget)
        q_Rectangle_1.setGeometry(QRect(33, 16, 173, 62))
        q_svg_widget_q_Rectangle_1_ = QSvgWidget(q_Rectangle_1)
        q_svg_widget_q_Rectangle_1_.setGeometry(QRect(0, 0, 173, 62))
        q_svg_widget_q_Rectangle_1_.load("svg/file9.svg")
        q_Rectangle_2 = QLabel(central_widget)
        q_Rectangle_2.setGeometry(QRect(42, 105, 173, 62))
        q_svg_widget_q_Rectangle_2_ = QSvgWidget(q_Rectangle_2)
        q_svg_widget_q_Rectangle_2_.setGeometry(QRect(0, 0, 173, 62))
        q_svg_widget_q_Rectangle_2_.load("svg/file10.svg")
        MainWindow.setCentralWidget(central_widget)


def open_window():
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Windowq_PyQt_Figma_Designer()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    open_window()