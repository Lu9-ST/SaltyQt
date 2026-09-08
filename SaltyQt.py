# -*- coding: utf-8 -*-
"""
Python-only port of saltthepass.js by Nic Jansma + Qt6 GUI
"""

import base64
import hashlib
import sys

from Crypto.Hash import RIPEMD160, keccak
from PySide6.QtCore import QEvent, QMimeData, Qt
from PySide6.QtGui import QDrag
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
                               QLineEdit)

from stp_ui import Ui_Dialog

_ALGOS = {"md5": hashlib.md5, "sha1": hashlib.sha1,
          "sha2": hashlib.sha512, "sha3": hashlib.sha3_512}

def saltthepass(hash_name: str, master: str, domain: str, phrase: str = "") -> str:
    data = (master + domain + phrase).encode("utf-8")
    #data = bytes(ord(c) & 0xFF for c in (master + domain + phrase)) latin-1 version, unused
    if hash_name == "keccak512":
        digest = keccak.new(digest_bits=512, data=data).digest()
    elif hash_name == "ripemd160":
        digest = RIPEMD160.new(data).digest()
    else:
        digest = _ALGOS[hash_name](data).digest()
    b64 = base64.b64encode(digest).decode("ascii")
    return b64.rstrip("=").replace("+", "-").replace("/", "_")


class SaltThePassDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self._full_salted = ""
        self.drag_press_pos = None
        self._drag_text = ""

        # Regenerate as the inputs change
        self.ui.strMasterPass.textChanged.connect(self._update)
        self.ui.strDomainName.textChanged.connect(self._update)
        self.ui.strDomainPhrase.textChanged.connect(self._update)
        self.ui.selHash.currentTextChanged.connect(self._update)

        # Slider only truncates the output
        self.ui.sliderCharCount.valueChanged.connect(self._apply_truncation)

        # Checkable show/hide buttons
        self.ui.btnShowPass.toggled.connect(
            lambda shown: self._set_echo(self.ui.strMasterPass, shown))
        self.ui.btnShowSalted.toggled.connect(
            lambda shown: self._set_echo(self.ui.strSaltedPass, shown))

        reset = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Reset)
        reset.clicked.connect(self._reset_fields)

        # Native drag-out for the plain-text fields
        self.ui.strDomainName.setDragEnabled(True)
        self.ui.strDomainPhrase.setDragEnabled(True)
        #self.ui.strMasterPass.setDragEnabled(True)
        #self.ui.strSaltedPass.setDragEnabled(True)
        # Masked/read-only fields must have a custom implementation for dragging
        self.ui.strMasterPass.installEventFilter(self)
        self.ui.strSaltedPass.installEventFilter(self)

        self._apply_truncation(self.ui.sliderCharCount.value())

    # ------------------------------------------------------------------ #

    @staticmethod
    def _set_echo(edit, shown):
        edit.setEchoMode(QLineEdit.EchoMode.Normal if shown
                         else QLineEdit.EchoMode.Password)

    def _hash_name(self):
        return self.ui.selHash.currentText().lower().replace("-", "")

    # ------------------------------------------------------------------ #

    def _update(self):
        master = self.ui.strMasterPass.text()
        domain = self.ui.strDomainName.text()
        if master and domain:
            self._full_salted = saltthepass(
                self._hash_name(), master, domain,
                self.ui.strDomainPhrase.text())
        else:
            self._full_salted = ""
        self._apply_truncation(self.ui.sliderCharCount.value())

    def _apply_truncation(self, count):
        self.ui.label_4.setText(f"{count} characters")
        self.ui.strSaltedPass.setText(self._full_salted[:count])

    def _reset_fields(self):
        for edit in (self.ui.strMasterPass, self.ui.strDomainName,
                     self.ui.strDomainPhrase):
            edit.clear()
        self.ui.sliderCharCount.setValue(20)
        self.ui.selHash.setCurrentIndex(4)

    # ------------- copy & drag for masked / read-only fields ----------- #
    # ----- (Qt Does Not want you copying/cutting passwords lol) -------- #
    def eventFilter(self, obj, event):
        if obj is self.ui.strMasterPass or obj is self.ui.strSaltedPass:
            t = event.type()

            if t == QEvent.Type.KeyPress:
                mods = event.modifiers()
                key = event.key()

                # Ctrl+C / Ctrl+Ins = copy
                if (obj.echoMode() == QLineEdit.EchoMode.Password
                        and (mods & Qt.KeyboardModifier.ControlModifier)
                        and key in (Qt.Key.Key_C, Qt.Key.Key_Insert)):
                    QApplication.clipboard().setText(
                        obj.selectedText() or obj.text())
                    return True

                # Ctrl+X / Shift+Del = cut
                if obj is self.ui.strMasterPass and (
                        (mods & Qt.KeyboardModifier.ControlModifier)
                        and key == Qt.Key.Key_X
                        or (mods & Qt.KeyboardModifier.ShiftModifier)
                        and key == Qt.Key.Key_Delete):
                    QApplication.clipboard().setText(
                        obj.selectedText() or obj.text())
                    obj.clear()
                    return True

            elif t == QEvent.Type.MouseButtonPress:
                self._drag_press_pos = None
                self._drag_text = ""
                if event.button() == Qt.MouseButton.LeftButton:
                    pos = event.position().toPoint()
                    start = obj.selectionStart()
                    end = obj.selectionEnd()
                    # once the widget handles this press it places the caret and the selection is gone
                    if start != -1 and start <= obj.cursorPositionAt(pos) <= end:
                        self._drag_press_pos = pos
                        self._drag_text = obj.selectedText()

            elif t == QEvent.Type.MouseButtonRelease:
                self._drag_press_pos = None

            elif (t == QEvent.Type.MouseMove
                    and self._drag_press_pos is not None
                    and (event.buttons() & Qt.MouseButton.LeftButton)):
                if ((event.position().toPoint() - self._drag_press_pos)
                        .manhattanLength()
                        >= QApplication.startDragDistance()):
                    self._drag_press_pos = None
                    text, self._drag_text = self._drag_text, ""
                    if text:
                        mime = QMimeData()
                        mime.setText(text)
                        drag = QDrag(obj)
                        drag.setMimeData(mime)
                        drag.exec(Qt.DropAction.CopyAction)
                        return True

        return super().eventFilter(obj, event)

def main():
    app = QApplication(sys.argv)
    dialog = SaltThePassDialog()
    dialog.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
