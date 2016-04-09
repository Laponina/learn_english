import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QWidget
from PyQt5.QtGui import QColor, QStandardItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

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
        self.wrong_words = []
        self.load_data()
        self.initui()
        self.show()

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
        # self.ButtonExit.clicked.connect(lambda : self.close())
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
            self.wrong_words.append(self.words[self.num_done])
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

        self.update_progress()
        if self.num_done >= len(self.words):
            self.complete()

    def complete(self):
        print("complete")
        self.results = Results(self)
        self.close()


class Results(QDialog):
    def __init__(self, parent):
        super().__init__()

        loadUi('qt_ui/results.ui', self)
        self.parent = parent
        self.wrong_words = self.parent.wrong_words
        self.row = 0
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setWindowModality(Qt.WindowModal)
        self.percentage.setText('сделано верно %s из %s' % (str(self.parent.num_true), str(self.parent.num_done)))
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.listwords.setColumnCount(2)
        self.listwords.setRowCount(4)
        self.listwords.verticalHeader().hide()
        self.listwords.horizontalHeader().hide()
        # self.listwords.setItem(1, 1, QTableWidgetItem("Hello"))
        for word in self.wrong_words:
            self.listwords.setItem(self.row, 0, QTableWidgetItem(word['english_word']))
            self.listwords.setItem(self.row, 1, QTableWidgetItem(word['russian_word']))
            self.row += 1


        # def init(parentwindow):
        #     SmallWindow = QWidget(parentwindow)
        #     form = Results()
        #     form.setupUi(SmallWindow)
        #     return form, SmallWindow

    def line_treatment(ru_str):
        # TODO: убрать лишние пробелы из введенной строки (потом)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translate_ru = Translate_RU()
    # resulte = Results()
    sys.exit(app.exec_())
