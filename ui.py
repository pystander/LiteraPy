#!/usr/bin/env python3
# LiteraPy v1.0.0
# Copyright (c) 2021 pystander

import litera
import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel, QLineEdit, QWidget

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        # Create widgets
        self.search_lbl = QLabel(self)
        self.adsearch_lbl = QLabel(self)
        line = QLineEdit(self)

        # Window settings
        self.setGeometry(0, 0, 640, 480)
        self.setWindowTitle("UI")
        self.show()

        # Line position
        line.move(0, 0)
        self.search_lbl.move(0, 40)
        self.adsearch_lbl.move(0, 80)

        # Text change
        line.textChanged[str].connect(self.inputSearch)

    # Change on text
    def inputSearch(self, text):
        result = litera.search(text)
        ad_result = litera.adsearch(text)

        # Search result
        if result != None:
            self.search_lbl.setText(", ".join(result[:10]))
        else:
            self.search_lbl.setText("")

        # Adsearch result
        if ad_result != None:
            self.adsearch_lbl.setText(", ".join(ad_result[:10]))
        else:
            self.adsearch_lbl.setText("")

        self.search_lbl.adjustSize()
        self.adsearch_lbl.adjustSize()

def main():
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
