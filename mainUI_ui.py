# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import icon_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(537, 186)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(537, 186))
        mainWindow.setMaximumSize(QSize(537, 186))
        icon = QIcon()
        icon.addFile(u":/icon0/education.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAnimated(True)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 20, 531, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.progressBar_visio = QProgressBar(self.gridLayoutWidget)
        self.progressBar_visio.setObjectName(u"progressBar_visio")
        self.progressBar_visio.setMinimumSize(QSize(311, 35))
        self.progressBar_visio.setMaximumSize(QSize(311, 35))
        self.progressBar_visio.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;         /* \u8fb9\u6846\u989c\u8272 */\n"
"    border-radius: 5px;             /* \u5706\u89d2\u534a\u5f84 */\n"
"    text-align: center;              /* \u6587\u672c\u5c45\u4e2d */\n"
"    background-color: #ffffff;      /* \u8fdb\u5ea6\u6761\u80cc\u666f\u989c\u8272\uff08\u672a\u586b\u5145\u90e8\u5206\uff09 */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #aaffaa;      /* \u586b\u5145\u90e8\u5206\u7684\u989c\u8272\uff08\u8fdb\u5ea6\uff09 */\n"
"    width: 20px;                    /* \u586b\u5145\u90e8\u5206\u7684\u5bbd\u5ea6 */\n"
"}")
        self.progressBar_visio.setValue(0)

        self.gridLayout.addWidget(self.progressBar_visio, 1, 1, 1, 1)

        self.pushButton_open_word = QPushButton(self.gridLayoutWidget)
        self.pushButton_open_word.setObjectName(u"pushButton_open_word")
        self.pushButton_open_word.setMinimumSize(QSize(191, 41))
        self.pushButton_open_word.setMaximumSize(QSize(191, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.pushButton_open_word.setFont(font)

        self.gridLayout.addWidget(self.pushButton_open_word, 0, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.progressBar_word = QProgressBar(self.gridLayoutWidget)
        self.progressBar_word.setObjectName(u"progressBar_word")
        self.progressBar_word.setMinimumSize(QSize(311, 35))
        self.progressBar_word.setMaximumSize(QSize(311, 35))
        self.progressBar_word.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;         /* \u8fb9\u6846\u989c\u8272 */\n"
"    border-radius: 5px;             /* \u5706\u89d2\u534a\u5f84 */\n"
"    text-align: center;              /* \u6587\u672c\u5c45\u4e2d */\n"
"    background-color: #ffffff;      /* \u8fdb\u5ea6\u6761\u80cc\u666f\u989c\u8272\uff08\u672a\u586b\u5145\u90e8\u5206\uff09 */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #aaffaa;      /* \u586b\u5145\u90e8\u5206\u7684\u989c\u8272\uff08\u8fdb\u5ea6\uff09 */\n"
"    width: 20px;                    /* \u586b\u5145\u90e8\u5206\u7684\u5bbd\u5ea6 */\n"
"}")
        self.progressBar_word.setValue(0)

        self.gridLayout.addWidget(self.progressBar_word, 0, 1, 1, 1)

        self.pushButton_open_visio = QPushButton(self.gridLayoutWidget)
        self.pushButton_open_visio.setObjectName(u"pushButton_open_visio")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_open_visio.sizePolicy().hasHeightForWidth())
        self.pushButton_open_visio.setSizePolicy(sizePolicy1)
        self.pushButton_open_visio.setMinimumSize(QSize(191, 41))
        self.pushButton_open_visio.setMaximumSize(QSize(41, 16777215))
        self.pushButton_open_visio.setFont(font)

        self.gridLayout.addWidget(self.pushButton_open_visio, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Visio\u8f6cTiff", None))
        self.pushButton_open_word.setText(QCoreApplication.translate("mainWindow", u"\u8f6c\u6362\u5185\u5d4cVisio\u7684Word\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"DPI\u8bbe\u7f6e  ", None))
        self.pushButton_open_visio.setText(QCoreApplication.translate("mainWindow", u"\u8f6c\u6362Visio\u6587\u4ef6", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"600", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"300", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"1200", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"200", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"500", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("mainWindow", u"400", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("mainWindow", u"100", None))

        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Developed by MatrixEE", None))
    # retranslateUi

