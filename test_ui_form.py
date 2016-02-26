import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


# with open('elementary words.json') as f: // я забыла, как это работает
#     words = f.read()
words = [
    {
        "english_word": "do",
        "russian_word": "делать",
        "remark": "You can do it!",
        "rus_remark": "Ты можешь сделать это!"
    },
    {
        "english_word": "play",
        "russian_word": "играть",
        "remark": "She plays the piano",
        "rus_remark": "Она играет на пианино"
    }
]


class Translate_RU(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/torussian.ui', self)
        self.initui()

    def initui(self):
        self.english_word.append(words[kol_done]['english_word'])
        self.remark.setText(words[kol_done]['remark'])
        self.buttonANSWER.clicked.connect(on_buttonANSWER)


def on_buttonANSWER(kol_true):
    # QLineEdit.clear()
    # print(widget.lineEdit.text())
    # widget.lineEdit_2.clear()
    # widget.lineEdit_2.insert(widget.lineEdit.text())
    if widget.russian_word.toPlainText() == words[kol_done]['russian_word']:
        print('YES')
        kol_true += 1
    else:
        print('NO')

    kol_done += 1


def on_button_next(kol_done):
    kol_done += 1


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
