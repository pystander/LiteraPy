#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

# Import libraries
import litera
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

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
            self.search_browser.setText('\n'.join(result))
        else:
            self.search_browser.setText("")

        if adresult != None:
            self.adsearch_browser.setText('\n'.join(adresult))
        else:
            self.adsearch_browser.setText("")

def main():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
