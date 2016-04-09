from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        loadUi('qt_ui/main.ui', self)
        self.initui()

    def initui(self):
        self.torussian.clicked.connect(self.btn_russian)
        self.toenglish.clicked.connect(self.btn_english)
        self.customization.clicked.connect(self.btn_customization)

    def btn_russian(self):
        pass

    def btn_english(self):
        pass

    def btn_customization(self):
        pass


class Customization():
    def __init__(self):
        super().__init__()
        loadUi('qt_ui/dictionary.ui', self)
        self.initui()

    def initui(self):
        pass
