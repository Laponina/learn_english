import sys
import os
import json
import random
import time
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

with open(location('data/elementary words')) as f:
    words = json.load(f)


class Translate_RU(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/torussian.ui', self)
        self.step = 0
        self.col_false = QColor(255, 0, 0)
        self.col_true = QColor(0, 255, 0)
        self.initui()

    def initui(self):
        self.english_word.append(words[kol_done]['english_word'])
        self.remark.setText(words[kol_done]['remark'])
        self.partProcess.setText('%s / %s' % (str(kol_done + 1), '10'))
        self.buttonANSWER.clicked.connect(button_answer)
        self.buttonNEXT.clicked.connect(button_next)
        self.process()

    def process(self):
        if self.step > 10:
            pass
        self.step += 1
        self.progress.setValue(self.step)


def button_answer():
    # widget.russian_word.setText("Test")
    # widget.russian_word.setTextColor(QColor(255, 0, 0))


    global kol_done, kol_true
    if widget.russian_word.toPlainText() == words[kol_done]['russian_word']:
        print('YES')
        widget.russian_word.toPlainText("Test")
        widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col_true.name())
        time.sleep(2)
        kol_true += 1
    else:
        print('NO')
        widget.russian_word.setTextColor(widget.col_false)
        widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col_false.name())
        widget.error.setText(words[kol_done]['russian_word'])
        time.sleep(2)
        widget.buttonANSWER.setText('Next')
    kol_done += 1
    widget.english_word.clear()
    widget.russian_word.clear()


def button_next():
    global kol_done
    widget.error.setText(words[kol_done]['russian_word'])
    time.sleep(2)
    widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col_false.name())
    kol_done += 1
    widget.english_word.clear()
    widget.russian_word.clear()


def line_treatment(str):
    # убрать лишние пробелы из введенной строки
    pass


# def make_words(words):
#     когда будет словарь. Собирает список слов для тренировки
#     while len(words) < 10:
#         el = random.randint(0, len(data))
#         if el not in words:
#             words.append(el)
#
# words = []
kol_true = 0
kol_done = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Translate_RU()
    widget.show()
    sys.exit(app.exec_())
