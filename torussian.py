import sys
import os
import json
import random
import time
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

# KOL_WORDS = 2  # временно, заменить потом на 10

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)


class Translate_RU(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/torussian.ui', self)
        self.col_false = QColor(255, 0, 0)
        self.col_true = QColor(0, 255, 0)
        self.col = QColor(0, 0, 0)
        self.num_done = 0
        self.num_true = 0
        self.words = None
        self.load_data()
        self.initui()

    def load_data(self):
        with open(location('data/elementary words')) as f:
            self.words = json.load(f)

    def initui(self):
        self.english_word.setText(self.words[self.num_done]['english_word'])  # append
        self.remark.setText(self.words[self.num_done]['remark'])
        self.buttonANSWER.setText('ANSWER')
        self.buttonANSWER.autoDefault()
        self.buttonANSWER.clicked.connect(self.button_answer)
        self.progress.setRange(1, len(self.words))
        self.update_progress()

    def update_progress(self):
        self.progress.setValue(self.num_done + 1)
        self.partProcess.setText('%s / %s' % (str(self.num_done + 1), str(len(self.words))))

    def button_answer(self):
        print('button ANSWER clicked')
        self.russian_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())
        if self.russian_word.toPlainText() == self.words[self.num_done]['russian_word']:  # если слово введено правильно
            print('YES')
            self.russian_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_true.name())  # меняю цвет текста на зеленый
            self.num_true += 1
        else:
            print('NO')
            self.error.setText(self.words[self.num_done]['russian_word'])  # выводим правильный ответ
            self.russian_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_false.name())  # меняю цвет текста на красный
        self.buttonANSWER.setText('Next')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.answ_next)
        self.buttonANSWER.clicked.disconnect(self.button_answer)

    def answ_next(self):
        print('button NEXT clicked')
        self.num_done += 1
        self.russian_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())  # возвращаю черный цвет текста
        self.buttonANSWER.setText('ANSWER')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.button_answer)
        self.buttonANSWER.clicked.disconnect(self.answ_next)
        print(self.num_done)
        if self.num_done < len(self.words):
            self.english_word.clear()
            self.russian_word.clear()
            self.error.clear()
            self.english_word.setText(self.words[self.num_done]['english_word'])  # append
            self.remark.setText(self.words[self.num_done]['remark'])
        else:
            self.showChildWindow()
        self.update_progress()

    def showChildWindow(self):
        self.childForm, self.Results = results.init()
        results.show()


class Results(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/results.ui', self)
        self.setWindowModality(Qt.WindowModal)
        self.setupUi()

    def setupUi(self):
        self.percentage.setText('сделано верно %s из %s' % (str(widget.num_true), str(widget.num_done)))
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.show()

    def init(parentwindow):
        SmallWindow = QDialog(parentwindow)
        results = Results()
        results.setupUi()
        return results, SmallWindow


def line_treatment(ru_str):
    # TODO: убрать лишние пробелы из введенной строки (потом)
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Translate_RU()
    results = Results()
    widget.show()
    sys.exit(app.exec_())
