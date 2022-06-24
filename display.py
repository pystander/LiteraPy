#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import sys
import litera
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

UI_PATH = 'interface.ui'
DMOD_PATH = 'dmod.ui'

class UI(QMainWindow):
    def __init__(self):
        # Load .ui file and elements
        super(UI, self).__init__()
        uic.loadUi(UI_PATH, self)

        self.lang = 'zh-CHT'

        # Events
        self.search_input.textChanged[str].connect(self.input_search)
        self.lang_chs.stateChanged.connect(self.lang_state)
        self.dmod_action.triggered.connect(self.dmod_open)

        self.show()

    def input_search(self, word: str):
        result = litera.search(word, lang=self.lang)
        adresult = litera.adsearch(word, lang=self.lang)

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

    def dmod_open(self):
        self.dmod = DM()
        self.dmod.show()

class DM(QMainWindow):
    def __init__(self):
        # Load .ui file and elements
        super(DM, self).__init__()
        uic.loadUi(DMOD_PATH, self)

        # Events
        self.cht_input.textChanged[str].connect(self.find_dup)
        self.chs_input.textChanged[str].connect(self.find_dup)

        self.show()

    def find_dup(self, word: str):
        is_found = litera.trie_cht.find_word(word)

        if is_found:
            cht, chs = litera.ch_pair(word)
            self.cht_input.setText(cht)
            self.chs_input.setText(chs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())
