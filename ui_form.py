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
    QRadioButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1394, 754)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(1070, 150, 301, 131))
        self.btnClosePosition = QPushButton(self.groupBox)
        self.btnClosePosition.setObjectName(u"btnClosePosition")
        self.btnClosePosition.setGeometry(QRect(20, 50, 141, 41))
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1070, 310, 301, 331))
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
        self.btnMakeLong = QPushButton(self.layoutWidget)
        self.btnMakeLong.setObjectName(u"btnMakeLong")
        self.btnMakeLong.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btnMakeLong)

        self.btnMakeShort = QPushButton(self.layoutWidget)
        self.btnMakeShort.setObjectName(u"btnMakeShort")

        self.horizontalLayout.addWidget(self.btnMakeShort)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(1070, 10, 301, 121))
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
        self.layoutWidget2.setGeometry(QRect(10, 30, 191, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.leToken = QLineEdit(self.layoutWidget2)
        self.leToken.setObjectName(u"leToken")

        self.horizontalLayout_4.addWidget(self.leToken)

        self.tableView = QTableView(Widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 1021, 731))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u8ba2\u5355\u64cd\u4f5c:", None))
        self.btnClosePosition.setText(QCoreApplication.translate("Widget", u"\u4e00\u952e\u5168\u90e8\u5e73\u4ed3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u5e02\u4ef7\u5f00\u4ed3\u64cd\u4f5c:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u7c7b\u578b:", None))
        self.rbtnUsdtBase.setText(QCoreApplication.translate("Widget", u"U\u672c\u4f4d", None))
        self.rbtnTokenBase.setText(QCoreApplication.translate("Widget", u"\u5e01\u672c\u4f4d", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u500d\u6570:", None))
        self.leLeverage.setPlaceholderText(QCoreApplication.translate("Widget", u"\u6760\u6746\u500d\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u6b62\u635f:", None))
        self.leStopLossRatio.setPlaceholderText(QCoreApplication.translate("Widget", u"\u80fd\u627f\u53d7\u4e8f\u635f\u7684\u767e\u5206\u6bd4", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u6570\u91cf:", None))
        self.leAmount.setPlaceholderText(QCoreApplication.translate("Widget", u"U\u7684\u6570\u91cf,\u5fc5\u987b\u5927\u4e8e6", None))
        self.btnMakeLong.setText(QCoreApplication.translate("Widget", u"\u5f00\u591a", None))
        self.btnMakeShort.setText(QCoreApplication.translate("Widget", u"\u5f00\u7a7a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u5e01\u79cd\u7ba1\u7406:", None))
        self.btnDeleteToken.setText(QCoreApplication.translate("Widget", u"\u5220\u9664", None))
        self.btnAddToken.setText(QCoreApplication.translate("Widget", u"\u6dfb\u52a0", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5e01\u540d:", None))
        self.leToken.setPlaceholderText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u5e01\u540d...", None))
    # retranslateUi

