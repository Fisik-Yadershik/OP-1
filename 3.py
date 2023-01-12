#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Перепишите программу из предыдущего задания так,
чтобы интерфейс выглядел по-другому.
"""

from PySide2.QtWidgets import QWidget, QApplication, QPushButton,\
    QHBoxLayout, QVBoxLayout, QLabel, QLineEdit
from PySide2.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3")
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

    def widgets(self):
        box = QVBoxLayout()
        layout = QHBoxLayout()
        box.addWidget(self.label)
        box.addWidget(self.line)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        layout.addWidget(self.btn5)
        layout.addWidget(self.btn6)
        layout.addWidget(self.btn7)
        box.addLayout(layout)
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
    window.widgets()
    window.show()
    sys.exit(app.exec_())
