#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите простейший калькулятор, состоящий из двух
текстовых полей, куда пользователь вводит числа, и четырех кнопок
"+", "-", "*", "/". Результат вычисления должен отображаться в метке.
Если арифметическое действие выполнить невозможно (например, если были
введены буквы, а не числа), то в метке должно появляться слово "ошибка"
"""

from PySide2.QtWidgets import QWidget, QApplication, QLabel,\
    QPushButton, QLineEdit, QVBoxLayout
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1")
        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        self.btn1 = QPushButton("+", self)
        self.btn2 = QPushButton("-", self)
        self.btn3 = QPushButton("*", self)
        self.btn4 = QPushButton("/", self)
        self.label = QLabel()
        self.initializeUI()

    def initializeUI(self):
        box = QVBoxLayout()
        box.addWidget(self.line1)
        box.addWidget(self.line2)
        box.addWidget(self.btn1)
        box.addWidget(self.btn2)
        box.addWidget(self.btn3)
        box.addWidget(self.btn4)
        box.addWidget(self.label)
        self.setLayout(box)

        self.btn1.clicked.connect(self.add)
        self.btn2.clicked.connect(self.sub)
        self.btn3.clicked.connect(self.mul)
        self.btn4.clicked.connect(self.div)

    def add(self):
        try:
            res = float(self.line1.text()) + float(self.line1.text())
            self.label.setText(str(res))
        except ValueError:
            self.label.setText("Ошибка")

    def sub(self):
        try:
            res = float(self.line1.text()) - float(self.line2.text())
            self.label.setText(str(res))
        except ValueError:
            self.label.setText("Ошибка")

    def mul(self):
        try:
            res = float(self.line1.text()) * float(self.line2.text())
            self.label.setText(str(res))
        except ValueError:
            self.label.setText("Ошибка")

    def div(self):
        if float(self.line2.text()) != 0:
            try:
                res = float(self.line1.text()) / float(self.line2.text())
                self.label.setText(str(res))
            except ValueError:
                self.label.setText("Ошибка")
        else:
            self.label.setText("Деление на ноль!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
