#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, qApp, QMessageBox, QApplication, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        test = QPushButton("Стартовый тест")
        trening = QPushButton('Тренировка')
        dictionary = QPushButton('Словарь')
        out = QPushButton('Выход')


        grid = QGridLayout()

        grid.addWidget(test, 1, 1)
        grid.addWidget(trening, 2, 1)
        grid.addWidget(dictionary, 3, 1)
        grid.addWidget(out, 4, 1)

        self.setLayout(grid)

        #only for QMainWindow
        # exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(qApp.quit)
        #
        # self.statusBar()
        #
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAction)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Menubar')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:  # по нажатию на Esc завершается приложение
            self.close()

    def button_click(self):

        sender = self.sender()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
