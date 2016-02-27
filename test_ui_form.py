import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from functools import partial


# with open('elementary words.json') as f: // я забыла, как это работает
#     words = f.read()
word = {
        "english_word": "do",
        "russian_word": "делать",
        "remark": "You can do it!",
        "rus_remark": "Ты можешь сделать это!"
        }


class Translate_RU(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/torussian.ui', self)
        self.initui()

    def initui(self):
        self.english_word.append(word['english_word'])
        self.remark.setText(word['remark'])
        self.buttonANSWER.clicked.connect(on_buttonANSWER, partial(on_buttonANSWER(), kol_true, kol_done))

    def progress(self):
        self.step += 1
        self.process.setValue(self.step)


def on_buttonANSWER():
    # QLineEdit.clear()
    # print(widget.lineEdit.text())
    # widget.lineEdit_2.clear()
    # widget.lineEdit_2.insert(widget.lineEdit.text())
    if widget.russian_word.toPlainText() == word['russian_word']:
        print('YES')
        kol_true += 1
    else:
        print('NO')

    kol_done += 1


def on_button_next(kol_done):
    # kol_done += 1
    pass



# widget.Dialog.connect()
# widget.english_word.append(word['english_word'])
# widget.remark.setText(word['remark'])

kol_true = 0
kol_done = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Translate_RU()

    print(kol_true)

    widget.show()
    sys.exit(app.exec_())
