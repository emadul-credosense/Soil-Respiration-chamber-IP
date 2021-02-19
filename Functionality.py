from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from bleak import discover
from datetime import datetime
from datetime import date

# characteristic of targeted device, this will be dynamic
characteristic_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"


class functionality:
    def __init__(self):
        self.currentStatus = 0
        self.saveDataArray = []

    # Show message on view save data, bluetooth scan, connect fail
    def showMessage(self,icons, title, message):
        msg = QMessageBox()
        msg.setIcon(icons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/playstore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    # Scanning for Device
    async def scanForDevices(self):
        try:
            devices = await discover(timeout=3.0)
            return devices

        except Exception:
            self.showMessage(icons=QMessageBox.Warning,title="Warning",message="Please check your bluetooth connection before search")
            # Showing notice if pc bluetooth is off

    # connecting the device
    async def connectingDevice(self, client):
        self.client = client
        try:
            await self.client.connect()
        except Exception:
            pass

    # Sending Data
    async def sendData(self, client, dataBytes):
        try:
            await client.write_gatt_char(characteristic_UUID, dataBytes)
        except Exception:
            pass

    # receiving and extracting real data
    async def receiveData(self, client):
        try:
            dataFromEsp = await client.read_gatt_char(characteristic_UUID)
            self.dataConverterToUse(dataFromEsp.decode())

        except Exception:
            pass

    # Converting to real data
    def dataConverterToUse(self, dataString):
        try:
            print(dataString)
            self.splitDataString = dataString.split('+')
            self.actualData = f"{dataString[0]}+{dataString[1] + dataString[2] + dataString[3]}+{dataString[4] + dataString[5] + dataString[6] + dataString[7] + dataString[8]}+{dataString[9] + dataString[10] + dataString[11]}+{self.splitDataString[1]}+{self.splitDataString[2]} "
            self.breakActualData = self.actualData.split('+')
            print(self.breakActualData)
            # Deducting and multiplying career
            self.AT = (int(self.breakActualData[1]) / 10) - 25
            self.CP = int(self.breakActualData[2]) / 10
            self.ST = (int(self.breakActualData[3]) / 10) - 25
            self.RH = int(self.breakActualData[4])
            self.SM = int(self.breakActualData[5])
            self.currentStatus = self.breakActualData[0]

            if int(self.currentStatus) == 1:
                self.msg = "open"

            elif int(self.currentStatus) == 0:
                self.msg = "Close"
            self.saveDataArray.append(str(self.AT))
            self.saveDataArray.append(str(self.CP))
            self.saveDataArray.append(str(self.ST))
            self.saveDataArray.append(str(self.RH))
            self.saveDataArray.append(str(self.SM))
            self.saveDataArray.append(self.msg)

        except Exception:
            pass

    # Saving data as CSV
    def saveData(self):
        try:
            self.timeOnly = self.timeOnly()
            self.dateOnly = date.today().strftime("%d-%B-%Y")
            file = open(f"data\\{self.dateOnly}.csv", "a")
            file.write(
                f"{self.dateOnly},{self.timeOnly},{self.saveDataArray[0]},{self.saveDataArray[1]},{self.saveDataArray[2]},{self.saveDataArray[3]},{self.saveDataArray[4]},{self.saveDataArray[5]}\n")
            file.close()
        except Exception:
            pass

    # checking device connection status
    async def deviceConnectionStatus(self, client):
        connectionStatus = await client.is_connected()
        return connectionStatus

    # Disconnecting Device
    async def disconnect(self, client):
        await client.disconnect()

    # Creating file with header to save data
    def createFile(self):
        try:
            self.dateOnly = date.today().strftime("%d-%B-%Y")
            file = open(f"data\\{self.dateOnly}.csv", "x")
            file.write(
                "Date(DD-MM-YY), Time(24-hour),Chamber air temperature (°C),Chamber pressure(mBar), Soil temperature (°C), Chamber relative humidity (%),Soil moisture (%), Chamber Status(Open/Closed)\n")
            file.close()
        except Exception:
            pass

    # Time function for plotting
    def timeOnly(self):
        self.timeDate = datetime.now()
        return f"{self.timeDate.hour}:{self.timeDate.minute}:{self.timeDate.second}"

    # Current date time format, to send to Respiration Chamber
    def currentTimeDate(self):
        self.timeDate = datetime.now()
        # converting data into bytearray
        timeDateData = f"{self.timeDate.hour}:{self.timeDate.minute}:{self.timeDate.second}:{self.timeDate.day}:{self.timeDate.month}:{self.timeDate.year}"
        return bytearray(timeDateData, 'utf-8')

