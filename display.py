#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import sys
import litera
import dict
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

UI_PATH = 'ui/interface.ui'
DMOD_PATH = 'ui/dmod.ui'

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

        self.init()

        # Events
        self.cht_input.textChanged[str].connect(self.find_dup)
        self.chs_input.textChanged[str].connect(self.find_dup)
        self.add_button.clicked.connect(self.add_word)
        self.clear_button.clicked.connect(self.clear)
        self.reset_button.clicked.connect(self.reset)
        self.apply_button.clicked.connect(self.apply)

        self.show()

    def init(self):
        self.dmod_temp = ""
        self.dmod_browser.setText(self.dmod_temp)

    def find_dup(self, word: str):
        is_found_cht = litera.trie_cht.find_word(word)
        is_found_chs = litera.trie_chs.find_word(word)

        if is_found_cht or is_found_chs:
            cht, chs, pinyin = litera.ch_pair(word)
            self.cht_input.setText(cht)
            self.chs_input.setText(chs)
            self.pinyin_input.setText(pinyin)
            return True

        return False

    def add_word(self):
        if self.find_dup(self.cht_input.text()) or self.find_dup(self.chs_input.text()):
            print("Word existed")
            return

        cht = self.cht_input.text()
        chs = self.chs_input.text()
        pinyin = self.pinyin_input.text()

        line = cht + '\t' + chs + '\t' + pinyin
        self.dmod_temp += line + '\n'
        self.dmod_browser.setText(self.dmod_temp)

    def delete_word(self):
        if not (self.find_dup(self.cht_input.text()) or self.find_dup(self.chs_input.text())):
            print("Word not existed")
            return

    def clear(self):
        self.cht_input.setText("")
        self.chs_input.setText("")
        self.pinyin_input.setText("")

    def reset(self):
        self.clear()
        self.init()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def apply(self):
        dict.dmod(mode='a', data=self.dmod_temp)
        self.reset()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())
