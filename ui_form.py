# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QTableView, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1465, 768)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1451, 731))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 1111, 671))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1140, 150, 301, 341))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 210, 49, 30))
        self.rbtnUsdtBase = QRadioButton(self.groupBox_2)
        self.rbtnUsdtBase.setObjectName(u"rbtnUsdtBase")
        self.rbtnUsdtBase.setGeometry(QRect(80, 70, 66, 28))
        self.rbtnTokenBase = QRadioButton(self.groupBox_2)
        self.rbtnTokenBase.setObjectName(u"rbtnTokenBase")
        self.rbtnTokenBase.setGeometry(QRect(150, 70, 71, 28))
        self.lbPosition = QLabel(self.groupBox_2)
        self.lbPosition.setObjectName(u"lbPosition")
        self.lbPosition.setGeometry(QRect(130, 250, 161, 20))
        font = QFont()
        font.setPointSize(10)
        self.lbPosition.setFont(font)
        self.lbPosition.setLayoutDirection(Qt.RightToLeft)
        self.btnMakeShort = QPushButton(self.groupBox_2)
        self.btnMakeShort.setObjectName(u"btnMakeShort")
        self.btnMakeShort.setGeometry(QRect(40, 280, 91, 41))
        self.btnMakeLong = QPushButton(self.groupBox_2)
        self.btnMakeLong.setObjectName(u"btnMakeLong")
        self.btnMakeLong.setGeometry(QRect(180, 280, 91, 41))
        self.btnMakeLong.setAutoDefault(False)
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 100, 34, 50))
        self.leStopLossRatio = QLineEdit(self.groupBox_2)
        self.leStopLossRatio.setObjectName(u"leStopLossRatio")
        self.leStopLossRatio.setGeometry(QRect(80, 160, 191, 31))
        self.leLeverage = QLineEdit(self.groupBox_2)
        self.leLeverage.setObjectName(u"leLeverage")
        self.leLeverage.setGeometry(QRect(80, 110, 191, 30))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 34, 30))
        self.leAmount = QLineEdit(self.groupBox_2)
        self.leAmount.setObjectName(u"leAmount")
        self.leAmount.setGeometry(QRect(80, 210, 191, 31))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 70, 34, 22))
        self.lbAvailMargin = QLabel(self.groupBox_2)
        self.lbAvailMargin.setObjectName(u"lbAvailMargin")
        self.lbAvailMargin.setGeometry(QRect(40, 40, 231, 21))
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(1140, 10, 301, 121))
        self.layoutWidget = QWidget(self.groupBox_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 241, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnDeleteToken = QPushButton(self.layoutWidget)
        self.btnDeleteToken.setObjectName(u"btnDeleteToken")

        self.horizontalLayout_5.addWidget(self.btnDeleteToken)

        self.btnAddToken = QPushButton(self.layoutWidget)
        self.btnAddToken.setObjectName(u"btnAddToken")

        self.horizontalLayout_5.addWidget(self.btnAddToken)

        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 241, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.leToken = QLineEdit(self.layoutWidget1)
        self.leToken.setObjectName(u"leToken")

        self.horizontalLayout_4.addWidget(self.leToken)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(1140, 530, 301, 151))
        self.btnDecreaseMargin = QPushButton(self.groupBox)
        self.btnDecreaseMargin.setObjectName(u"btnDecreaseMargin")
        self.btnDecreaseMargin.setGeometry(QRect(50, 100, 88, 25))
        self.btnIncreaseMargin = QPushButton(self.groupBox)
        self.btnIncreaseMargin.setObjectName(u"btnIncreaseMargin")
        self.btnIncreaseMargin.setGeometry(QRect(180, 100, 88, 25))
        self.leAdjustMarginAmount = QLineEdit(self.groupBox)
        self.leAdjustMarginAmount.setObjectName(u"leAdjustMarginAmount")
        self.leAdjustMarginAmount.setGeometry(QRect(70, 50, 201, 25))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 50, 71, 21))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableViewCurPositions = QTableView(self.tab_2)
        self.tableViewCurPositions.setObjectName(u"tableViewCurPositions")
        self.tableViewCurPositions.setGeometry(QRect(10, 10, 1281, 671))
        self.btnClosePosition = QPushButton(self.tab_2)
        self.btnClosePosition.setObjectName(u"btnClosePosition")
        self.btnClosePosition.setGeometry(QRect(1300, 330, 121, 41))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableViewCurrentOpenOrders = QTableView(self.tab_4)
        self.tableViewCurrentOpenOrders.setObjectName(u"tableViewCurrentOpenOrders")
        self.tableViewCurrentOpenOrders.setGeometry(QRect(10, 10, 1421, 691))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.leApiKey = QLineEdit(self.tab_3)
        self.leApiKey.setObjectName(u"leApiKey")
        self.leApiKey.setGeometry(QRect(300, 190, 681, 41))
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 200, 66, 17))
        self.leSecretKey = QLineEdit(self.tab_3)
        self.leSecretKey.setObjectName(u"leSecretKey")
        self.leSecretKey.setGeometry(QRect(300, 280, 681, 41))
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 290, 66, 17))
        self.btnSaveApiKeySecret = QPushButton(self.tab_3)
        self.btnSaveApiKeySecret.setObjectName(u"btnSaveApiKeySecret")
        self.btnSaveApiKeySecret.setGeometry(QRect(800, 410, 181, 61))
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5e02\u4ef7\u5f00\u4ed3\u64cd\u4f5c:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u4fdd\u8bc1\u91d1:", None))
        self.rbtnUsdtBase.setText(QCoreApplication.translate("Widget", u"U\u672c\u4f4d", None))
        self.rbtnTokenBase.setText(QCoreApplication.translate("Widget", u"\u5e01\u672c\u4f4d", None))
        self.lbPosition.setText(QCoreApplication.translate("Widget", u"\u53ef\u5f00\u4ed3\u4f4d: 0 USDT", None))
        self.btnMakeShort.setText(QCoreApplication.translate("Widget", u"\u5f00\u7a7a", None))
        self.btnMakeLong.setText(QCoreApplication.translate("Widget", u"\u5f00\u591a", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u500d\u6570:", None))
        self.leStopLossRatio.setPlaceholderText(QCoreApplication.translate("Widget", u"\u80fd\u627f\u53d7\u4e8f\u635f\u7684\u767e\u5206\u6bd4", None))
        self.leLeverage.setPlaceholderText(QCoreApplication.translate("Widget", u"\u6760\u6746\u500d\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u6b62\u635f:", None))
        self.leAmount.setPlaceholderText(QCoreApplication.translate("Widget", u"USDT\u7684\u6570\u91cf", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u7c7b\u578b:", None))
        self.lbAvailMargin.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u4ea4\u6613\u5bf9\u7ba1\u7406:", None))
        self.btnDeleteToken.setText(QCoreApplication.translate("Widget", u"\u5220\u9664", None))
        self.btnAddToken.setText(QCoreApplication.translate("Widget", u"\u6dfb\u52a0", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5e01\u540d:", None))
        self.leToken.setPlaceholderText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u5e01\u540d\u6216\u4ea4\u6613\u5bf9...", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u8c03\u6574\u4fdd\u8bc1\u91d1:", None))
        self.btnDecreaseMargin.setText(QCoreApplication.translate("Widget", u"\u51cf\u5c11", None))
        self.btnIncreaseMargin.setText(QCoreApplication.translate("Widget", u"\u589e\u52a0", None))
        self.leAdjustMarginAmount.setPlaceholderText(QCoreApplication.translate("Widget", u"USDT\u4fdd\u8bc1\u91d1\u8c03\u6574\u91cf", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u8c03\u6574\u91cf:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u4e3b\u754c\u9762", None))
        self.btnClosePosition.setText(QCoreApplication.translate("Widget", u"\u4e00\u952e\u5e02\u4ef7\u5168\u5e73", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u4ed3\u4f4d\u7ba1\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Widget", u"\u5f53\u524d\u59d4\u6258", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"API \u5bc6\u94a5:", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u5bc6\u94a5\uff1a", None))
        self.btnSaveApiKeySecret.setText(QCoreApplication.translate("Widget", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"API\u5bc6\u94a5\u7ba1\u7406", None))
    # retranslateUi

