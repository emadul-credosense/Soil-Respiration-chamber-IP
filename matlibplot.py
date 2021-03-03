from subplotfunction import matlibplot1
from bleak import BleakClient
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Matlibplot(object):
    def __init__(self, window, address):
        super(Ui_Matlibplot, self).__init__()
        self.client = BleakClient(address)
        self.setupUi(window)

    def setupUi(self, Matlibplot):
        Matlibplot.setObjectName("Matlibplot")
        Matlibplot.resize(808, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Matlibplot.sizePolicy().hasHeightForWidth())
        Matlibplot.setSizePolicy(sizePolicy)
        Matlibplot.setMinimumSize(QtCore.QSize(800, 650))
        Matlibplot.setMaximumSize(QtCore.QSize(808, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/playstore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Matlibplot.setWindowIcon(icon)
        Matlibplot.setStyleSheet("background-color:#2E3440;\n"
"color:#D8DEE9;\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(Matlibplot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 640))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 640))
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(9, -1, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("border:0px solid white;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = matlibplot1(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("border: 1px solid white;")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(770, 80))
        self.frame.setMaximumSize(QtCore.QSize(770, 85))
        self.frame.setStyleSheet("QFrame{\n"
"border-bottom: 1px solid #404859;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 181, 14))
        self.label_10.setMinimumSize(QtCore.QSize(0, 14))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-bottom:0px solid;")
        self.label_10.setObjectName("label_10")
        self.Timer = QtWidgets.QSlider(self.frame)
        self.Timer.setGeometry(QtCore.QRect(229, 40, 321, 22))
        self.Timer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Timer.setMouseTracking(True)
        self.Timer.setTabletTracking(True)
        self.Timer.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Timer.setAcceptDrops(False)
        self.Timer.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    border-radius: 3px;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.Timer.setMinimum(1)
        self.Timer.setMaximum(10)
        self.Timer.setOrientation(QtCore.Qt.Horizontal)
        self.Timer.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.Timer.setObjectName("Timer")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(230, 20, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-bottom:0px solid white;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(540, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-bottom: 0px solid white;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(310, 0, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-bottom: 0px solid white;")
        self.label_13.setObjectName("label_13")
        self.SavedFileButton = QtWidgets.QPushButton(self.frame)
        self.SavedFileButton.setGeometry(QtCore.QRect(600, 40, 131, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SavedFileButton.setFont(font)
        self.SavedFileButton.setStyleSheet("border:1px solid  rgb(199, 199, 199);\n"
"border-radius: 4px;\n"
"padding-top: 2px;\n"
"padding-bottom:2px;\n"
"padding-left:10px;\n"
"padding-right:10px;")
        self.SavedFileButton.setObjectName("SavedFileButton")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(70, 10, 57, 24))
        self.frame_2.setStyleSheet(" background: #677590;\n"
"border-bottom:0px solid white;\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.toggleButton = QtWidgets.QSlider(self.frame_2)
        self.toggleButton.setEnabled(True)
        self.toggleButton.setGeometry(QtCore.QRect(0, 1, 54, 22))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggleButton.setMouseTracking(True)
        self.toggleButton.setToolTipDuration(0)
        self.toggleButton.setStyleSheet("QSlider::groove:horizontal {\n"
"    width: 50px;\n"
"    border-bottom: 0px solid white;\n"
"    border-radius:10px;\n"
"    height: 20px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: #677590;\n"
"    margin: 0px 0px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width:20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    background: #2E3440;\n"
"     margin: 0px 4px; \n"
"   /* expand outside the groove */\n"
"}\n"
"")
        self.toggleButton.setMaximum(1)
        self.toggleButton.setSliderPosition(0)
        self.toggleButton.setOrientation(QtCore.Qt.Horizontal)
        self.toggleButton.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.toggleButton.setObjectName("toggleButton")
        self.StopDLButton = QtWidgets.QPushButton(self.frame)
        self.StopDLButton.setGeometry(QtCore.QRect(600, 10, 131, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StopDLButton.setFont(font)
        self.StopDLButton.setStyleSheet("border:1px solid  rgb(199, 199, 199);\n"
"border-radius: 4px;\n"
"padding-top: 2px;\n"
"padding-bottom:2px;\n"
"padding-left:10px;\n"
"padding-right:10px;")
        self.StopDLButton.setObjectName("StopDLButton")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        Matlibplot.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Matlibplot)
        self.statusbar.setObjectName("statusbar")
        Matlibplot.setStatusBar(self.statusbar)

        self.retranslateUi(Matlibplot)
        QtCore.QMetaObject.connectSlotsByName(Matlibplot)

    def retranslateUi(self, Matlibplot):
        _translate = QtCore.QCoreApplication.translate
        Matlibplot.setWindowTitle(_translate("Matlibplot", "CS-RC5 Control Panel"))
        self.label_10.setText(_translate("Matlibplot", "Chamber status: Closed"))
        self.label_11.setText(_translate("Matlibplot", "1"))
        self.label_12.setText(_translate("Matlibplot", "10"))
        self.label_13.setText(_translate("Matlibplot", "Adjust data collection rate (sec)"))
        self.SavedFileButton.setText(_translate("Matlibplot", "View Saved File"))
        self.StopDLButton.setText(_translate("Matlibplot", "Stop Logging"))

