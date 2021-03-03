import asyncio
import os
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

import Functionality
from matlibplot import Ui_Matlibplot


# inheriting Matlibplot


class lineGraph(Ui_Matlibplot):
    def __init__(self, parent=None, parent1=None, ):
        super(lineGraph, self).__init__(parent, parent1)

        self.features = Functionality.functionality()
        # Creating file to save data
        self.features.createFile()
        loop = asyncio.get_event_loop()
        # Connecting Device to program
        loop.run_until_complete(self.features.connectingDevice(self.client))
        loop1 = asyncio.get_event_loop()
        # Sending date and time to reset rtc
        loop1.run_until_complete(self.features.sendData(self.client, self.features.currentTimeDate()))
        # Run control panel functionality in a thread to avoid crush
        self.runInThread()
        # All the button and slider function
        self.toggleButton.valueChanged.connect(self.toggleButtonSlider)
        self.Timer.valueChanged.connect(self.sendDelay)
        self.SavedFileButton.clicked.connect(self.viewSavedFile)
        self.StopDLButton.setCheckable(True)
        self.StopDLButton.clicked.connect(self.stopData)

    # Show message on view save data

    # Function for stop logging data
    def stopData(self):
        # Toggling of Stop and start data log function
        if self.StopDLButton.isChecked():
            self.StopDLButton.setText("Start Logging")
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.features.disconnect(self.client))
        else:
            self.StopDLButton.setText("Stop Logging")
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.features.connectingDevice(self.client))

    # Function view saved files
    def viewSavedFile(self):
        loop = asyncio.get_event_loop()
        DeviceConnected = loop.run_until_complete(self.features.deviceConnectionStatus(self.client))
        if DeviceConnected:
            self.features.showMessage(icons=QMessageBox.Warning, title="Stop",
                                      message="Stop data logging before viewing saved file(s)")
        else:
            # Default path
            path = os.getcwd()
            # Data folder path path
            NewPath = path + '\\data'
            path = os.path.realpath(NewPath)
            os.startfile(path)

    # Function to start threading
    def runInThread(self):
        self.run = thread(self.client, self.label_10)
        self.run.start()

    # Toggle button functionality
    def toggleButtonSlider(self, value):

        self.state = value
        if self.state == 1:
            self.changeStateToLight()
            try:
                Data = "closed"
                dataArray = bytearray(Data, 'utf-8')
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.features.sendData(self.client, dataArray))
            except Exception:
                pass

        else:
            try:
                Data = "open"
                dataArray = bytearray(Data, 'utf-8')
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.features.sendData(self.client, dataArray))
                self.changeStateToDark()
            except Exception:
                pass

    # Changing toggle button & frame color
    def changeStateToDark(self):
        self.toggleButton.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "    width: 50px;\n"
                                        "    border-radius:10px;\n"
                                        "    height: 20px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                        "    background:#677590;\n"
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
        self.frame_2.setStyleSheet(
            " background: #677590;"
            "\n"
            "border-radius:10px;")

    def changeStateToLight(self):
        self.toggleButton.setStyleSheet("QSlider::groove:horizontal {\n"
                                        "    width: 50px;\n"
                                        "    border-radius:10px;\n"
                                        "    height: 20px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                        "    background:#C0C0C0;\n"
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
        self.frame_2.setStyleSheet(
            " background: #C0C0C0;"
            "\n"
            "border-radius:10px;")

    # Sending delay from python to esp
    def sendDelay(self, delayVal):
        try:
            print(self.widget.interval)
            self.widget.interval = delayVal
            self.Delay = delayVal
            delayData = f"{self.Delay}"
            dataArray = bytearray(delayData, 'utf-8')
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.features.sendData(self.client, dataArray))
        except Exception:
            pass


class thread(QThread):
    def __init__(self, address, label):
        super(thread, self).__init__()
        self.client = address
        self.label10 = label

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        while True:
            try:
                self.fromFunctionality = Functionality.functionality()
                loop.run_until_complete(self.fromFunctionality.receiveData(self.client))
                # Setting current chamber status
                print("in thread")
                if self.fromFunctionality.currentStatus == 0:

                    self.label10.setText("Chamber status: Close")
                # ToDo(important): this two should be uncommented before release
                # self.fromFunctionality.saveData()
                # self.fromFunctionality.saveDataArray.clear()
                else:
                    self.label10.setText("Chamber status: Open")
            except Exception:
                pass
