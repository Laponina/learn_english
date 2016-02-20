#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 3 lesson:  расположение

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication, QPushButton, QAction, qApp, QMessageBox, QMainWindow)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        button = QPushButton("Click me")

        grid = QGridLayout()

        grid.addWidget(button, 3, 1)

        self.setLayout(grid)

        self.setGeometry(100, 100, 350, 300)
        self.setWindowTitle('Review')
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
