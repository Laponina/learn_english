import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QLineEdit




def on_buttonANSWER(kol_true):
    # QLineEdit.clear()
    # print(widget.lineEdit.text())
    # widget.lineEdit_2.clear()
    # widget.lineEdit_2.insert(widget.lineEdit.text())
    if widget.russian_word.toPlainText() == word['russian_word']:
        print('YES')
        kol_true += 1
    else:
        print('NO')


# widget.Dialog.connect()

word = {'english_word': 'do', 'russian_word': 'делать', 'remark': 'You can do it!'}
app = QApplication(sys.argv)
widget = loadUi('qt_ui/demo_form.ui')

# widget.pushOK.clicked.connect(on_buttonOK)
widget.english_word.append(word['english_word'])
widget.remark.setText(word['remark'])

kol_true = 0
widget.buttonANSWER.clicked.connect(on_buttonANSWER)
print(kol_true)

widget.show()
sys.exit(app.exec_())
