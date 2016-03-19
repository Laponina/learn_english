import sys
import os
import json
import random
import time
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi

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
        self.buttonNEXT.clicked.connect(self.button_next)
        # self.progress.minimum =
        self.progress.setRange(1, len(self.words))
        self.update_progress()


    def update_progress(self):
        self.progress.setValue(self.num_done + 1)
        self.partProcess.setText('%s / %s' % (str(self.num_done + 1), str(len(self.words))))


    def button_answer(self):
        self.russian_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())
        if self.russian_word.toPlainText() == self.words[self.num_done]['russian_word']:  # если слово введено правильно
            print('YES')
            self.buttonNEXT.setDisabled(True)  # делаем кнопку неактивной
            self.russian_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_true.name())  # меняю цвет текста на зеленый
            self.num_true += 1
        else:
            print('NO')
            self.error.setText(self.words[self.num_done]['russian_word'])  # выводим правильный ответ
            self.buttonNEXT.setDisabled(True)  # делаем кнопку неактивной
            self.russian_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_false.name())  # меняю цвет текста на красный
        self.buttonANSWER.setText('Next')  # меняю название кнопки
        # widget.english_word.clear()
        # widget.russian_word.clear()
        self.buttonANSWER.clicked.connect(self.answ_next)


    def button_next(self):
        self.error.setText(self.words[self.num_done]['russian_word'])  # выводим правильный ответ
        self.russian_word.setStyleSheet(
            "QTextEdit { color: %s }" % self.col_false.name())  # меняю цвет текста на красный
        self.buttonNEXT.setDisabled(True)  # делаем кнопку неактивной
        self.buttonANSWER.setText('Next')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.answ_next)


    def answ_next(self):
        self.num_done += 1
        self.russian_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())  # возвращаю черный цвет текста
        self.buttonNEXT.setDisabled(False)  # делаем кнопку активной
        self.buttonANSWER.setText('ANSWER')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.button_answer)
        print(self.num_done)
        if self.num_done < len(self.words):
            self.english_word.clear()
            self.russian_word.clear()
            self.error.clear()
            self.english_word.setText(self.words[self.num_done]['english_word'])  # append
            self.remark.setText(self.words[self.num_done]['remark'])
        else:
            pass
        self.update_progress()
        # self.progress.value = self.num_done

class results(QDialog):
    def __init__(self):
        super(SettingsWidgets, self).__init__()




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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Translate_RU()
    widget.show()
    sys.exit(app.exec_())
