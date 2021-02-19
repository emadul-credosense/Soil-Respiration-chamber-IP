import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from Functionality import functionality
from ScanPageFunction import ScanPage
from graphs import lineGraph
from splash import Ui_SplashScreen
from PyQt5 import QtCore

progressBarCounter = 0


# Inheriting splash.py
class SplashScreen(Ui_SplashScreen):
    def __init__(self, window):
        super(SplashScreen, self).__init__()
        # Splash progress bar time function
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progressBar)
        self.timer.start(20)
        self.window = window

    # Splash Screen Progress bar
    def progressBar(self):
        global progressBarCounter
        self.startProgressBar.setTextVisible(False)
        self.startProgressBar.setValue(progressBarCounter)
        if progressBarCounter > 100:
            self.timer.stop()
            self.showScanPage()
        progressBarCounter += 2

    # Showing splash screen on beginning
    def ShowSplash(self):
        self.splashWindow = QMainWindow()
        self.setupUi(self.splashWindow)
        self.splashWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.splashWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.splashWindow.show()
        MainWindow.hide()

    # Showing Scan page which is mainWindow
    def showScanPage(self):
        self.splashWindow.close()
        self.scan = ScanPage(self.window)
        self.scan.devicelist.clicked.connect(self.scan.getSelectedDevice)
        self.scan.connectButton.clicked.connect(self.showGraphs)
        MainWindow.show()

    # Windows Loading icon
    def waiting_window(self):
        try:
            QApplication.setOverrideCursor(Qt.WaitCursor)
        except Exception:
            pass

    def waiting_window_end(self):
        try:
            QApplication.restoreOverrideCursor()
        except Exception:
            pass

    # Showing graph page
    def showGraphs(self):
        try:
            self.feature = functionality()
            if self.scan.selectedDevice == "":
                self.feature.showMessage(icons=QMessageBox.Warning, title="Warning",
                                         message="Please select CredoSense SRC-5 device to connect")

            else:
                self.waiting_window()
                self.graphWindow = QMainWindow()
                # self.selectedDevice is the current selected device to connect from ScanPageFunctionality

                self.graphUi = lineGraph(self.graphWindow, self.scan.selectedDevice)
                self.waiting_window_end()
                self.graphWindow.show()
                MainWindow.close()

        except Exception:
            pass


# ToDo 1: add multiple device switching functionality after opening app

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = SplashScreen(MainWindow)
ui.ShowSplash()
sys.exit(app.exec_())
