from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
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
        model = QStandardItemModel([word["english_word"] for word in words])
        self.list_word.setModel(model)
        self.list_word.setEditTriggers(0)
        self.list_word.viewMode(words)
        # model = QStandardItemModel(3, 4)
        # for row in range(0, 3):
        #     for column in range(0, 3):
        #         item = QStandardItem("({0}, {1})".format(row, column))
        #         model.setItem(row, column, item)
        # self.list_word.setModel(model)
        self.list_word.resizeColumnsToContents()
        self.list_word.resizeRowsToContents()
        self.list_word.setHorizontalHeaderLabels([
                "english_word", "russian_word", "remark", "rus_remark"
                ])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = dictionary_form()
    widget.show()
    sys.exit(app.exec_())
