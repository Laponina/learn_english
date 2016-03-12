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
        self.col_false = QColor(255, 0, 0)
        self.col_true = QColor(0, 255, 0)
        self.col = QColor(0, 0, 0)
        self.initui()

    def initui(self):
        self.english_word.setText(words[kol_done]['english_word'])  # append
        self.remark.setText(words[kol_done]['remark'])
        self.partProcess.setText('%s / %s' % (str(kol_done + 1), '10'))
        self.buttonANSWER.setText('ANSWER')
        self.buttonANSWER.autoDefault()
        self.buttonANSWER.clicked.connect(button_answer)
        self.buttonNEXT.clicked.connect(button_next)
        self.process()

    def process(self):
        # разобраться!
        self.progress.setRange(1, 10)
        self.progress.setValue(kol_done)


def button_answer():
    global kol_done, kol_true
    if widget.russian_word.toPlainText() == words[kol_done]['russian_word']:
        print('YES')
        widget.buttonANSWER.setDisabled(True)
        widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col_true.name())
        time.sleep(2)
        kol_true += 1
    else:
        print('NO')
        widget.error.setText(words[kol_done]['russian_word'])
        widget.buttonANSWER.setDisabled(True)
        widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col_false.name())
        widget.error.setText(words[kol_done]['russian_word'])
        time.sleep(2)  # TODO: почему задержка выполняется после всех действий?
        # widget.buttonANSWER.setText('Next')
    kol_done += 1
    # widget.english_word.clear()
    # widget.russian_word.clear()
    widget.buttonANSWER.setDisabled(False)  # !
    widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col.name())


def button_next():
    global kol_done
    widget.error.setText(words[kol_done]['russian_word'])
    widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col_false.name())
    widget.buttonANSWER.setDisabled(True)  # !
    time.sleep(2)
    kol_done += 1
    # TODO: кнопка не становится неактивной, если это писать. Как исправить? (тоже самое при нажатии на кнопку "ANSWER")
    widget.buttonANSWER.setDisabled(False)
    widget.english_word.clear()
    widget.russian_word.clear()
    widget.russian_word.setStyleSheet("QTextEdit { color: %s }" % widget.col.name())


def line_treatment(ru_str):
    # TODO: убрать лишние пробелы из введенной строки (потом)
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
