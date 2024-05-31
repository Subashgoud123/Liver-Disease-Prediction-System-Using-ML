# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'first_draftVIXBpd.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from rmodule import solve
import sys
import sklearn

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn.metrics import precision_score, recall_score, f1_score


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 703)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"/* DarkTheme.qss */\n"
                                 "QMainWindow {\n"
                                 "    background-color: #123;\n"
                                 "\n"
                                 "	align-items: center; /* Center align horizontally */\n"
                                 "    justify-content: center;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget {\n"
                                 "    background-color: #ABC;\n"
                                 "	\n"
                                 "    color: #FFF;\n"
                                 "    display: flex;\n"
                                 "    flex-direction: column;\n"
                                 "    align-items: center; /* Center align horizontally */\n"
                                 "    justify-content: center; /* Center align vertically */\n"
                                 "}\n"
                                 "\n"
                                 "/* Apply styles to QLabel, QLineEdit, and QPushButton */\n"
                                 "QLabel {\n"
                                 "    color: #FFF; /* Text color for labels */\n"
                                 "    align: center; /* Center align text */\n"
                                 "}\n"
                                 "/* DarkTheme.qss */\n"
                                 "QPlainTextEdit {\n"
                                 "    background-color: #ABC; /* Background color */\n"
                                 "    color: #FFF; /* Text color */\n"
                                 "     /* Border style */\n"
                                 "    padding: 5px; /* Padding around the text */\n"
                                 "    font-family: Arial, sans-serif; /* Font family */\n"
                                 "    font-size: 14px; /* Font size */\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit {\n"
                                 "    background-color: #FFF; /* Light background color for lin"
                                 "e edits */\n"
                                 "    color: #000; /* Dark text color for line edits */\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: #666;\n"
                                 "    color: #FFF;\n"
                                 "}\n"
                                 "\n"
                                 "/* Add more styles for different widgets as needed */\n"
                                 "QLabel{\n"
                                 "padding: 5px; /* Padding around the text */\n"
                                 "    font-family: Arial, sans-serif; /* Font family */\n"
                                 "    font-size: 14px; /* Font size */\n"
                                 "lign-items: center;}\n"
                                 "QGroupBox{\n"
                                 "background-color: #444;\n"
                                 "	\n"
                                 "    color: #FFF;\n"
                                 "    display: flex;\n"
                                 "    flex-direction: column;\n"
                                 "    align-items: center; /* Center align horizontally */\n"
                                 "    justify-content: center; /* Center align vertically */\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QMainWindow {\n"
                                         "    background-color: #333;\n"
                                         "    color: #FFF;\n"
                                         "}\n"
                                         "Qcentralwidget{\n"
                                         "	background-color:#000;\n"
                                         "}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 40, 789, 381))
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"/* DarkTheme.qss */\n"
                                  "QMainWindow {\n"
                                  "    background-color: #333;\n"
                                  "\n"
                                  "    color: #FFF;\n"
                                  "	align-items: center; /* Center align horizontally */\n"
                                  "    justify-content: center;\n"
                                  "}\n"
                                  "\n"
                                  "QWidget {\n"
                                  "    background-color: #444;\n"
                                  "	border-radius: 10px;\n"
                                  "	border: 2px solid #1E6086;\n"
                                  "    color: #FFF;\n"
                                  "    display: flex;\n"
                                  "    flex-direction: column;\n"
                                  "    align-items: center; /* Center align horizontally */\n"
                                  "    justify-content: center; /* Center align vertically */\n"
                                  "}\n"
                                  "\n"
                                  "/* Apply styles to QLabel, QLineEdit, and QPushButton */\n"
                                  "QLabel {\n"
                                  "    color: #FFF; /* Text color for labels */\n"
                                  "    align: center; /* Center align text */\n"
                                  "}\n"
                                  "/* DarkTheme.qss */\n"
                                  "QPlainTextEdit {\n"
                                  "    background-color: #ABC; /* Background color */\n"
                                  "    color: #FFF; /* Text color */\n"
                                  "     /* Border style */\n"
                                  "    padding: 5px; /* Padding around the text */\n"
                                  "    font-family: Arial, sans-serif; /* Font family */\n"
                                  "    font-size: 14px; /* Font size */\n"
                                  "}\n"
                                  "\n"
                                  "QLin"
                                  "eEdit {\n"
                                  "    background-color: #FFF; /* Light background color for line edits */\n"
                                  "    color: #000; /* Dark text color for line edits */\n"
                                  "}\n"
                                  "\n"
                                  "QPushButton {\n"
                                  "    background-color: #666;\n"
                                  "    color: #FFF;\n"
                                  "}\n"
                                  "\n"
                                  "/* Add more styles for different widgets as needed */\n"
                                  "QLabel{\n"
                                  "padding: 5px; /* Padding around the text */\n"
                                  "    font-family: Arial, sans-serif; /* Font family */\n"
                                  "    font-size: 14px; /* Font size */\n"
                                  "lign-items: center;}\n"
                                  "QGroupBox{\n"
                                  "background-color: #444;\n"
                                  "	\n"
                                  "    color: #FFF;\n"
                                  "	border: 1px solid #444;\n"
                                  "    display: flex;\n"
                                  "    flex-direction: column;\n"
                                  "    align-items: center; /* Center align horizontally */\n"
                                  "    justify-content: center; /* Center align vertically */\n"
                                  "}\n"
                                  "")
        self.verticalGroupBox = QGroupBox(self.widget)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setGeometry(QRect(40, 30, 711, 241))
        sizePolicy.setHeightForWidth(
            self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy)
        self.verticalGroupBox.setStyleSheet(u"border:#FFF")
        self.verticalLayout_2 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalGroupBox = QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.horizontalGroupBox.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox.setSizePolicy(sizePolicy1)
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.horizontalGroupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_10.addWidget(self.label_16)

        self.horizontalSpacer_28 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_28)

        self.label_17 = QLabel(self.horizontalGroupBox)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.horizontalSpacer_29 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_29)

        self.label_18 = QLabel(self.horizontalGroupBox)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.horizontalSpacer_30 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_30)

        self.INpu_label_6 = QLabel(self.horizontalGroupBox)
        self.INpu_label_6.setObjectName(u"INpu_label_6")

        self.horizontalLayout_10.addWidget(self.INpu_label_6)

        self.verticalLayout_2.addWidget(self.horizontalGroupBox)

        self.horizontalGroupBox_4 = QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox_4.setObjectName(u"horizontalGroupBox_4")
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalGroupBox_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Edit_1 = QPlainTextEdit(self.horizontalGroupBox_4)
        self.Edit_1.setObjectName(u"Edit_1")
        self.Edit_1.setAcceptDrops(True)
        self.Edit_1.setInputMethodHints(Qt.ImhNone)
        self.Edit_1.setCursorWidth(0)

        self.horizontalLayout_12.addWidget(self.Edit_1)

        self.horizontalSpacer_34 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_34)

        self.Edit_2 = QPlainTextEdit(self.horizontalGroupBox_4)
        self.Edit_2.setObjectName(u"Edit_2")
        self.Edit_2.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_12.addWidget(self.Edit_2)

        self.horizontalSpacer_35 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_35)

        self.Edit_3 = QPlainTextEdit(self.horizontalGroupBox_4)
        self.Edit_3.setObjectName(u"Edit_3")
        self.Edit_3.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_12.addWidget(self.Edit_3)

        self.horizontalSpacer_36 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_36)

        self.Edit_4 = QPlainTextEdit(self.horizontalGroupBox_4)
        self.Edit_4.setObjectName(u"Edit_4")
        self.Edit_4.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_12.addWidget(self.Edit_4)

        self.verticalLayout_2.addWidget(self.horizontalGroupBox_4)

        self.horizontalGroupBox_2 = QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox_2.setObjectName(u"horizontalGroupBox_2")
        sizePolicy1.setHeightForWidth(
            self.horizontalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_19 = QLabel(self.horizontalGroupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_11.addWidget(self.label_19)

        self.horizontalSpacer_31 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_31)

        self.label_20 = QLabel(self.horizontalGroupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_11.addWidget(self.label_20)

        self.horizontalSpacer_32 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_32)

        self.label_21 = QLabel(self.horizontalGroupBox_2)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.horizontalSpacer_33 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_33)

        self.INpu_label_7 = QLabel(self.horizontalGroupBox_2)
        self.INpu_label_7.setObjectName(u"INpu_label_7")

        self.horizontalLayout_11.addWidget(self.INpu_label_7)

        self.verticalLayout_2.addWidget(self.horizontalGroupBox_2)

        self.horizontalGroupBox_3 = QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox_3.setObjectName(u"horizontalGroupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.horizontalGroupBox_3.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalGroupBox_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Edit_5 = QPlainTextEdit(self.horizontalGroupBox_3)
        self.Edit_5.setObjectName(u"Edit_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.Edit_5.sizePolicy().hasHeightForWidth())
        self.Edit_5.setSizePolicy(sizePolicy3)
        self.Edit_5.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_9.addWidget(self.Edit_5)

        self.horizontalSpacer_25 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_25)

        self.Edit_6 = QPlainTextEdit(self.horizontalGroupBox_3)
        self.Edit_6.setObjectName(u"Edit_6")
        self.Edit_6.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_9.addWidget(self.Edit_6)

        self.horizontalSpacer_26 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_26)

        self.Edit_7 = QPlainTextEdit(self.horizontalGroupBox_3)
        self.Edit_7.setObjectName(u"Edit_7")
        self.Edit_7.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_9.addWidget(self.Edit_7)

        self.horizontalSpacer_27 = QSpacerItem(
            40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_27)

        self.Edit_8 = QPlainTextEdit(self.horizontalGroupBox_3)
        self.Edit_8.setObjectName(u"Edit_8")
        self.Edit_8.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_9.addWidget(self.Edit_8)

        self.verticalLayout_2.addWidget(self.horizontalGroupBox_3)

        self.horizontalGroupBox_5 = QGroupBox(self.widget)
        self.horizontalGroupBox_5.setObjectName(u"horizontalGroupBox_5")
        self.horizontalGroupBox_5.setGeometry(QRect(30, 260, 707, 52))
        sizePolicy1.setHeightForWidth(
            self.horizontalGroupBox_5.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_5.setSizePolicy(sizePolicy1)
        self.horizontalGroupBox_5.setStyleSheet(u"border:#FFF")
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalGroupBox_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_39 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_39)

        self.label_22 = QLabel(self.horizontalGroupBox_5)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setMaximumSize(QSize(174, 16777215))

        self.horizontalLayout_13.addWidget(self.label_22)

        self.horizontalSpacer_37 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_37)

        self.horizontalSpacer_40 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_40)

        self.label_23 = QLabel(self.horizontalGroupBox_5)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_13.addWidget(self.label_23)

        self.horizontalSpacer_41 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_41)

        self.horizontalSpacer_38 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_38)

        self.horizontalGroupBox_6 = QGroupBox(self.widget)
        self.horizontalGroupBox_6.setObjectName(u"horizontalGroupBox_6")
        self.horizontalGroupBox_6.setGeometry(QRect(90, 310, 521, 61))
        sizePolicy1.setHeightForWidth(
            self.horizontalGroupBox_6.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_6.setSizePolicy(sizePolicy1)
        self.horizontalGroupBox_6.setStyleSheet(u"/* DarkTheme.qss */\n"
                                                "QMainWindow {\n"
                                                "    background-color: #333;\n"
                                                "	baclground-image:C:\\Users\\G SUNIHERA\\Downloads\\WhatsApp Image 2023-11-06 at 6.23.44 PM.jpeg;\n"
                                                "    color: #FFF;\n"
                                                "	align-items: center; /* Center align horizontally */\n"
                                                "    justify-content: center;\n"
                                                "}\n"
                                                "\n"
                                                "QWidget {\n"
                                                "    background-color: #444;\n"
                                                "	\n"
                                                "    color: #FFF;\n"
                                                "    display: flex;\n"
                                                "    flex-direction: column;\n"
                                                "    align-items: center; /* Center align horizontally */\n"
                                                "    justify-content: center; /* Center align vertically */\n"
                                                "}\n"
                                                "\n"
                                                "/* Apply styles to QLabel, QLineEdit, and QPushButton */\n"
                                                "QLabel {\n"
                                                "    color: #FFF; /* Text color for labels */\n"
                                                "    align: center; /* Center align text */\n"
                                                "}\n"
                                                "/* DarkTheme.qss */\n"
                                                "QPlainTextEdit {\n"
                                                "    background-color: #ABC; /* Background color */\n"
                                                "    color: #FFF; /* Text color */\n"
                                                "     /* Border style */\n"
                                                "    padding: 5px; /* Padding around the text */\n"
                                                "    font-family: Arial, sans-serif; /* Font family */\n"
                                                "    font-si"
                                                "ze: 14px; /* Font size */\n"
                                                "}\n"
                                                "\n"
                                                "QLineEdit {\n"
                                                "    background-color: #FFF; /* Light background color for line edits */\n"
                                                "    color: #000; /* Dark text color for line edits */\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton {\n"
                                                "    background-color: #666;\n"
                                                "    color: #FFF;\n"
                                                "}\n"
                                                "\n"
                                                "/* Add more styles for different widgets as needed */\n"
                                                "QLabel{\n"
                                                "padding: 5px; /* Padding around the text */\n"
                                                "    font-family: Arial, sans-serif; /* Font family */\n"
                                                "    font-size: 14px; /* Font size */\n"
                                                "lign-items: center;}\n"
                                                "QGroupBox{\n"
                                                "background-color: #444;\n"
                                                "	\n"
                                                "    color: #FFF;\n"
                                                "    display: flex;\n"
                                                "    flex-direction: column;\n"
                                                "    align-items: center; /* Center align horizontally */\n"
                                                "    justify-content: center; /* Center align vertically */\n"
                                                "}\n"
                                                "QhorizontalGroupBox{\n"
                                                "	border: 1px solid red;\n"
                                                "}\n"
                                                "")
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalGroupBox_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_48 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_48)

        self.horizontalSpacer_47 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_47)

        self.horizontalSpacer_42 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_42)

        self.horizontalSpacer_51 = QSpacerItem(
            180, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_51)

        self.Edit_9 = QPlainTextEdit(self.horizontalGroupBox_6)
        self.Edit_9.setObjectName(u"Edit_9")
        sizePolicy3.setHeightForWidth(
            self.Edit_9.sizePolicy().hasHeightForWidth())
        self.Edit_9.setSizePolicy(sizePolicy3)
        self.Edit_9.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_14.addWidget(self.Edit_9)

        self.horizontalSpacer_50 = QSpacerItem(
            180, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_50)

        self.horizontalSpacer_49 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_49)

        self.horizontalSpacer_43 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_43)

        self.Edit_10 = QPlainTextEdit(self.horizontalGroupBox_6)
        self.Edit_10.setObjectName(u"Edit_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.Edit_10.sizePolicy().hasHeightForWidth())
        self.Edit_10.setSizePolicy(sizePolicy5)
        self.Edit_10.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_14.addWidget(self.Edit_10)

        self.horizontalSpacer_44 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_44)

        self.horizontalSpacer_45 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_45)

        self.horizontalSpacer_46 = QSpacerItem(
            40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_46)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 450, 111, 41))
        self.pushButton.clicked.connect(self.check_input)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "font:14;\n"
                                      "border-radius: 10px;}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #1E6086; /* Background color when hovered */\n"
                                      "    border: 2px solid #3DAEE9; /* Border when hovered */\n"
                                      "    color: white; /* Text color when hovered */\n"
                                      "}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 560, 901, 81))
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
                                 "font: 63 28pt \"Yu Gothic UI Semibold\";")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 450, 111, 41))
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
                                        "font:14;\n"
                                        "border-radius: 10px;}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: #1E6086; /* Background color when hovered */\n"
                                        "    border: 2px solid #3DAEE9; /* Border when hovered */\n"
                                        "    color: white; /* Text color when hovered */\n"
                                        "}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_16.setText(QCoreApplication.translate(
            "MainWindow", u"      Age", None))
        self.label_17.setText(QCoreApplication.translate(
            "MainWindow", u"     Gender", None))
        self.label_18.setText(QCoreApplication.translate(
            "MainWindow", u"Total_Bilirubin", None))
        self.INpu_label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Direct_Bilirubin", None))
        self.Edit_1.setPlainText(
            QCoreApplication.translate("MainWindow", u"", None))
        self.label_19.setText(QCoreApplication.translate(
            "MainWindow", u"Alkaline_Phosphotase", None))
        self.label_20.setText(QCoreApplication.translate(
            "MainWindow", u"Alamine_Aminotransferase", None))
        self.label_21.setText(QCoreApplication.translate(
            "MainWindow", u"Aspartate_Aminotransferase", None))
        self.INpu_label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Total_Protiens", None))
        self.Edit_5.setPlainText(QCoreApplication.translate("MainWindow", u""
                                                            "", None))
        self.label_22.setText(QCoreApplication.translate(
            "MainWindow", u"                            Albumin", None))
        self.label_23.setText(QCoreApplication.translate(
            "MainWindow", u"        Albumin_and_Globulin_Ratio", None))
        self.Edit_9.setPlainText(QCoreApplication.translate("MainWindow", u""
                                                            "", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Submit", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"Next Prediction", None))
    # retranslateUi

    def check_input(self):
        in1 = self.Edit_1.toPlainText()
        in2 = self.Edit_2.toPlainText().strip()
        in3 = self.Edit_3.toPlainText()
        in4 = self.Edit_4.toPlainText()
        in5 = self.Edit_5.toPlainText()
        in6 = self.Edit_6.toPlainText()
        in7 = self.Edit_7.toPlainText()
        in8 = self.Edit_8.toPlainText()
        in9 = self.Edit_9.toPlainText()
        in10 = self.Edit_10.toPlainText()
        li = [in1, in2, in3, in4, in5, in6, in7, in8, in9, in10]
        status = True
        c = 0
        for i in range(0, 10):
            if li[i] != "\n" and li[i] != "":
                if i != 1:
                    try:
                        li[i] = float(li[i])
                    except:
                        status = False
                        print(i)
                        break
                else:
                    if str(li[1]).lower() != "Male".lower() and str(li[1]).lower() != "Female".lower():
                        print("Gen")
                        status = False
                        break
            else:
                li[i] = None
                c += 1
                if c > 4:
                    status = False
                    break

        print(li)
        if status == True:
            if str(solve(li)[0]) == "1":
                result_text = "Liver Disease is Present"
            else:
                result_text = "Healthy"
        else:
            result_text = "Please Check Your input Once"
        self.label.setText(result_text)

    def clear(self):
        self.Edit_1.setPlainText("")
        self.Edit_2.setPlainText("")
        self.Edit_3.setPlainText("")
        self.Edit_4.setPlainText("")
        self.Edit_5.setPlainText("")
        self.Edit_6.setPlainText("")
        self.Edit_7.setPlainText("")
        self.Edit_8.setPlainText("")
        self.Edit_9.setPlainText("")
        self.Edit_10.setPlainText("")


if __name__ == '__main__':
    app = QApplication()
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
