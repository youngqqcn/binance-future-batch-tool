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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(510, 250, 234, 215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rbtnUsdtBase = QRadioButton(self.widget)
        self.rbtnUsdtBase.setObjectName(u"rbtnUsdtBase")

        self.horizontalLayout_2.addWidget(self.rbtnUsdtBase)

        self.rbtnTokenBase = QRadioButton(self.widget)
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
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.leMultiples = QLineEdit(self.widget)
        self.leMultiples.setObjectName(u"leMultiples")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leMultiples)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.leStopLossRatio = QLineEdit(self.widget)
        self.leStopLossRatio.setObjectName(u"leStopLossRatio")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leStopLossRatio)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.leAmount = QLineEdit(self.widget)
        self.leAmount.setObjectName(u"leAmount")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.leAmount)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.btnMakeLong = QPushButton(self.widget)
        self.btnMakeLong.setObjectName(u"btnMakeLong")
        self.btnMakeLong.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btnMakeLong)

        self.btnMakeShort = QPushButton(self.widget)
        self.btnMakeShort.setObjectName(u"btnMakeShort")

        self.horizontalLayout.addWidget(self.btnMakeShort)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 10)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.widget1 = QWidget(Widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(90, 60, 301, 471))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.leToken = QLineEdit(self.widget1)
        self.leToken.setObjectName(u"leToken")

        self.horizontalLayout_4.addWidget(self.leToken)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnDeleteToken = QPushButton(self.widget1)
        self.btnDeleteToken.setObjectName(u"btnDeleteToken")

        self.horizontalLayout_5.addWidget(self.btnDeleteToken)

        self.btnAddToken = QPushButton(self.widget1)
        self.btnAddToken.setObjectName(u"btnAddToken")

        self.horizontalLayout_5.addWidget(self.btnAddToken)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.listView = QListView(self.widget1)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_4.addWidget(self.listView)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u7c7b\u578b:", None))
        self.rbtnUsdtBase.setText(QCoreApplication.translate("Widget", u"U\u672c\u4f4d", None))
        self.rbtnTokenBase.setText(QCoreApplication.translate("Widget", u"\u5e01\u672c\u4f4d", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u500d\u6570:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u6b62\u635f(%):", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u6570\u91cf:", None))
        self.btnMakeLong.setText(QCoreApplication.translate("Widget", u"\u5f00\u591a", None))
        self.btnMakeShort.setText(QCoreApplication.translate("Widget", u"\u5f00\u7a7a", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5e01\u5bf9\u7ba1\u7406:", None))
        self.leToken.setPlaceholderText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u5e01\u540d...", None))
        self.btnDeleteToken.setText(QCoreApplication.translate("Widget", u"\u5220\u9664", None))
        self.btnAddToken.setText(QCoreApplication.translate("Widget", u"\u6dfb\u52a0", None))
    # retranslateUi

