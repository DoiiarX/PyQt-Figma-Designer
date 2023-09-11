try:
    import gui_handler as GuiHandler
    import gui_controller as GuiController
except Exception as e:
    print("Exception while importing gui_handler.py or controller.py")
    print(e)
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


class QWindowViewPyqtFigmaDesigner(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(466.9, 311.5)
        central_widget = QWidget(MainWindow)
        MainWindow.setFixedSize(466.9, 311.5)
        MainWindow.setWindowTitle("PyQt Figma Designer")

        view_pyqt_figma_designer_0 = QLabel(central_widget)
        view_pyqt_figma_designer_0.setGeometry(QRect(0, 0, 466, 311))
        q_svg_widget_view_pyqt_figma_designer_0 = QSvgWidget(view_pyqt_figma_designer_0)
        q_svg_widget_view_pyqt_figma_designer_0.setGeometry(QRect(0, 0, 466, 311))
        q_svg_widget_view_pyqt_figma_designer_0.load("svg/file1.svg")
        view_rectangle_9 = QLabel(central_widget)

        view_rectangle_9_0 = QLabel(central_widget)
        view_rectangle_9_0.setGeometry(QRect(0, 0, 466, 311))
        q_svg_widget_view_rectangle_9_0 = QSvgWidget(view_rectangle_9_0)
        q_svg_widget_view_rectangle_9_0.setGeometry(QRect(0, 0, 466, 311))
        q_svg_widget_view_rectangle_9_0.load("svg/file2.svg")
        view_rectangle_8 = QLabel(central_widget)

        view_rectangle_8_0 = QLabel(central_widget)
        view_rectangle_8_0.setGeometry(QRect(0, 0, 466, 58))
        q_svg_widget_view_rectangle_8_0 = QSvgWidget(view_rectangle_8_0)
        q_svg_widget_view_rectangle_8_0.setGeometry(QRect(0, 0, 466, 58))
        q_svg_widget_view_rectangle_8_0.load("svg/file3.svg")
        view_custom_button_create_project = QLabel(central_widget)
        view_normal = QLabel(central_widget)

        view_normal_0 = QLabel(central_widget)
        view_normal_0.setGeometry(QRect(166, 266, 154, 33))
        q_svg_widget_view_normal_0 = QSvgWidget(view_normal_0)
        q_svg_widget_view_normal_0.setGeometry(QRect(0, 0, 154, 33))
        q_svg_widget_view_normal_0.load("svg/file4.svg")
        view_buttontext = QLabel(central_widget)
        view_buttontext_0 = QLabel(central_widget)
        view_buttontext_0.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_0.setFont(font)
        view_buttontext_0.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_0.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_0.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_0.setMouseTracking(False)
        view_buttontext_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_0_set_text(text: str):
            view_buttontext_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_0_set_text = view_buttontext_0_set_text
        except:
            print("No function view_buttontext_0_set_text defined. Current text : " + view_buttontext_0.text())

        view_buttontext_1 = QPushButton(central_widget)
        view_buttontext_1.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_1.setFlat(True)
        view_buttontext_1.setAutoFillBackground(False)
        view_buttontext_1.setObjectName("view_buttontext_1")
        view_buttontext_1.setMouseTracking(True)
        view_buttontext_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_1.setAcceptDrops(False)

        def __view_buttontext_1_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_1_clicked()
            except:
                print("No function view_buttontext_1_clicked defined")

        view_buttontext_1.clicked.connect(__view_buttontext_1_clicked)
        view_buttontext_1.setFocusPolicy(Qt.NoFocus)
        view_buttontext_1.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_normal_1 = QLabel(central_widget)
        view_disabled = QLabel(central_widget)

        view_disabled_0 = QLabel(central_widget)
        view_disabled_0.setGeometry(QRect(166, 266, 154, 33))
        q_svg_widget_view_disabled_0 = QSvgWidget(view_disabled_0)
        q_svg_widget_view_disabled_0.setGeometry(QRect(0, 0, 154, 33))
        q_svg_widget_view_disabled_0.load("svg/file5.svg")
        view_buttontext_2 = QLabel(central_widget)
        view_buttontext_3 = QLabel(central_widget)
        view_buttontext_3.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_3.setFont(font)
        view_buttontext_3.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_3.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_3.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_3.setMouseTracking(False)
        view_buttontext_3.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_3_set_text(text: str):
            view_buttontext_3.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_3_set_text = view_buttontext_3_set_text
        except:
            print("No function view_buttontext_3_set_text defined. Current text : " + view_buttontext_3.text())

        view_buttontext_4 = QPushButton(central_widget)
        view_buttontext_4.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_4.setFlat(True)
        view_buttontext_4.setAutoFillBackground(False)
        view_buttontext_4.setObjectName("view_buttontext_4")
        view_buttontext_4.setMouseTracking(True)
        view_buttontext_4.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_4.setAcceptDrops(False)

        def __view_buttontext_4_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_4_clicked()
            except:
                print("No function view_buttontext_4_clicked defined")

        view_buttontext_4.clicked.connect(__view_buttontext_4_clicked)
        view_buttontext_4.setFocusPolicy(Qt.NoFocus)
        view_buttontext_4.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_disabled_1 = QLabel(central_widget)
        view_pressed = QLabel(central_widget)

        view_pressed_0 = QLabel(central_widget)
        view_pressed_0.setGeometry(QRect(166, 266, 154, 33))
        q_svg_widget_view_pressed_0 = QSvgWidget(view_pressed_0)
        q_svg_widget_view_pressed_0.setGeometry(QRect(0, 0, 154, 33))
        q_svg_widget_view_pressed_0.load("svg/file6.svg")
        view_buttontext_5 = QLabel(central_widget)
        view_buttontext_6 = QLabel(central_widget)
        view_buttontext_6.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_6.setFont(font)
        view_buttontext_6.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_6.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_6.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_6.setMouseTracking(False)
        view_buttontext_6.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_6_set_text(text: str):
            view_buttontext_6.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_6_set_text = view_buttontext_6_set_text
        except:
            print("No function view_buttontext_6_set_text defined. Current text : " + view_buttontext_6.text())

        view_buttontext_7 = QPushButton(central_widget)
        view_buttontext_7.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_7.setFlat(True)
        view_buttontext_7.setAutoFillBackground(False)
        view_buttontext_7.setObjectName("view_buttontext_7")
        view_buttontext_7.setMouseTracking(True)
        view_buttontext_7.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_7.setAcceptDrops(False)

        def __view_buttontext_7_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_7_clicked()
            except:
                print("No function view_buttontext_7_clicked defined")

        view_buttontext_7.clicked.connect(__view_buttontext_7_clicked)
        view_buttontext_7.setFocusPolicy(Qt.NoFocus)
        view_buttontext_7.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_pressed_1 = QLabel(central_widget)
        view_mouse_over = QLabel(central_widget)

        view_mouse_over_0 = QLabel(central_widget)
        view_mouse_over_0.setGeometry(QRect(166, 266, 154, 33))
        q_svg_widget_view_mouse_over_0 = QSvgWidget(view_mouse_over_0)
        q_svg_widget_view_mouse_over_0.setGeometry(QRect(0, 0, 154, 33))
        q_svg_widget_view_mouse_over_0.load("svg/file7.svg")
        view_buttontext_8 = QLabel(central_widget)
        view_buttontext_9 = QLabel(central_widget)
        view_buttontext_9.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_9.setFont(font)
        view_buttontext_9.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_9.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_9.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_9.setMouseTracking(False)
        view_buttontext_9.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_9_set_text(text: str):
            view_buttontext_9.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_9_set_text = view_buttontext_9_set_text
        except:
            print("No function view_buttontext_9_set_text defined. Current text : " + view_buttontext_9.text())

        view_buttontext_10 = QPushButton(central_widget)
        view_buttontext_10.setGeometry(QRect(208, 276, 70, 12))
        view_buttontext_10.setFlat(True)
        view_buttontext_10.setAutoFillBackground(False)
        view_buttontext_10.setObjectName("view_buttontext_10")
        view_buttontext_10.setMouseTracking(True)
        view_buttontext_10.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_10.setAcceptDrops(False)

        def __view_buttontext_10_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_10_clicked()
            except:
                print("No function view_buttontext_10_clicked defined")

        view_buttontext_10.clicked.connect(__view_buttontext_10_clicked)
        view_buttontext_10.setFocusPolicy(Qt.NoFocus)
        view_buttontext_10.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_mouse_over_1 = QLabel(central_widget)
        view_custom_button_create_project_0 = QLabel(central_widget)

        view_custom_button_create_project_1 = QPushButton(central_widget)
        view_custom_button_create_project_1.setGeometry(QRect(166, 266, 154, 33))
        view_custom_button_create_project_1.setFlat(True)
        view_custom_button_create_project_1.setAutoFillBackground(False)
        view_custom_button_create_project_1.setObjectName("view_custom_button_create_project_1")
        view_custom_button_create_project_1.setMouseTracking(True)
        view_custom_button_create_project_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_custom_button_create_project_1.setAcceptDrops(False)
        view_custom_button_create_project_1.setFocusPolicy(Qt.NoFocus)
        self.view_custom_button_create_project_1_enabled = True

        def __view_custom_button_create_project_1_mouse_over(*args, **kwargs):
            if self.view_custom_button_create_project_1_enabled:
                view_mouse_over.setVisible(True)
                view_mouse_over_0.setVisible(True)
                view_mouse_over_1.setVisible(True)
                view_buttontext_8.setVisible(True)
                view_buttontext_9.setVisible(True)
                view_buttontext_10.setVisible(True)
                view_pressed.setVisible(False)
                view_pressed_0.setVisible(False)
                view_pressed_1.setVisible(False)
                view_buttontext_5.setVisible(False)
                view_buttontext_6.setVisible(False)
                view_buttontext_7.setVisible(False)
                view_disabled.setVisible(False)
                view_disabled_0.setVisible(False)
                view_disabled_1.setVisible(False)
                view_buttontext_2.setVisible(False)
                view_buttontext_3.setVisible(False)
                view_buttontext_4.setVisible(False)

        def __view_custom_button_create_project_1_mouse_leave(*args, **kwargs):
            if self.view_custom_button_create_project_1_enabled:
                view_mouse_over.setVisible(False)
                view_mouse_over_0.setVisible(False)
                view_mouse_over_1.setVisible(False)
                view_buttontext_8.setVisible(False)
                view_buttontext_9.setVisible(False)
                view_buttontext_10.setVisible(False)
                view_pressed.setVisible(False)
                view_pressed_0.setVisible(False)
                view_pressed_1.setVisible(False)
                view_buttontext_5.setVisible(False)
                view_buttontext_6.setVisible(False)
                view_buttontext_7.setVisible(False)
                view_disabled.setVisible(False)
                view_disabled_0.setVisible(False)
                view_disabled_1.setVisible(False)
                view_buttontext_2.setVisible(False)
                view_buttontext_3.setVisible(False)
                view_buttontext_4.setVisible(False)

        def __view_custom_button_create_project_1_mouse_press(*args, **kwargs):
            if self.view_custom_button_create_project_1_enabled:
                view_mouse_over.setVisible(False)
                view_mouse_over_0.setVisible(False)
                view_mouse_over_1.setVisible(False)
                view_buttontext_8.setVisible(False)
                view_buttontext_9.setVisible(False)
                view_buttontext_10.setVisible(False)
                view_pressed.setVisible(True)
                view_pressed_0.setVisible(True)
                view_pressed_1.setVisible(True)
                view_buttontext_5.setVisible(True)
                view_buttontext_6.setVisible(True)
                view_buttontext_7.setVisible(True)
                view_disabled.setVisible(False)
                view_disabled_0.setVisible(False)
                view_disabled_1.setVisible(False)
                view_buttontext_2.setVisible(False)
                view_buttontext_3.setVisible(False)
                view_buttontext_4.setVisible(False)

        def __view_custom_button_create_project_1_mouse_release(*args, **kwargs):
            if self.view_custom_button_create_project_1_enabled:
                view_mouse_over.setVisible(True)
                view_mouse_over_0.setVisible(True)
                view_mouse_over_1.setVisible(True)
                view_buttontext_8.setVisible(True)
                view_buttontext_9.setVisible(True)
                view_buttontext_10.setVisible(True)
                view_pressed.setVisible(False)
                view_pressed_0.setVisible(False)
                view_pressed_1.setVisible(False)
                view_buttontext_5.setVisible(False)
                view_buttontext_6.setVisible(False)
                view_buttontext_7.setVisible(False)
                view_disabled.setVisible(False)
                view_disabled_0.setVisible(False)
                view_disabled_1.setVisible(False)
                view_buttontext_2.setVisible(False)
                view_buttontext_3.setVisible(False)
                view_buttontext_4.setVisible(False)
                view_custom_button_create_project_1.clicked.emit()

        def __view_custom_button_create_project_1_disable(*args, **kwargs):
            self.view_custom_button_create_project_1_enabled = False
            view_mouse_over.setVisible(False)
            view_mouse_over_0.setVisible(False)
            view_mouse_over_1.setVisible(False)
            view_buttontext_8.setVisible(False)
            view_buttontext_9.setVisible(False)
            view_buttontext_10.setVisible(False)
            view_pressed.setVisible(False)
            view_pressed_0.setVisible(False)
            view_pressed_1.setVisible(False)
            view_buttontext_5.setVisible(False)
            view_buttontext_6.setVisible(False)
            view_buttontext_7.setVisible(False)
            view_disabled.setVisible(True)
            view_disabled_0.setVisible(True)
            view_disabled_1.setVisible(True)
            view_buttontext_2.setVisible(True)
            view_buttontext_3.setVisible(True)
            view_buttontext_4.setVisible(True)
            view_custom_button_create_project_1.setMouseTracking(False)
            view_custom_button_create_project_1.setFocusPolicy(Qt.NoFocus)
            view_custom_button_create_project_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        def __view_custom_button_create_project_1_enable(*args, **kwargs):
            self.view_custom_button_create_project_1_enabled = True
            view_mouse_over.setVisible(False)
            view_mouse_over_0.setVisible(False)
            view_mouse_over_1.setVisible(False)
            view_buttontext_8.setVisible(False)
            view_buttontext_9.setVisible(False)
            view_buttontext_10.setVisible(False)
            view_pressed.setVisible(False)
            view_pressed_0.setVisible(False)
            view_pressed_1.setVisible(False)
            view_buttontext_5.setVisible(False)
            view_buttontext_6.setVisible(False)
            view_buttontext_7.setVisible(False)
            view_disabled.setVisible(False)
            view_disabled_0.setVisible(False)
            view_disabled_1.setVisible(False)
            view_buttontext_2.setVisible(False)
            view_buttontext_3.setVisible(False)
            view_buttontext_4.setVisible(False)
            view_custom_button_create_project_1.setMouseTracking(True)

        def __view_custom_button_create_project_1_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_custom_button_create_project_1_clicked()
            except:
                print("No function view_custom_button_create_project_1_clicked defined")

        view_custom_button_create_project_1.clicked.connect(__view_custom_button_create_project_1_clicked)
        view_custom_button_create_project_1.enterEvent = __view_custom_button_create_project_1_mouse_over
        view_custom_button_create_project_1.leaveEvent = __view_custom_button_create_project_1_mouse_leave
        view_custom_button_create_project_1.mousePressEvent = __view_custom_button_create_project_1_mouse_press
        view_custom_button_create_project_1.mouseReleaseEvent = __view_custom_button_create_project_1_mouse_release
        view_custom_button_create_project_1.disable = __view_custom_button_create_project_1_disable
        view_custom_button_create_project_1.enable = __view_custom_button_create_project_1_enable

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_custom_button_create_project_1_enable = view_custom_button_create_project_1.enable
            GuiController.ViewPyqtFigmaDesignerController.view_custom_button_create_project_1_disable = view_custom_button_create_project_1.disable
        except:
            print("No function view_custom_button_create_project_1_enable defined")
            print("No function view_custom_button_create_project_1_disable defined")
        view_mouse_over.setVisible(False)
        view_mouse_over_0.setVisible(False)
        view_mouse_over_1.setVisible(False)
        view_buttontext_8.setVisible(False)
        view_buttontext_9.setVisible(False)
        view_buttontext_10.setVisible(False)
        view_pressed.setVisible(False)
        view_pressed_0.setVisible(False)
        view_pressed_1.setVisible(False)
        view_buttontext_5.setVisible(False)
        view_buttontext_6.setVisible(False)
        view_buttontext_7.setVisible(False)
        view_disabled.setVisible(False)
        view_disabled_0.setVisible(False)
        view_disabled_1.setVisible(False)
        view_buttontext_2.setVisible(False)
        view_buttontext_3.setVisible(False)
        view_buttontext_4.setVisible(False)
        view_custom_button_browse = QLabel(central_widget)
        view_normal_2 = QLabel(central_widget)

        view_normal_3 = QLabel(central_widget)
        view_normal_3.setGeometry(QRect(324, 84, 121, 33))
        q_svg_widget_view_normal_3 = QSvgWidget(view_normal_3)
        q_svg_widget_view_normal_3.setGeometry(QRect(0, 0, 121, 33))
        q_svg_widget_view_normal_3.load("svg/file8.svg")
        view_buttontext_11 = QLabel(central_widget)
        view_buttontext_12 = QLabel(central_widget)
        view_buttontext_12.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_12.setFont(font)
        view_buttontext_12.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_12.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_12.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_12.setMouseTracking(False)
        view_buttontext_12.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_12_set_text(text: str):
            view_buttontext_12.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_12_set_text = view_buttontext_12_set_text
        except:
            print("No function view_buttontext_12_set_text defined. Current text : " + view_buttontext_12.text())

        view_buttontext_13 = QPushButton(central_widget)
        view_buttontext_13.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_13.setFlat(True)
        view_buttontext_13.setAutoFillBackground(False)
        view_buttontext_13.setObjectName("view_buttontext_13")
        view_buttontext_13.setMouseTracking(True)
        view_buttontext_13.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_13.setAcceptDrops(False)

        def __view_buttontext_13_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_13_clicked()
            except:
                print("No function view_buttontext_13_clicked defined")

        view_buttontext_13.clicked.connect(__view_buttontext_13_clicked)
        view_buttontext_13.setFocusPolicy(Qt.NoFocus)
        view_buttontext_13.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_normal_4 = QLabel(central_widget)
        view_disabled_2 = QLabel(central_widget)

        view_disabled_3 = QLabel(central_widget)
        view_disabled_3.setGeometry(QRect(324, 84, 121, 33))
        q_svg_widget_view_disabled_3 = QSvgWidget(view_disabled_3)
        q_svg_widget_view_disabled_3.setGeometry(QRect(0, 0, 121, 33))
        q_svg_widget_view_disabled_3.load("svg/file9.svg")
        view_buttontext_14 = QLabel(central_widget)
        view_buttontext_15 = QLabel(central_widget)
        view_buttontext_15.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_15.setFont(font)
        view_buttontext_15.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_15.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_15.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_15.setMouseTracking(False)
        view_buttontext_15.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_15_set_text(text: str):
            view_buttontext_15.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_15_set_text = view_buttontext_15_set_text
        except:
            print("No function view_buttontext_15_set_text defined. Current text : " + view_buttontext_15.text())

        view_buttontext_16 = QPushButton(central_widget)
        view_buttontext_16.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_16.setFlat(True)
        view_buttontext_16.setAutoFillBackground(False)
        view_buttontext_16.setObjectName("view_buttontext_16")
        view_buttontext_16.setMouseTracking(True)
        view_buttontext_16.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_16.setAcceptDrops(False)

        def __view_buttontext_16_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_16_clicked()
            except:
                print("No function view_buttontext_16_clicked defined")

        view_buttontext_16.clicked.connect(__view_buttontext_16_clicked)
        view_buttontext_16.setFocusPolicy(Qt.NoFocus)
        view_buttontext_16.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_disabled_4 = QLabel(central_widget)
        view_pressed_2 = QLabel(central_widget)

        view_pressed_3 = QLabel(central_widget)
        view_pressed_3.setGeometry(QRect(324, 84, 121, 33))
        q_svg_widget_view_pressed_3 = QSvgWidget(view_pressed_3)
        q_svg_widget_view_pressed_3.setGeometry(QRect(0, 0, 121, 33))
        q_svg_widget_view_pressed_3.load("svg/file10.svg")
        view_buttontext_17 = QLabel(central_widget)
        view_buttontext_18 = QLabel(central_widget)
        view_buttontext_18.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_18.setFont(font)
        view_buttontext_18.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_18.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_18.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_18.setMouseTracking(False)
        view_buttontext_18.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_18_set_text(text: str):
            view_buttontext_18.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_18_set_text = view_buttontext_18_set_text
        except:
            print("No function view_buttontext_18_set_text defined. Current text : " + view_buttontext_18.text())

        view_buttontext_19 = QPushButton(central_widget)
        view_buttontext_19.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_19.setFlat(True)
        view_buttontext_19.setAutoFillBackground(False)
        view_buttontext_19.setObjectName("view_buttontext_19")
        view_buttontext_19.setMouseTracking(True)
        view_buttontext_19.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_19.setAcceptDrops(False)

        def __view_buttontext_19_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_19_clicked()
            except:
                print("No function view_buttontext_19_clicked defined")

        view_buttontext_19.clicked.connect(__view_buttontext_19_clicked)
        view_buttontext_19.setFocusPolicy(Qt.NoFocus)
        view_buttontext_19.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_pressed_4 = QLabel(central_widget)
        view_mouse_over_2 = QLabel(central_widget)

        view_mouse_over_3 = QLabel(central_widget)
        view_mouse_over_3.setGeometry(QRect(324, 84, 121, 33))
        q_svg_widget_view_mouse_over_3 = QSvgWidget(view_mouse_over_3)
        q_svg_widget_view_mouse_over_3.setGeometry(QRect(0, 0, 121, 33))
        q_svg_widget_view_mouse_over_3.load("svg/file11.svg")
        view_buttontext_20 = QLabel(central_widget)
        view_buttontext_21 = QLabel(central_widget)
        view_buttontext_21.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_buttontext_21.setFont(font)
        view_buttontext_21.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        view_buttontext_21.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_21.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        view_buttontext_21.setMouseTracking(False)
        view_buttontext_21.setContextMenuPolicy(Qt.NoContextMenu)

        def view_buttontext_21_set_text(text: str):
            view_buttontext_21.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_buttontext_21_set_text = view_buttontext_21_set_text
        except:
            print("No function view_buttontext_21_set_text defined. Current text : " + view_buttontext_21.text())

        view_buttontext_22 = QPushButton(central_widget)
        view_buttontext_22.setGeometry(QRect(366, 95, 37, 12))
        view_buttontext_22.setFlat(True)
        view_buttontext_22.setAutoFillBackground(False)
        view_buttontext_22.setObjectName("view_buttontext_22")
        view_buttontext_22.setMouseTracking(True)
        view_buttontext_22.setContextMenuPolicy(Qt.NoContextMenu)
        view_buttontext_22.setAcceptDrops(False)

        def __view_buttontext_22_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_buttontext_22_clicked()
            except:
                print("No function view_buttontext_22_clicked defined")

        view_buttontext_22.clicked.connect(__view_buttontext_22_clicked)
        view_buttontext_22.setFocusPolicy(Qt.NoFocus)
        view_buttontext_22.setStyleSheet("background-color: rgba(255, 255, 255, 30);")
        view_mouse_over_4 = QLabel(central_widget)
        view_custom_button_browse_0 = QLabel(central_widget)

        view_custom_button_browse_1 = QPushButton(central_widget)
        view_custom_button_browse_1.setGeometry(QRect(324, 84, 121, 33))
        view_custom_button_browse_1.setFlat(True)
        view_custom_button_browse_1.setAutoFillBackground(False)
        view_custom_button_browse_1.setObjectName("view_custom_button_browse_1")
        view_custom_button_browse_1.setMouseTracking(True)
        view_custom_button_browse_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_custom_button_browse_1.setAcceptDrops(False)
        view_custom_button_browse_1.setFocusPolicy(Qt.NoFocus)
        self.view_custom_button_browse_1_enabled = True

        def __view_custom_button_browse_1_mouse_over(*args, **kwargs):
            if self.view_custom_button_browse_1_enabled:
                view_mouse_over_2.setVisible(True)
                view_mouse_over_3.setVisible(True)
                view_mouse_over_4.setVisible(True)
                view_buttontext_20.setVisible(True)
                view_buttontext_21.setVisible(True)
                view_buttontext_22.setVisible(True)
                view_pressed_2.setVisible(False)
                view_pressed_3.setVisible(False)
                view_pressed_4.setVisible(False)
                view_buttontext_17.setVisible(False)
                view_buttontext_18.setVisible(False)
                view_buttontext_19.setVisible(False)
                view_disabled_2.setVisible(False)
                view_disabled_3.setVisible(False)
                view_disabled_4.setVisible(False)
                view_buttontext_14.setVisible(False)
                view_buttontext_15.setVisible(False)
                view_buttontext_16.setVisible(False)

        def __view_custom_button_browse_1_mouse_leave(*args, **kwargs):
            if self.view_custom_button_browse_1_enabled:
                view_mouse_over_2.setVisible(False)
                view_mouse_over_3.setVisible(False)
                view_mouse_over_4.setVisible(False)
                view_buttontext_20.setVisible(False)
                view_buttontext_21.setVisible(False)
                view_buttontext_22.setVisible(False)
                view_pressed_2.setVisible(False)
                view_pressed_3.setVisible(False)
                view_pressed_4.setVisible(False)
                view_buttontext_17.setVisible(False)
                view_buttontext_18.setVisible(False)
                view_buttontext_19.setVisible(False)
                view_disabled_2.setVisible(False)
                view_disabled_3.setVisible(False)
                view_disabled_4.setVisible(False)
                view_buttontext_14.setVisible(False)
                view_buttontext_15.setVisible(False)
                view_buttontext_16.setVisible(False)

        def __view_custom_button_browse_1_mouse_press(*args, **kwargs):
            if self.view_custom_button_browse_1_enabled:
                view_mouse_over_2.setVisible(False)
                view_mouse_over_3.setVisible(False)
                view_mouse_over_4.setVisible(False)
                view_buttontext_20.setVisible(False)
                view_buttontext_21.setVisible(False)
                view_buttontext_22.setVisible(False)
                view_pressed_2.setVisible(True)
                view_pressed_3.setVisible(True)
                view_pressed_4.setVisible(True)
                view_buttontext_17.setVisible(True)
                view_buttontext_18.setVisible(True)
                view_buttontext_19.setVisible(True)
                view_disabled_2.setVisible(False)
                view_disabled_3.setVisible(False)
                view_disabled_4.setVisible(False)
                view_buttontext_14.setVisible(False)
                view_buttontext_15.setVisible(False)
                view_buttontext_16.setVisible(False)

        def __view_custom_button_browse_1_mouse_release(*args, **kwargs):
            if self.view_custom_button_browse_1_enabled:
                view_mouse_over_2.setVisible(True)
                view_mouse_over_3.setVisible(True)
                view_mouse_over_4.setVisible(True)
                view_buttontext_20.setVisible(True)
                view_buttontext_21.setVisible(True)
                view_buttontext_22.setVisible(True)
                view_pressed_2.setVisible(False)
                view_pressed_3.setVisible(False)
                view_pressed_4.setVisible(False)
                view_buttontext_17.setVisible(False)
                view_buttontext_18.setVisible(False)
                view_buttontext_19.setVisible(False)
                view_disabled_2.setVisible(False)
                view_disabled_3.setVisible(False)
                view_disabled_4.setVisible(False)
                view_buttontext_14.setVisible(False)
                view_buttontext_15.setVisible(False)
                view_buttontext_16.setVisible(False)
                view_custom_button_browse_1.clicked.emit()

        def __view_custom_button_browse_1_disable(*args, **kwargs):
            self.view_custom_button_browse_1_enabled = False
            view_mouse_over_2.setVisible(False)
            view_mouse_over_3.setVisible(False)
            view_mouse_over_4.setVisible(False)
            view_buttontext_20.setVisible(False)
            view_buttontext_21.setVisible(False)
            view_buttontext_22.setVisible(False)
            view_pressed_2.setVisible(False)
            view_pressed_3.setVisible(False)
            view_pressed_4.setVisible(False)
            view_buttontext_17.setVisible(False)
            view_buttontext_18.setVisible(False)
            view_buttontext_19.setVisible(False)
            view_disabled_2.setVisible(True)
            view_disabled_3.setVisible(True)
            view_disabled_4.setVisible(True)
            view_buttontext_14.setVisible(True)
            view_buttontext_15.setVisible(True)
            view_buttontext_16.setVisible(True)
            view_custom_button_browse_1.setMouseTracking(False)
            view_custom_button_browse_1.setFocusPolicy(Qt.NoFocus)
            view_custom_button_browse_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        def __view_custom_button_browse_1_enable(*args, **kwargs):
            self.view_custom_button_browse_1_enabled = True
            view_mouse_over_2.setVisible(False)
            view_mouse_over_3.setVisible(False)
            view_mouse_over_4.setVisible(False)
            view_buttontext_20.setVisible(False)
            view_buttontext_21.setVisible(False)
            view_buttontext_22.setVisible(False)
            view_pressed_2.setVisible(False)
            view_pressed_3.setVisible(False)
            view_pressed_4.setVisible(False)
            view_buttontext_17.setVisible(False)
            view_buttontext_18.setVisible(False)
            view_buttontext_19.setVisible(False)
            view_disabled_2.setVisible(False)
            view_disabled_3.setVisible(False)
            view_disabled_4.setVisible(False)
            view_buttontext_14.setVisible(False)
            view_buttontext_15.setVisible(False)
            view_buttontext_16.setVisible(False)
            view_custom_button_browse_1.setMouseTracking(True)

        def __view_custom_button_browse_1_clicked(*args, **kwargs):
            try:
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_custom_button_browse_1_clicked()
            except:
                print("No function view_custom_button_browse_1_clicked defined")

        view_custom_button_browse_1.clicked.connect(__view_custom_button_browse_1_clicked)
        view_custom_button_browse_1.enterEvent = __view_custom_button_browse_1_mouse_over
        view_custom_button_browse_1.leaveEvent = __view_custom_button_browse_1_mouse_leave
        view_custom_button_browse_1.mousePressEvent = __view_custom_button_browse_1_mouse_press
        view_custom_button_browse_1.mouseReleaseEvent = __view_custom_button_browse_1_mouse_release
        view_custom_button_browse_1.disable = __view_custom_button_browse_1_disable
        view_custom_button_browse_1.enable = __view_custom_button_browse_1_enable

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_custom_button_browse_1_enable = view_custom_button_browse_1.enable
            GuiController.ViewPyqtFigmaDesignerController.view_custom_button_browse_1_disable = view_custom_button_browse_1.disable
        except:
            print("No function view_custom_button_browse_1_enable defined")
            print("No function view_custom_button_browse_1_disable defined")
        view_mouse_over_2.setVisible(False)
        view_mouse_over_3.setVisible(False)
        view_mouse_over_4.setVisible(False)
        view_buttontext_20.setVisible(False)
        view_buttontext_21.setVisible(False)
        view_buttontext_22.setVisible(False)
        view_pressed_2.setVisible(False)
        view_pressed_3.setVisible(False)
        view_pressed_4.setVisible(False)
        view_buttontext_17.setVisible(False)
        view_buttontext_18.setVisible(False)
        view_buttontext_19.setVisible(False)
        view_disabled_2.setVisible(False)
        view_disabled_3.setVisible(False)
        view_disabled_4.setVisible(False)
        view_buttontext_14.setVisible(False)
        view_buttontext_15.setVisible(False)
        view_buttontext_16.setVisible(False)
        view_checkbox_overwrite_handlers = QLabel(central_widget)
        view_overwrite_handlers = QLabel(central_widget)
        view_overwrite_handlers_0 = QLabel(central_widget)
        view_overwrite_handlers_0.setText("Overwrite handlers")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_overwrite_handlers_0.setFont(font)
        view_overwrite_handlers_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        view_overwrite_handlers_0.setGeometry(QRect(45, 237, 129, 12))
        view_overwrite_handlers_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_overwrite_handlers_0.setMouseTracking(False)
        view_overwrite_handlers_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_overwrite_handlers_0_set_text(text: str):
            view_overwrite_handlers_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_overwrite_handlers_0_set_text = view_overwrite_handlers_0_set_text
        except:
            print(
                "No function view_overwrite_handlers_0_set_text defined. Current text : " + view_overwrite_handlers_0.text())
        view_rectangle_31 = QLabel(central_widget)

        view_rectangle_31_0 = QLabel(central_widget)
        view_rectangle_31_0.setGeometry(QRect(17, 234, 19, 19))
        q_svg_widget_view_rectangle_31_0 = QSvgWidget(view_rectangle_31_0)
        q_svg_widget_view_rectangle_31_0.setGeometry(QRect(0, 0, 19, 19))
        q_svg_widget_view_rectangle_31_0.load("svg/file12.svg")
        view_checked = QLabel(central_widget)

        view_checked_0 = QLabel(central_widget)
        view_checked_0.setGeometry(QRect(21, 237, 12, 12))
        q_svg_widget_view_checked_0 = QSvgWidget(view_checked_0)
        q_svg_widget_view_checked_0.setGeometry(QRect(0, 0, 12, 12))
        q_svg_widget_view_checked_0.load("svg/file13.svg")
        view_path_5_copy_10 = QLabel(central_widget)

        view_path_5_copy_10_0 = QLabel(central_widget)
        view_path_5_copy_10_0.setGeometry(QRect(23, 240, 8, 6))
        q_svg_widget_view_path_5_copy_10_0 = QSvgWidget(view_path_5_copy_10_0)
        q_svg_widget_view_path_5_copy_10_0.setGeometry(QRect(0, 0, 8, 6))
        q_svg_widget_view_path_5_copy_10_0.load("svg/file14.svg")
        view_checked_1 = QLabel(central_widget)
        view_checkbox_overwrite_handlers_0 = QLabel(central_widget)

        self.view_checkbox_overwrite_handlers_1_checked = False
        view_checkbox_overwrite_handlers_1 = QPushButton(central_widget)
        view_checkbox_overwrite_handlers_1.setGeometry(QRect(17, 234, 157, 19))
        view_checkbox_overwrite_handlers_1.setFlat(True)
        view_checkbox_overwrite_handlers_1.setAutoFillBackground(False)
        view_checkbox_overwrite_handlers_1.setObjectName("view_checkbox_overwrite_handlers_1")
        view_checkbox_overwrite_handlers_1.setMouseTracking(True)
        view_checkbox_overwrite_handlers_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_checkbox_overwrite_handlers_1.setAcceptDrops(False)
        view_checkbox_overwrite_handlers_1.setFocusPolicy(Qt.NoFocus)
        view_checkbox_overwrite_handlers_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        def __view_checkbox_overwrite_handlers_1_check_changed():
            self.view_checkbox_overwrite_handlers_1_checked = not self.view_checkbox_overwrite_handlers_1_checked
            try:
                view_checked.setVisible(self.view_checkbox_overwrite_handlers_1_checked)
                view_checked_0.setVisible(self.view_checkbox_overwrite_handlers_1_checked)
                view_checked_1.setVisible(self.view_checkbox_overwrite_handlers_1_checked)
                view_path_5_copy_10.setVisible(self.view_checkbox_overwrite_handlers_1_checked)
                view_path_5_copy_10_0.setVisible(self.view_checkbox_overwrite_handlers_1_checked)

                GuiHandler.ViewPyqtFigmaDesignerHandler.view_checkbox_overwrite_handlers_1_check_changed(
                    self.view_checkbox_overwrite_handlers_1_checked)
            except:
                print("No function view_checkbox_overwrite_handlers_1_check_changed defined. Checked = " + str(
                    view_checked.isVisible()))

        view_checkbox_overwrite_handlers_1.clicked.connect(__view_checkbox_overwrite_handlers_1_check_changed)
        view_checked.setVisible(False)
        view_checked_0.setVisible(False)
        view_checked_1.setVisible(False)
        view_path_5_copy_10.setVisible(False)
        view_path_5_copy_10_0.setVisible(False)
        view_progressbar_progress = QLabel(central_widget)
        view_rectangle_7 = QLabel(central_widget)

        view_rectangle_7_0 = QLabel(central_widget)
        view_rectangle_7_0.setGeometry(QRect(0, 305, 466, 16))
        q_svg_widget_view_rectangle_7_0 = QSvgWidget(view_rectangle_7_0)
        q_svg_widget_view_rectangle_7_0.setGeometry(QRect(0, 0, 466, 16))
        q_svg_widget_view_rectangle_7_0.load("svg/file15.svg")
        view_rectangle_71 = QLabel(central_widget)

        view_rectangle_71_0 = QLabel(central_widget)
        view_rectangle_71_0.setGeometry(QRect(0, 305, 466, 16))
        q_svg_widget_view_rectangle_71_0 = QSvgWidget(view_rectangle_71_0)
        q_svg_widget_view_rectangle_71_0.setGeometry(QRect(0, 0, 466, 16))
        q_svg_widget_view_rectangle_71_0.load("svg/file16.svg")
        view_progressbar_progress_0 = QLabel(central_widget)

        def __view_progressbar_progress_1_set_progress(progress: float):
            view_rectangle_71.setGeometry(QRect(0.0, 305.9, 466.9 * progress, 16.799999999999997))
            view_rectangle_71_0.setGeometry(QRect(0.0, 305.9, 466.9 * progress, 16.799999999999997))

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_progressbar_progress_1_set_progress = __view_progressbar_progress_1_set_progress
        except:
            print("No function view_progressbar_progress_1_set_progress defined. Progress = " + str(progress))
        view_window_title = QLabel(central_widget)
        view_window_title_0 = QLabel(central_widget)
        view_window_title_0.setText("New Project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(18)
        view_window_title_0.setFont(font)
        view_window_title_0.setStyleSheet("color: rgba(37.00000159442425, 37.00000159442425, 37.00000159442425, 255.0)")
        view_window_title_0.setGeometry(QRect(17, 11, 144, 31))
        view_window_title_0.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        view_window_title_0.setMouseTracking(False)
        view_window_title_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_window_title_0_set_text(text: str):
            view_window_title_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_window_title_0_set_text = view_window_title_0_set_text
        except:
            print("No function view_window_title_0_set_text defined. Current text : " + view_window_title_0.text())
        view_group_slider_scale = QLabel(central_widget)
        view_slider_scale = QLabel(central_widget)
        view_ωelements2_highlight = QLabel(central_widget)

        view_ωelements2_highlight_0 = QLabel(central_widget)
        view_ωelements2_highlight_0.setGeometry(QRect(288, 242, 154, 4))
        q_svg_widget_view_ωelements2_highlight_0 = QSvgWidget(view_ωelements2_highlight_0)
        q_svg_widget_view_ωelements2_highlight_0.setGeometry(QRect(0, 0, 154, 4))
        q_svg_widget_view_ωelements2_highlight_0.load("svg/file17.svg")
        view_ωelementsknob = QLabel(central_widget)
        view__knob = QLabel(central_widget)

        view__knob_0 = QLabel(central_widget)
        view__knob_0.setGeometry(QRect(359, 237, 14, 14))
        q_svg_widget_view__knob_0 = QSvgWidget(view__knob_0)
        q_svg_widget_view__knob_0.setGeometry(QRect(0, 0, 14, 14))
        q_svg_widget_view__knob_0.load("svg/file18.svg")
        view_states = QLabel(central_widget)

        view_states_0 = QLabel(central_widget)
        view_states_0.setGeometry(QRect(352, 230, 28, 28))
        q_svg_widget_view_states_0 = QSvgWidget(view_states_0)
        q_svg_widget_view_states_0.setGeometry(QRect(0, 0, 28, 28))
        q_svg_widget_view_states_0.load("svg/file19.svg")
        view_states.setVisible(False)
        view_states_0.setVisible(False)
        view_ωelementsknob_0 = QLabel(central_widget)
        view_slider_scale_0 = QLabel(central_widget)

        self.view_slider_scale_1_captured = False
        self.view_slider_scale_1_value = 0.5

        def __view_slider_scale_1_update_thumb_position(*args, **kwargs):
            view_ωelementsknob.setGeometry(
                QRect(288.4 + 154.7 * self.view_slider_scale_1_value - 7.0, 237.29999999999998, 28.0, 28.0))
            view_ωelementsknob_0.setGeometry(
                QRect(288.4 + 154.7 * self.view_slider_scale_1_value - 7.0, 237.29999999999998, 28.0, 28.0))
            view__knob.setGeometry(
                QRect(288.4 + 154.7 * self.view_slider_scale_1_value - 7.0, 237.29999999999998, 28.0, 28.0))
            view__knob_0.setGeometry(
                QRect(288.4 + 154.7 * self.view_slider_scale_1_value - 7.0, 237.29999999999998, 28.0, 28.0))
            view_states.setGeometry(
                QRect(288.4 + 154.7 * self.view_slider_scale_1_value - 7.0, 237.29999999999998, 28.0, 28.0))
            view_states_0.setGeometry(
                QRect(288.4 + 154.7 * self.view_slider_scale_1_value - 7.0, 237.29999999999998, 28.0, 28.0))

            if self.view_slider_scale_1_captured and len(args) > 0:
                x, y, width, height = (288.4, 237.29999999999998, 154.7, 14.0)
                event = args[0]
                mouse_x, mouse_y = event.x(), event.y()
                self.view_slider_scale_1_value = mouse_x / width
                if self.view_slider_scale_1_value < 0:
                    self.view_slider_scale_1_value = 0
                if self.view_slider_scale_1_value > 1:
                    self.view_slider_scale_1_value = 1
                try:
                    GuiHandler.ViewPyqtFigmaDesignerHandler.view_slider_scale_1_value_changed(
                        self.view_slider_scale_1_value)
                except:
                    print("No function view_slider_scale_1_value_changed defined. Value = " + str(
                        self.view_slider_scale_1_value))

        def __view_slider_scale_1_mouse_press(*args, **kwargs):
            self.view_slider_scale_1_captured = True
            __view_slider_scale_1_update_thumb_position(*args, **kwargs)

        def __view_slider_scale_1_mouse_release(*args, **kwargs):
            self.view_slider_scale_1_captured = False

        def __view_slider_scale_1_mouse_move(*args, **kwargs):
            __view_slider_scale_1_update_thumb_position(*args, **kwargs)

        def __view_slider_scale_1_set_value(value: float):
            self.view_slider_scale_1_value = value
            __view_slider_scale_1_update_thumb_position()

        view_slider_scale_1 = QPushButton(central_widget)
        view_slider_scale_1.setGeometry(QRect(288, 237, 154, 14))
        view_slider_scale_1.setFlat(True)
        view_slider_scale_1.setAutoFillBackground(False)
        view_slider_scale_1.setObjectName("view_slider_scale_1")
        view_slider_scale_1.setMouseTracking(True)
        view_slider_scale_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_slider_scale_1.setAcceptDrops(False)
        view_slider_scale_1.setFocusPolicy(Qt.NoFocus)
        view_slider_scale_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        view_slider_scale_1.mousePressEvent = __view_slider_scale_1_mouse_press
        view_slider_scale_1.mouseReleaseEvent = __view_slider_scale_1_mouse_release
        view_slider_scale_1.mouseMoveEvent = __view_slider_scale_1_mouse_move
        try:
            GuiController.ViewPyqtFigmaDesignerController.view_slider_scale_1_set_value = __view_slider_scale_1_set_value
        except:
            print("No function view_slider_scale_1_set_value defined. Value = " + str(self.view_slider_scale_1_value))

        __view_slider_scale_1_update_thumb_position()
        view_scale = QLabel(central_widget)
        view_scale_0 = QLabel(central_widget)
        view_scale_0.setText("Scale")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_scale_0.setFont(font)
        view_scale_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        view_scale_0.setGeometry(QRect(215, 237, 57, 12))
        view_scale_0.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        view_scale_0.setMouseTracking(False)
        view_scale_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_scale_0_set_text(text: str):
            view_scale_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_scale_0_set_text = view_scale_0_set_text
        except:
            print("No function view_scale_0_set_text defined. Current text : " + view_scale_0.text())
        view_x1 = QLabel(central_widget)
        view_x1_0 = QLabel(central_widget)
        view_x1_0.setText("x1")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        view_x1_0.setFont(font)
        view_x1_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        view_x1_0.setGeometry(QRect(343, 221, 44, 12))
        view_x1_0.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        view_x1_0.setMouseTracking(False)
        view_x1_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_x1_0_set_text(text: str):
            view_x1_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_x1_0_set_text = view_x1_0_set_text
        except:
            print("No function view_x1_0_set_text defined. Current text : " + view_x1_0.text())
        view_group_slider_scale_0 = QLabel(central_widget)
        view_group_text_field_project_directory = QLabel(central_widget)
        view_inset = QLabel(central_widget)

        view_inset_0 = QLabel(central_widget)
        view_inset_0.setGeometry(QRect(18, 84, 294, 30))
        q_svg_widget_view_inset_0 = QSvgWidget(view_inset_0)
        q_svg_widget_view_inset_0.setGeometry(QRect(0, 0, 294, 30))
        q_svg_widget_view_inset_0.load("svg/file20.svg")
        view_label_and_value = QLabel(central_widget)
        view_label_and_value.setVisible(False)
        view_inset_1 = QLabel(central_widget)
        view_title = QLabel(central_widget)
        view_title_0 = QLabel(central_widget)
        view_title_0.setText("Project directory")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_title_0.setFont(font)
        view_title_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        view_title_0.setGeometry(QRect(32, 92, 128, 15))
        view_title_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_title_0.setMouseTracking(False)
        view_title_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_title_0_set_text(text: str):
            view_title_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_title_0_set_text = view_title_0_set_text
        except:
            print("No function view_title_0_set_text defined. Current text : " + view_title_0.text())
        view_custom_text_field_directory = QLabel(central_widget)
        view_background = QLabel(central_widget)
        view_bounds = QLabel(central_widget)
        view_hint = QLabel(central_widget)
        view_hint_0 = QLabel(central_widget)
        view_hint_0.setText("Enter path")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_hint_0.setFont(font)
        view_hint_0.setStyleSheet("color: rgba(60.00000022351742, 60.00000022351742, 67.00000360608101, 255.0)")
        view_hint_0.setGeometry(QRect(130, 92, 179, 15))
        view_hint_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_hint_0.setMouseTracking(False)
        view_hint_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_hint_0_set_text(text: str):
            view_hint_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_hint_0_set_text = view_hint_0_set_text
        except:
            print("No function view_hint_0_set_text defined. Current text : " + view_hint_0.text())
        view_text = QLabel(central_widget)
        view_text_0 = QLabel(central_widget)
        view_text_0.setText("...")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_text_0.setFont(font)
        view_text_0.setStyleSheet("color: rgba(105.8958412706852, 105.8958412706852, 105.8958412706852, 255.0)")
        view_text_0.setGeometry(QRect(125, 92, 179, 15))
        view_text_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_text_0.setMouseTracking(False)
        view_text_0.setContextMenuPolicy(Qt.NoContextMenu)

        def view_text_0_set_text(text: str):
            view_text_0.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_text_0_set_text = view_text_0_set_text
        except:
            print("No function view_text_0_set_text defined. Current text : " + view_text_0.text())
        view_custom_text_field_directory_0 = QLabel(central_widget)

        view_custom_text_field_directory_1 = QLineEdit(central_widget)
        view_custom_text_field_directory_1.setGeometry(QRect(125, 92, 179, 15))
        view_custom_text_field_directory_1.setAutoFillBackground(False)
        view_custom_text_field_directory_1.setObjectName("view_custom_text_field_directory_1")
        view_custom_text_field_directory_1.setMouseTracking(True)
        view_custom_text_field_directory_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_custom_text_field_directory_1.setAcceptDrops(False)
        view_custom_text_field_directory_1.setFont(view_text_0.font())
        text_color = view_text_0.styleSheet().split("color: ")[1].split(";")[0]
        view_text_0.setStyleSheet("color: rgba(255, 255, 255, 0);")
        view_text_0.hide()
        view_custom_text_field_directory_1.setStyleSheet(
            "color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
        try:
            GuiController.ViewPyqtFigmaDesignerController.view_custom_text_field_directory_1_set_text = view_custom_text_field_directory_1.setText
        except:
            print(
                "No function view_custom_text_field_directory_1_set_text defined. Current text : " + view_custom_text_field_directory_1.text())

        def __view_custom_text_field_directory_1_text_changed(*args, **kwargs):
            if view_custom_text_field_directory_1.text() == "":
                view_hint_0.show()
            else:
                view_hint_0.hide()
                view_text_0_set_text(view_custom_text_field_directory_1.text())

            try:
                current_text = view_custom_text_field_directory_1.text()
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_custom_text_field_directory_1_text_changed(current_text)
            except:
                print(
                    "No function view_custom_text_field_directory_1_text_changed defined. Current text : " + current_text)

        __view_custom_text_field_directory_1_text_changed()
        view_custom_text_field_directory_1.textChanged.connect(__view_custom_text_field_directory_1_text_changed)
        view_group_text_field_project_directory_0 = QLabel(central_widget)
        view_group_text_field_figma_token = QLabel(central_widget)
        view_inset_2 = QLabel(central_widget)

        view_inset_3 = QLabel(central_widget)
        view_inset_3.setGeometry(QRect(18, 133, 424, 30))
        q_svg_widget_view_inset_3 = QSvgWidget(view_inset_3)
        q_svg_widget_view_inset_3.setGeometry(QRect(0, 0, 424, 30))
        q_svg_widget_view_inset_3.load("svg/file21.svg")
        view_label_and_value_0 = QLabel(central_widget)
        view_label_and_value_0.setVisible(False)
        view_inset_4 = QLabel(central_widget)
        view_title_1 = QLabel(central_widget)
        view_title_2 = QLabel(central_widget)
        view_title_2.setText("Figma API token")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_title_2.setFont(font)
        view_title_2.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        view_title_2.setGeometry(QRect(32, 142, 185, 15))
        view_title_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_title_2.setMouseTracking(False)
        view_title_2.setContextMenuPolicy(Qt.NoContextMenu)

        def view_title_2_set_text(text: str):
            view_title_2.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_title_2_set_text = view_title_2_set_text
        except:
            print("No function view_title_2_set_text defined. Current text : " + view_title_2.text())
        view_custom_text_field_figma_token = QLabel(central_widget)
        view_background_0 = QLabel(central_widget)
        view_bounds_0 = QLabel(central_widget)
        view_hint_1 = QLabel(central_widget)
        view_hint_2 = QLabel(central_widget)
        view_hint_2.setText("Enter Figma REST API token")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_hint_2.setFont(font)
        view_hint_2.setStyleSheet("color: rgba(60.00000022351742, 60.00000022351742, 67.00000360608101, 255.0)")
        view_hint_2.setGeometry(QRect(130, 141, 301, 15))
        view_hint_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_hint_2.setMouseTracking(False)
        view_hint_2.setContextMenuPolicy(Qt.NoContextMenu)

        def view_hint_2_set_text(text: str):
            view_hint_2.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_hint_2_set_text = view_hint_2_set_text
        except:
            print("No function view_hint_2_set_text defined. Current text : " + view_hint_2.text())
        view_text_1 = QLabel(central_widget)
        view_text_2 = QLabel(central_widget)
        view_text_2.setText("...")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_text_2.setFont(font)
        view_text_2.setStyleSheet("color: rgba(105.8958412706852, 105.8958412706852, 105.8958412706852, 255.0)")
        view_text_2.setGeometry(QRect(125, 142, 301, 15))
        view_text_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_text_2.setMouseTracking(False)
        view_text_2.setContextMenuPolicy(Qt.NoContextMenu)

        def view_text_2_set_text(text: str):
            view_text_2.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_text_2_set_text = view_text_2_set_text
        except:
            print("No function view_text_2_set_text defined. Current text : " + view_text_2.text())
        view_custom_text_field_figma_token_0 = QLabel(central_widget)

        view_custom_text_field_figma_token_1 = QLineEdit(central_widget)
        view_custom_text_field_figma_token_1.setGeometry(QRect(125, 141, 311, 15))
        view_custom_text_field_figma_token_1.setAutoFillBackground(False)
        view_custom_text_field_figma_token_1.setObjectName("view_custom_text_field_figma_token_1")
        view_custom_text_field_figma_token_1.setMouseTracking(True)
        view_custom_text_field_figma_token_1.setContextMenuPolicy(Qt.NoContextMenu)
        view_custom_text_field_figma_token_1.setAcceptDrops(False)
        view_custom_text_field_figma_token_1.setFont(view_text_2.font())
        text_color = view_text_2.styleSheet().split("color: ")[1].split(";")[0]
        view_text_2.setStyleSheet("color: rgba(255, 255, 255, 0);")
        view_text_2.hide()
        view_custom_text_field_figma_token_1.setStyleSheet(
            "color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
        try:
            GuiController.ViewPyqtFigmaDesignerController.view_custom_text_field_figma_token_1_set_text = view_custom_text_field_figma_token_1.setText
        except:
            print(
                "No function view_custom_text_field_figma_token_1_set_text defined. Current text : " + view_custom_text_field_figma_token_1.text())

        def __view_custom_text_field_figma_token_1_text_changed(*args, **kwargs):
            if view_custom_text_field_figma_token_1.text() == "":
                view_hint_2.show()
            else:
                view_hint_2.hide()
                view_text_2_set_text(view_custom_text_field_figma_token_1.text())

            try:
                current_text = view_custom_text_field_figma_token_1.text()
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_custom_text_field_figma_token_1_text_changed(current_text)
            except:
                print(
                    "No function view_custom_text_field_figma_token_1_text_changed defined. Current text : " + current_text)

        __view_custom_text_field_figma_token_1_text_changed()
        view_custom_text_field_figma_token_1.textChanged.connect(__view_custom_text_field_figma_token_1_text_changed)
        view_group_text_field_figma_token_0 = QLabel(central_widget)
        view_group_text_field_figma_token_1 = QLabel(central_widget)
        view_inset_5 = QLabel(central_widget)

        view_inset_6 = QLabel(central_widget)
        view_inset_6.setGeometry(QRect(17, 182, 424, 30))
        q_svg_widget_view_inset_6 = QSvgWidget(view_inset_6)
        q_svg_widget_view_inset_6.setGeometry(QRect(0, 0, 424, 30))
        q_svg_widget_view_inset_6.load("svg/file22.svg")
        view_label_and_value_1 = QLabel(central_widget)
        view_label_and_value_1.setVisible(False)
        view_inset_7 = QLabel(central_widget)
        view_title_3 = QLabel(central_widget)
        view_title_4 = QLabel(central_widget)
        view_title_4.setText("Input file URL")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_title_4.setFont(font)
        view_title_4.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        view_title_4.setGeometry(QRect(32, 191, 185, 15))
        view_title_4.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_title_4.setMouseTracking(False)
        view_title_4.setContextMenuPolicy(Qt.NoContextMenu)

        def view_title_4_set_text(text: str):
            view_title_4.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_title_4_set_text = view_title_4_set_text
        except:
            print("No function view_title_4_set_text defined. Current text : " + view_title_4.text())
        view_custom_text_field_figma_token_2 = QLabel(central_widget)
        view_background_1 = QLabel(central_widget)
        view_bounds_1 = QLabel(central_widget)
        view_hint_3 = QLabel(central_widget)
        view_hint_4 = QLabel(central_widget)
        view_hint_4.setText("Enter the link to your Figma file")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_hint_4.setFont(font)
        view_hint_4.setStyleSheet("color: rgba(60.00000022351742, 60.00000022351742, 67.00000360608101, 255.0)")
        view_hint_4.setGeometry(QRect(129, 190, 301, 15))
        view_hint_4.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_hint_4.setMouseTracking(False)
        view_hint_4.setContextMenuPolicy(Qt.NoContextMenu)

        def view_hint_4_set_text(text: str):
            view_hint_4.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_hint_4_set_text = view_hint_4_set_text
        except:
            print("No function view_hint_4_set_text defined. Current text : " + view_hint_4.text())
        view_text_3 = QLabel(central_widget)
        view_text_4 = QLabel(central_widget)
        view_text_4.setText("...")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        view_text_4.setFont(font)
        view_text_4.setStyleSheet("color: rgba(105.8958412706852, 105.8958412706852, 105.8958412706852, 255.0)")
        view_text_4.setGeometry(QRect(125, 190, 301, 15))
        view_text_4.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        view_text_4.setMouseTracking(False)
        view_text_4.setContextMenuPolicy(Qt.NoContextMenu)

        def view_text_4_set_text(text: str):
            view_text_4.setText(text)

        try:
            GuiController.ViewPyqtFigmaDesignerController.view_text_4_set_text = view_text_4_set_text
        except:
            print("No function view_text_4_set_text defined. Current text : " + view_text_4.text())
        view_custom_text_field_figma_token_3 = QLabel(central_widget)

        view_custom_text_field_figma_token_4 = QLineEdit(central_widget)
        view_custom_text_field_figma_token_4.setGeometry(QRect(125, 190, 311, 15))
        view_custom_text_field_figma_token_4.setAutoFillBackground(False)
        view_custom_text_field_figma_token_4.setObjectName("view_custom_text_field_figma_token_4")
        view_custom_text_field_figma_token_4.setMouseTracking(True)
        view_custom_text_field_figma_token_4.setContextMenuPolicy(Qt.NoContextMenu)
        view_custom_text_field_figma_token_4.setAcceptDrops(False)
        view_custom_text_field_figma_token_4.setFont(view_text_4.font())
        text_color = view_text_4.styleSheet().split("color: ")[1].split(";")[0]
        view_text_4.setStyleSheet("color: rgba(255, 255, 255, 0);")
        view_text_4.hide()
        view_custom_text_field_figma_token_4.setStyleSheet(
            "color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
        try:
            GuiController.ViewPyqtFigmaDesignerController.view_custom_text_field_figma_token_4_set_text = view_custom_text_field_figma_token_4.setText
        except:
            print(
                "No function view_custom_text_field_figma_token_4_set_text defined. Current text : " + view_custom_text_field_figma_token_4.text())

        def __view_custom_text_field_figma_token_4_text_changed(*args, **kwargs):
            if view_custom_text_field_figma_token_4.text() == "":
                view_hint_4.show()
            else:
                view_hint_4.hide()
                view_text_4_set_text(view_custom_text_field_figma_token_4.text())

            try:
                current_text = view_custom_text_field_figma_token_4.text()
                GuiHandler.ViewPyqtFigmaDesignerHandler.view_custom_text_field_figma_token_4_text_changed(current_text)
            except:
                print(
                    "No function view_custom_text_field_figma_token_4_text_changed defined. Current text : " + current_text)

        __view_custom_text_field_figma_token_4_text_changed()
        view_custom_text_field_figma_token_4.textChanged.connect(__view_custom_text_field_figma_token_4_text_changed)
        view_group_text_field_figma_token_2 = QLabel(central_widget)
        view_pyqt_figma_designer_logoremovebgpreview_1 = QLabel(central_widget)

        view_pyqt_figma_designer_logoremovebgpreview_1_0 = QLabel(central_widget)
        view_pyqt_figma_designer_logoremovebgpreview_1_0.setGeometry(QRect(396, 0, 58, 58))
        q_svg_widget_view_pyqt_figma_designer_logoremovebgpreview_1_0 = QSvgWidget(
            view_pyqt_figma_designer_logoremovebgpreview_1_0)
        q_svg_widget_view_pyqt_figma_designer_logoremovebgpreview_1_0.setGeometry(QRect(0, 0, 58, 58))
        q_svg_widget_view_pyqt_figma_designer_logoremovebgpreview_1_0.load("svg/file23.svg")
        MainWindow.setCentralWidget(central_widget)
        GuiHandler.ViewPyqtFigmaDesignerHandler.window_started()


import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = QWindowViewPyqtFigmaDesigner()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec()