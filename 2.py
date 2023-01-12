#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из семи кнопок, цвета которых
соответствуют цветам радуги. При нажатии на ту или иную кнопку
в текстовое поле должен вставляться код цвета, а в метку – название
цвета. Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный,
#ff7d00 – оранжевый, #ffff00 – желтый, #00ff00 – зеленый,
#007dff – голубой, #0000ff – синий, #7d00ff – фиолетовый.
"""

from PySide2.QtWidgets import QWidget, QApplication, QLabel,\
    QPushButton, QLineEdit, QVBoxLayout
from PySide2.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2")
        self.line = QLineEdit(self)
        self.label = QLabel(self)
        self.btn1 = QPushButton(self)
        self.btn2 = QPushButton(self)
        self.btn3 = QPushButton(self)
        self.btn4 = QPushButton(self)
        self.btn5 = QPushButton(self)
        self.btn6 = QPushButton(self)
        self.btn7 = QPushButton(self)
        self.initializeUI()

    def initializeUI(self):
        self.label.setAlignment(Qt.AlignHCenter)
        self.line.setAlignment(Qt.AlignHCenter)

        self.btn1.setStyleSheet("background-color: #ff0000;")
        self.btn1.clicked.connect(self.bt1)
        self.btn2.setStyleSheet("background-color: #ff7d00;")
        self.btn2.clicked.connect(self.bt2)
        self.btn3.setStyleSheet("background-color: #ffff00;")
        self.btn3.clicked.connect(self.bt3)
        self.btn4.setStyleSheet("background-color: #00ff00;")
        self.btn4.clicked.connect(self.bt4)
        self.btn5.setStyleSheet("background-color: #007dff;")
        self.btn5.clicked.connect(self.bt5)
        self.btn6.setStyleSheet("background-color: #0000ff;")
        self.btn6.clicked.connect(self.bt6)
        self.btn7.setStyleSheet("background-color: #7d00ff;")
        self.btn7.clicked.connect(self.bt7)

    def vertical_box(self):
        box = QVBoxLayout()
        box.addWidget(self.label)
        box.addWidget(self.line)
        box.addWidget(self.btn1)
        box.addWidget(self.btn2)
        box.addWidget(self.btn3)
        box.addWidget(self.btn4)
        box.addWidget(self.btn5)
        box.addWidget(self.btn6)
        box.addWidget(self.btn7)
        self.setLayout(box)

    def bt1(self):
        self.label.setText("Красный")
        self.line.setText("#ff0000")

    def bt2(self):
        self.label.setText("Оранжевый")
        self.line.setText("#ff7d00")

    def bt3(self):
        self.label.setText("Желтый")
        self.line.setText("#ffff00")

    def bt4(self):
        self.label.setText("Зеленый")
        self.line.setText("#00ff00")

    def bt5(self):
        self.label.setText("Голубой")
        self.line.setText("#007dff")

    def bt6(self):
        self.label.setText("Синий")
        self.line.setText("#0000ff")

    def bt7(self):
        self.label.setText("Фиолетовый")
        self.line.setText("#7d00ff")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.vertical_box()
    window.show()
    sys.exit(app.exec_())
