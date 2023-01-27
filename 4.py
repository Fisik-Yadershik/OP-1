#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу, состоящую из однострочного и многострочного
текстовых полей и двух кнопок "Открыть" и "Сохранить".  При клике
на первую должен открываться на чтение файл, чье имя указано в поле
класса Entry, а содержимое файла должно загружаться в поле типа Text.
При клике на вторую кнопку текст, введенный пользователем в экземпляр
Text, должен сохраняться в файле под именем, которое пользователь указал
в однострочном текстовом поле. Файлы будут читаться и записываться в том
же каталоге, что и файл скрипта, если указывать имена файлов без адреса.
"""


import sys
from PySide2.QtWidgets import QApplication, QFileDialog, QWidget, QVBoxLayout,\
    QTextEdit, QHBoxLayout, QPushButton, QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("4")
        self.line = QLineEdit(self)
        self.label = QTextEdit(self)
        self.btn1 = QPushButton("Открыть файл", self)
        self.btn2 = QPushButton("Сохранить файл", self)
        self.displayWidgets()

    def displayWidgets(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addLayout(hbox)
        self.btn1.clicked.connect(self.open)
        self.btn2.clicked.connect(self.save)
        hbox.addWidget(self.line)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def open(self):
        if self.line.text() == '':
            file_name = QFileDialog.getOpenFileName(self)
            with open(file_name[0], 'r', encoding="utf-8") as f:
                location = f.read()
            self.label.setText(location)
        else:
            try:
                file_name = self.line.text()
                with open(file_name, 'r', encoding="utf-8") as f:
                    location = f.read()
                self.label.setText(location)
            except ValueError:
                self.label.setText("Файл не найден")

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            'Текстовый файл',
            '',
            '(*.txt)'
        )
        if filename:
            text = self.label.toPlainText()
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(text)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
