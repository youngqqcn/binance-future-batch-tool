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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1394, 754)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 1361, 721))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 1011, 651))
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1030, 230, 301, 321))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 253, 258))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rbtnUsdtBase = QRadioButton(self.layoutWidget)
        self.rbtnUsdtBase.setObjectName(u"rbtnUsdtBase")

        self.horizontalLayout_2.addWidget(self.rbtnUsdtBase)

        self.rbtnTokenBase = QRadioButton(self.layoutWidget)
        self.rbtnTokenBase.setObjectName(u"rbtnTokenBase")

        self.horizontalLayout_2.addWidget(self.rbtnTokenBase)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.leLeverage = QLineEdit(self.layoutWidget)
        self.leLeverage.setObjectName(u"leLeverage")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leLeverage)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.leStopLossRatio = QLineEdit(self.layoutWidget)
        self.leStopLossRatio.setObjectName(u"leStopLossRatio")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leStopLossRatio)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.leAmount = QLineEdit(self.layoutWidget)
        self.leAmount.setObjectName(u"leAmount")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leAmount)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.btnMakeShort = QPushButton(self.layoutWidget)
        self.btnMakeShort.setObjectName(u"btnMakeShort")

        self.horizontalLayout.addWidget(self.btnMakeShort)

        self.btnMakeLong = QPushButton(self.layoutWidget)
        self.btnMakeLong.setObjectName(u"btnMakeLong")
        self.btnMakeLong.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btnMakeLong)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(1040, 40, 301, 121))
        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 80, 241, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnDeleteToken = QPushButton(self.layoutWidget1)
        self.btnDeleteToken.setObjectName(u"btnDeleteToken")

        self.horizontalLayout_5.addWidget(self.btnDeleteToken)

        self.btnAddToken = QPushButton(self.layoutWidget1)
        self.btnAddToken.setObjectName(u"btnAddToken")

        self.horizontalLayout_5.addWidget(self.btnAddToken)

        self.layoutWidget2 = QWidget(self.groupBox_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 241, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.leToken = QLineEdit(self.layoutWidget2)
        self.leToken.setObjectName(u"leToken")

        self.horizontalLayout_4.addWidget(self.leToken)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableViewCurPositions = QTableView(self.tab_2)
        self.tableViewCurPositions.setObjectName(u"tableViewCurPositions")
        self.tableViewCurPositions.setGeometry(QRect(10, 10, 1111, 651))
        self.btnGetCurrentPosition = QPushButton(self.tab_2)
        self.btnGetCurrentPosition.setObjectName(u"btnGetCurrentPosition")
        self.btnGetCurrentPosition.setGeometry(QRect(1150, 170, 151, 61))
        self.btnClosePosition = QPushButton(self.tab_2)
        self.btnClosePosition.setObjectName(u"btnClosePosition")
        self.btnClosePosition.setGeometry(QRect(1150, 270, 161, 61))
        self.tabWidget.addTab(self.tab_2, "")
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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5e02\u4ef7\u5f00\u4ed3\u64cd\u4f5c:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u7c7b\u578b:", None))
        self.rbtnUsdtBase.setText(QCoreApplication.translate("Widget", u"U\u672c\u4f4d", None))
        self.rbtnTokenBase.setText(QCoreApplication.translate("Widget", u"\u5e01\u672c\u4f4d", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u500d\u6570:", None))
        self.leLeverage.setPlaceholderText(QCoreApplication.translate("Widget", u"\u6760\u6746\u500d\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u6b62\u635f:", None))
        self.leStopLossRatio.setPlaceholderText(QCoreApplication.translate("Widget", u"\u80fd\u627f\u53d7\u4e8f\u635f\u7684\u767e\u5206\u6bd4", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u6570\u91cf:", None))
        self.leAmount.setPlaceholderText(QCoreApplication.translate("Widget", u"USDT\u7684\u6570\u91cf,\u5fc5\u987b\u5927\u4e8e6", None))
        self.btnMakeShort.setText(QCoreApplication.translate("Widget", u"\u5f00\u7a7a", None))
        self.btnMakeLong.setText(QCoreApplication.translate("Widget", u"\u5f00\u591a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u4ea4\u6613\u5bf9\u7ba1\u7406:", None))
        self.btnDeleteToken.setText(QCoreApplication.translate("Widget", u"\u5220\u9664", None))
        self.btnAddToken.setText(QCoreApplication.translate("Widget", u"\u6dfb\u52a0", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5e01\u540d:", None))
        self.leToken.setPlaceholderText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u5e01\u540d\u6216\u4ea4\u6613\u5bf9...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u4e3b\u754c\u9762", None))
        self.btnGetCurrentPosition.setText(QCoreApplication.translate("Widget", u"\u83b7\u53d6\u5f53\u524d\u6240\u6709\u4ed3\u4f4d", None))
        self.btnClosePosition.setText(QCoreApplication.translate("Widget", u"\u4e00\u952e\u5168\u90e8\u5e73\u4ed3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u4ed3\u4f4d\u7ba1\u7406", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"API \u5bc6\u94a5:", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u5bc6\u94a5\uff1a", None))
        self.btnSaveApiKeySecret.setText(QCoreApplication.translate("Widget", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"\u5bc6\u94a5\u7ba1\u7406", None))
    # retranslateUi

