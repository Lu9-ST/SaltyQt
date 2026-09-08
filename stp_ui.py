# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'saltthepasswMgVpA.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QComboBox, QDialogButtonBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSlider, QWidget)


def eye_icon() -> QIcon:
    icon = QIcon()
    for name, state in (("password-show-on", QIcon.State.Off),
                        ("password-show-off",  QIcon.State.On)):
        themed = QIcon.fromTheme(name)
        if themed.isNull():
            continue
        for px in (16, 24, 32):  # a few sizes so the theme picks a sharp one
            icon.addPixmap(themed.pixmap(px), QIcon.Mode.Normal, state)
    return icon

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 250)
        Dialog.setMinimumSize(QSize(410, 250))
        icon = QIcon(QIcon.fromTheme(u"dialog-password"))
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.strMasterPass = QLineEdit(Dialog)
        self.strMasterPass.setObjectName(u"strMasterPass")
        self.strMasterPass.setEchoMode(QLineEdit.EchoMode.Password)
        self.strMasterPass.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.strMasterPass, 0, 0, 1, 4)

        self.btnShowPass = QPushButton(Dialog)
        self.btnShowPass.setObjectName(u"btnShowPass")
        icon = eye_icon()
        self.btnShowPass.setIcon(icon)
        self.btnShowPass.setCheckable(True)
        self.btnShowPass.setChecked(False)

        self.gridLayout.addWidget(self.btnShowPass, 0, 4, 1, 1)

        self.strDomainName = QLineEdit(Dialog)
        self.strDomainName.setObjectName(u"strDomainName")

        self.gridLayout.addWidget(self.strDomainName, 1, 0, 1, 5)

        self.strDomainPhrase = QLineEdit(Dialog)
        self.strDomainPhrase.setObjectName(u"strDomainPhrase")

        self.gridLayout.addWidget(self.strDomainPhrase, 2, 0, 1, 5)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.selHash = QComboBox(Dialog)
        self.selHash.addItem("")
        self.selHash.addItem("")
        self.selHash.addItem("")
        self.selHash.addItem("")
        self.selHash.addItem("")
        self.selHash.addItem("")
        self.selHash.setObjectName(u"selHash")

        self.gridLayout.addWidget(self.selHash, 3, 1, 1, 1)

        self.sliderCharCount = QSlider(Dialog)
        self.sliderCharCount.setObjectName(u"sliderCharCount")
        self.sliderCharCount.setMinimum(1)
        self.sliderCharCount.setMaximum(86)
        self.sliderCharCount.setValue(20)
        self.sliderCharCount.setOrientation(Qt.Orientation.Horizontal)
        self.sliderCharCount.setInvertedAppearance(False)
        self.sliderCharCount.setInvertedControls(False)

        self.gridLayout.addWidget(self.sliderCharCount, 3, 2, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 2)

        self.strSaltedPass = QLineEdit(Dialog)
        self.strSaltedPass.setObjectName(u"strSaltedPass")
        self.strSaltedPass.setAcceptDrops(False)
        self.strSaltedPass.setEchoMode(QLineEdit.EchoMode.Password)
        self.strSaltedPass.setCursor(Qt.CursorShape.CrossCursor)
        self.strSaltedPass.setReadOnly(True)
        self.strSaltedPass.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.strSaltedPass, 4, 0, 1, 4)

        self.btnShowSalted = QPushButton(Dialog)
        self.btnShowSalted.setObjectName(u"btnShowSalted")
        self.btnShowSalted.setIcon(icon)
        self.btnShowSalted.setCheckable(True)
        self.btnShowSalted.setChecked(False)

        self.gridLayout.addWidget(self.btnShowSalted, 4, 4, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close|QDialogButtonBox.StandardButton.Reset)

        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 5)

        QWidget.setTabOrder(self.strMasterPass, self.btnShowPass)
        QWidget.setTabOrder(self.btnShowPass, self.strDomainName)
        QWidget.setTabOrder(self.strDomainName, self.strDomainPhrase)
        QWidget.setTabOrder(self.strDomainPhrase, self.selHash)
        QWidget.setTabOrder(self.selHash, self.sliderCharCount)
        QWidget.setTabOrder(self.sliderCharCount, self.strSaltedPass)
        QWidget.setTabOrder(self.strSaltedPass, self.btnShowSalted)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.selHash.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"SaltThePass", None))
        self.strMasterPass.setPlaceholderText(QCoreApplication.translate("Dialog", u"Master Password (don't use this anywhere else!)", None))
        self.btnShowPass.setText("")
        self.strDomainName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Domain Name (example.com)", None))
        self.strDomainPhrase.setPlaceholderText(QCoreApplication.translate("Dialog", u"Domain Phrase (optional)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Hash", None))
        self.selHash.setItemText(0, QCoreApplication.translate("Dialog", u"MD5", None))
        self.selHash.setItemText(1, QCoreApplication.translate("Dialog", u"SHA-1", None))
        self.selHash.setItemText(2, QCoreApplication.translate("Dialog", u"SHA-2", None))
        self.selHash.setItemText(3, QCoreApplication.translate("Dialog", u"SHA-3", None))
        self.selHash.setItemText(4, QCoreApplication.translate("Dialog", u"Keccak512", None))
        self.selHash.setItemText(5, QCoreApplication.translate("Dialog", u"RIPEMD-160", None))

        self.selHash.setCurrentText(QCoreApplication.translate("Dialog", u"Keccak512", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"XX characters", None))
        self.strSaltedPass.setText("")
        self.strSaltedPass.setPlaceholderText(QCoreApplication.translate("Dialog", u"Salted Password", None))
        self.btnShowSalted.setText("")
    # retranslateUi

