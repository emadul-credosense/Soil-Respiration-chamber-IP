from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(700, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SplashScreen.sizePolicy().hasHeightForWidth())
        SplashScreen.setSizePolicy(sizePolicy)
        SplashScreen.setMinimumSize(QtCore.QSize(700, 400))
        SplashScreen.setMaximumSize(QtCore.QSize(700, 400))
        SplashScreen.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
                                           "    color:rgb(46,52,64);\n"
                                           "    background-color: rgb(46,52,64);\n"
                                           "}\n"
                                           "\n"
                                           "QLabel{\n"
                                           "    color: rgb(216,222,233);\n"
                                           "}\n"
                                           "\n"
                                           "QProgressBar{\n"
                                           "    background-color:rgb(46,52,64);\n"
                                           "    color : rgb(46,52,64);\n"
                                           "    text-align:center;\n"
                                           "    text-visibility:none;\n"
                                           "    border-style:none;\n"
                                           "}\n"
                                           "\n"
                                           "QProgressBar::Chunk{\n"
                                           "background-color: rgb(236,239,244);\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label = QtWidgets.QLabel(self.dropShadowFrame)
        self.label.setGeometry(QtCore.QRect(20, 160, 651, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 651, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.startProgressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.startProgressBar.setGeometry(QtCore.QRect(30, 300, 601, 3))
        self.startProgressBar.setMaximumSize(QtCore.QSize(16777215, 23))
        self.startProgressBar.setStyleSheet("")
        self.startProgressBar.setProperty("value", 24)
        self.startProgressBar.setObjectName("startProgressBar")
        self.label_4 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_4.setGeometry(QtCore.QRect(300, 70, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/credologo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_5.setGeometry(QtCore.QRect(550, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label.setText(_translate("SplashScreen", "Soil Respiration Chamber"))
        self.label_2.setText(_translate("SplashScreen", "Interfacing SoftWare"))
        self.label_5.setText(_translate("SplashScreen", "By CredoSense"))
