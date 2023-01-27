#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, в которой имеется несколько кнопок, индикатор которых выключен (indicatoron=0).
Если какая-нибудь кнопка включается, то в метке должна отображаться
соответствующая ей информация.
"""

from PySide2.QtWidgets import QWidget, QApplication,\
    QPushButton, QButtonGroup, QGridLayout, QLabel
from PySide2.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5")
        self.setGeometry(100, 100, 300, 50)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        self.rbutton1 = QPushButton('Кнопка1')
        self.rbutton1.setCheckable(True)
        self.rbutton2 = QPushButton('Кнопка2')
        self.rbutton2.setCheckable(True)
        self.rbutton3 = QPushButton('Кнопка3')
        self.rbutton3.setCheckable(True)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.rbutton1)
        self.button_group.addButton(self.rbutton2)
        self.button_group.addButton(self.rbutton3)
        self.button_group.buttonClicked.connect(self.rbutton_clicked)
        self.grid_layot()

    def grid_layot(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.rbutton1, 1, 0)
        grid.addWidget(self.rbutton2, 2, 0)
        grid.addWidget(self.rbutton3, 3, 0)
        grid.addWidget(self.label, 2, 2)
        self.setLayout(grid)

    def rbutton_clicked(self, button):
        self.label.setText(people[button.text()])


if __name__ == "__main__":
    people = {
        'Кнопка1': 'Действительно 1',
        'Кнопка2': 'Действительно 2',
        'Кнопка3': 'Действительно 3'
    }
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
