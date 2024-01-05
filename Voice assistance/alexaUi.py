


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AlexaUi(object):
    def setupUi(self, AlexaUi):
        AlexaUi.setObjectName("AlexaUi")
        AlexaUi.resize(2673, 898)
        self.centralwidget = QtWidgets.QWidget(AlexaUi)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-310, -110, 1731, 881))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/new.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 460, 701, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../new/giphy.gif"))
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 50, 151, 51))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 0, 451, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Downloads/virual assist name.gif"))
        self.label_5.setObjectName("label_5")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(144, 660, 91, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 660, 81, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 340, 331, 81))
        self.label.setText("")
        self.label.setObjectName("label")
        
        AlexaUi.setCentralWidget(self.centralwidget)
        AlexaUi.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(AlexaUi)
        QtCore.QMetaObject.connectSlotsByName(AlexaUi)

    def retranslateUi(self, AlexaUi):
        _translate = QtCore.QCoreApplication.translate
        AlexaUi.setWindowTitle(_translate("AlexaUi", "MainWindow"))
        self.pushButton.setText(_translate("AlexaUi", "Start"))
        self.pushButton_2.setText(_translate("AlexaUi", "Exit"))

    def display_spoken_text(self, text):
        self.spoken_text_label.setText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlexaUi = QtWidgets.QMainWindow()
    ui = Ui_AlexaUi()
    ui.setupUi(AlexaUi)
    AlexaUi.show()
    spoken_text = "Hello, how can I assist you?"
    ui.display_spoken_text(spoken_text)

    sys.exit(app.exec_())
   
