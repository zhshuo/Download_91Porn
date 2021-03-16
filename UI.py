from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 182)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_num = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.gridLayout.addWidget(self.lineEdit_num, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font-family: Metropolis;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"font-weight: 800;\n"
"color: #565656;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font-family: Metropolis;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"font-weight: 800;\n"
"color: #565656;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_count = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_count.setObjectName("lineEdit_count")
        self.gridLayout.addWidget(self.lineEdit_count, 3, 1, 1, 1)
        self.lineEdit_src = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_src.setObjectName("lineEdit_src")
        self.gridLayout.addWidget(self.lineEdit_src, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("font-family: Metropolis;\n"
"font-size: 18px;\n"
"line-height: 28px;\n"
"font-weight: 800;\n"
"color: #565656;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.pushButton_random = QtWidgets.QPushButton(self.frame)
        self.pushButton_random.setObjectName("pushButton_random")
        self.gridLayout.addWidget(self.pushButton_random, 1, 2, 1, 1)
        self.toolButton_src = QtWidgets.QToolButton(self.frame)
        self.toolButton_src.setObjectName("toolButton_src")
        self.gridLayout.addWidget(self.toolButton_src, 5, 2, 1, 1)
        self.pushButton_random_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_random_2.setObjectName("pushButton_random_2")
        self.gridLayout.addWidget(self.pushButton_random_2, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_start.setStyleSheet("")
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.lineEdit_num.setPlaceholderText("车牌号")
        self.lineEdit_count.setPlaceholderText("别超过50")
        self.lineEdit_src.setPlaceholderText("D://资源//")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "车牌识别系统"))
        self.label_2.setText(_translate("Form", "多来几部："))
        self.label.setText(_translate("Form", "车牌："))
        self.label_3.setText(_translate("Form", "保存路径："))
        self.pushButton_random.setText(_translate("Form", "随机"))
        self.toolButton_src.setText(_translate("Form", "..."))
        self.pushButton_random_2.setText(_translate("Form", "随机"))
        self.pushButton_start.setText(_translate("Form", "开始下载"))

