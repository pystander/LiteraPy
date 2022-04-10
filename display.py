#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import litera
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit

UI_PATH = 'interface.ui'

class UI(QMainWindow):
    def __init__(self):
        # Load .ui file and elements
        super(UI, self).__init__()
        uic.loadUi(UI_PATH, self)

        # Events
        self.input.textChanged[str].connect(self.inputSearch)

    def inputSearch(self, text):
        result = litera.search(text)
        adresult = litera.adsearch(text)

        if result != None:
            self.search_label.setText(' '.join(result[:10]))
            self.search_label.adjustSize()
        else:
            self.search_label.setText("")

        if adresult != None:
            self.adsearch_label.setText(' '.join(adresult[:10]))
            self.adsearch_label.adjustSize()
        else:
            self.adsearch_label.setText("")

def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
