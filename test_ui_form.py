import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QLineEdit


def on_buttonOK(event):
    # QLineEdit.clear()
    # print(widget.lineEdit.text())
    # widget.lineEdit_2.clear()
    # widget.lineEdit_2.insert(widget.lineEdit.text())
    pass


word = {'english_word': 'do', 'russian_word': 'делать', 'remark': 'You can do it!'}
app = QApplication(sys.argv)
widget = loadUi('qt_ui/demo_form.ui')

# widget.pushOK.clicked.connect(on_buttonOK)
widget.english_word.append(word['english_word'])
widget.remark.setText(word['remark'])

# widget.russian_word.QtGui.QTextEdit()
print(widget.russian_word.toPlainText (), '!')
widget.show()
sys.exit(app.exec_())
