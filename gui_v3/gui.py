try:
    import gui_controller as GuiController    
except Exception as e:
    print("Exception while importing gui_controller.py")
    print(e)
try : 
    import gui_handler as GuiHandler
except Exception as e:
    print("Exception while importing gui_handler.py")
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



class QWindowPyqtFigmaDesignerGuiV3(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(466.9, 311.5)
        self.pyqt_figma_designer_gui_v3 = QWidget(MainWindow)
        MainWindow.setFixedSize(466.9, 311.5)
        MainWindow.setWindowTitle("PyQt Figma Designer  GUI V3")
        
        self.pyqt_figma_designer_gui_v3_0 = QLabel(self.pyqt_figma_designer_gui_v3)
        self.pyqt_figma_designer_gui_v3_0.setGeometry(QRect(0, 0, 466, 311))
        self.q_svg_widget_pyqt_figma_designer_gui_v3_0 = QSvgWidget(self.pyqt_figma_designer_gui_v3_0)
        self.q_svg_widget_pyqt_figma_designer_gui_v3_0.setGeometry(QRect(0, 0, 466, 311))
        self.q_svg_widget_pyqt_figma_designer_gui_v3_0.load("svg/file1.svg")
        self.rectangle_9 = QWidget(self.pyqt_figma_designer_gui_v3)
        self.rectangle_9.setGeometry(QRect(0, 0, 466, 311))
        self.rectangle_9.setObjectName("rectangle_9")
        
        self.rectangle_9_0 = QLabel(self.rectangle_9)
        self.rectangle_9_0.setGeometry(QRect(0, 0, 466, 311))
        self.q_svg_widget_rectangle_9_0 = QSvgWidget(self.rectangle_9_0)
        self.q_svg_widget_rectangle_9_0.setGeometry(QRect(0, 0, 466, 311))
        self.q_svg_widget_rectangle_9_0.load("svg/file2.svg")
        self.rectangle_8 = QWidget(self.pyqt_figma_designer_gui_v3)
        self.rectangle_8.setGeometry(QRect(0, 0, 466, 58))
        self.rectangle_8.setObjectName("rectangle_8")
        
        self.rectangle_8_0 = QLabel(self.rectangle_8)
        self.rectangle_8_0.setGeometry(QRect(0, 0, 466, 58))
        self.q_svg_widget_rectangle_8_0 = QSvgWidget(self.rectangle_8_0)
        self.q_svg_widget_rectangle_8_0.setGeometry(QRect(0, 0, 466, 58))
        self.q_svg_widget_rectangle_8_0.load("svg/file3.svg")
        self.window_title = QWidget(self.pyqt_figma_designer_gui_v3)
        self.window_title.setGeometry(QRect(17, 11, 178, 31))
        self.window_title.setObjectName("window_title")
        self.window_title_0 = QLabel(self.window_title)
        self.window_title_0.setText("PyQtFD GUI V3")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(18)
        self.window_title_0.setFont(font)
        self.window_title_0.setStyleSheet("color: rgba(37.00000159442425, 37.00000159442425, 37.00000159442425, 255.0)")
        self.window_title_0.setGeometry(QRect(0, 0, 178, 31))
        self.window_title_0.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.window_title_0.setMouseTracking(False)
        self.window_title_0.setContextMenuPolicy(Qt.NoContextMenu)
        def window_title_0_set_text(text:str):
            self.window_title_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.window_title_0_set_text = window_title_0_set_text
        except NameError:
            print("No function window_title_0_set_text defined. Current text : " + self.window_title_0.text())
        except Exception as e:
            print("Caught exception while trying to call window_title_0_set_text : " + str(e))
        self.tabs_view = QWidget(self.pyqt_figma_designer_gui_v3)
        self.tabs_view.setGeometry(QRect(19, 67, 428, 227))
        self.tabs_view.setObjectName("tabs_view")
        self.tabs_view_0 = QWidget(self.tabs_view)
        self.tabs_view_0.setGeometry(QRect(0, 0, 428, 227))
        self.tabs_view_0.setObjectName("tabs_view_0")
        self.background = QWidget(self.tabs_view_0)
        self.background.setGeometry(QRect(0, 0, 427, 80))
        self.background.setObjectName("background")
        self.background_0 = QWidget(self.background)
        self.background_0.setGeometry(QRect(0, 0, 427, 80))
        self.background_0.setObjectName("background_0")
        self.tabs_bar = QWidget(self.background_0)
        self.tabs_bar.setGeometry(QRect(117, 0, 221, 32))
        self.tabs_bar.setObjectName("tabs_bar")
        
        self.tabs_bar_0 = QLabel(self.tabs_bar)
        self.tabs_bar_0.setGeometry(QRect(0, 0, 221, 32))
        self.q_svg_widget_tabs_bar_0 = QSvgWidget(self.tabs_bar_0)
        self.q_svg_widget_tabs_bar_0.setGeometry(QRect(0, 0, 221, 32))
        self.q_svg_widget_tabs_bar_0.load("svg/file4.svg")
        self.tab_compile = QWidget(self.background_0)
        self.tab_compile.setGeometry(QRect(237, 2, 99, 27))
        self.tab_compile.setObjectName("tab_compile")
        self.tab_compile_0 = QWidget(self.tab_compile)
        self.tab_compile_0.setGeometry(QRect(0, 0, 99, 27))
        self.tab_compile_0.setObjectName("tab_compile_0")
        self.compile = QWidget(self.tab_compile_0)
        self.compile.setGeometry(QRect(-5, 0, 105, 28))
        self.compile.setObjectName("compile")
        self.compile_0 = QLabel(self.compile)
        self.compile_0.setText("Compile")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.compile_0.setFont(font)
        self.compile_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.compile_0.setGeometry(QRect(0, 0, 105, 28))
        self.compile_0.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.compile_0.setMouseTracking(False)
        self.compile_0.setContextMenuPolicy(Qt.NoContextMenu)
        def compile_0_set_text(text:str):
            self.compile_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.TabCompile0Controller.compile_0_set_text = compile_0_set_text
        except NameError:
            print("No function compile_0_set_text defined. Current text : " + self.compile_0.text())
        except Exception as e:
            print("Caught exception while trying to call compile_0_set_text : " + str(e))
        self.tab_download = QWidget(self.background_0)
        self.tab_download.setGeometry(QRect(126, 2, 99, 27))
        self.tab_download.setObjectName("tab_download")
        self.tab_download_0 = QWidget(self.tab_download)
        self.tab_download_0.setGeometry(QRect(0, 0, 99, 27))
        self.tab_download_0.setObjectName("tab_download_0")
        self.compile_1 = QWidget(self.tab_download_0)
        self.compile_1.setGeometry(QRect(-4, 0, 103, 28))
        self.compile_1.setObjectName("compile_1")
        self.compile_2 = QLabel(self.compile_1)
        self.compile_2.setText("Download")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.compile_2.setFont(font)
        self.compile_2.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.compile_2.setGeometry(QRect(0, 0, 103, 28))
        self.compile_2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.compile_2.setMouseTracking(False)
        self.compile_2.setContextMenuPolicy(Qt.NoContextMenu)
        def compile_2_set_text(text:str):
            self.compile_2.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.TabDownload0Controller.compile_2_set_text = compile_2_set_text
        except NameError:
            print("No function compile_2_set_text defined. Current text : " + self.compile_2.text())
        except Exception as e:
            print("Caught exception while trying to call compile_2_set_text : " + str(e))
        self.group_text_field_project_directory = QWidget(self.background_0)
        self.group_text_field_project_directory.setGeometry(QRect(0, 46, 427, 33))
        self.group_text_field_project_directory.setObjectName("group_text_field_project_directory")
        self.group_text_field_project_directory_0 = QWidget(self.group_text_field_project_directory)
        self.group_text_field_project_directory_0.setGeometry(QRect(0, 0, 427, 33))
        self.group_text_field_project_directory_0.setObjectName("group_text_field_project_directory_0")
        self.inset = QWidget(self.group_text_field_project_directory_0)
        self.inset.setGeometry(QRect(0, 0, 294, 30))
        self.inset.setObjectName("inset")
        
        self.inset_0 = QLabel(self.inset)
        self.inset_0.setGeometry(QRect(0, 0, 294, 30))
        self.q_svg_widget_inset_0 = QSvgWidget(self.inset_0)
        self.q_svg_widget_inset_0.setGeometry(QRect(0, 0, 294, 30))
        self.q_svg_widget_inset_0.load("svg/file5.svg")
        self.inset_1 = QWidget(self.inset)
        self.inset_1.setGeometry(QRect(0, 0, 294, 30))
        self.inset_1.setObjectName("inset_1")
        self.label_and_value = QWidget(self.inset_1)
        self.label_and_value.setGeometry(QRect(11, 0, 241, 30))
        self.label_and_value.setObjectName("label_and_value")
        self.title = QWidget(self.group_text_field_project_directory_0)
        self.title.setGeometry(QRect(14, 7, 128, 15))
        self.title.setObjectName("title")
        self.title_0 = QLabel(self.title)
        self.title_0.setText("Project directory")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.title_0.setFont(font)
        self.title_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.title_0.setGeometry(QRect(0, 0, 128, 15))
        self.title_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title_0.setMouseTracking(False)
        self.title_0.setContextMenuPolicy(Qt.NoContextMenu)
        def title_0_set_text(text:str):
            self.title_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.title_0_set_text = title_0_set_text
        except NameError:
            print("No function title_0_set_text defined. Current text : " + self.title_0.text())
        except Exception as e:
            print("Caught exception while trying to call title_0_set_text : " + str(e))
        self.custom_text_field_directory = QWidget(self.group_text_field_project_directory_0)
        self.custom_text_field_directory.setGeometry(QRect(107, 0, 189, 31))
        self.custom_text_field_directory.setObjectName("custom_text_field_directory")
        self.custom_text_field_directory_0 = QWidget(self.custom_text_field_directory)
        self.custom_text_field_directory_0.setGeometry(QRect(0, 0, 189, 31))
        self.custom_text_field_directory_0.setObjectName("custom_text_field_directory_0")
        self.background_1 = QWidget(self.custom_text_field_directory_0)
        self.background_1.setGeometry(QRect(0, 0, 189, 31))
        self.background_1.setObjectName("background_1")
        self.bounds = QWidget(self.custom_text_field_directory_0)
        self.bounds.setGeometry(QRect(0, 7, 179, 15))
        self.bounds.setObjectName("bounds")
        self.hint = QWidget(self.custom_text_field_directory_0)
        self.hint.setGeometry(QRect(4, 7, 179, 15))
        self.hint.setObjectName("hint")
        self.hint_0 = QLabel(self.hint)
        self.hint_0.setText("Enter path")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.hint_0.setFont(font)
        self.hint_0.setStyleSheet("color: rgba(60.00000022351742, 60.00000022351742, 67.00000360608101, 255.0)")
        self.hint_0.setGeometry(QRect(0, 0, 179, 15))
        self.hint_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.hint_0.setMouseTracking(False)
        self.hint_0.setContextMenuPolicy(Qt.NoContextMenu)
        def hint_0_set_text(text:str):
            self.hint_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.CustomTextFieldDirectory0Controller.hint_0_set_text = hint_0_set_text
        except NameError:
            print("No function hint_0_set_text defined. Current text : " + self.hint_0.text())
        except Exception as e:
            print("Caught exception while trying to call hint_0_set_text : " + str(e))
        self.text = QWidget(self.custom_text_field_directory_0)
        self.text.setGeometry(QRect(0, 7, 179, 15))
        self.text.setObjectName("text")
        self.text_0 = QLabel(self.text)
        self.text_0.setText("...")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.text_0.setFont(font)
        self.text_0.setStyleSheet("color: rgba(105.8958412706852, 105.8958412706852, 105.8958412706852, 255.0)")
        self.text_0.setGeometry(QRect(0, 0, 179, 15))
        self.text_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.text_0.setMouseTracking(False)
        self.text_0.setContextMenuPolicy(Qt.NoContextMenu)
        def text_0_set_text(text:str):
            self.text_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.CustomTextFieldDirectory0Controller.text_0_set_text = text_0_set_text
        except NameError:
            print("No function text_0_set_text defined. Current text : " + self.text_0.text())
        except Exception as e:
            print("Caught exception while trying to call text_0_set_text : " + str(e))
        
        self.custom_text_field_directory_1 = QLineEdit(self.custom_text_field_directory)
        self.custom_text_field_directory_1.setGeometry(QRect(0, 7, 179, 15))
        self.custom_text_field_directory_1.setAutoFillBackground(False)
        self.custom_text_field_directory_1.setObjectName("custom_text_field_directory_1")
        self.custom_text_field_directory_1.setMouseTracking(True)
        self.custom_text_field_directory_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.custom_text_field_directory_1.setAcceptDrops(False)
        self.custom_text_field_directory_1.setFont(self.text_0.font())
        text_color = self.text_0.styleSheet().split("color: ")[1].split(";")[0]
        self.text_0.setStyleSheet("color: rgba(255, 255, 255, 0);")
        self.text_0.hide()
        self.custom_text_field_directory_1.setStyleSheet("color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.custom_text_field_directory_1_set_text = self.custom_text_field_directory_1.setText
        except NameError:
            print("No function custom_text_field_directory_1_set_text defined. Current text : " + self.custom_text_field_directory_1.text())
        except Exception as e:
            print("Caught exception while trying to call custom_text_field_directory_1_set_text : " + str(e))
        
        def __custom_text_field_directory_1_text_changed(*args, **kwargs):    
            if self.custom_text_field_directory_1.text() == "" :
                self.hint_0.show()
            else :
                self.hint_0.hide()
                text_0_set_text(self.custom_text_field_directory_1.text())              
                   
            try : 
                current_text = self.custom_text_field_directory_1.text()
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.Background0Handler.GroupTextFieldProjectDirectory0Handler.custom_text_field_directory_1_text_changed(current_text)
            except NameError:
                print("No function custom_text_field_directory_1_text_changed defined. Current text : " + current_text)
            except Exception as e:
                print("Caught exception while trying to call custom_text_field_directory_1_text_changed : " + str(e))
        
        __custom_text_field_directory_1_text_changed()   
        self.custom_text_field_directory_1.textChanged.connect(__custom_text_field_directory_1_text_changed)
        self.custom_button_browse = QWidget(self.group_text_field_project_directory_0)
        self.custom_button_browse.setGeometry(QRect(305, 0, 121, 33))
        self.custom_button_browse.setObjectName("custom_button_browse")
        self.custom_button_browse_0 = QWidget(self.custom_button_browse)
        self.custom_button_browse_0.setGeometry(QRect(0, 0, 121, 33))
        self.custom_button_browse_0.setObjectName("custom_button_browse_0")
        self.normal = QWidget(self.custom_button_browse_0)
        self.normal.setGeometry(QRect(0, 0, 121, 33))
        self.normal.setObjectName("normal")
        
        self.normal_0 = QLabel(self.normal)
        self.normal_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_normal_0 = QSvgWidget(self.normal_0)
        self.q_svg_widget_normal_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_normal_0.load("svg/file6.svg")
        self.normal_1 = QWidget(self.normal)
        self.normal_1.setGeometry(QRect(0, 0, 121, 33))
        self.normal_1.setObjectName("normal_1")
        self.text_1 = QWidget(self.normal_1)
        self.text_1.setGeometry(QRect(42, 10, 37, 12))
        self.text_1.setObjectName("text_1")
        self.text_2 = QLabel(self.text_1)
        self.text_2.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_2.setFont(font)
        self.text_2.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_2.setGeometry(QRect(0, 0, 37, 12))
        self.text_2.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_2.setMouseTracking(False)
        self.text_2.setContextMenuPolicy(Qt.NoContextMenu)
        def text_2_set_text(text:str):
            self.text_2.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.CustomButtonBrowse0Controller.Normal1Controller.text_2_set_text = text_2_set_text
        except NameError:
            print("No function text_2_set_text defined. Current text : " + self.text_2.text())
        except Exception as e:
            print("Caught exception while trying to call text_2_set_text : " + str(e))
        self.disabled = QWidget(self.custom_button_browse_0)
        self.disabled.setGeometry(QRect(0, 0, 121, 33))
        self.disabled.setObjectName("disabled")
        
        self.disabled_0 = QLabel(self.disabled)
        self.disabled_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_disabled_0 = QSvgWidget(self.disabled_0)
        self.q_svg_widget_disabled_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_disabled_0.load("svg/file7.svg")
        self.disabled_1 = QWidget(self.disabled)
        self.disabled_1.setGeometry(QRect(0, 0, 121, 33))
        self.disabled_1.setObjectName("disabled_1")
        self.text_3 = QWidget(self.disabled_1)
        self.text_3.setGeometry(QRect(42, 10, 37, 12))
        self.text_3.setObjectName("text_3")
        self.text_4 = QLabel(self.text_3)
        self.text_4.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_4.setFont(font)
        self.text_4.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_4.setGeometry(QRect(0, 0, 37, 12))
        self.text_4.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_4.setMouseTracking(False)
        self.text_4.setContextMenuPolicy(Qt.NoContextMenu)
        def text_4_set_text(text:str):
            self.text_4.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.CustomButtonBrowse0Controller.Disabled1Controller.text_4_set_text = text_4_set_text
        except NameError:
            print("No function text_4_set_text defined. Current text : " + self.text_4.text())
        except Exception as e:
            print("Caught exception while trying to call text_4_set_text : " + str(e))
        self.pressed = QWidget(self.custom_button_browse_0)
        self.pressed.setGeometry(QRect(0, 0, 121, 33))
        self.pressed.setObjectName("pressed")
        
        self.pressed_0 = QLabel(self.pressed)
        self.pressed_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_pressed_0 = QSvgWidget(self.pressed_0)
        self.q_svg_widget_pressed_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_pressed_0.load("svg/file8.svg")
        self.pressed_1 = QWidget(self.pressed)
        self.pressed_1.setGeometry(QRect(0, 0, 121, 33))
        self.pressed_1.setObjectName("pressed_1")
        self.text_5 = QWidget(self.pressed_1)
        self.text_5.setGeometry(QRect(42, 10, 37, 12))
        self.text_5.setObjectName("text_5")
        self.text_6 = QLabel(self.text_5)
        self.text_6.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_6.setFont(font)
        self.text_6.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_6.setGeometry(QRect(0, 0, 37, 12))
        self.text_6.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_6.setMouseTracking(False)
        self.text_6.setContextMenuPolicy(Qt.NoContextMenu)
        def text_6_set_text(text:str):
            self.text_6.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.CustomButtonBrowse0Controller.Pressed1Controller.text_6_set_text = text_6_set_text
        except NameError:
            print("No function text_6_set_text defined. Current text : " + self.text_6.text())
        except Exception as e:
            print("Caught exception while trying to call text_6_set_text : " + str(e))
        self.mouse_over = QWidget(self.custom_button_browse_0)
        self.mouse_over.setGeometry(QRect(0, 0, 121, 33))
        self.mouse_over.setObjectName("mouse_over")
        
        self.mouse_over_0 = QLabel(self.mouse_over)
        self.mouse_over_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_mouse_over_0 = QSvgWidget(self.mouse_over_0)
        self.q_svg_widget_mouse_over_0.setGeometry(QRect(0, 0, 121, 33))
        self.q_svg_widget_mouse_over_0.load("svg/file9.svg")
        self.mouse_over_1 = QWidget(self.mouse_over)
        self.mouse_over_1.setGeometry(QRect(0, 0, 121, 33))
        self.mouse_over_1.setObjectName("mouse_over_1")
        self.text_7 = QWidget(self.mouse_over_1)
        self.text_7.setGeometry(QRect(42, 10, 37, 12))
        self.text_7.setObjectName("text_7")
        self.text_8 = QLabel(self.text_7)
        self.text_8.setText("Browse")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_8.setFont(font)
        self.text_8.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_8.setGeometry(QRect(0, 0, 37, 12))
        self.text_8.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_8.setMouseTracking(False)
        self.text_8.setContextMenuPolicy(Qt.NoContextMenu)
        def text_8_set_text(text:str):
            self.text_8.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.CustomButtonBrowse0Controller.MouseOver1Controller.text_8_set_text = text_8_set_text
        except NameError:
            print("No function text_8_set_text defined. Current text : " + self.text_8.text())
        except Exception as e:
            print("Caught exception while trying to call text_8_set_text : " + str(e))
        
        self.custom_button_browse_1 = QPushButton(self.custom_button_browse)
        self.custom_button_browse_1.setGeometry(QRect(0, 0, 121, 33))
        self.custom_button_browse_1.setFlat(True)
        self.custom_button_browse_1.setAutoFillBackground(False)
        self.custom_button_browse_1.setObjectName("custom_button_browse_1")
        self.custom_button_browse_1.setMouseTracking(True)
        self.custom_button_browse_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.custom_button_browse_1.setAcceptDrops(False)
        self.custom_button_browse_1.setFocusPolicy(Qt.NoFocus)
        self.custom_button_browse_1_enabled = True
        def __custom_button_browse_1_mouse_over(*args, **kwargs):
            if self.custom_button_browse_1_enabled :
                self.mouse_over.setVisible(True)
                self.pressed.setVisible(False)
                self.disabled.setVisible(False)
        def __custom_button_browse_1_mouse_leave(*args, **kwargs):
            if self.custom_button_browse_1_enabled :
                self.mouse_over.setVisible(False)
                self.pressed.setVisible(False)
                self.disabled.setVisible(False)
        def __custom_button_browse_1_mouse_press(*args, **kwargs):
            if self.custom_button_browse_1_enabled :
                self.mouse_over.setVisible(False)
                self.pressed.setVisible(True)
                self.disabled.setVisible(False)
        def __custom_button_browse_1_mouse_release(*args, **kwargs):
            if self.custom_button_browse_1_enabled :
                self.mouse_over.setVisible(True)
                self.pressed.setVisible(False)
                self.disabled.setVisible(False)
                self.custom_button_browse_1.clicked.emit()
        def __custom_button_browse_1_disable(*args, **kwargs):
            self.custom_button_browse_1_enabled = False
            self.mouse_over.setVisible(False)
            self.pressed.setVisible(False)
            self.disabled.setVisible(True)
            self.custom_button_browse_1.setMouseTracking(False)
            self.custom_button_browse_1.setFocusPolicy(Qt.NoFocus)
            self.custom_button_browse_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        def __custom_button_browse_1_enable(*args, **kwargs):
            self.custom_button_browse_1_enabled = True
            self.mouse_over.setVisible(False)
            self.pressed.setVisible(False)
            self.disabled.setVisible(False)
            self.custom_button_browse_1.setMouseTracking(True)
        
        def __custom_button_browse_1_clicked(*args, **kwargs):
            try :
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.Background0Handler.GroupTextFieldProjectDirectory0Handler.custom_button_browse_1_clicked()
            except NameError:
                print("No function custom_button_browse_1_clicked defined")
            except Exception as e:
                print("Caught exception while trying to call custom_button_browse_1_clicked : " + str(e))
        
        self.custom_button_browse_1.clicked.connect(__custom_button_browse_1_clicked)
        self.custom_button_browse_1.enterEvent = __custom_button_browse_1_mouse_over
        self.custom_button_browse_1.leaveEvent = __custom_button_browse_1_mouse_leave
        self.custom_button_browse_1.mousePressEvent = __custom_button_browse_1_mouse_press
        self.custom_button_browse_1.mouseReleaseEvent = __custom_button_browse_1_mouse_release
        self.custom_button_browse_1.disable = __custom_button_browse_1_disable
        self.custom_button_browse_1.enable = __custom_button_browse_1_enable
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.custom_button_browse_1_enable = self.custom_button_browse_1.enable
        except NameError:
            print("No function custom_button_browse_1_enable defined")
        except Exception as e:
            print("Error while linking custom_button_browse_1_enable to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.custom_button_browse_1_enable : " + str(e))
            
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.custom_button_browse_1_disable = self.custom_button_browse_1.disable
        except NameError :
            print("No function custom_button_browse_1_disable defined")
        except Exception as e:
            print("Error while linking custom_button_browse_1_disable to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.Background0Controller.GroupTextFieldProjectDirectory0Controller.custom_button_browse_1_disable : " + str(e))
        self.mouse_over.setVisible(False)
        self.pressed.setVisible(False)
        self.disabled.setVisible(False)
        self.tabs_content = QWidget(self.tabs_view_0)
        self.tabs_content.setGeometry(QRect(0, 88, 428, 139))
        self.tabs_content.setObjectName("tabs_content")
        self.tabs_content_0 = QWidget(self.tabs_content)
        self.tabs_content_0.setGeometry(QRect(0, 0, 428, 139))
        self.tabs_content_0.setObjectName("tabs_content_0")
        self.compile_options = QWidget(self.tabs_content_0)
        self.compile_options.setGeometry(QRect(0, 0, 427, 139))
        self.compile_options.setObjectName("compile_options")
        self.compile_options_0 = QWidget(self.compile_options)
        self.compile_options_0.setGeometry(QRect(0, 0, 427, 139))
        self.compile_options_0.setObjectName("compile_options_0")
        self.checkbox_overwrite_handlers = QWidget(self.compile_options_0)
        self.checkbox_overwrite_handlers.setGeometry(QRect(0, 9, 157, 19))
        self.checkbox_overwrite_handlers.setObjectName("checkbox_overwrite_handlers")
        self.checkbox_overwrite_handlers_0 = QWidget(self.checkbox_overwrite_handlers)
        self.checkbox_overwrite_handlers_0.setGeometry(QRect(0, 0, 157, 19))
        self.checkbox_overwrite_handlers_0.setObjectName("checkbox_overwrite_handlers_0")
        self.overwrite_handlers = QWidget(self.checkbox_overwrite_handlers_0)
        self.overwrite_handlers.setGeometry(QRect(28, 3, 129, 12))
        self.overwrite_handlers.setObjectName("overwrite_handlers")
        self.overwrite_handlers_0 = QLabel(self.overwrite_handlers)
        self.overwrite_handlers_0.setText("Overwrite handlers")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.overwrite_handlers_0.setFont(font)
        self.overwrite_handlers_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.overwrite_handlers_0.setGeometry(QRect(0, 0, 129, 12))
        self.overwrite_handlers_0.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.overwrite_handlers_0.setMouseTracking(False)
        self.overwrite_handlers_0.setContextMenuPolicy(Qt.NoContextMenu)
        def overwrite_handlers_0_set_text(text:str):
            self.overwrite_handlers_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.CheckboxOverwriteHandlers0Controller.overwrite_handlers_0_set_text = overwrite_handlers_0_set_text
        except NameError:
            print("No function overwrite_handlers_0_set_text defined. Current text : " + self.overwrite_handlers_0.text())
        except Exception as e:
            print("Caught exception while trying to call overwrite_handlers_0_set_text : " + str(e))
        self.rectangle_31 = QWidget(self.checkbox_overwrite_handlers_0)
        self.rectangle_31.setGeometry(QRect(0, 0, 19, 19))
        self.rectangle_31.setObjectName("rectangle_31")
        
        self.rectangle_31_0 = QLabel(self.rectangle_31)
        self.rectangle_31_0.setGeometry(QRect(0, 0, 19, 19))
        self.q_svg_widget_rectangle_31_0 = QSvgWidget(self.rectangle_31_0)
        self.q_svg_widget_rectangle_31_0.setGeometry(QRect(0, 0, 19, 19))
        self.q_svg_widget_rectangle_31_0.load("svg/file10.svg")
        self.checked = QWidget(self.checkbox_overwrite_handlers_0)
        self.checked.setGeometry(QRect(3, 3, 12, 12))
        self.checked.setObjectName("checked")
        
        self.checked_0 = QLabel(self.checked)
        self.checked_0.setGeometry(QRect(0, 0, 12, 12))
        self.q_svg_widget_checked_0 = QSvgWidget(self.checked_0)
        self.q_svg_widget_checked_0.setGeometry(QRect(0, 0, 12, 12))
        self.q_svg_widget_checked_0.load("svg/file11.svg")
        self.checked_1 = QWidget(self.checked)
        self.checked_1.setGeometry(QRect(0, 0, 12, 12))
        self.checked_1.setObjectName("checked_1")
        self.path_5_copy_10 = QWidget(self.checked_1)
        self.path_5_copy_10.setGeometry(QRect(2, 2, 8, 8))
        self.path_5_copy_10.setObjectName("path_5_copy_10")
        
        self.path_5_copy_10_0 = QLabel(self.path_5_copy_10)
        self.path_5_copy_10_0.setGeometry(QRect(0, 0, 8, 8))
        self.q_svg_widget_path_5_copy_10_0 = QSvgWidget(self.path_5_copy_10_0)
        self.q_svg_widget_path_5_copy_10_0.setGeometry(QRect(0, 0, 8, 8))
        self.q_svg_widget_path_5_copy_10_0.load("svg/file12.svg")
        
        self.checkbox_overwrite_handlers_1_checked = False
        self.checkbox_overwrite_handlers_1 = QPushButton(self.checkbox_overwrite_handlers)
        self.checkbox_overwrite_handlers_1.setGeometry(QRect(0, 0, 157, 19))
        self.checkbox_overwrite_handlers_1.setFlat(True)
        self.checkbox_overwrite_handlers_1.setAutoFillBackground(False)
        self.checkbox_overwrite_handlers_1.setObjectName("checkbox_overwrite_handlers_1")
        self.checkbox_overwrite_handlers_1.setMouseTracking(True)
        self.checkbox_overwrite_handlers_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.checkbox_overwrite_handlers_1.setAcceptDrops(False)
        self.checkbox_overwrite_handlers_1.setFocusPolicy(Qt.NoFocus)
        self.checkbox_overwrite_handlers_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                
        def __checkbox_overwrite_handlers_1_check_changed():
            self.checkbox_overwrite_handlers_1_checked = not self.checkbox_overwrite_handlers_1_checked
            try :
                self.checked.setVisible(self.checkbox_overwrite_handlers_1_checked)
        
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.TabsContent0Handler.CompileOptions0Handler.checkbox_overwrite_handlers_1_check_changed(self.checkbox_overwrite_handlers_1_checked)
            except NameError:
                print("No function checkbox_overwrite_handlers_1_check_changed defined. Checked = " + str(self.checkbox_overwrite_handlers_1_checked))
            except Exception as e:
                print("Caught exception while trying to call checkbox_overwrite_handlers_1_check_changed : " + str(e))
        def __checkbox_overwrite_handlers_1_set_checked(checked:bool):
            self.checkbox_overwrite_handlers_1_checked = checked
            self.checked.setVisible(self.checkbox_overwrite_handlers_1_checked)
        
            
        self.checkbox_overwrite_handlers_1.clicked.connect(__checkbox_overwrite_handlers_1_check_changed)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.checkbox_overwrite_handlers_1_set_checked = __checkbox_overwrite_handlers_1_set_checked
        except NameError:
            print("No function checkbox_overwrite_handlers_1_set_checked defined. Checked = " + str(self.checkbox_overwrite_handlers_1_checked))
        except Exception as e:
            print("Caught exception while trying to set the function checkbox_overwrite_handlers_1_set_checked : " + str(e))
        self.checked.setVisible(False)
        self.group_slider_scale = QWidget(self.compile_options_0)
        self.group_slider_scale.setGeometry(QRect(200, 0, 227, 29))
        self.group_slider_scale.setObjectName("group_slider_scale")
        self.group_slider_scale_0 = QWidget(self.group_slider_scale)
        self.group_slider_scale_0.setGeometry(QRect(0, 0, 227, 29))
        self.group_slider_scale_0.setObjectName("group_slider_scale_0")
        self.slider_scale = QWidget(self.group_slider_scale_0)
        self.slider_scale.setGeometry(QRect(72, 15, 154, 14))
        self.slider_scale.setObjectName("slider_scale")
        self.slider_scale_0 = QWidget(self.slider_scale)
        self.slider_scale_0.setGeometry(QRect(0, 0, 154, 14))
        self.slider_scale_0.setObjectName("slider_scale_0")
        self.ωelements2_highlight = QWidget(self.slider_scale_0)
        self.ωelements2_highlight.setGeometry(QRect(0, 4, 154, 4))
        self.ωelements2_highlight.setObjectName("ωelements2_highlight")
        
        self.ωelements2_highlight_0 = QLabel(self.ωelements2_highlight)
        self.ωelements2_highlight_0.setGeometry(QRect(0, 0, 154, 4))
        self.q_svg_widget_ωelements2_highlight_0 = QSvgWidget(self.ωelements2_highlight_0)
        self.q_svg_widget_ωelements2_highlight_0.setGeometry(QRect(0, 0, 154, 4))
        self.q_svg_widget_ωelements2_highlight_0.load("svg/file13.svg")
        self.ωelementsknob = QWidget(self.slider_scale_0)
        self.ωelementsknob.setGeometry(QRect(70, 0, 14, 14))
        self.ωelementsknob.setObjectName("ωelementsknob")
        self.ωelementsknob_0 = QWidget(self.ωelementsknob)
        self.ωelementsknob_0.setGeometry(QRect(0, 0, 14, 14))
        self.ωelementsknob_0.setObjectName("ωelementsknob_0")
        self.knob = QWidget(self.ωelementsknob_0)
        self.knob.setGeometry(QRect(0, 0, 14, 14))
        self.knob.setObjectName("knob")
        
        self.knob_0 = QLabel(self.knob)
        self.knob_0.setGeometry(QRect(0, 0, 14, 14))
        self.q_svg_widget_knob_0 = QSvgWidget(self.knob_0)
        self.q_svg_widget_knob_0.setGeometry(QRect(0, 0, 14, 14))
        self.q_svg_widget_knob_0.load("svg/file14.svg")
        self.states = QWidget(self.ωelementsknob_0)
        self.states.setGeometry(QRect(-7, -7, 28, 28))
        self.states.setObjectName("states")
        
        self.slider_scale_1_captured = False
        self.slider_scale_1_value = 0.5
        def __slider_scale_1_update_thumb_position(*args, **kwargs):
            if self.slider_scale_1_captured and len(args) > 0 :
                x, y, width, height = (0.0, 0.0, 154.7, 14.0)
                event = args[0]
                mouse_x, mouse_y = event.x(), event.y()
                self.slider_scale_1_value = mouse_x / width
                if self.slider_scale_1_value < 0 :
                    self.slider_scale_1_value = 0
                if self.slider_scale_1_value > 1 :
                    self.slider_scale_1_value = 1
                try :
                    GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.TabsContent0Handler.CompileOptions0Handler.GroupSliderScale0Handler.slider_scale_1_value_changed(self.slider_scale_1_value)
                except : 
                    print("No function slider_scale_1_value_changed defined. Value = " + str(self.slider_scale_1_value))
            self.ωelementsknob.setGeometry(QRect(0.0 + 140.7 * self.slider_scale_1_value, 0.0, 28.0, 28.0))
            self.ωelementsknob_0.setGeometry(QRect(0.0 + 140.7 * self.slider_scale_1_value, 0.0, 28.0, 28.0))
            self.knob.setGeometry(QRect(0.0 + 140.7 * self.slider_scale_1_value, 0.0, 28.0, 28.0))
            self.knob_0.setGeometry(QRect(0.0 + 140.7 * self.slider_scale_1_value, 0.0, 28.0, 28.0))
            self.states.setGeometry(QRect(0.0 + 140.7 * self.slider_scale_1_value, 0.0, 28.0, 28.0))
        
        def __slider_scale_1_mouse_press(*args, **kwargs):
            self.slider_scale_1_captured = True
            __slider_scale_1_update_thumb_position(*args, **kwargs)
        
        def __slider_scale_1_mouse_release(*args, **kwargs):
            self.slider_scale_1_captured = False
        
        def __slider_scale_1_mouse_move(*args, **kwargs):          
            __slider_scale_1_update_thumb_position(*args, **kwargs)
        
        def __slider_scale_1_set_value(value:float) :
            self.slider_scale_1_value = value
            __slider_scale_1_update_thumb_position()
        
        self.slider_scale_1 = QPushButton(self.slider_scale)
        self.slider_scale_1.setGeometry(QRect(0, 0, 154, 14))
        self.slider_scale_1.setFlat(True)
        self.slider_scale_1.setAutoFillBackground(False)
        self.slider_scale_1.setObjectName("slider_scale_1")
        self.slider_scale_1.setMouseTracking(True)
        self.slider_scale_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.slider_scale_1.setAcceptDrops(False)
        self.slider_scale_1.setFocusPolicy(Qt.NoFocus)
        self.slider_scale_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.slider_scale_1.mousePressEvent = __slider_scale_1_mouse_press
        self.slider_scale_1.mouseReleaseEvent = __slider_scale_1_mouse_release
        self.slider_scale_1.mouseMoveEvent = __slider_scale_1_mouse_move
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.GroupSliderScale0Controller.slider_scale_1_set_value = __slider_scale_1_set_value    
        except NameError:
            print("No function slider_scale_1_set_value defined. Value = " + str(self.slider_scale_1_value))
        except Exception as e:
            print("Error while linking slider_scale_1_set_value to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.GroupSliderScale0Controller.slider_scale_1_set_value : " + str(e))
        __slider_scale_1_update_thumb_position()
        self.ωelementsknob.setParent(self.slider_scale_1)
        self.ωelementsknob_0.setParent(self.slider_scale_1)
        self.knob.setParent(self.slider_scale_1)
        self.knob_0.setParent(self.slider_scale_1)
        self.states.setParent(self.slider_scale_1)
        self.scale = QWidget(self.group_slider_scale_0)
        self.scale.setGeometry(QRect(0, 15, 57, 12))
        self.scale.setObjectName("scale")
        self.scale_0 = QLabel(self.scale)
        self.scale_0.setText("Scale")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.scale_0.setFont(font)
        self.scale_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.scale_0.setGeometry(QRect(0, 0, 57, 12))
        self.scale_0.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.scale_0.setMouseTracking(False)
        self.scale_0.setContextMenuPolicy(Qt.NoContextMenu)
        def scale_0_set_text(text:str):
            self.scale_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.GroupSliderScale0Controller.scale_0_set_text = scale_0_set_text
        except NameError:
            print("No function scale_0_set_text defined. Current text : " + self.scale_0.text())
        except Exception as e:
            print("Caught exception while trying to call scale_0_set_text : " + str(e))
        self.x1 = QWidget(self.group_slider_scale_0)
        self.x1.setGeometry(QRect(128, 0, 44, 12))
        self.x1.setObjectName("x1")
        self.x1_0 = QLabel(self.x1)
        self.x1_0.setText("x1")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.x1_0.setFont(font)
        self.x1_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.x1_0.setGeometry(QRect(0, 0, 44, 12))
        self.x1_0.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.x1_0.setMouseTracking(False)
        self.x1_0.setContextMenuPolicy(Qt.NoContextMenu)
        def x1_0_set_text(text:str):
            self.x1_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.GroupSliderScale0Controller.x1_0_set_text = x1_0_set_text
        except NameError:
            print("No function x1_0_set_text defined. Current text : " + self.x1_0.text())
        except Exception as e:
            print("Caught exception while trying to call x1_0_set_text : " + str(e))
        self.custom_button_create_project = QWidget(self.compile_options_0)
        self.custom_button_create_project.setGeometry(QRect(151, 105, 163, 33))
        self.custom_button_create_project.setObjectName("custom_button_create_project")
        self.custom_button_create_project_0 = QWidget(self.custom_button_create_project)
        self.custom_button_create_project_0.setGeometry(QRect(0, 0, 163, 33))
        self.custom_button_create_project_0.setObjectName("custom_button_create_project_0")
        self.normal_2 = QWidget(self.custom_button_create_project_0)
        self.normal_2.setGeometry(QRect(0, 0, 163, 33))
        self.normal_2.setObjectName("normal_2")
        
        self.normal_3 = QLabel(self.normal_2)
        self.normal_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_normal_3 = QSvgWidget(self.normal_3)
        self.q_svg_widget_normal_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_normal_3.load("svg/file15.svg")
        self.normal_4 = QWidget(self.normal_2)
        self.normal_4.setGeometry(QRect(0, 0, 163, 33))
        self.normal_4.setObjectName("normal_4")
        self.text_9 = QWidget(self.normal_4)
        self.text_9.setGeometry(QRect(42, 10, 79, 12))
        self.text_9.setObjectName("text_9")
        self.text_10 = QLabel(self.text_9)
        self.text_10.setText("Compile project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_10.setFont(font)
        self.text_10.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_10.setGeometry(QRect(0, 0, 79, 12))
        self.text_10.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_10.setMouseTracking(False)
        self.text_10.setContextMenuPolicy(Qt.NoContextMenu)
        def text_10_set_text(text:str):
            self.text_10.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.CustomButtonCreateProject0Controller.Normal4Controller.text_10_set_text = text_10_set_text
        except NameError:
            print("No function text_10_set_text defined. Current text : " + self.text_10.text())
        except Exception as e:
            print("Caught exception while trying to call text_10_set_text : " + str(e))
        self.disabled_2 = QWidget(self.custom_button_create_project_0)
        self.disabled_2.setGeometry(QRect(0, 0, 163, 33))
        self.disabled_2.setObjectName("disabled_2")
        
        self.disabled_3 = QLabel(self.disabled_2)
        self.disabled_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_disabled_3 = QSvgWidget(self.disabled_3)
        self.q_svg_widget_disabled_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_disabled_3.load("svg/file16.svg")
        self.disabled_4 = QWidget(self.disabled_2)
        self.disabled_4.setGeometry(QRect(0, 0, 163, 33))
        self.disabled_4.setObjectName("disabled_4")
        self.text_11 = QWidget(self.disabled_4)
        self.text_11.setGeometry(QRect(42, 10, 79, 12))
        self.text_11.setObjectName("text_11")
        self.text_12 = QLabel(self.text_11)
        self.text_12.setText("Compile project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_12.setFont(font)
        self.text_12.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_12.setGeometry(QRect(0, 0, 79, 12))
        self.text_12.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_12.setMouseTracking(False)
        self.text_12.setContextMenuPolicy(Qt.NoContextMenu)
        def text_12_set_text(text:str):
            self.text_12.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.CustomButtonCreateProject0Controller.Disabled4Controller.text_12_set_text = text_12_set_text
        except NameError:
            print("No function text_12_set_text defined. Current text : " + self.text_12.text())
        except Exception as e:
            print("Caught exception while trying to call text_12_set_text : " + str(e))
        self.pressed_2 = QWidget(self.custom_button_create_project_0)
        self.pressed_2.setGeometry(QRect(0, 0, 163, 33))
        self.pressed_2.setObjectName("pressed_2")
        
        self.pressed_3 = QLabel(self.pressed_2)
        self.pressed_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_pressed_3 = QSvgWidget(self.pressed_3)
        self.q_svg_widget_pressed_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_pressed_3.load("svg/file17.svg")
        self.pressed_4 = QWidget(self.pressed_2)
        self.pressed_4.setGeometry(QRect(0, 0, 163, 33))
        self.pressed_4.setObjectName("pressed_4")
        self.text_13 = QWidget(self.pressed_4)
        self.text_13.setGeometry(QRect(42, 10, 79, 12))
        self.text_13.setObjectName("text_13")
        self.text_14 = QLabel(self.text_13)
        self.text_14.setText("Compile project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_14.setFont(font)
        self.text_14.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_14.setGeometry(QRect(0, 0, 79, 12))
        self.text_14.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_14.setMouseTracking(False)
        self.text_14.setContextMenuPolicy(Qt.NoContextMenu)
        def text_14_set_text(text:str):
            self.text_14.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.CustomButtonCreateProject0Controller.Pressed4Controller.text_14_set_text = text_14_set_text
        except NameError:
            print("No function text_14_set_text defined. Current text : " + self.text_14.text())
        except Exception as e:
            print("Caught exception while trying to call text_14_set_text : " + str(e))
        self.mouse_over_2 = QWidget(self.custom_button_create_project_0)
        self.mouse_over_2.setGeometry(QRect(0, 0, 163, 33))
        self.mouse_over_2.setObjectName("mouse_over_2")
        
        self.mouse_over_3 = QLabel(self.mouse_over_2)
        self.mouse_over_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_mouse_over_3 = QSvgWidget(self.mouse_over_3)
        self.q_svg_widget_mouse_over_3.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_mouse_over_3.load("svg/file18.svg")
        self.mouse_over_4 = QWidget(self.mouse_over_2)
        self.mouse_over_4.setGeometry(QRect(0, 0, 163, 33))
        self.mouse_over_4.setObjectName("mouse_over_4")
        self.text_15 = QWidget(self.mouse_over_4)
        self.text_15.setGeometry(QRect(42, 10, 79, 12))
        self.text_15.setObjectName("text_15")
        self.text_16 = QLabel(self.text_15)
        self.text_16.setText("Compile project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_16.setFont(font)
        self.text_16.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_16.setGeometry(QRect(0, 0, 79, 12))
        self.text_16.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_16.setMouseTracking(False)
        self.text_16.setContextMenuPolicy(Qt.NoContextMenu)
        def text_16_set_text(text:str):
            self.text_16.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.CustomButtonCreateProject0Controller.MouseOver4Controller.text_16_set_text = text_16_set_text
        except NameError:
            print("No function text_16_set_text defined. Current text : " + self.text_16.text())
        except Exception as e:
            print("Caught exception while trying to call text_16_set_text : " + str(e))
        
        self.custom_button_create_project_1 = QPushButton(self.custom_button_create_project)
        self.custom_button_create_project_1.setGeometry(QRect(0, 0, 163, 33))
        self.custom_button_create_project_1.setFlat(True)
        self.custom_button_create_project_1.setAutoFillBackground(False)
        self.custom_button_create_project_1.setObjectName("custom_button_create_project_1")
        self.custom_button_create_project_1.setMouseTracking(True)
        self.custom_button_create_project_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.custom_button_create_project_1.setAcceptDrops(False)
        self.custom_button_create_project_1.setFocusPolicy(Qt.NoFocus)
        self.custom_button_create_project_1_enabled = True
        def __custom_button_create_project_1_mouse_over(*args, **kwargs):
            if self.custom_button_create_project_1_enabled :
                self.mouse_over_2.setVisible(True)
                self.pressed_2.setVisible(False)
                self.disabled_2.setVisible(False)
        def __custom_button_create_project_1_mouse_leave(*args, **kwargs):
            if self.custom_button_create_project_1_enabled :
                self.mouse_over_2.setVisible(False)
                self.pressed_2.setVisible(False)
                self.disabled_2.setVisible(False)
        def __custom_button_create_project_1_mouse_press(*args, **kwargs):
            if self.custom_button_create_project_1_enabled :
                self.mouse_over_2.setVisible(False)
                self.pressed_2.setVisible(True)
                self.disabled_2.setVisible(False)
        def __custom_button_create_project_1_mouse_release(*args, **kwargs):
            if self.custom_button_create_project_1_enabled :
                self.mouse_over_2.setVisible(True)
                self.pressed_2.setVisible(False)
                self.disabled_2.setVisible(False)
                self.custom_button_create_project_1.clicked.emit()
        def __custom_button_create_project_1_disable(*args, **kwargs):
            self.custom_button_create_project_1_enabled = False
            self.mouse_over_2.setVisible(False)
            self.pressed_2.setVisible(False)
            self.disabled_2.setVisible(True)
            self.custom_button_create_project_1.setMouseTracking(False)
            self.custom_button_create_project_1.setFocusPolicy(Qt.NoFocus)
            self.custom_button_create_project_1.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        def __custom_button_create_project_1_enable(*args, **kwargs):
            self.custom_button_create_project_1_enabled = True
            self.mouse_over_2.setVisible(False)
            self.pressed_2.setVisible(False)
            self.disabled_2.setVisible(False)
            self.custom_button_create_project_1.setMouseTracking(True)
        
        def __custom_button_create_project_1_clicked(*args, **kwargs):
            try :
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.TabsContent0Handler.CompileOptions0Handler.custom_button_create_project_1_clicked()
            except NameError:
                print("No function custom_button_create_project_1_clicked defined")
            except Exception as e:
                print("Caught exception while trying to call custom_button_create_project_1_clicked : " + str(e))
        
        self.custom_button_create_project_1.clicked.connect(__custom_button_create_project_1_clicked)
        self.custom_button_create_project_1.enterEvent = __custom_button_create_project_1_mouse_over
        self.custom_button_create_project_1.leaveEvent = __custom_button_create_project_1_mouse_leave
        self.custom_button_create_project_1.mousePressEvent = __custom_button_create_project_1_mouse_press
        self.custom_button_create_project_1.mouseReleaseEvent = __custom_button_create_project_1_mouse_release
        self.custom_button_create_project_1.disable = __custom_button_create_project_1_disable
        self.custom_button_create_project_1.enable = __custom_button_create_project_1_enable
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.custom_button_create_project_1_enable = self.custom_button_create_project_1.enable
        except NameError:
            print("No function custom_button_create_project_1_enable defined")
        except Exception as e:
            print("Error while linking custom_button_create_project_1_enable to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.custom_button_create_project_1_enable : " + str(e))
            
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.custom_button_create_project_1_disable = self.custom_button_create_project_1.disable
        except NameError :
            print("No function custom_button_create_project_1_disable defined")
        except Exception as e:
            print("Error while linking custom_button_create_project_1_disable to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.CompileOptions0Controller.custom_button_create_project_1_disable : " + str(e))
        self.mouse_over_2.setVisible(False)
        self.pressed_2.setVisible(False)
        self.disabled_2.setVisible(False)
        self.download_options = QWidget(self.tabs_content_0)
        self.download_options.setGeometry(QRect(0, 7, 425, 131))
        self.download_options.setObjectName("download_options")
        self.download_options_0 = QWidget(self.download_options)
        self.download_options_0.setGeometry(QRect(0, 0, 425, 131))
        self.download_options_0.setObjectName("download_options_0")
        self.custom_button_create_project_2 = QWidget(self.download_options_0)
        self.custom_button_create_project_2.setGeometry(QRect(151, 98, 163, 33))
        self.custom_button_create_project_2.setObjectName("custom_button_create_project_2")
        self.custom_button_create_project_3 = QWidget(self.custom_button_create_project_2)
        self.custom_button_create_project_3.setGeometry(QRect(0, 0, 163, 33))
        self.custom_button_create_project_3.setObjectName("custom_button_create_project_3")
        self.normal_5 = QWidget(self.custom_button_create_project_3)
        self.normal_5.setGeometry(QRect(0, 0, 163, 33))
        self.normal_5.setObjectName("normal_5")
        
        self.normal_6 = QLabel(self.normal_5)
        self.normal_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_normal_6 = QSvgWidget(self.normal_6)
        self.q_svg_widget_normal_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_normal_6.load("svg/file19.svg")
        self.normal_7 = QWidget(self.normal_5)
        self.normal_7.setGeometry(QRect(0, 0, 163, 33))
        self.normal_7.setObjectName("normal_7")
        self.text_17 = QWidget(self.normal_7)
        self.text_17.setGeometry(QRect(46, 10, 70, 12))
        self.text_17.setObjectName("text_17")
        self.text_18 = QLabel(self.text_17)
        self.text_18.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_18.setFont(font)
        self.text_18.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_18.setGeometry(QRect(0, 0, 70, 12))
        self.text_18.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_18.setMouseTracking(False)
        self.text_18.setContextMenuPolicy(Qt.NoContextMenu)
        def text_18_set_text(text:str):
            self.text_18.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.CustomButtonCreateProject3Controller.Normal7Controller.text_18_set_text = text_18_set_text
        except NameError:
            print("No function text_18_set_text defined. Current text : " + self.text_18.text())
        except Exception as e:
            print("Caught exception while trying to call text_18_set_text : " + str(e))
        self.disabled_5 = QWidget(self.custom_button_create_project_3)
        self.disabled_5.setGeometry(QRect(0, 0, 163, 33))
        self.disabled_5.setObjectName("disabled_5")
        
        self.disabled_6 = QLabel(self.disabled_5)
        self.disabled_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_disabled_6 = QSvgWidget(self.disabled_6)
        self.q_svg_widget_disabled_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_disabled_6.load("svg/file20.svg")
        self.disabled_7 = QWidget(self.disabled_5)
        self.disabled_7.setGeometry(QRect(0, 0, 163, 33))
        self.disabled_7.setObjectName("disabled_7")
        self.text_19 = QWidget(self.disabled_7)
        self.text_19.setGeometry(QRect(46, 10, 70, 12))
        self.text_19.setObjectName("text_19")
        self.text_20 = QLabel(self.text_19)
        self.text_20.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_20.setFont(font)
        self.text_20.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_20.setGeometry(QRect(0, 0, 70, 12))
        self.text_20.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_20.setMouseTracking(False)
        self.text_20.setContextMenuPolicy(Qt.NoContextMenu)
        def text_20_set_text(text:str):
            self.text_20.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.CustomButtonCreateProject3Controller.Disabled7Controller.text_20_set_text = text_20_set_text
        except NameError:
            print("No function text_20_set_text defined. Current text : " + self.text_20.text())
        except Exception as e:
            print("Caught exception while trying to call text_20_set_text : " + str(e))
        self.pressed_5 = QWidget(self.custom_button_create_project_3)
        self.pressed_5.setGeometry(QRect(0, 0, 163, 33))
        self.pressed_5.setObjectName("pressed_5")
        
        self.pressed_6 = QLabel(self.pressed_5)
        self.pressed_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_pressed_6 = QSvgWidget(self.pressed_6)
        self.q_svg_widget_pressed_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_pressed_6.load("svg/file21.svg")
        self.pressed_7 = QWidget(self.pressed_5)
        self.pressed_7.setGeometry(QRect(0, 0, 163, 33))
        self.pressed_7.setObjectName("pressed_7")
        self.text_21 = QWidget(self.pressed_7)
        self.text_21.setGeometry(QRect(46, 10, 70, 12))
        self.text_21.setObjectName("text_21")
        self.text_22 = QLabel(self.text_21)
        self.text_22.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_22.setFont(font)
        self.text_22.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_22.setGeometry(QRect(0, 0, 70, 12))
        self.text_22.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_22.setMouseTracking(False)
        self.text_22.setContextMenuPolicy(Qt.NoContextMenu)
        def text_22_set_text(text:str):
            self.text_22.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.CustomButtonCreateProject3Controller.Pressed7Controller.text_22_set_text = text_22_set_text
        except NameError:
            print("No function text_22_set_text defined. Current text : " + self.text_22.text())
        except Exception as e:
            print("Caught exception while trying to call text_22_set_text : " + str(e))
        self.mouse_over_5 = QWidget(self.custom_button_create_project_3)
        self.mouse_over_5.setGeometry(QRect(0, 0, 163, 33))
        self.mouse_over_5.setObjectName("mouse_over_5")
        
        self.mouse_over_6 = QLabel(self.mouse_over_5)
        self.mouse_over_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_mouse_over_6 = QSvgWidget(self.mouse_over_6)
        self.q_svg_widget_mouse_over_6.setGeometry(QRect(0, 0, 163, 33))
        self.q_svg_widget_mouse_over_6.load("svg/file22.svg")
        self.mouse_over_7 = QWidget(self.mouse_over_5)
        self.mouse_over_7.setGeometry(QRect(0, 0, 163, 33))
        self.mouse_over_7.setObjectName("mouse_over_7")
        self.text_23 = QWidget(self.mouse_over_7)
        self.text_23.setGeometry(QRect(46, 10, 70, 12))
        self.text_23.setObjectName("text_23")
        self.text_24 = QLabel(self.text_23)
        self.text_24.setText("Create project")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.text_24.setFont(font)
        self.text_24.setStyleSheet("color: rgba(255.0, 255.0, 255.0, 255.0)")
        self.text_24.setGeometry(QRect(0, 0, 70, 12))
        self.text_24.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.text_24.setMouseTracking(False)
        self.text_24.setContextMenuPolicy(Qt.NoContextMenu)
        def text_24_set_text(text:str):
            self.text_24.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.CustomButtonCreateProject3Controller.MouseOver7Controller.text_24_set_text = text_24_set_text
        except NameError:
            print("No function text_24_set_text defined. Current text : " + self.text_24.text())
        except Exception as e:
            print("Caught exception while trying to call text_24_set_text : " + str(e))
        
        self.custom_button_create_project_4 = QPushButton(self.custom_button_create_project_2)
        self.custom_button_create_project_4.setGeometry(QRect(0, 0, 163, 33))
        self.custom_button_create_project_4.setFlat(True)
        self.custom_button_create_project_4.setAutoFillBackground(False)
        self.custom_button_create_project_4.setObjectName("custom_button_create_project_4")
        self.custom_button_create_project_4.setMouseTracking(True)
        self.custom_button_create_project_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.custom_button_create_project_4.setAcceptDrops(False)
        self.custom_button_create_project_4.setFocusPolicy(Qt.NoFocus)
        self.custom_button_create_project_4_enabled = True
        def __custom_button_create_project_4_mouse_over(*args, **kwargs):
            if self.custom_button_create_project_4_enabled :
                self.mouse_over_5.setVisible(True)
                self.pressed_5.setVisible(False)
                self.disabled_5.setVisible(False)
        def __custom_button_create_project_4_mouse_leave(*args, **kwargs):
            if self.custom_button_create_project_4_enabled :
                self.mouse_over_5.setVisible(False)
                self.pressed_5.setVisible(False)
                self.disabled_5.setVisible(False)
        def __custom_button_create_project_4_mouse_press(*args, **kwargs):
            if self.custom_button_create_project_4_enabled :
                self.mouse_over_5.setVisible(False)
                self.pressed_5.setVisible(True)
                self.disabled_5.setVisible(False)
        def __custom_button_create_project_4_mouse_release(*args, **kwargs):
            if self.custom_button_create_project_4_enabled :
                self.mouse_over_5.setVisible(True)
                self.pressed_5.setVisible(False)
                self.disabled_5.setVisible(False)
                self.custom_button_create_project_4.clicked.emit()
        def __custom_button_create_project_4_disable(*args, **kwargs):
            self.custom_button_create_project_4_enabled = False
            self.mouse_over_5.setVisible(False)
            self.pressed_5.setVisible(False)
            self.disabled_5.setVisible(True)
            self.custom_button_create_project_4.setMouseTracking(False)
            self.custom_button_create_project_4.setFocusPolicy(Qt.NoFocus)
            self.custom_button_create_project_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        def __custom_button_create_project_4_enable(*args, **kwargs):
            self.custom_button_create_project_4_enabled = True
            self.mouse_over_5.setVisible(False)
            self.pressed_5.setVisible(False)
            self.disabled_5.setVisible(False)
            self.custom_button_create_project_4.setMouseTracking(True)
        
        def __custom_button_create_project_4_clicked(*args, **kwargs):
            try :
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.TabsContent0Handler.DownloadOptions0Handler.custom_button_create_project_4_clicked()
            except NameError:
                print("No function custom_button_create_project_4_clicked defined")
            except Exception as e:
                print("Caught exception while trying to call custom_button_create_project_4_clicked : " + str(e))
        
        self.custom_button_create_project_4.clicked.connect(__custom_button_create_project_4_clicked)
        self.custom_button_create_project_4.enterEvent = __custom_button_create_project_4_mouse_over
        self.custom_button_create_project_4.leaveEvent = __custom_button_create_project_4_mouse_leave
        self.custom_button_create_project_4.mousePressEvent = __custom_button_create_project_4_mouse_press
        self.custom_button_create_project_4.mouseReleaseEvent = __custom_button_create_project_4_mouse_release
        self.custom_button_create_project_4.disable = __custom_button_create_project_4_disable
        self.custom_button_create_project_4.enable = __custom_button_create_project_4_enable
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.custom_button_create_project_4_enable = self.custom_button_create_project_4.enable
        except NameError:
            print("No function custom_button_create_project_4_enable defined")
        except Exception as e:
            print("Error while linking custom_button_create_project_4_enable to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.custom_button_create_project_4_enable : " + str(e))
            
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.custom_button_create_project_4_disable = self.custom_button_create_project_4.disable
        except NameError :
            print("No function custom_button_create_project_4_disable defined")
        except Exception as e:
            print("Error while linking custom_button_create_project_4_disable to PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.custom_button_create_project_4_disable : " + str(e))
        self.mouse_over_5.setVisible(False)
        self.pressed_5.setVisible(False)
        self.disabled_5.setVisible(False)
        self.group_text_field_figma_token = QWidget(self.download_options_0)
        self.group_text_field_figma_token.setGeometry(QRect(0, 0, 424, 31))
        self.group_text_field_figma_token.setObjectName("group_text_field_figma_token")
        self.group_text_field_figma_token_0 = QWidget(self.group_text_field_figma_token)
        self.group_text_field_figma_token_0.setGeometry(QRect(0, 0, 424, 31))
        self.group_text_field_figma_token_0.setObjectName("group_text_field_figma_token_0")
        self.inset_2 = QWidget(self.group_text_field_figma_token_0)
        self.inset_2.setGeometry(QRect(0, 0, 424, 30))
        self.inset_2.setObjectName("inset_2")
        
        self.inset_3 = QLabel(self.inset_2)
        self.inset_3.setGeometry(QRect(0, 0, 424, 30))
        self.q_svg_widget_inset_3 = QSvgWidget(self.inset_3)
        self.q_svg_widget_inset_3.setGeometry(QRect(0, 0, 424, 30))
        self.q_svg_widget_inset_3.load("svg/file23.svg")
        self.inset_4 = QWidget(self.inset_2)
        self.inset_4.setGeometry(QRect(0, 0, 424, 30))
        self.inset_4.setObjectName("inset_4")
        self.label_and_value_0 = QWidget(self.inset_4)
        self.label_and_value_0.setGeometry(QRect(11, 0, 241, 30))
        self.label_and_value_0.setObjectName("label_and_value_0")
        self.title_1 = QWidget(self.group_text_field_figma_token_0)
        self.title_1.setGeometry(QRect(14, 8, 185, 15))
        self.title_1.setObjectName("title_1")
        self.title_2 = QLabel(self.title_1)
        self.title_2.setText("Figma API token")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.title_2.setGeometry(QRect(0, 0, 185, 15))
        self.title_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title_2.setMouseTracking(False)
        self.title_2.setContextMenuPolicy(Qt.NoContextMenu)
        def title_2_set_text(text:str):
            self.title_2.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken0Controller.title_2_set_text = title_2_set_text
        except NameError:
            print("No function title_2_set_text defined. Current text : " + self.title_2.text())
        except Exception as e:
            print("Caught exception while trying to call title_2_set_text : " + str(e))
        self.custom_text_field_figma_token = QWidget(self.group_text_field_figma_token_0)
        self.custom_text_field_figma_token.setGeometry(QRect(107, 0, 317, 31))
        self.custom_text_field_figma_token.setObjectName("custom_text_field_figma_token")
        self.custom_text_field_figma_token_0 = QWidget(self.custom_text_field_figma_token)
        self.custom_text_field_figma_token_0.setGeometry(QRect(0, 0, 317, 31))
        self.custom_text_field_figma_token_0.setObjectName("custom_text_field_figma_token_0")
        self.background_2 = QWidget(self.custom_text_field_figma_token_0)
        self.background_2.setGeometry(QRect(0, 0, 317, 31))
        self.background_2.setObjectName("background_2")
        self.bounds_0 = QWidget(self.custom_text_field_figma_token_0)
        self.bounds_0.setGeometry(QRect(0, 7, 311, 15))
        self.bounds_0.setObjectName("bounds_0")
        self.hint_1 = QWidget(self.custom_text_field_figma_token_0)
        self.hint_1.setGeometry(QRect(4, 7, 301, 15))
        self.hint_1.setObjectName("hint_1")
        self.hint_2 = QLabel(self.hint_1)
        self.hint_2.setText("Enter Figma REST API token")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.hint_2.setFont(font)
        self.hint_2.setStyleSheet("color: rgba(60.00000022351742, 60.00000022351742, 67.00000360608101, 255.0)")
        self.hint_2.setGeometry(QRect(0, 0, 301, 15))
        self.hint_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.hint_2.setMouseTracking(False)
        self.hint_2.setContextMenuPolicy(Qt.NoContextMenu)
        def hint_2_set_text(text:str):
            self.hint_2.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken0Controller.CustomTextFieldFigmaToken0Controller.hint_2_set_text = hint_2_set_text
        except NameError:
            print("No function hint_2_set_text defined. Current text : " + self.hint_2.text())
        except Exception as e:
            print("Caught exception while trying to call hint_2_set_text : " + str(e))
        self.text_25 = QWidget(self.custom_text_field_figma_token_0)
        self.text_25.setGeometry(QRect(0, 8, 301, 15))
        self.text_25.setObjectName("text_25")
        self.text_26 = QLabel(self.text_25)
        self.text_26.setText("...")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.text_26.setFont(font)
        self.text_26.setStyleSheet("color: rgba(105.8958412706852, 105.8958412706852, 105.8958412706852, 255.0)")
        self.text_26.setGeometry(QRect(0, 0, 301, 15))
        self.text_26.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.text_26.setMouseTracking(False)
        self.text_26.setContextMenuPolicy(Qt.NoContextMenu)
        def text_26_set_text(text:str):
            self.text_26.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken0Controller.CustomTextFieldFigmaToken0Controller.text_26_set_text = text_26_set_text
        except NameError:
            print("No function text_26_set_text defined. Current text : " + self.text_26.text())
        except Exception as e:
            print("Caught exception while trying to call text_26_set_text : " + str(e))
        
        self.custom_text_field_figma_token_1 = QLineEdit(self.custom_text_field_figma_token)
        self.custom_text_field_figma_token_1.setGeometry(QRect(0, 7, 311, 15))
        self.custom_text_field_figma_token_1.setAutoFillBackground(False)
        self.custom_text_field_figma_token_1.setObjectName("custom_text_field_figma_token_1")
        self.custom_text_field_figma_token_1.setMouseTracking(True)
        self.custom_text_field_figma_token_1.setContextMenuPolicy(Qt.NoContextMenu)
        self.custom_text_field_figma_token_1.setAcceptDrops(False)
        self.custom_text_field_figma_token_1.setFont(self.text_26.font())
        text_color = self.text_26.styleSheet().split("color: ")[1].split(";")[0]
        self.text_26.setStyleSheet("color: rgba(255, 255, 255, 0);")
        self.text_26.hide()
        self.custom_text_field_figma_token_1.setStyleSheet("color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken0Controller.custom_text_field_figma_token_1_set_text = self.custom_text_field_figma_token_1.setText
        except NameError:
            print("No function custom_text_field_figma_token_1_set_text defined. Current text : " + self.custom_text_field_figma_token_1.text())
        except Exception as e:
            print("Caught exception while trying to call custom_text_field_figma_token_1_set_text : " + str(e))
        
        def __custom_text_field_figma_token_1_text_changed(*args, **kwargs):    
            if self.custom_text_field_figma_token_1.text() == "" :
                self.hint_2.show()
            else :
                self.hint_2.hide()
                text_26_set_text(self.custom_text_field_figma_token_1.text())              
                   
            try : 
                current_text = self.custom_text_field_figma_token_1.text()
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.TabsContent0Handler.DownloadOptions0Handler.GroupTextFieldFigmaToken0Handler.custom_text_field_figma_token_1_text_changed(current_text)
            except NameError:
                print("No function custom_text_field_figma_token_1_text_changed defined. Current text : " + current_text)
            except Exception as e:
                print("Caught exception while trying to call custom_text_field_figma_token_1_text_changed : " + str(e))
        
        __custom_text_field_figma_token_1_text_changed()   
        self.custom_text_field_figma_token_1.textChanged.connect(__custom_text_field_figma_token_1_text_changed)
        self.group_text_field_figma_token_1 = QWidget(self.download_options_0)
        self.group_text_field_figma_token_1.setGeometry(QRect(0, 49, 424, 31))
        self.group_text_field_figma_token_1.setObjectName("group_text_field_figma_token_1")
        self.group_text_field_figma_token_2 = QWidget(self.group_text_field_figma_token_1)
        self.group_text_field_figma_token_2.setGeometry(QRect(0, 0, 424, 31))
        self.group_text_field_figma_token_2.setObjectName("group_text_field_figma_token_2")
        self.inset_5 = QWidget(self.group_text_field_figma_token_2)
        self.inset_5.setGeometry(QRect(0, 0, 424, 30))
        self.inset_5.setObjectName("inset_5")
        
        self.inset_6 = QLabel(self.inset_5)
        self.inset_6.setGeometry(QRect(0, 0, 424, 30))
        self.q_svg_widget_inset_6 = QSvgWidget(self.inset_6)
        self.q_svg_widget_inset_6.setGeometry(QRect(0, 0, 424, 30))
        self.q_svg_widget_inset_6.load("svg/file24.svg")
        self.inset_7 = QWidget(self.inset_5)
        self.inset_7.setGeometry(QRect(0, 0, 424, 30))
        self.inset_7.setObjectName("inset_7")
        self.label_and_value_1 = QWidget(self.inset_7)
        self.label_and_value_1.setGeometry(QRect(11, 0, 241, 30))
        self.label_and_value_1.setObjectName("label_and_value_1")
        self.title_3 = QWidget(self.group_text_field_figma_token_2)
        self.title_3.setGeometry(QRect(14, 8, 185, 15))
        self.title_3.setObjectName("title_3")
        self.title_4 = QLabel(self.title_3)
        self.title_4.setText("Input file URL")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.title_4.setFont(font)
        self.title_4.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.title_4.setGeometry(QRect(0, 0, 185, 15))
        self.title_4.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title_4.setMouseTracking(False)
        self.title_4.setContextMenuPolicy(Qt.NoContextMenu)
        def title_4_set_text(text:str):
            self.title_4.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken2Controller.title_4_set_text = title_4_set_text
        except NameError:
            print("No function title_4_set_text defined. Current text : " + self.title_4.text())
        except Exception as e:
            print("Caught exception while trying to call title_4_set_text : " + str(e))
        self.custom_text_field_figma_token_2 = QWidget(self.group_text_field_figma_token_2)
        self.custom_text_field_figma_token_2.setGeometry(QRect(107, 0, 317, 31))
        self.custom_text_field_figma_token_2.setObjectName("custom_text_field_figma_token_2")
        self.custom_text_field_figma_token_3 = QWidget(self.custom_text_field_figma_token_2)
        self.custom_text_field_figma_token_3.setGeometry(QRect(0, 0, 317, 31))
        self.custom_text_field_figma_token_3.setObjectName("custom_text_field_figma_token_3")
        self.background_3 = QWidget(self.custom_text_field_figma_token_3)
        self.background_3.setGeometry(QRect(0, 0, 317, 31))
        self.background_3.setObjectName("background_3")
        self.bounds_1 = QWidget(self.custom_text_field_figma_token_3)
        self.bounds_1.setGeometry(QRect(0, 7, 311, 15))
        self.bounds_1.setObjectName("bounds_1")
        self.hint_3 = QWidget(self.custom_text_field_figma_token_3)
        self.hint_3.setGeometry(QRect(4, 7, 301, 15))
        self.hint_3.setObjectName("hint_3")
        self.hint_4 = QLabel(self.hint_3)
        self.hint_4.setText("Enter the link to your Figma file")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.hint_4.setFont(font)
        self.hint_4.setStyleSheet("color: rgba(60.00000022351742, 60.00000022351742, 67.00000360608101, 255.0)")
        self.hint_4.setGeometry(QRect(0, 0, 301, 15))
        self.hint_4.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.hint_4.setMouseTracking(False)
        self.hint_4.setContextMenuPolicy(Qt.NoContextMenu)
        def hint_4_set_text(text:str):
            self.hint_4.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken2Controller.CustomTextFieldFigmaToken3Controller.hint_4_set_text = hint_4_set_text
        except NameError:
            print("No function hint_4_set_text defined. Current text : " + self.hint_4.text())
        except Exception as e:
            print("Caught exception while trying to call hint_4_set_text : " + str(e))
        self.text_27 = QWidget(self.custom_text_field_figma_token_3)
        self.text_27.setGeometry(QRect(1, 7, 301, 15))
        self.text_27.setObjectName("text_27")
        self.text_28 = QLabel(self.text_27)
        self.text_28.setText("...")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(8)
        self.text_28.setFont(font)
        self.text_28.setStyleSheet("color: rgba(105.8958412706852, 105.8958412706852, 105.8958412706852, 255.0)")
        self.text_28.setGeometry(QRect(0, 0, 301, 15))
        self.text_28.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.text_28.setMouseTracking(False)
        self.text_28.setContextMenuPolicy(Qt.NoContextMenu)
        def text_28_set_text(text:str):
            self.text_28.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken2Controller.CustomTextFieldFigmaToken3Controller.text_28_set_text = text_28_set_text
        except NameError:
            print("No function text_28_set_text defined. Current text : " + self.text_28.text())
        except Exception as e:
            print("Caught exception while trying to call text_28_set_text : " + str(e))
        
        self.custom_text_field_figma_token_4 = QLineEdit(self.custom_text_field_figma_token_2)
        self.custom_text_field_figma_token_4.setGeometry(QRect(0, 7, 311, 15))
        self.custom_text_field_figma_token_4.setAutoFillBackground(False)
        self.custom_text_field_figma_token_4.setObjectName("custom_text_field_figma_token_4")
        self.custom_text_field_figma_token_4.setMouseTracking(True)
        self.custom_text_field_figma_token_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.custom_text_field_figma_token_4.setAcceptDrops(False)
        self.custom_text_field_figma_token_4.setFont(self.text_28.font())
        text_color = self.text_28.styleSheet().split("color: ")[1].split(";")[0]
        self.text_28.setStyleSheet("color: rgba(255, 255, 255, 0);")
        self.text_28.hide()
        self.custom_text_field_figma_token_4.setStyleSheet("color: " + text_color + "; background-color: rgba(255, 255, 255, 0); border: 0px solid rgba(255, 255, 255, 0);")
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsContent0Controller.DownloadOptions0Controller.GroupTextFieldFigmaToken2Controller.custom_text_field_figma_token_4_set_text = self.custom_text_field_figma_token_4.setText
        except NameError:
            print("No function custom_text_field_figma_token_4_set_text defined. Current text : " + self.custom_text_field_figma_token_4.text())
        except Exception as e:
            print("Caught exception while trying to call custom_text_field_figma_token_4_set_text : " + str(e))
        
        def __custom_text_field_figma_token_4_text_changed(*args, **kwargs):    
            if self.custom_text_field_figma_token_4.text() == "" :
                self.hint_4.show()
            else :
                self.hint_4.hide()
                text_28_set_text(self.custom_text_field_figma_token_4.text())              
                   
            try : 
                current_text = self.custom_text_field_figma_token_4.text()
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.TabsView0Handler.TabsContent0Handler.DownloadOptions0Handler.GroupTextFieldFigmaToken2Handler.custom_text_field_figma_token_4_text_changed(current_text)
            except NameError:
                print("No function custom_text_field_figma_token_4_text_changed defined. Current text : " + current_text)
            except Exception as e:
                print("Caught exception while trying to call custom_text_field_figma_token_4_text_changed : " + str(e))
        
        __custom_text_field_figma_token_4_text_changed()   
        self.custom_text_field_figma_token_4.textChanged.connect(__custom_text_field_figma_token_4_text_changed)
        self.tabs_bar_1 = QWidget(self.tabs_view_0)
        self.tabs_bar_1.setGeometry(QRect(120, 2, 216, 27))
        self.tabs_bar_1.setObjectName("tabs_bar_1")
        self.tabs_bar_2 = QWidget(self.tabs_bar_1)
        self.tabs_bar_2.setGeometry(QRect(0, 0, 216, 27))
        self.tabs_bar_2.setObjectName("tabs_bar_2")
        self.selected = QWidget(self.tabs_bar_2)
        self.selected.setGeometry(QRect(110, 0, 105, 27))
        self.selected.setObjectName("selected")
        
        self.selected_0 = QLabel(self.selected)
        self.selected_0.setGeometry(QRect(0, 0, 105, 27))
        self.q_svg_widget_selected_0 = QSvgWidget(self.selected_0)
        self.q_svg_widget_selected_0.setGeometry(QRect(0, 0, 105, 27))
        self.q_svg_widget_selected_0.load("svg/file25.svg")
        self.selected_1 = QWidget(self.selected)
        self.selected_1.setGeometry(QRect(0, 0, 105, 27))
        self.selected_1.setObjectName("selected_1")
        self.download = QWidget(self.selected_1)
        self.download.setGeometry(QRect(0, 0, 105, 28))
        self.download.setObjectName("download")
        self.download_0 = QLabel(self.download)
        self.download_0.setText("Compile")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.download_0.setFont(font)
        self.download_0.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.download_0.setGeometry(QRect(0, 0, 105, 28))
        self.download_0.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.download_0.setMouseTracking(False)
        self.download_0.setContextMenuPolicy(Qt.NoContextMenu)
        def download_0_set_text(text:str):
            self.download_0.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsBar2Controller.Selected1Controller.download_0_set_text = download_0_set_text
        except NameError:
            print("No function download_0_set_text defined. Current text : " + self.download_0.text())
        except Exception as e:
            print("Caught exception while trying to call download_0_set_text : " + str(e))
        self.selected_2 = QWidget(self.tabs_bar_2)
        self.selected_2.setGeometry(QRect(0, 0, 105, 27))
        self.selected_2.setObjectName("selected_2")
        
        self.selected_3 = QLabel(self.selected_2)
        self.selected_3.setGeometry(QRect(0, 0, 105, 27))
        self.q_svg_widget_selected_3 = QSvgWidget(self.selected_3)
        self.q_svg_widget_selected_3.setGeometry(QRect(0, 0, 105, 27))
        self.q_svg_widget_selected_3.load("svg/file26.svg")
        self.selected_4 = QWidget(self.selected_2)
        self.selected_4.setGeometry(QRect(0, 0, 105, 27))
        self.selected_4.setObjectName("selected_4")
        self.download_1 = QWidget(self.selected_4)
        self.download_1.setGeometry(QRect(0, 0, 105, 28))
        self.download_1.setObjectName("download_1")
        self.download_2 = QLabel(self.download_1)
        self.download_2.setText("Download")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.download_2.setFont(font)
        self.download_2.setStyleSheet("color: rgba(0.0, 0.0, 0.0, 255.0)")
        self.download_2.setGeometry(QRect(0, 0, 105, 28))
        self.download_2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.download_2.setMouseTracking(False)
        self.download_2.setContextMenuPolicy(Qt.NoContextMenu)
        def download_2_set_text(text:str):
            self.download_2.setText(text)
        
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.TabsView0Controller.TabsBar2Controller.Selected4Controller.download_2_set_text = download_2_set_text
        except NameError:
            print("No function download_2_set_text defined. Current text : " + self.download_2.text())
        except Exception as e:
            print("Caught exception while trying to call download_2_set_text : " + str(e))
        def __select_tab(i):
            self.download_options.setVisible(i == 0)
            self.selected_2.setVisible(i == 0)
            self.compile_options.setVisible(i == 1)
            self.selected.setVisible(i == 1)
        
            try :
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.tabs_view_1_tab_changed(i)
            except NameError:
                print("No function tabs_view_1_tab_changed defined. Tab = " + str(i))
            except Exception as e:
                print("Caught exception while trying to call tabs_view_1_tab_changed : " + str(e))
        __select_tab_0 = lambda: __select_tab(0)
        __select_tab_1 = lambda: __select_tab(1)
        
        self.tabs_view_1 = QLabel(self.tabs_view)
        
        selected_2_button = QPushButton(self.tabs_bar_2)
        selected_2_button.setGeometry(QRect(0, 0, 105, 27))
        selected_2_button.setFlat(True)
        selected_2_button.setObjectName("selected_2_button")
        selected_2_button.setMouseTracking(True)
        selected_2_button.setContextMenuPolicy(Qt.NoContextMenu)
        selected_2_button.setAcceptDrops(False)
        selected_2_button.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        selected_2_button.clicked.connect(__select_tab_0)
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.tabs_view_1_set_tab = __select_tab
        except NameError:
            print("No function tabs_view_1_set_tab defined. Current tab : 0")
        except Exception as e:
            print("Caught exception while trying to set the function tabs_view_1_set_tab : " + str(e))
        self.download_options.setVisible(True)
        self.selected_2.setVisible(True)
        
        selected_button = QPushButton(self.tabs_bar_2)
        selected_button.setGeometry(QRect(110, 0, 105, 27))
        selected_button.setFlat(True)
        selected_button.setObjectName("selected_button")
        selected_button.setMouseTracking(True)
        selected_button.setContextMenuPolicy(Qt.NoContextMenu)
        selected_button.setAcceptDrops(False)
        selected_button.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        selected_button.clicked.connect(__select_tab_1)
        try :
            GuiController.PyqtFigmaDesignerGuiV3Controller.tabs_view_1_set_tab = __select_tab
        except NameError:
            print("No function tabs_view_1_set_tab defined. Current tab : 1")
        except Exception as e:
            print("Caught exception while trying to set the function tabs_view_1_set_tab : " + str(e))
        self.compile_options.setVisible(False)
        self.selected.setVisible(False)
        self.pyqt_figma_designer_logoremovebgpreview_1 = QWidget(self.pyqt_figma_designer_gui_v3)
        self.pyqt_figma_designer_logoremovebgpreview_1.setGeometry(QRect(396, 0, 58, 58))
        self.pyqt_figma_designer_logoremovebgpreview_1.setObjectName("pyqt_figma_designer_logoremovebgpreview_1")
        
        self.pyqt_figma_designer_logoremovebgpreview_1_0 = QLabel(self.pyqt_figma_designer_logoremovebgpreview_1)
        self.pyqt_figma_designer_logoremovebgpreview_1_0.setGeometry(QRect(0, 0, 58, 58))
        self.q_svg_widget_pyqt_figma_designer_logoremovebgpreview_1_0 = QSvgWidget(self.pyqt_figma_designer_logoremovebgpreview_1_0)
        self.q_svg_widget_pyqt_figma_designer_logoremovebgpreview_1_0.setGeometry(QRect(0, 0, 58, 58))
        self.q_svg_widget_pyqt_figma_designer_logoremovebgpreview_1_0.load("svg/file27.svg")
        MainWindow.setCentralWidget(self.pyqt_figma_designer_gui_v3)

        try : 
            GuiHandler.PyqtFigmaDesignerGuiV3Handler.window_started()            
        except NameError:
            print("No function PyqtFigmaDesignerGuiV3Handler.window_started defined.")
        except Exception as e:
            print("Caught exception while trying to call PyqtFigmaDesignerGuiV3Handler.window_started : " + str(e))
        def __window_closed(*args, **kwargs):
            try :
                GuiHandler.PyqtFigmaDesignerGuiV3Handler.window_closed()
            except NameError:
                print("No function PyqtFigmaDesignerGuiV3Handler.window_closed defined.")
            except Exception as e:
                print("Caught exception while trying to call PyqtFigmaDesignerGuiV3Handler.window_closed : " + str(e))
        MainWindow.closeEvent = __window_closed
        
import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = QWindowPyqtFigmaDesignerGuiV3()
ui.setupUi(MainWindow)
MainWindow.show()
app.exec()