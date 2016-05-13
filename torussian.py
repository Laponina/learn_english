import sys
import os
import json
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QComboBox
from PyQt5.QtGui import QColor, QStandardItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)


class Choose_themeRU(QDialog):
    def __init__(self, parent):
        super().__init__()
        loadUi('qt_ui/question.ui', self)
        self.parent = parent
        self.words = self.parent.words
        self.themes = self.parent.themes
        self.selectedtheme = None
        self.initui()
        self.show()

    def initui(self):
        for theme in self.themes:
            self.box_themes.addItem(theme)
        self.selectedtheme = self.box_themes.currentText()
        print(self.selectedtheme)
        self.start_test.clicked.connect(self.complete)

    def complete(self):
        print("complete")
        self.to_russian = Translate_RU(self, self.selectedtheme)
        self.close()


class Translate_RU(QDialog):
    def __init__(self, parent, theme):
        super().__init__()
        loadUi('qt_ui/torussian.ui', self)
        self.parent = parent
        self.theme = theme
        self.col_false = QColor(255, 0, 0)
        self.col_true = QColor(0, 255, 0)
        self.col = QColor(0, 0, 0)
        self.num_done = 0
        self.num_true = 0
        self.wrong_words = []
        self.themes = self.parent.themes
        self.words = []
        self.all_words = self.parent.words
        self.addwords()
        self.initui()
        self.show()

    def addwords(self):
        for word in self.all_words:
            if word["theme"] == self.theme:
                self.words.append(word)

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
        if line_treatment(self.russian_word.toPlainText()) == self.words[self.num_done][
            'russian_word']:  # если слово введено правильно
            print('YES')
            self.russian_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_true.name())  # меняю цвет текста на зеленый
            self.num_true += 1
            self.words[self.num_done]["rating"] -= 10
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
        self.results = Results(self)  # вывод результатов - новое окно results
        self.close()

    def closeEvent(self, e):
        self.main = MainWindow()
        self.close()


class Choose_themeEN(QDialog):
    def __init__(self, parent):
        super().__init__()
        loadUi('qt_ui/question.ui', self)
        self.parent = parent
        self.words = self.parent.words
        self.themes = self.parent.themes
        self.selectedtheme = None
        self.initui()
        self.show()

    def initui(self):
        for theme in self.themes:
            self.box_themes.addItem(theme)
        self.selectedtheme = self.box_themes.currentText()
        print(self.selectedtheme)
        self.start_test.clicked.connect(self.complete)

    def complete(self):
        print("complete")
        self.to_english = Translate_EN(self, self.selectedtheme)
        self.close()


class Translate_EN(QDialog):
    def __init__(self, parent, theme):
        super().__init__()

        loadUi('qt_ui/toenglish.ui', self)
        self.parent = parent
        self.theme = theme
        self.themes = self.parent.themes
        self.col_false = QColor(255, 0, 0)
        self.col_true = QColor(0, 255, 0)
        self.col = QColor(0, 0, 0)
        self.num_done = 0
        self.num_true = 0
        self.all_words = self.parent.words
        self.words = []
        self.wrong_words = []
        self.addwords()
        self.initui()
        self.show()

    def addwords(self):
        for word in self.all_words:
            if word["theme"] == self.theme:
                self.words.append(word)

    def initui(self):
        self.russian_word.setText(self.words[self.num_done]['russian_word'])  # append
        self.remark.setText(self.words[self.num_done]['rus_remark'])
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
        self.english_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())
        if line_treatment(self.english_word.toPlainText()) == self.words[self.num_done][
            'english_word']:  # если слово введено правильно
            print('YES')
            self.english_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_true.name())  # меняю цвет текста на зеленый
            self.num_true += 1
            self.words[self.num_done]["rating"] -= 10
        else:
            print('NO')
            self.wrong_words.append(self.words[self.num_done])
            self.error.setText(self.words[self.num_done]['english_word'])  # выводим правильный ответ
            self.english_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_false.name())  # меняю цвет текста на красный
        self.buttonANSWER.setText('Next')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.answ_next)
        self.buttonANSWER.clicked.disconnect(self.button_answer)

    def answ_next(self):
        print('button NEXT clicked')
        self.num_done += 1
        self.english_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())  # возвращаю черный цвет текста
        self.buttonANSWER.setText('ANSWER')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.button_answer)
        self.buttonANSWER.clicked.disconnect(self.answ_next)
        print(self.num_done)
        if self.num_done < len(self.words):
            self.english_word.clear()
            self.russian_word.clear()
            self.error.clear()
            self.russian_word.setText(self.words[self.num_done]['russian_word'])  # append
            self.remark.setText(self.words[self.num_done]['rus_remark'])

        self.update_progress()
        if self.num_done >= len(self.words):
            self.complete()

    def complete(self):
        print("complete")
        # FIXME: почему-то окно с результатми под главным окном
        self.results = Results(self)
        self.close()

    def closeEvent(self, e):
        self.main = MainWindow()
        self.close()


class Results(QDialog):
    def __init__(self, parent):
        super().__init__()

        loadUi('qt_ui/results.ui', self)
        self.parent = parent
        self.wrong_words = self.parent.wrong_words
        self.column = 2
        self.row = 0
        self.width = 341 - 2
        self.height = 201 - 2
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setWindowModality(Qt.WindowModal)
        self.percentage.setText('сделано верно %s из %s' % (str(self.parent.num_true), str(self.parent.num_done)))
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.listwords.setColumnCount(2)
        self.listwords.setRowCount(len(self.wrong_words))
        self.listwords.setColumnWidth(1, self.width / 2)  # изменила ширину столбцов
        self.listwords.setColumnWidth(0, self.width / 2)
        self.listwords.verticalHeader().hide()
        self.listwords.horizontalHeader().hide()
        for num in range(len(self.wrong_words)):
            self.listwords.setColumnWidth(num, self.width / self.column)  # изменила ширину столбцов
            self.listwords.setRowHeight(num, self.height / len(self.wrong_words))
        # self.listwords.setItem(1, 1, QTableWidgetItem("Hello"))
        for word in self.wrong_words:
            self.listwords.setItem(self.row, 0, QTableWidgetItem(word['english_word']))
            self.listwords.setItem(self.row, 1, QTableWidgetItem(word['russian_word']))
            self.row += 1

    def closeEvent(self, e):
        self.main = MainWindow()
        self.close()


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/main.ui', self)
        self.initui()
        self.words = None
        self.themes = None
        self.load_data()
        self.show()

    def initui(self):
        self.torussian.clicked.connect(self.btn_russian)
        self.toenglish.clicked.connect(self.btn_english)
        self.customization.clicked.connect(self.btn_customization)
        self.toexit.clicked.connect(self.close)
        self.start_test.clicked.connect(self.btn_test)

    def load_data(self):
        with open(location('data/elementary words')) as f:
            self.words = json.load(f)

        with open(location('data/themes')) as f:
            self.themes = json.load(f)

    def btn_russian(self):
        self.choose_theme = Choose_themeRU(self)
        self.close()

    def btn_english(self):
        self.choose_theme = Choose_themeEN(self)
        self.close()

    def btn_customization(self):
        self.dictionary = Customization(self)
        self.close()

    def btn_test(self):
        self.starttesing = StartTest(self)
        self.close()


class StartTest(QDialog):
    def __init__(self, parent):
        super().__init__()

        loadUi('qt_ui/test.ui', self)
        self.parent = parent
        self.all_words = self.parent.words
        self.words = None
        self.wrong_words = []
        self.num_done = 0  # количество сделанных
        self.num_true = 0  # количество сделанных правильно
        self.col_false = QColor(255, 0, 0)
        self.col_true = QColor(0, 255, 0)
        self.col = QColor(0, 0, 0)
        self.lan_remark = None  # примечание на нужном языке
        self.lan_translate = None  # слово на нужном языке
        self.lan_word = None  # слово , которое нужно перевести, на нужном языке
        self.show()
        self.choose_words()
        self.initUi()

    def choose_words(self):
        self.words = self.all_words  # временно

    def initUi(self):
        if self.num_done % 2 == 0:
            self.lan_translate = "english_word"
            self.lan_word = "russian_word"
            self.lan_remark = "rus_remark"
        else:
            self.lan_word = "english_word"
            self.lan_language = "russian_word"
            self.lan_remark = "remark"
        self.word.setText(self.words[self.num_done]['russian_word'])  # append
        self.remark.setText(self.words[self.num_done]['rus_remark'])
        self.buttonANSWER.setText('ANSWER')
        self.buttonANSWER.autoDefault()
        self.buttonANSWER.clicked.connect(self.button_answer)
        self.buttonSTOP.clicked.connect(self.button_stop)
        self.progress.setRange(1, len(self.words))
        self.update_progress()

    def button_answer(self):
        print('button ANSWER clicked')
        if self.num_done % 2 == 0:
            self.lan_translate = "english_word"
            self.lan_word = "russian_word"
            self.lan_remark = "rus_remark"
        else:
            self.lan_word = "english_word"
            self.lan_translate = "russian_word"
            self.lan_remark = "remark"
        self.translated_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())

        print(self.lan_translate)
        print(self.lan_word)
        if line_treatment(self.translated_word.toPlainText()) == self.words[self.num_done][self.lan_translate]:
            # если слово введено правильно
            print('YES')
            self.translated_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_true.name())  # меняю цвет текста на зеленый
            self.num_true += 1
            self.words[self.num_done]["rating"] -= 10
        else:
            print('NO')
            self.wrong_words.append(self.words[self.num_done])
            self.error.setText(self.words[self.num_done][self.lan_translate])  # выводим правильный ответ
            self.translated_word.setStyleSheet(
                "QTextEdit { color: %s }" % self.col_false.name())  # меняю цвет текста на красный
        self.buttonANSWER.setText('Next')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.answ_next)
        self.buttonANSWER.clicked.disconnect(self.button_answer)

    def answ_next(self):
        print('button NEXT clicked')
        self.num_done += 1
        if self.num_done % 2 == 0:
            self.lan_translate = "english_word"
            self.lan_word = "russian_word"
            self.lan_remark = "rus_remark"
        else:
            self.lan_word = "english_word"
            self.lan_translate = "russian_word"
            self.lan_remark = "remark"

        self.translated_word.setStyleSheet("QTextEdit { color: %s }" % self.col.name())  # возвращаю черный цвет текста
        self.buttonANSWER.setText('ANSWER')  # меняю название кнопки
        self.buttonANSWER.clicked.connect(self.button_answer)
        self.buttonANSWER.clicked.disconnect(self.answ_next)
        if self.num_done < len(self.words):
            self.translated_word.clear()
            self.word.clear()
            self.error.clear()
            self.word.setText(self.words[self.num_done][self.lan_word])  # append
            self.remark.setText(self.words[self.num_done][self.lan_remark])

        self.update_progress()

        if self.num_done >= len(self.words):
            self.complete()

    def button_stop(self):
        # TODO: сделать воспрос: вы действительно хотите закночить тест преждевремено
        self.question_ex = Exit_question(self)

    def update_progress(self):
        self.progress.setValue(self.num_done + 1)
        self.partProcess.setText('%s / %s' % (str(self.num_done + 1), str(len(self.words))))

    def complete(self):
        self.results = Results(self)
        self.close()

    def closeEvent(self, e):
        self.main = MainWindow()
        self.close()


class Exit_question(QDialog):
    def __init__(self, parent):
        super().__init__()
        loadUi('qt_ui/exit_question.ui', self)
        self._parent = parent
        self.show()
        self.initui()

    def initui(self):
        self.bttnYES.clicked.connect(self.bttn_yes)
        self.bttnNO.clicked.connect(self.bttn_no)

    def bttn_yes(self):
        self.close()
        self._parent.close()

    def bttn_no(self):
        self.close()


class Customization(QDialog):
    def __init__(self, parent):
        super().__init__()
        loadUi('qt_ui/dictionary.ui', self)
        self.parent = parent
        self.words = self.parent.words
        self.themes = self.parent.themes
        self.column = 5
        self.row = len(self.words)
        self.width = 490
        self.hight = 270
        self.k_row = 0
        self.initui()
        self.show()

    def initui(self):
        self.list_words.setColumnCount(5)
        self.list_words.setRowCount(len(self.words))
        self.list_words.verticalHeader().hide()
        self.list_words.horizontalHeader().hide()

        for num in range(self.column):
            self.list_words.setColumnWidth(num, self.width / self.column)  # изменила ширину столбцов
            self.list_words.setRowHeight(num, self.hight / self.row)

        for word in self.words:
            self.list_words.setItem(self.k_row, 0, QTableWidgetItem(word['english_word']))
            self.list_words.setItem(self.k_row, 1, QTableWidgetItem(word['russian_word']))
            self.list_words.setItem(self.k_row, 2, QTableWidgetItem(word['remark']))
            self.list_words.setItem(self.k_row, 3, QTableWidgetItem(word['rus_remark']))
            self.list_words.setItem(self.k_row, 4, QTableWidgetItem(word['theme']))
            self.k_row += 1
        self.add_words.clicked.connect(self.btn_add)
        self.toremove.clicked.connect(self.btn_remove)
        self.tosave.clicked.connect(self.btn_save)
        self.tocancel.clicked.connect(self.btn_cancel)
        self.toback.clicked.connect(self.close)

    def btn_remove(self):
        index = self.list_words.row(self.list_words.currentItem())
        print(index)
        self.words.pop(index)
        self.list_words.removeRow(index)
        for num in range(self.column):
            self.list_words.setRowHeight(num, self.hight / len(self.words))
        print('удалено')

    def btn_save(self):
        self.words = []
        el = 0
        while el < self.list_words.rowCount():
            en_word = self.list_words.item(el, 0).text()
            ru_word = self.list_words.item(el, 1).text()
            remark = self.list_words.item(el, 2).text()
            ru_remark = self.list_words.item(el, 3).text()
            theme = self.list_words.item(el, 4).text()
            new_word = {
                "russian_word": ru_word,
                "rus_remark": ru_remark,
                "remark": remark,
                "english_word": en_word,
                "rating": 100,
                "theme": theme
            }
            el += 1
            self.words.append(new_word)
        self.rewrite_file()

    def rewrite_file(self):
        with open(location('data/elementary words'), 'w') as f:
            json.dump(self.words, f, ensure_ascii=False)

    def load_data(self):
        with open(location('data/elementary words')) as f:
            self.words = json.load(f)

    def btn_cancel(self):
        self.load_data()
        self.list_words.clear()
        self.k_row = 0
        self.load_data()
        self.list_words.setRowCount(len(self.words))
        # TO DO: сделать автоперенос последней строки

        for word in self.words:
            self.list_words.setItem(self.k_row, 0, QTableWidgetItem(word['english_word']))
            self.list_words.setItem(self.k_row, 1, QTableWidgetItem(word['russian_word']))
            self.list_words.setItem(self.k_row, 2, QTableWidgetItem(word['remark']))
            self.list_words.setItem(self.k_row, 3, QTableWidgetItem(word['rus_remark']))
            self.list_words.setItem(self.k_row, 4, QTableWidgetItem(word['theme']))
            self.k_row += 1

    def load_data(self):
        with open(location('data/elementary words')) as f:
            self.words = json.load(f)

    def btn_add(self):
        self.list_words.setRowCount(self.list_words.rowCount() + 1)

    def closeEvent(self, e):
        self.main = MainWindow()
        self.close()


def line_treatment(str):
    str = ' '.join(str.split())
    return str


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
