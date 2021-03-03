import asyncio
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

import Functionality
from scanpage import Ui_ScanWindow

progressBarCounter2 = 0


class ScanPage(Ui_ScanWindow, ):
    def __init__(self, parent=None):
        super(ScanPage, self).__init__(parent)
        # creating loop Event for scanning device. Scanning for device is a future data type
        loop = asyncio.get_event_loop()
        self.scanButton.clicked.connect(lambda: loop.run_until_complete(self.scanNShow()))
        # To know is there any credosense devices
        self.selectedDevice = ""
        self.scanButton.clicked.connect(self.scanNReset)

    def scanNReset(self):
        if self.scanButton.isChecked():
            self.scanButton.setText("Refresh")

    # declaring clear method for reset button
    def clear(self):
        try:
            print(threading.active_count())
            self.devicelist.clear()  # clearing list widget
            self.devicelist.clicked.disconnect(self.getSelectedDevice)  # disconnect getSelectedDevice method
        except Exception:
            pass

    # Scanning device and showing in list Widget
    async def scanNShow(self):
        try:
            self.waiting_window()
            # self.timer.start(10)
            self.devicelist.clear()
            self.selectedDevice = ""
            # calling Scan Function and getting discovered devices
            features = Functionality.functionality()
            self.devices = await features.scanForDevices()
            # Extracting device from object
            for device in self.devices:
                # formatting device name to show in list widget
                deviceName = f"\n{device.name}\n"
                if 'cs' in deviceName.lower():  # showing only credosense devices
                    # Adding device name address to list widget
                    self.devicelist.addItem(deviceName)

                else:
                    pass
            # If there is no device found
            if len(self.devicelist) == 0:
                self.devicelist.addItem("No CS-RC5 found")
            # getting selected device from among the devices

        except Exception:
            pass
        finally:
            self.waiting_window_end()

    # Getting macAddress of selected device
    def getSelectedDevice(self):
        try:
            currentDevice = self.devicelist.currentItem().text()
            getDeviceName = currentDevice.split('\n')
            for device in self.devices:
                if device.name.lower() == getDeviceName[1].lower():
                    self.selectedDevice = device.address

            # self.selectedDevice is the current selected device to connect
        except Exception:
            pass

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
