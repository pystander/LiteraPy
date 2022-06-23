#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import sys
import litera
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

UI_PATH = 'interface.ui'

class UI(QMainWindow):
    def __init__(self):
        # Load .ui file and elements
        super(UI, self).__init__()
        uic.loadUi(UI_PATH, self)

        self.lang = 'zh-CHT'

        # Events
        self.input.textChanged[str].connect(self.input_search)
        self.lang_chs.stateChanged.connect(self.lang_state)

    def input_search(self, text):
        result = litera.search(text, lang=self.lang)
        adresult = litera.adsearch(text, lang=self.lang)

        if result != None:
            self.search_browser.setText('\n'.join(result))
        else:
            self.search_browser.setText("")

        if adresult != None:
            self.adsearch_browser.setText('\n'.join(adresult))
        else:
            self.adsearch_browser.setText("")

    def lang_state(self, state):
        if state == QtCore.Qt.Checked:
            self.lang = 'zh-CHS'
        else:
            self.lang = 'zh-CHT'

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())
