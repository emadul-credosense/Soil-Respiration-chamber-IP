import asyncio
import time

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.gridspec import GridSpec

import Functionality


# Common Design For all the classes

def changeColor(name):
    name.patch.set_facecolor('#2E3440')
    name.tick_params(axis='x', colors='#D8DEE9')
    name.tick_params(axis='y', colors='#D8DEE9')
    name.spines['bottom'].set_color('#D8DEE9')
    name.spines['top'].set_color('#D8DEE9')
    name.spines['right'].set_color('#D8DEE9')
    name.spines['left'].set_color('#D8DEE9')


# class for chamber pressure
class matlibplot1(FigureCanvasQTAgg):

    def __init__(self, client):
        self.interval = 1
        self.sleep = 0
        # Bleak client received
        self.client = client
        # Plotting Unit
        self.fig = plt.figure(dpi=80, constrained_layout=True)
        # Making grid layout row , col
        gs = GridSpec(3, 2, figure=self.fig)
        # All the sub plots
        self.ax1 = self.fig.add_subplot(gs[0, :])
        self.ax2 = self.fig.add_subplot(gs[1, 0])
        self.ax3 = self.fig.add_subplot(gs[1, 1])
        self.ax4 = self.fig.add_subplot(gs[2, 0])
        self.ax5 = self.fig.add_subplot(gs[2, 1])
        # X & Y axis
        self.xs = []
        self.ys1 = []
        self.ys2 = []
        self.ys3 = []
        self.ys4 = []
        self.ys5 = []

        super(matlibplot1, self).__init__(self.fig)
        # Animation Function called in every 1 sec
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=self.interval * 1000)

        self.fig.patch.set_facecolor('#2E3440')
        # Changing color of all the sub plots
        changeColor(self.ax1)
        changeColor(self.ax2)
        changeColor(self.ax3)
        changeColor(self.ax4)
        changeColor(self.ax5)
        self.font = {'family': 'Arial',
                     'color': '#D8DEE9',
                     'weight': 'normal',
                     'size': 12,
                     }
        self.ax4.set_xlabel('Time', fontdict=self.font)
        self.ax5.set_xlabel('Time', fontdict=self.font)

    # Function for updating plot
    def animate(self, i):
        try:
            # receiving data for plot
            self.feature = Functionality.functionality()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.feature.receiveData(self.client))
            # Setting x axis data for all plot
            self.xs.append(self.feature.timeOnly())
            # Setting y axis data for all plot
            self.ys1.append(self.feature.CP)
            self.ys2.append(self.feature.AT)
            self.ys3.append(self.feature.RH)
            self.ys4.append(self.feature.SM)
            self.ys5.append(self.feature.ST)
            # Limiting data to number of 5
            self.xs = self.xs[-5:]
            self.ys1 = self.ys1[-5:]
            self.ys2 = self.ys2[-5:]
            self.ys3 = self.ys3[-5:]
            self.ys4 = self.ys4[-5:]
            self.ys5 = self.ys5[-5:]
            # clearing all subplots to plot update data
            self.ax1.clear()
            self.ax2.clear()
            self.ax3.clear()
            self.ax4.clear()
            self.ax5.clear()
            # Setting figure color which is outside of subplot color
            self.fig.patch.set_facecolor('#2E3440')
            # Changing color of all the sub plots update
            changeColor(self.ax1)
            changeColor(self.ax2)
            changeColor(self.ax3)
            changeColor(self.ax4)
            changeColor(self.ax5)

            # Setting y-axis data limit
            self.ax1.set_ylim([600, 1200])
            self.ax2.set_ylim([-25, 75])
            self.ax3.set_ylim([0, 100])
            self.ax4.set_ylim([0, 100])
            self.ax5.set_ylim([-25, 75])

            # Plotting data in all subplot
            self.ax1.plot(self.xs, self.ys1, color='#D8DEE9', linewidth=1)
            self.ax2.plot(self.xs, self.ys2, color='#D8DEE9', linewidth=1)
            self.ax3.plot(self.xs, self.ys3, color='#D8DEE9', linewidth=1)
            self.ax4.plot(self.xs, self.ys4, color='#D8DEE9', linewidth=1)
            self.ax5.plot(self.xs, self.ys5, color='#D8DEE9', linewidth=1)

            # Setting y-axis label
            self.ax1.set_ylabel('Cham. pressure (mbar)', fontdict=self.font)
            self.ax2.set_ylabel('Cham. air temp. (°C)', fontdict=self.font)
            self.ax3.set_ylabel('Cham. rel. humidity (%)', fontdict=self.font)
            self.ax4.set_ylabel('Soil moisture (%)', fontdict=self.font)
            self.ax5.set_ylabel('Soil temperature (°C)', fontdict=self.font)

            # Setting x-axis label
            self.ax1.set_xlabel('  ', fontdict=self.font)
            self.ax2.set_xlabel('  ', fontdict=self.font)
            self.ax3.set_xlabel('  ', fontdict=self.font)
            self.ax4.set_xlabel('Time', fontdict=self.font)
            self.ax5.set_xlabel('Time', fontdict=self.font)

            # ToDo(important): this two should be removed before release
            # Saving data after plotting and clearing array
            self.feature.saveData()
            self.feature.saveDataArray.clear()
            self.sleep = self.interval - 1
            if self.sleep != 0:
                time.sleep(self.sleep)
        except Exception:
            pass
