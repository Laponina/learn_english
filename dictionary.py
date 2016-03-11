from PyQt5.QtWidgets import QApplication, QDialog, QListView
from PyQt5.uic import loadUi
import json
import os
import sys

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

with open(location('data/elementary words')) as f:
    words = json.load(f)


class dictionary_form(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('qt_ui/dictionary.ui', self)

    def initui(self):
        self.list_word.setModel([1, 2, 3])
        self.list_word.Movement(0)
        self.list_word.viewMode(words)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = dictionary_form()
    widget.show()
    sys.exit(app.exec_())
