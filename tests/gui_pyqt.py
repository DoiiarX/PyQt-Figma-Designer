# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowsNxRLm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(401, 414)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionBrowseApk = QAction(MainWindow)
        self.actionBrowseApk.setObjectName(u"actionBrowseApk")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonBrowseProject = QPushButton(self.centralwidget)
        self.buttonBrowseProject.setObjectName(u"buttonBrowseProject")
        self.buttonBrowseProject.setGeometry(QRect(310, 40, 75, 24))
        self.editTextProjectPath = QLineEdit(self.centralwidget)
        self.editTextProjectPath.setObjectName(u"editTextProjectPath")
        self.editTextProjectPath.setEnabled(False)
        self.editTextProjectPath.setGeometry(QRect(10, 40, 291, 21))
        self.buttonCreateProject = QPushButton(self.centralwidget)
        self.buttonCreateProject.setObjectName(u"buttonCreateProject")
        self.buttonCreateProject.setGeometry(QRect(130, 70, 161, 24))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 100, 381, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.buttonRebuild = QPushButton(self.centralwidget)
        self.buttonRebuild.setObjectName(u"buttonRebuild")
        self.buttonRebuild.setGeometry(QRect(180, 370, 75, 24))
        font = QFont()
        font.setFamilies([u"Cascadia Mono Light"])
        font.setPointSize(6)
        self.buttonRebuild.setFont(font)
        self.buttonRefreshOverrides = QPushButton(self.centralwidget)
        self.buttonRefreshOverrides.setObjectName(u"buttonRefreshOverrides")
        self.buttonRefreshOverrides.setGeometry(QRect(320, 120, 75, 24))
        self.tableViewOverrides = QTableView(self.centralwidget)
        self.tableViewOverrides.setObjectName(u"tableViewOverrides")
        self.tableViewOverrides.setGeometry(QRect(10, 150, 381, 211))
        self.tableViewOverrides.setSortingEnabled(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 49, 16))
        self.editTextApkPath = QLineEdit(self.centralwidget)
        self.editTextApkPath.setObjectName(u"editTextApkPath")
        self.editTextApkPath.setEnabled(False)
        self.editTextApkPath.setGeometry(QRect(10, 10, 291, 21))
        self.buttonBrowseApk = QPushButton(self.centralwidget)
        self.buttonBrowseApk.setObjectName(u"buttonBrowseApk")
        self.buttonBrowseApk.setGeometry(QRect(310, 10, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OverrideIL2CPP", None))
        self.actionBrowseApk.setText(QCoreApplication.translate("MainWindow", u"BrowseApk", None))
        self.buttonBrowseProject.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.editTextProjectPath.setText(QCoreApplication.translate("MainWindow", u"Project directory", None))
        self.buttonCreateProject.setText(QCoreApplication.translate("MainWindow", u"Dump and create project", None))
        self.buttonRebuild.setText(QCoreApplication.translate("MainWindow", u"Rebuild APK", None))
        self.buttonRefreshOverrides.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Overrides", None))
        self.editTextApkPath.setText(QCoreApplication.translate("MainWindow", u"Input apk file", None))
        self.buttonBrowseApk.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
    # retranslateUi



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
