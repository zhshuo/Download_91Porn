#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_Form
import sys
from Download_91 import MyThread_Download_91


import requests
import threading
import os 
import time
import random


class Main_window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.init_func)
        self.pushButton_random.clicked.connect(self.random_num)
        self.pushButton_random_2.clicked.connect(self.random_count)
        self.toolButton_src.clicked.connect(self.open_src)

    def init_func(self):
        number=int(self.lineEdit_num.text())
        if self.lineEdit_count.text()=="":
            number_end=number+1
        else:
            number_end=number+int(self.lineEdit_count.text())
        if self.lineEdit_src.text()=="":
            client_src="D://资源//"
        else:
            client_src=self.lineEdit_src.text()

        while True:
            time.sleep(0.1)
            t=MyThread_Download_91(str(number),client_src)
            t.setDaemon(True)
            t.start()
            number=number+1
            print(number)
            if number==number_end:
                break

    def random_num(self):
        self.lineEdit_num.setText(str(random.randint(444000,444700)))

    def random_count(self):
        self.lineEdit_count.setText(str(random.randint(1, 50)))

    
    def open_src(self):
        file_path = QFileDialog.getExistingDirectory(self, "请选择检查路径", "D://")
        self.lineEdit_src.setText(file_path)


# 运行程序
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    app.exec()

