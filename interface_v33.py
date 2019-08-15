# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.nova_v12.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import PyQt5
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
#pacotes necessários
import sys
import pyqtgraph as pg
import time
import glob
from PyQt5.QtGui import QPixmap
import PyQt5.sip
from datetime import datetime
import struct
import numpy as np
# Se for instalar um pacote, NÃO instalar o serial, apenas o pyserial
import serial
from serial import Serial
from serial import SerialException

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 721, 651))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 231, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox_SerialPorts = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_SerialPorts.setGeometry(QtCore.QRect(20, 50, 69, 22))
        self.comboBox_SerialPorts.setObjectName("comboBox_SerialPorts")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(140, 90, 91, 16))
        self.label_35.setObjectName("label_35")
        self.doubleSpinBox_UpdateTime = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_UpdateTime.setGeometry(QtCore.QRect(140, 110, 62, 22))
        self.doubleSpinBox_UpdateTime.setDecimals(3)
        self.doubleSpinBox_UpdateTime.setProperty("value", 0.005)
        self.doubleSpinBox_UpdateTime.setObjectName("doubleSpinBox_UpdateTime")
        self.comboBox_Baudrate = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_Baudrate.setGeometry(QtCore.QRect(20, 110, 69, 22))
        self.comboBox_Baudrate.setObjectName("comboBox_Baudrate")
        self.label_41 = QtWidgets.QLabel(self.groupBox)
        self.label_41.setGeometry(QtCore.QRect(20, 90, 51, 16))
        self.label_41.setObjectName("label_41")
        self.pushButton_UpdatePorts = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_UpdatePorts.setGeometry(QtCore.QRect(130, 42, 81, 31))
        self.pushButton_UpdatePorts.setObjectName("pushButton_UpdatePorts")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 20, 421, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_Buffer = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_Buffer.setGeometry(QtCore.QRect(20, 50, 381, 91))
        self.textBrowser_Buffer.setObjectName("textBrowser_Buffer")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 320, 691, 281))
        self.groupBox_4.setObjectName("groupBox_4")
        self.spinBox_IndexBattery = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexBattery.setGeometry(QtCore.QRect(150, 230, 42, 22))
        self.spinBox_IndexBattery.setProperty("value", 2)
        self.spinBox_IndexBattery.setObjectName("spinBox_IndexBattery")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(150, 210, 61, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox_IndexEngineTemperature = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexEngineTemperature.setGeometry(QtCore.QRect(70, 230, 42, 22))
        self.spinBox_IndexEngineTemperature.setProperty("value", 1)
        self.spinBox_IndexEngineTemperature.setObjectName("spinBox_IndexEngineTemperature")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(150, 80, 61, 16))
        self.label_14.setObjectName("label_14")
        self.spinBox_IndexFuelPressure = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexFuelPressure.setGeometry(QtCore.QRect(150, 100, 42, 22))
        self.spinBox_IndexFuelPressure.setProperty("value", 2)
        self.spinBox_IndexFuelPressure.setObjectName("spinBox_IndexFuelPressure")
        self.spinBox_IndexOilPressure = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexOilPressure.setGeometry(QtCore.QRect(70, 100, 42, 22))
        self.spinBox_IndexOilPressure.setProperty("value", 1)
        self.spinBox_IndexOilPressure.setObjectName("spinBox_IndexOilPressure")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(70, 80, 31, 16))
        self.label_21.setObjectName("label_21")
        self.spinBox_IndexTPS = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexTPS.setGeometry(QtCore.QRect(230, 100, 42, 22))
        self.spinBox_IndexTPS.setProperty("value", 3)
        self.spinBox_IndexTPS.setObjectName("spinBox_IndexTPS")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(230, 80, 41, 16))
        self.label_22.setObjectName("label_22")
        self.spinBox_IndexFuelPumpRelay = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexFuelPumpRelay.setGeometry(QtCore.QRect(230, 230, 42, 22))
        self.spinBox_IndexFuelPumpRelay.setProperty("value", 3)
        self.spinBox_IndexFuelPumpRelay.setObjectName("spinBox_IndexFuelPumpRelay")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(210, 210, 81, 20))
        self.label_23.setObjectName("label_23")
        self.spinBox_IndexBreakPressureFront = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexBreakPressureFront.setGeometry(QtCore.QRect(390, 100, 42, 22))
        self.spinBox_IndexBreakPressureFront.setProperty("value", 5)
        self.spinBox_IndexBreakPressureFront.setObjectName("spinBox_IndexBreakPressureFront")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(390, 80, 61, 16))
        self.label_24.setObjectName("label_24")
        self.spinBox_IndexBreakPressureRear = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexBreakPressureRear.setGeometry(QtCore.QRect(310, 100, 42, 22))
        self.spinBox_IndexBreakPressureRear.setProperty("value", 4)
        self.spinBox_IndexBreakPressureRear.setObjectName("spinBox_IndexBreakPressureRear")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(310, 80, 61, 16))
        self.label_25.setObjectName("label_25")
        self.spinBox_IndexSpeed = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexSpeed.setGeometry(QtCore.QRect(310, 40, 42, 22))
        self.spinBox_IndexSpeed.setProperty("value", 4)
        self.spinBox_IndexSpeed.setObjectName("spinBox_IndexSpeed")
        self.label_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label_26.setGeometry(QtCore.QRect(310, 20, 61, 16))
        self.label_26.setObjectName("label_26")
        self.spinBox_IndexSparkcutRelay = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexSparkcutRelay.setGeometry(QtCore.QRect(390, 40, 42, 22))
        self.spinBox_IndexSparkcutRelay.setProperty("value", 5)
        self.spinBox_IndexSparkcutRelay.setObjectName("spinBox_IndexSparkcutRelay")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(370, 20, 91, 16))
        self.label_27.setObjectName("label_27")
        self.spinBox_IndexTime2 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexTime2.setGeometry(QtCore.QRect(150, 160, 42, 22))
        self.spinBox_IndexTime2.setProperty("value", 9)
        self.spinBox_IndexTime2.setObjectName("spinBox_IndexTime2")
        self.label_37 = QtWidgets.QLabel(self.groupBox_4)
        self.label_37.setGeometry(QtCore.QRect(150, 140, 61, 16))
        self.label_37.setObjectName("label_37")
        self.label_40 = QtWidgets.QLabel(self.groupBox_4)
        self.label_40.setGeometry(QtCore.QRect(310, 210, 71, 20))
        self.label_40.setObjectName("label_40")
        self.spinBox_IndexFanRelay = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexFanRelay.setGeometry(QtCore.QRect(310, 230, 42, 22))
        self.spinBox_IndexFanRelay.setProperty("value", 4)
        self.spinBox_IndexFanRelay.setObjectName("spinBox_IndexFanRelay")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label.setObjectName("label")
        self.label_42 = QtWidgets.QLabel(self.groupBox_4)
        self.label_42.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_4)
        self.label_43.setGeometry(QtCore.QRect(10, 230, 61, 16))
        self.label_43.setObjectName("label_43")
        self.spinBox_IndexTime1 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexTime1.setGeometry(QtCore.QRect(550, 40, 42, 22))
        self.spinBox_IndexTime1.setProperty("value", 7)
        self.spinBox_IndexTime1.setObjectName("spinBox_IndexTime1")
        self.label_45 = QtWidgets.QLabel(self.groupBox_4)
        self.label_45.setGeometry(QtCore.QRect(560, 20, 61, 16))
        self.label_45.setObjectName("label_45")
        self.spinBox_IndexRelayBoxTemperature = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexRelayBoxTemperature.setGeometry(QtCore.QRect(390, 230, 42, 22))
        self.spinBox_IndexRelayBoxTemperature.setProperty("value", 5)
        self.spinBox_IndexRelayBoxTemperature.setObjectName("spinBox_IndexRelayBoxTemperature")
        self.label_46 = QtWidgets.QLabel(self.groupBox_4)
        self.label_46.setGeometry(QtCore.QRect(380, 210, 81, 20))
        self.label_46.setObjectName("label_46")
        self.spinBox_IndexTime3 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexTime3.setGeometry(QtCore.QRect(630, 230, 42, 22))
        self.spinBox_IndexTime3.setProperty("value", 8)
        self.spinBox_IndexTime3.setObjectName("spinBox_IndexTime3")
        self.label_47 = QtWidgets.QLabel(self.groupBox_4)
        self.label_47.setGeometry(QtCore.QRect(640, 210, 61, 16))
        self.label_47.setObjectName("label_47")
        self.spinBox_IndexXAccel = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexXAccel.setGeometry(QtCore.QRect(70, 40, 42, 22))
        self.spinBox_IndexXAccel.setProperty("value", 1)
        self.spinBox_IndexXAccel.setObjectName("spinBox_IndexXAccel")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(150, 20, 61, 20))
        self.label_33.setObjectName("label_33")
        self.label_48 = QtWidgets.QLabel(self.groupBox_4)
        self.label_48.setGeometry(QtCore.QRect(230, 20, 61, 16))
        self.label_48.setObjectName("label_48")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(70, 20, 61, 16))
        self.label_34.setObjectName("label_34")
        self.spinBox_IndexYAccel = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexYAccel.setGeometry(QtCore.QRect(150, 40, 42, 22))
        self.spinBox_IndexYAccel.setProperty("value", 2)
        self.spinBox_IndexYAccel.setObjectName("spinBox_IndexYAccel")
        self.spinBox_IndexZAccel = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexZAccel.setGeometry(QtCore.QRect(230, 40, 42, 22))
        self.spinBox_IndexZAccel.setProperty("value", 3)
        self.spinBox_IndexZAccel.setObjectName("spinBox_IndexZAccel")
        self.label_51 = QtWidgets.QLabel(self.groupBox_4)
        self.label_51.setGeometry(QtCore.QRect(470, 80, 61, 16))
        self.label_51.setObjectName("label_51")
        self.spinBox_IndexWheelPos = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexWheelPos.setGeometry(QtCore.QRect(470, 100, 42, 22))
        self.spinBox_IndexWheelPos.setProperty("value", 6)
        self.spinBox_IndexWheelPos.setObjectName("spinBox_IndexWheelPos")
        self.spinBox_IndexBeacon = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexBeacon.setGeometry(QtCore.QRect(550, 100, 42, 22))
        self.spinBox_IndexBeacon.setProperty("value", 7)
        self.spinBox_IndexBeacon.setObjectName("spinBox_IndexBeacon")
        self.label_60 = QtWidgets.QLabel(self.groupBox_4)
        self.label_60.setGeometry(QtCore.QRect(70, 140, 61, 16))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.groupBox_4)
        self.label_61.setGeometry(QtCore.QRect(550, 80, 61, 16))
        self.label_61.setObjectName("label_61")
        self.spinBox_IndexCurrent = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexCurrent.setGeometry(QtCore.QRect(70, 160, 42, 22))
        self.spinBox_IndexCurrent.setProperty("value", 8)
        self.spinBox_IndexCurrent.setObjectName("spinBox_IndexCurrent")
        self.label_62 = QtWidgets.QLabel(self.groupBox_4)
        self.label_62.setGeometry(QtCore.QRect(450, 210, 81, 16))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.groupBox_4)
        self.label_63.setGeometry(QtCore.QRect(540, 210, 81, 16))
        self.label_63.setObjectName("label_63")
        self.spinBox_IndexBreakTempFront = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexBreakTempFront.setGeometry(QtCore.QRect(550, 230, 42, 22))
        self.spinBox_IndexBreakTempFront.setProperty("value", 7)
        self.spinBox_IndexBreakTempFront.setObjectName("spinBox_IndexBreakTempFront")
        self.spinBox_IndexBreakTempRear = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexBreakTempRear.setGeometry(QtCore.QRect(470, 230, 42, 22))
        self.spinBox_IndexBreakTempRear.setProperty("value", 6)
        self.spinBox_IndexBreakTempRear.setObjectName("spinBox_IndexBreakTempRear")
        self.spinBox_IndexSuspPos = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_IndexSuspPos.setGeometry(QtCore.QRect(470, 40, 42, 22))
        self.spinBox_IndexSuspPos.setProperty("value", 6)
        self.spinBox_IndexSuspPos.setObjectName("spinBox_IndexSuspPos")
        self.label_128 = QtWidgets.QLabel(self.groupBox_4)
        self.label_128.setGeometry(QtCore.QRect(470, 20, 61, 16))
        self.label_128.setObjectName("label_128")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 200, 311, 101))
        self.groupBox_16.setObjectName("groupBox_16")
        self.spinBox_WheelPosMax = QtWidgets.QSpinBox(self.groupBox_16)
        self.spinBox_WheelPosMax.setGeometry(QtCore.QRect(20, 50, 71, 22))
        self.spinBox_WheelPosMax.setMaximum(10000)
        self.spinBox_WheelPosMax.setProperty("value", 994)
        self.spinBox_WheelPosMax.setObjectName("spinBox_WheelPosMax")
        self.label_29 = QtWidgets.QLabel(self.groupBox_16)
        self.label_29.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_16)
        self.label_30.setGeometry(QtCore.QRect(120, 30, 81, 16))
        self.label_30.setObjectName("label_30")
        self.spinBox_WheelPosMin = QtWidgets.QSpinBox(self.groupBox_16)
        self.spinBox_WheelPosMin.setGeometry(QtCore.QRect(120, 50, 71, 22))
        self.spinBox_WheelPosMin.setMaximum(10000)
        self.spinBox_WheelPosMin.setProperty("value", 50)
        self.spinBox_WheelPosMin.setObjectName("spinBox_WheelPosMin")
        self.label_49 = QtWidgets.QLabel(self.groupBox_16)
        self.label_49.setGeometry(QtCore.QRect(210, 30, 91, 16))
        self.label_49.setObjectName("label_49")
        self.lineEdit_CurrentWheelPos = QtWidgets.QLineEdit(self.groupBox_16)
        self.lineEdit_CurrentWheelPos.setGeometry(QtCore.QRect(220, 50, 71, 21))
        self.lineEdit_CurrentWheelPos.setObjectName("lineEdit_CurrentWheelPos")
        self.groupBox_38 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_38.setGeometry(QtCore.QRect(350, 200, 121, 101))
        self.groupBox_38.setObjectName("groupBox_38")
        self.lineEdit_CalibrationConstant = QtWidgets.QLineEdit(self.groupBox_38)
        self.lineEdit_CalibrationConstant.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.lineEdit_CalibrationConstant.setObjectName("lineEdit_CalibrationConstant")
        self.label_64 = QtWidgets.QLabel(self.groupBox_38)
        self.label_64.setGeometry(QtCore.QRect(10, 30, 111, 21))
        self.label_64.setObjectName("label_64")
        self.groupBox_39 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_39.setGeometry(QtCore.QRect(500, 200, 191, 101))
        self.groupBox_39.setObjectName("groupBox_39")
        self.lineEdit_LastLap = QtWidgets.QLineEdit(self.groupBox_39)
        self.lineEdit_LastLap.setGeometry(QtCore.QRect(90, 20, 81, 21))
        self.lineEdit_LastLap.setObjectName("lineEdit_LastLap")
        self.lineEdit_LastLap2 = QtWidgets.QLineEdit(self.groupBox_39)
        self.lineEdit_LastLap2.setGeometry(QtCore.QRect(90, 60, 81, 21))
        self.lineEdit_LastLap2.setObjectName("lineEdit_LastLap2")
        self.label_70 = QtWidgets.QLabel(self.groupBox_39)
        self.label_70.setGeometry(QtCore.QRect(30, 20, 111, 21))
        self.label_70.setObjectName("label_70")
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_19.setGeometry(QtCore.QRect(20, 10, 671, 441))
        self.groupBox_19.setObjectName("groupBox_19")
        self.lineEdit_SetupDriver = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupDriver.setGeometry(QtCore.QRect(80, 130, 241, 20))
        self.lineEdit_SetupDriver.setObjectName("lineEdit_SetupDriver")
        self.label_31 = QtWidgets.QLabel(self.groupBox_19)
        self.label_31.setGeometry(QtCore.QRect(40, 130, 111, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_19)
        self.label_32.setGeometry(QtCore.QRect(50, 30, 111, 16))
        self.label_32.setObjectName("label_32")
        self.lineEdit_SetupCar = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupCar.setGeometry(QtCore.QRect(80, 30, 241, 20))
        self.lineEdit_SetupCar.setObjectName("lineEdit_SetupCar")
        self.label_50 = QtWidgets.QLabel(self.groupBox_19)
        self.label_50.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.label_50.setObjectName("label_50")
        self.lineEdit_SetupTrack = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupTrack.setGeometry(QtCore.QRect(80, 80, 241, 20))
        self.lineEdit_SetupTrack.setObjectName("lineEdit_SetupTrack")
        self.label_52 = QtWidgets.QLabel(self.groupBox_19)
        self.label_52.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.label_52.setObjectName("label_52")
        self.lineEdit_SetupTemperature = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupTemperature.setGeometry(QtCore.QRect(80, 180, 241, 20))
        self.lineEdit_SetupTemperature.setObjectName("lineEdit_SetupTemperature")
        self.label_53 = QtWidgets.QLabel(self.groupBox_19)
        self.label_53.setGeometry(QtCore.QRect(40, 230, 111, 16))
        self.label_53.setObjectName("label_53")
        self.lineEdit_SetupAntiroll = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupAntiroll.setGeometry(QtCore.QRect(80, 230, 241, 20))
        self.lineEdit_SetupAntiroll.setObjectName("lineEdit_SetupAntiroll")
        self.label_54 = QtWidgets.QLabel(self.groupBox_19)
        self.label_54.setGeometry(QtCore.QRect(160, 300, 111, 16))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_19)
        self.label_55.setGeometry(QtCore.QRect(340, 20, 111, 16))
        self.label_55.setObjectName("label_55")
        self.lineEdit_SetupWingAttackAngle = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupWingAttackAngle.setGeometry(QtCore.QRect(410, 30, 241, 20))
        self.lineEdit_SetupWingAttackAngle.setObjectName("lineEdit_SetupWingAttackAngle")
        self.label_56 = QtWidgets.QLabel(self.groupBox_19)
        self.label_56.setGeometry(QtCore.QRect(340, 80, 111, 16))
        self.label_56.setObjectName("label_56")
        self.lineEdit_SetupEngineMap = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupEngineMap.setGeometry(QtCore.QRect(410, 80, 241, 20))
        self.lineEdit_SetupEngineMap.setObjectName("lineEdit_SetupEngineMap")
        self.label_57 = QtWidgets.QLabel(self.groupBox_19)
        self.label_57.setGeometry(QtCore.QRect(340, 130, 111, 16))
        self.label_57.setObjectName("label_57")
        self.lineEdit_SetupBalanceBar = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupBalanceBar.setGeometry(QtCore.QRect(410, 130, 241, 20))
        self.lineEdit_SetupBalanceBar.setObjectName("lineEdit_SetupBalanceBar")
        self.label_58 = QtWidgets.QLabel(self.groupBox_19)
        self.label_58.setGeometry(QtCore.QRect(340, 180, 111, 16))
        self.label_58.setObjectName("label_58")
        self.lineEdit_SetupDifferential = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupDifferential.setGeometry(QtCore.QRect(410, 180, 241, 20))
        self.lineEdit_SetupDifferential.setObjectName("lineEdit_SetupDifferential")
        self.label_59 = QtWidgets.QLabel(self.groupBox_19)
        self.label_59.setGeometry(QtCore.QRect(40, 380, 111, 16))
        self.label_59.setObjectName("label_59")
        self.lineEdit_SetupTirePressureRear = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupTirePressureRear.setGeometry(QtCore.QRect(80, 380, 241, 20))
        self.lineEdit_SetupTirePressureRear.setObjectName("lineEdit_SetupTirePressureRear")
        self.label_71 = QtWidgets.QLabel(self.groupBox_19)
        self.label_71.setGeometry(QtCore.QRect(40, 330, 111, 16))
        self.label_71.setObjectName("label_71")
        self.lineEdit_SetupTirePressureFront = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupTirePressureFront.setGeometry(QtCore.QRect(80, 330, 241, 20))
        self.lineEdit_SetupTirePressureFront.setObjectName("lineEdit_SetupTirePressureFront")
        self.textEdit_SetupComments = QtWidgets.QTextEdit(self.groupBox_19)
        self.textEdit_SetupComments.setGeometry(QtCore.QRect(410, 280, 241, 121))
        self.textEdit_SetupComments.setObjectName("textEdit_SetupComments")
        self.label_72 = QtWidgets.QLabel(self.groupBox_19)
        self.label_72.setGeometry(QtCore.QRect(340, 280, 111, 16))
        self.label_72.setObjectName("label_72")
        self.label_127 = QtWidgets.QLabel(self.groupBox_19)
        self.label_127.setGeometry(QtCore.QRect(360, 40, 51, 16))
        self.label_127.setObjectName("label_127")
        self.label_73 = QtWidgets.QLabel(self.groupBox_19)
        self.label_73.setGeometry(QtCore.QRect(330, 230, 111, 16))
        self.label_73.setObjectName("label_73")
        self.lineEdit_SetupAcquisitionRate = QtWidgets.QLineEdit(self.groupBox_19)
        self.lineEdit_SetupAcquisitionRate.setGeometry(QtCore.QRect(410, 230, 241, 20))
        self.lineEdit_SetupAcquisitionRate.setObjectName("lineEdit_SetupAcquisitionRate")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 470, 671, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_FileName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_FileName.setGeometry(QtCore.QRect(30, 70, 371, 21))
        self.lineEdit_FileName.setObjectName("lineEdit_FileName")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(30, 50, 141, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(500, 100, 91, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(180, 20, 71, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton_SaveFile = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_SaveFile.setGeometry(QtCore.QRect(450, 60, 75, 23))
        self.pushButton_SaveFile.setObjectName("pushButton_SaveFile")
        self.pushButton_StopSaveFile = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_StopSaveFile.setGeometry(QtCore.QRect(540, 60, 75, 23))
        self.pushButton_StopSaveFile.setObjectName("pushButton_StopSaveFile")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 121, 211))
        self.groupBox_5.setObjectName("groupBox_5")
        self.progressBar_EngineTemperature = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_EngineTemperature.setGeometry(QtCore.QRect(20, 40, 31, 141))
        self.progressBar_EngineTemperature.setProperty("value", 24)
        self.progressBar_EngineTemperature.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_EngineTemperature.setObjectName("progressBar_EngineTemperature")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_5)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 160, 51, 16))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 250, 691, 321))
        self.groupBox_7.setObjectName("groupBox_7")
        # gráfico
        self.graphicsView_EngineData = pg.PlotWidget(self.groupBox_7)
        self.graphicsView_EngineData.setGeometry(QtCore.QRect(30, 21, 481, 281))
        self.graphicsView_EngineData.setObjectName("graphicsView_EngineData")
        self.checkBox_Voltage = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_Voltage.setGeometry(QtCore.QRect(560, 220, 70, 17))
        self.checkBox_Voltage.setObjectName("checkBox_Voltage")
        self.checkBox_FuelPressure = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_FuelPressure.setGeometry(QtCore.QRect(560, 190, 101, 17))
        self.checkBox_FuelPressure.setObjectName("checkBox_FuelPressure")
        self.checkBox_EngineTemperature = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_EngineTemperature.setGeometry(QtCore.QRect(560, 160, 91, 17))
        self.checkBox_EngineTemperature.setObjectName("checkBox_EngineTemperature")
        self.checkBox_OilPressure = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_OilPressure.setGeometry(QtCore.QRect(560, 130, 91, 17))
        self.checkBox_OilPressure.setObjectName("checkBox_OilPressure")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setGeometry(QtCore.QRect(270, 20, 121, 211))
        self.groupBox_9.setObjectName("groupBox_9")
        self.progressBar_FuelPressure = QtWidgets.QProgressBar(self.groupBox_9)
        self.progressBar_FuelPressure.setGeometry(QtCore.QRect(20, 40, 31, 141))
        self.progressBar_FuelPressure.setMaximum(6)
        self.progressBar_FuelPressure.setProperty("value", 0)
        self.progressBar_FuelPressure.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_FuelPressure.setObjectName("progressBar_FuelPressure")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox_9)
        self.layoutWidget_3.setGeometry(QtCore.QRect(60, 160, 61, 16))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_4.addWidget(self.label_18)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(400, 20, 121, 211))
        self.groupBox_10.setObjectName("groupBox_10")
        self.progressBar_BatteryVoltage = QtWidgets.QProgressBar(self.groupBox_10)
        self.progressBar_BatteryVoltage.setGeometry(QtCore.QRect(20, 40, 41, 141))
        self.progressBar_BatteryVoltage.setMaximum(15)
        self.progressBar_BatteryVoltage.setProperty("value", -1)
        self.progressBar_BatteryVoltage.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_BatteryVoltage.setObjectName("progressBar_BatteryVoltage")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_10)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 160, 41, 16))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(140, 20, 121, 211))
        self.groupBox_6.setObjectName("groupBox_6")
        self.progressBar_OilPressure = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_OilPressure.setGeometry(QtCore.QRect(20, 40, 31, 141))
        self.progressBar_OilPressure.setMaximum(8)
        self.progressBar_OilPressure.setProperty("value", 0)
        self.progressBar_OilPressure.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_OilPressure.setObjectName("progressBar_OilPressure")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(60, 160, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 160, 51, 16))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_17.setGeometry(QtCore.QRect(530, 20, 171, 211))
        self.groupBox_17.setObjectName("groupBox_17")
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_21.setGeometry(QtCore.QRect(10, 30, 151, 41))
        self.groupBox_21.setTitle("")
        self.groupBox_21.setObjectName("groupBox_21")
        self.radioButton_FanRelay = QtWidgets.QRadioButton(self.groupBox_21)
        self.radioButton_FanRelay.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.radioButton_FanRelay.setObjectName("radioButton_FanRelay")
        self.groupBox_22 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_22.setGeometry(QtCore.QRect(10, 90, 151, 41))
        self.groupBox_22.setTitle("")
        self.groupBox_22.setObjectName("groupBox_22")
        self.radioButton_FuelPumpRelay = QtWidgets.QRadioButton(self.groupBox_22)
        self.radioButton_FuelPumpRelay.setGeometry(QtCore.QRect(20, 10, 101, 17))
        self.radioButton_FuelPumpRelay.setChecked(True)
        self.radioButton_FuelPumpRelay.setAutoExclusive(True)
        self.radioButton_FuelPumpRelay.setAutoRepeatDelay(300)
        self.radioButton_FuelPumpRelay.setObjectName("radioButton_FuelPumpRelay")
        self.groupBox_23 = QtWidgets.QGroupBox(self.groupBox_17)
        self.groupBox_23.setGeometry(QtCore.QRect(10, 150, 151, 41))
        self.groupBox_23.setTitle("")
        self.groupBox_23.setObjectName("groupBox_23")
        self.radioButton_SparkcutRelay = QtWidgets.QRadioButton(self.groupBox_23)
        self.radioButton_SparkcutRelay.setGeometry(QtCore.QRect(20, 10, 101, 17))
        self.radioButton_SparkcutRelay.setObjectName("radioButton_SparkcutRelay")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 370, 291, 201))
        self.groupBox_8.setObjectName("groupBox_8")
        self.dial_WheelPos = QtWidgets.QDial(self.groupBox_8)
        self.dial_WheelPos.setGeometry(QtCore.QRect(50, 30, 131, 161))
        self.dial_WheelPos.setMinimum(-120)
        self.dial_WheelPos.setMaximum(120)
        self.dial_WheelPos.setPageStep(10)
        self.dial_WheelPos.setInvertedAppearance(False)
        self.dial_WheelPos.setInvertedControls(True)
        self.dial_WheelPos.setObjectName("dial_WheelPos")
        self.label_19 = QtWidgets.QLabel(self.groupBox_8)
        self.label_19.setGeometry(QtCore.QRect(180, 100, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setScaledContents(False)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_8)
        self.label_20.setGeometry(QtCore.QRect(260, 100, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(450, 240, 231, 101))
        self.groupBox_11.setObjectName("groupBox_11")
        self.progressBar_TPS = QtWidgets.QProgressBar(self.groupBox_11)
        self.progressBar_TPS.setGeometry(QtCore.QRect(20, 32, 191, 31))
        self.progressBar_TPS.setProperty("value", 24)
        self.progressBar_TPS.setObjectName("progressBar_TPS")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 20, 421, 331))
        self.groupBox_12.setObjectName("groupBox_12")
        # gráfico do diagrama GG
        self.graphicsView_DiagramaGG = pg.GraphicsLayoutWidget(self.groupBox_12)
        self.graphicsView_DiagramaGG.setGeometry(QtCore.QRect(20, 30, 371, 271))
        self.graphicsView_DiagramaGG.setObjectName("graphicsView_DiagramaGG")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_13.setGeometry(QtCore.QRect(450, 20, 231, 201))
        self.groupBox_13.setObjectName("groupBox_13")
        self.progressBar_FrontBreakBalance = QtWidgets.QProgressBar(self.groupBox_13)
        self.progressBar_FrontBreakBalance.setGeometry(QtCore.QRect(40, 50, 171, 31))
        self.progressBar_FrontBreakBalance.setProperty("value", 24)
        self.progressBar_FrontBreakBalance.setObjectName("progressBar_FrontBreakBalance")
        self.label_67 = QtWidgets.QLabel(self.groupBox_13)
        self.label_67.setGeometry(QtCore.QRect(80, 110, 91, 16))
        self.label_67.setObjectName("label_67")
        self.label_66 = QtWidgets.QLabel(self.groupBox_13)
        self.label_66.setGeometry(QtCore.QRect(80, 30, 91, 16))
        self.label_66.setObjectName("label_66")
        self.progressBar_RearBreakBalance = QtWidgets.QProgressBar(self.groupBox_13)
        self.progressBar_RearBreakBalance.setGeometry(QtCore.QRect(40, 130, 171, 31))
        self.progressBar_RearBreakBalance.setProperty("value", 24)
        self.progressBar_RearBreakBalance.setObjectName("progressBar_RearBreakBalance")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_14.setGeometry(QtCore.QRect(320, 370, 171, 201))
        self.groupBox_14.setObjectName("groupBox_14")
        self.progressBar_FrontBreakPressure = QtWidgets.QProgressBar(self.groupBox_14)
        self.progressBar_FrontBreakPressure.setGeometry(QtCore.QRect(30, 40, 41, 141))
        self.progressBar_FrontBreakPressure.setMaximum(70)
        self.progressBar_FrontBreakPressure.setProperty("value", 24)
        self.progressBar_FrontBreakPressure.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_FrontBreakPressure.setObjectName("progressBar_FrontBreakPressure")
        self.label_36 = QtWidgets.QLabel(self.groupBox_14)
        self.label_36.setGeometry(QtCore.QRect(118, 160, 21, 14))
        self.label_36.setObjectName("label_36")
        self.label_65 = QtWidgets.QLabel(self.groupBox_14)
        self.label_65.setGeometry(QtCore.QRect(90, 160, 22, 14))
        self.label_65.setObjectName("label_65")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_15.setGeometry(QtCore.QRect(509, 370, 171, 201))
        self.groupBox_15.setObjectName("groupBox_15")
        self.progressBar_RearBreakPressure = QtWidgets.QProgressBar(self.groupBox_15)
        self.progressBar_RearBreakPressure.setGeometry(QtCore.QRect(30, 40, 41, 141))
        self.progressBar_RearBreakPressure.setMaximum(70)
        self.progressBar_RearBreakPressure.setProperty("value", 24)
        self.progressBar_RearBreakPressure.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_RearBreakPressure.setObjectName("progressBar_RearBreakPressure")
        self.label_68 = QtWidgets.QLabel(self.groupBox_15)
        self.label_68.setGeometry(QtCore.QRect(118, 160, 21, 14))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.groupBox_15)
        self.label_69.setGeometry(QtCore.QRect(90, 160, 22, 14))
        self.label_69.setObjectName("label_69")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_20.setGeometry(QtCore.QRect(30, 20, 661, 291))
        self.groupBox_20.setObjectName("groupBox_20")
        self.tableWidget_StrainGauge = QtWidgets.QTableWidget(self.groupBox_20)
        self.tableWidget_StrainGauge.setGeometry(QtCore.QRect(40, 50, 351, 211))
        self.tableWidget_StrainGauge.setObjectName("tableWidget_StrainGauge")
        self.tableWidget_StrainGauge.setColumnCount(3)
        self.tableWidget_StrainGauge.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_StrainGauge.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(8, 2, item)
        self.tableWidget_StrainGauge.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget_StrainGauge.verticalHeader().setDefaultSectionSize(20)
        self.progressBar_WeightDistribuition4 = QtWidgets.QProgressBar(self.groupBox_20)
        self.progressBar_WeightDistribuition4.setGeometry(QtCore.QRect(530, 180, 31, 61))
        self.progressBar_WeightDistribuition4.setMaximum(150)
        self.progressBar_WeightDistribuition4.setProperty("value", 24)
        self.progressBar_WeightDistribuition4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_WeightDistribuition4.setObjectName("progressBar_WeightDistribuition4")
        self.progressBar_WeightDistribuition3 = QtWidgets.QProgressBar(self.groupBox_20)
        self.progressBar_WeightDistribuition3.setGeometry(QtCore.QRect(470, 180, 31, 61))
        self.progressBar_WeightDistribuition3.setMaximum(150)
        self.progressBar_WeightDistribuition3.setProperty("value", 24)
        self.progressBar_WeightDistribuition3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_WeightDistribuition3.setObjectName("progressBar_WeightDistribuition3")
        self.progressBar_WeightDistribuition2 = QtWidgets.QProgressBar(self.groupBox_20)
        self.progressBar_WeightDistribuition2.setGeometry(QtCore.QRect(530, 90, 31, 61))
        self.progressBar_WeightDistribuition2.setMaximum(150)
        self.progressBar_WeightDistribuition2.setProperty("value", 24)
        self.progressBar_WeightDistribuition2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_WeightDistribuition2.setObjectName("progressBar_WeightDistribuition2")
        self.progressBar_WeightDistribuition1 = QtWidgets.QProgressBar(self.groupBox_20)
        self.progressBar_WeightDistribuition1.setGeometry(QtCore.QRect(470, 90, 31, 61))
        self.progressBar_WeightDistribuition1.setMaximum(150)
        self.progressBar_WeightDistribuition1.setProperty("value", 24)
        self.progressBar_WeightDistribuition1.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_WeightDistribuition1.setObjectName("progressBar_WeightDistribuition1")
        self.label_129 = QtWidgets.QLabel(self.groupBox_20)
        self.label_129.setGeometry(QtCore.QRect(460, 40, 121, 16))
        self.label_129.setObjectName("label_129")
        self.tabWidget.addTab(self.tab_5, "")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(1200, 560, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.pushButton_PauseProgram = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_PauseProgram.setGeometry(QtCore.QRect(1180, 420, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_PauseProgram.setFont(font)
        self.pushButton_PauseProgram.setObjectName("pushButton_PauseProgram")
        self.pushButton_StartProgram = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_StartProgram.setGeometry(QtCore.QRect(1180, 370, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_StartProgram.setFont(font)
        self.pushButton_StartProgram.setObjectName("pushButton_StartProgram")
        self.groupBox_18 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_18.setGeometry(QtCore.QRect(750, 0, 401, 701))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_18.setFont(font)
        self.groupBox_18.setObjectName("groupBox_18")
        self.tableWidget_Package1 = QtWidgets.QTableWidget(self.groupBox_18)
        self.tableWidget_Package1.setGeometry(QtCore.QRect(20, 30, 351, 191))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_Package1.setFont(font)
        self.tableWidget_Package1.setObjectName("tableWidget_Package1")
        self.tableWidget_Package1.setColumnCount(3)
        self.tableWidget_Package1.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(7, 2, item)
        self.tableWidget_Package1.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget_Package1.verticalHeader().setDefaultSectionSize(20)
        self.label_38 = QtWidgets.QLabel(self.groupBox_18)
        self.label_38.setGeometry(QtCore.QRect(20, 10, 71, 20))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_18)
        self.label_39.setGeometry(QtCore.QRect(20, 220, 71, 20))
        self.label_39.setObjectName("label_39")
        self.tableWidget_Package2 = QtWidgets.QTableWidget(self.groupBox_18)
        self.tableWidget_Package2.setGeometry(QtCore.QRect(20, 240, 351, 241))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_Package2.setFont(font)
        self.tableWidget_Package2.setObjectName("tableWidget_Package2")
        self.tableWidget_Package2.setColumnCount(3)
        self.tableWidget_Package2.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(9, 2, item)
        self.tableWidget_Package2.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget_Package2.verticalHeader().setDefaultSectionSize(20)
        self.label_44 = QtWidgets.QLabel(self.groupBox_18)
        self.label_44.setGeometry(QtCore.QRect(20, 480, 71, 20))
        self.label_44.setObjectName("label_44")
        self.tableWidget_Package3 = QtWidgets.QTableWidget(self.groupBox_18)
        self.tableWidget_Package3.setGeometry(QtCore.QRect(20, 500, 351, 191))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_Package3.setFont(font)
        self.tableWidget_Package3.setObjectName("tableWidget_Package3")
        self.tableWidget_Package3.setColumnCount(3)
        self.tableWidget_Package3.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Package3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(7, 2, item)
        self.tableWidget_Package3.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget_Package3.verticalHeader().setDefaultSectionSize(20)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(1160, 150, 181, 81))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.pushButton_SaveSetupValues = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SaveSetupValues.setGeometry(QtCore.QRect(1180, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SaveSetupValues.setFont(font)
        self.pushButton_SaveSetupValues.setObjectName("pushButton_SaveSetupValues")
        self.pushButton_Exit.raise_()
        self.pushButton_PauseProgram.raise_()
        self.pushButton_StartProgram.raise_()
        self.groupBox_18.raise_()
        self.label_28.raise_()
        self.tabWidget.raise_()
        self.pushButton_SaveSetupValues.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUpdate_Serial_Ports = QtWidgets.QAction(MainWindow)
        self.actionUpdate_Serial_Ports.setObjectName("actionUpdate_Serial_Ports")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpdate_Serial_Ports)
        self.menubar.addAction(self.menuFile.menuAction())

        # inicializações
        self.save = 0  # variável que define se salva dados no txt 0= não salva, 1=salva
        self.stop = 1  # variável que define se o programa está pausado/parado 0= não parado, 1= parado
        self.label_12.setText("No saving...")  # informa na interface que os dados não estão sendo salvos
        self.arq = 0
        self.arq_laptime = 0
        self.array_temp = np.array([]).astype('int')
        self.array_fuel_p = np.array([]).astype('int')
        self.array_oil_p = np.array([]).astype('int')
        self.array_battery = np.array([]).astype('int')
        self.array_leitura = np.array([]).astype('int')
        self.x = np.array([]).astype('int')
        self.y = np.array([]).astype('int')
        self.w1 = self.graphicsView_DiagramaGG.addPlot()
        self.w1.setRange(xRange=[-2, 2])
        self.w1.setRange(yRange=[-2, 2])
        self.s = np.array([]).astype('int')
        self.divisor = 1
        self.array_lap = np.array([]).astype('int')
        self.aux_time = np.array([0]).astype('int')
        # Vetores para mostrar últimos dados recebidos (TEMPORARIO)
        self.buffer1 = np.array([]).astype('int')
        self.buffer2 = np.array([]).astype('int')
        self.buffer3 = np.array([]).astype('int')
        self.buffer4 = np.array([]).astype('int')
        self.buffer5 = np.array([]).astype('int')
        self.buffer6 = np.array([]).astype('int')
        self.sec = 0
        self.cont = 0
        self.exe_time = 0

        # ações
        self.pushButton_Exit.clicked.connect(self.exit)  # botão para fechar a interface
        self.pushButton_PauseProgram.clicked.connect(self.stop_program)  # botão para pausar o programa
        self.pushButton_StartProgram.clicked.connect(self.start_program)  # botão para iniciar o programa
        self.pushButton_SaveFile.clicked.connect(self.gravacao)  # botão para iniciar gravação de dados no txt
        self.pushButton_StopSaveFile.clicked.connect(self.stop_gravacao)  # botão para parar a gravação de dados txt
        self.pushButton_UpdatePorts.clicked.connect(
            self.update_ports)  # botão para atualizar as portas seriis disponíveis
        self.pushButton_SaveSetupValues.clicked.connect(
            lambda: self.update_setup(self.spinBox_WheelPosMax, self.spinBox_WheelPosMin,
                                      self.lineEdit_CalibrationConstant,
                                      self.lineEdit_SetupCar, self.lineEdit_SetupTrack, self.lineEdit_SetupDriver,
                                      self.lineEdit_SetupTemperature, self.lineEdit_SetupAntiroll,
                                      self.lineEdit_SetupTirePressureFront, self.lineEdit_SetupTirePressureRear,
                                      self.lineEdit_SetupWingAttackAngle, self.lineEdit_SetupEngineMap,
                                      self.lineEdit_SetupBalanceBar, self.lineEdit_SetupDifferential,self.lineEdit_SetupAcquisitionRate,
                                      self.textEdit_SetupComments))  # botão para atualizar os dados de setup no arquivo txt
        self.actionExit.triggered.connect(self.exit)  # realiza a ação para fechar a interface

        self.comboBox_SerialPorts.addItems(self.serial_ports())  # mostra as portas seriais disponíveis
        self.comboBox_SerialPorts.currentIndexChanged.connect(self.selection_port)
        self.comboBox_Baudrate.addItems(
            ["38400", "1200", "2400", "9600", "19200", "57600", "115200"])  # mostra os baudrates disponíveis
        self.comboBox_Baudrate.currentIndexChanged.connect(self.selection_baudrate)
        self.pixmap = QPixmap("image1.png")
        self.label_28.setPixmap(self.pixmap)
        self.update_values(self.spinBox_WheelPosMax, self.spinBox_WheelPosMin, self.lineEdit_CalibrationConstant,
                           self.lineEdit_SetupCar,
                           self.lineEdit_SetupTrack, self.lineEdit_SetupDriver,
                           self.lineEdit_SetupTemperature, self.lineEdit_SetupAntiroll,
                           self.lineEdit_SetupTirePressureFront, self.lineEdit_SetupTirePressureRear,
                           self.lineEdit_SetupWingAttackAngle,
                           self.lineEdit_SetupEngineMap, self.lineEdit_SetupBalanceBar,
                           self.lineEdit_SetupDifferential,
                           self.textEdit_SetupComments)  # inicializa os valores de setup de acordo com o arquivo setup

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "XBEE SERIAL PORT SETTINGS"))
        self.label_2.setText(_translate("MainWindow", "Serial Resource Name"))
        self.label_35.setText(_translate("MainWindow", "Update Time [s]"))
        self.label_41.setText(_translate("MainWindow", "Baud Rate"))
        self.pushButton_UpdatePorts.setText(_translate("MainWindow", "Update Ports"))
        self.groupBox_3.setTitle(_translate("MainWindow", "DATA PACK"))
        self.label_3.setText(_translate("MainWindow", "String read at buffer"))
        self.groupBox_4.setTitle(_translate("MainWindow", "DATA POSITION"))
        self.label_4.setText(_translate("MainWindow", "Battery"))
        self.label_5.setText(_translate("MainWindow", "Eng Temp "))
        self.label_14.setText(_translate("MainWindow", "Fuel P"))
        self.label_21.setText(_translate("MainWindow", "Oil P"))
        self.label_22.setText(_translate("MainWindow", "TPS"))
        self.label_23.setText(_translate("MainWindow", "Fuel Pump Relay"))
        self.label_24.setText(_translate("MainWindow", "Break P (F)"))
        self.label_25.setText(_translate("MainWindow", "Break P (R)"))
        self.label_26.setText(_translate("MainWindow", "Speed"))
        self.label_27.setText(_translate("MainWindow", "Sparkcut Relay"))
        self.label_37.setText(_translate("MainWindow", "Time "))
        self.label_40.setText(_translate("MainWindow", "Fan Relay"))
        self.label.setText(_translate("MainWindow", "Package 1"))
        self.label_42.setText(_translate("MainWindow", "Package 2"))
        self.label_43.setText(_translate("MainWindow", "Package 3"))
        self.label_45.setText(_translate("MainWindow", "Time"))
        self.label_46.setText(_translate("MainWindow", "Relay Box T"))
        self.label_47.setText(_translate("MainWindow", "Time "))
        self.label_33.setText(_translate("MainWindow", "Y_Accel"))
        self.label_48.setText(_translate("MainWindow", "Z_Accel"))
        self.label_34.setText(_translate("MainWindow", "X_Accel"))
        self.label_51.setText(_translate("MainWindow", "Wheel Pos"))
        self.label_60.setText(_translate("MainWindow", "Current"))
        self.label_61.setText(_translate("MainWindow", "Beacon"))
        self.label_62.setText(_translate("MainWindow", "Break Temp (R)"))
        self.label_63.setText(_translate("MainWindow", "Break Temp (F)"))
        self.label_128.setText(_translate("MainWindow", "Susp Pos"))
        self.groupBox_16.setTitle(_translate("MainWindow", "WHEEL POSITION CALIBRATION"))
        self.label_29.setText(_translate("MainWindow", "Wheel Pos Max"))
        self.label_30.setText(_translate("MainWindow", "Wheel Pos Min"))
        self.label_49.setText(_translate("MainWindow", "Current Wheel Pos"))
        self.groupBox_38.setTitle(_translate("MainWindow", "STRAIN GAUGE"))
        self.label_64.setText(_translate("MainWindow", "Calibration Constant"))
        self.groupBox_39.setTitle(_translate("MainWindow", "LAP TIME"))
        self.label_70.setText(_translate("MainWindow", "Last Lap"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Settings"))
        self.groupBox_19.setTitle(_translate("MainWindow", "CAR SETUP"))
        self.label_31.setText(_translate("MainWindow", "Driver:"))
        self.label_32.setText(_translate("MainWindow", "Car:"))
        self.lineEdit_SetupCar.setText(_translate("MainWindow", "TR-06"))
        self.label_50.setText(_translate("MainWindow", "Track:"))
        self.label_52.setText(_translate("MainWindow", "Temperature:"))
        self.label_53.setText(_translate("MainWindow", "Antiroll:"))
        self.label_54.setText(_translate("MainWindow", "Tire Pressure"))
        self.label_55.setText(_translate("MainWindow", "Wing attack"))
        self.label_56.setText(_translate("MainWindow", "Engine map:"))
        self.label_57.setText(_translate("MainWindow", "Balance Bar:"))
        self.label_58.setText(_translate("MainWindow", "Differential:"))
        self.label_59.setText(_translate("MainWindow", "Rear:"))
        self.label_71.setText(_translate("MainWindow", "Front:"))
        self.label_72.setText(_translate("MainWindow", "Comments:"))
        self.label_127.setText(_translate("MainWindow", "angle:"))
        self.label_73.setText(_translate("MainWindow", "Acquisition Rate:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "FILE SETTINGS"))
        self.label_11.setText(_translate("MainWindow", "File Name (Ex.:TesteRBC)"))
        self.label_12.setText(_translate("MainWindow", "No saving..."))
        self.label_13.setText(_translate("MainWindow", "Choose File"))
        self.pushButton_SaveFile.setText(_translate("MainWindow", "Save"))
        self.pushButton_StopSaveFile.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Setup"))
        self.groupBox_5.setTitle(_translate("MainWindow", "ENGINE TEMPERATURE"))
        self.progressBar_EngineTemperature.setFormat(_translate("MainWindow", "%p"))
        self.label_6.setText(_translate("MainWindow", "49"))
        self.label_9.setText(_translate("MainWindow", "ºC"))
        self.groupBox_7.setTitle(_translate("MainWindow", "PLOT"))
        self.checkBox_Voltage.setText(_translate("MainWindow", "Voltage"))
        self.checkBox_FuelPressure.setText(_translate("MainWindow", "Fuel Pressure"))
        self.checkBox_EngineTemperature.setText(_translate("MainWindow", "Engine Temp."))
        self.checkBox_OilPressure.setText(_translate("MainWindow", "Oil Pressure"))
        self.groupBox_9.setTitle(_translate("MainWindow", "FUEL PRESSURE"))
        self.progressBar_FuelPressure.setFormat(_translate("MainWindow", "%p"))
        self.label_17.setText(_translate("MainWindow", "49"))
        self.label_18.setText(_translate("MainWindow", "Bar"))
        self.groupBox_10.setTitle(_translate("MainWindow", "BATTERY VOLTAGE"))
        self.progressBar_BatteryVoltage.setFormat(_translate("MainWindow", "%p"))
        self.label_15.setText(_translate("MainWindow", "49"))
        self.label_16.setText(_translate("MainWindow", "V"))
        self.groupBox_6.setTitle(_translate("MainWindow", "OIL PRESSURE"))
        self.progressBar_OilPressure.setFormat(_translate("MainWindow", "%p"))
        self.label_10.setText(_translate("MainWindow", "49"))
        self.label_8.setText(_translate("MainWindow", "Bar"))
        self.groupBox_17.setTitle(_translate("MainWindow", "RELAY ACTIVATION"))
        self.radioButton_FanRelay.setText(_translate("MainWindow", "Fan Relay"))
        self.radioButton_FuelPumpRelay.setText(_translate("MainWindow", "Fuel Pump Relay"))
        self.radioButton_SparkcutRelay.setText(_translate("MainWindow", "Sparkcut Relay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Engine | Battery | Relay"))
        self.groupBox_8.setTitle(_translate("MainWindow", "WHEEL POS (Deg)"))
        self.label_19.setText(_translate("MainWindow", "1"))
        self.label_20.setText(_translate("MainWindow", "º"))
        self.groupBox_11.setTitle(_translate("MainWindow", "TPS"))
        self.progressBar_TPS.setFormat(_translate("MainWindow", "%p%"))
        self.groupBox_12.setTitle(_translate("MainWindow", "G - G DIAGRAM"))
        self.groupBox_13.setTitle(_translate("MainWindow", "BREAK BALANCE"))
        self.label_67.setText(_translate("MainWindow", "Rear Break"))
        self.label_66.setText(_translate("MainWindow", "Front Break"))
        self.groupBox_14.setTitle(_translate("MainWindow", "FRONT BREAK PRESSURE"))
        self.progressBar_FrontBreakPressure.setFormat(_translate("MainWindow", "%p"))
        self.label_36.setText(_translate("MainWindow", "Bar"))
        self.label_65.setText(_translate("MainWindow", "49"))
        self.groupBox_15.setTitle(_translate("MainWindow", "REAR BREAK PRESSURE"))
        self.progressBar_RearBreakPressure.setFormat(_translate("MainWindow", "%p"))
        self.label_68.setText(_translate("MainWindow", "Bar"))
        self.label_69.setText(_translate("MainWindow", "49"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Wheel | TPS | Brake"))
        self.groupBox_20.setTitle(_translate("MainWindow", "STRAIN GAUGE"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_StrainGauge.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_StrainGauge.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.tableWidget_StrainGauge.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VALUE"))
        item = self.tableWidget_StrainGauge.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UNITY"))
        __sortingEnabled = self.tableWidget_StrainGauge.isSortingEnabled()
        self.tableWidget_StrainGauge.setSortingEnabled(False)
        item = self.tableWidget_StrainGauge.item(0, 0)
        item.setText(_translate("MainWindow", "P1 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(0, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(1, 0)
        item.setText(_translate("MainWindow", "P2 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(1, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(2, 0)
        item.setText(_translate("MainWindow", "P3 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(2, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(3, 0)
        item.setText(_translate("MainWindow", "P4 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(3, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(4, 0)
        item.setText(_translate("MainWindow", "P5 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(4, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(5, 0)
        item.setText(_translate("MainWindow", "P6 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(5, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(6, 0)
        item.setText(_translate("MainWindow", "P7 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(6, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(7, 0)
        item.setText(_translate("MainWindow", "P8 Strain Gauge"))
        item = self.tableWidget_StrainGauge.item(7, 2)
        item.setText(_translate("MainWindow", "MPa"))
        item = self.tableWidget_StrainGauge.item(8, 0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_StrainGauge.item(8, 2)
        item.setText(_translate("MainWindow", "ms"))
        self.tableWidget_StrainGauge.setSortingEnabled(__sortingEnabled)
        self.progressBar_WeightDistribuition4.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_WeightDistribuition3.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_WeightDistribuition2.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_WeightDistribuition1.setFormat(_translate("MainWindow", "%p"))
        self.label_129.setText(_translate("MainWindow", "Weight Distribuition (Kg)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Strain Gauge"))
        self.pushButton_Exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_PauseProgram.setText(_translate("MainWindow", "PAUSE PROGRAM"))
        self.pushButton_StartProgram.setText(_translate("MainWindow", "START PROGRAM"))
        self.groupBox_18.setTitle(_translate("MainWindow", "Data List"))
        item = self.tableWidget_Package1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_Package1.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_Package1.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_Package1.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_Package1.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_Package1.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_Package1.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_Package1.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_Package1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.tableWidget_Package1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VALUE"))
        item = self.tableWidget_Package1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UNITY"))
        __sortingEnabled = self.tableWidget_Package1.isSortingEnabled()
        self.tableWidget_Package1.setSortingEnabled(False)
        item = self.tableWidget_Package1.item(0, 0)
        item.setText(_translate("MainWindow", "Acceleration X"))
        item = self.tableWidget_Package1.item(0, 2)
        item.setText(_translate("MainWindow", "g"))
        item = self.tableWidget_Package1.item(1, 0)
        item.setText(_translate("MainWindow", "Acceleration Y"))
        item = self.tableWidget_Package1.item(1, 2)
        item.setText(_translate("MainWindow", "g"))
        item = self.tableWidget_Package1.item(2, 0)
        item.setText(_translate("MainWindow", "Acceleration Z"))
        item = self.tableWidget_Package1.item(2, 2)
        item.setText(_translate("MainWindow", "g"))
        item = self.tableWidget_Package1.item(3, 0)
        item.setText(_translate("MainWindow", "Front Speed"))
        item = self.tableWidget_Package1.item(3, 2)
        item.setText(_translate("MainWindow", "km/h"))
        item = self.tableWidget_Package1.item(4, 0)
        item.setText(_translate("MainWindow", "Rear Speed"))
        item = self.tableWidget_Package1.item(4, 2)
        item.setText(_translate("MainWindow", "km/h"))
        item = self.tableWidget_Package1.item(5, 0)
        item.setText(_translate("MainWindow", "Sparkcut Relay"))
        item = self.tableWidget_Package1.item(5, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget_Package1.item(6, 0)
        item.setText(_translate("MainWindow", "Suspention Pos."))
        item = self.tableWidget_Package1.item(6, 2)
        item.setText(_translate("MainWindow", "mm"))
        item = self.tableWidget_Package1.item(7, 0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_Package1.item(7, 2)
        item.setText(_translate("MainWindow", "ms"))
        self.tableWidget_Package1.setSortingEnabled(__sortingEnabled)
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p>PACKAGE 1</p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p>PACKAGE 2</p></body></html>"))
        item = self.tableWidget_Package2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_Package2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_Package2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_Package2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_Package2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_Package2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_Package2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_Package2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_Package2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_Package2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_Package2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.tableWidget_Package2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VALUE"))
        item = self.tableWidget_Package2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UNITY"))
        __sortingEnabled = self.tableWidget_Package2.isSortingEnabled()
        self.tableWidget_Package2.setSortingEnabled(False)
        item = self.tableWidget_Package2.item(0, 0)
        item.setText(_translate("MainWindow", "Beacon"))
        item = self.tableWidget_Package2.item(0, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget_Package2.item(1, 0)
        item.setText(_translate("MainWindow", "Break Pressure(F)"))
        item = self.tableWidget_Package2.item(1, 2)
        item.setText(_translate("MainWindow", "Bar"))
        item = self.tableWidget_Package2.item(2, 0)
        item.setText(_translate("MainWindow", "Break Pressure(R)"))
        item = self.tableWidget_Package2.item(2, 2)
        item.setText(_translate("MainWindow", "Bar"))
        item = self.tableWidget_Package2.item(3, 0)
        item.setText(_translate("MainWindow", "Current"))
        item = self.tableWidget_Package2.item(3, 2)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget_Package2.item(4, 0)
        item.setText(_translate("MainWindow", "Fuel Pressure"))
        item = self.tableWidget_Package2.item(4, 2)
        item.setText(_translate("MainWindow", "Bar"))
        item = self.tableWidget_Package2.item(5, 0)
        item.setText(_translate("MainWindow", "Oil Pressure"))
        item = self.tableWidget_Package2.item(5, 2)
        item.setText(_translate("MainWindow", "Bar"))
        item = self.tableWidget_Package2.item(6, 0)
        item.setText(_translate("MainWindow", "RPM"))
        item = self.tableWidget_Package2.item(6, 2)
        item.setText(_translate("MainWindow", "km/h"))
        item = self.tableWidget_Package2.item(7, 0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_Package2.item(7, 2)
        item.setText(_translate("MainWindow", "ms"))
        item = self.tableWidget_Package2.item(8, 0)
        item.setText(_translate("MainWindow", "TPS"))
        item = self.tableWidget_Package2.item(8, 2)
        item.setText(_translate("MainWindow", "%"))
        item = self.tableWidget_Package2.item(9, 0)
        item.setText(_translate("MainWindow", "Wheel Position"))
        item = self.tableWidget_Package2.item(9, 2)
        item.setText(_translate("MainWindow", "Degree ( º )"))
        self.tableWidget_Package2.setSortingEnabled(__sortingEnabled)
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p>PACKAGE 3</p></body></html>"))
        item = self.tableWidget_Package3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_Package3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_Package3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_Package3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_Package3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_Package3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_Package3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_Package3.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_Package3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.tableWidget_Package3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VALUE"))
        item = self.tableWidget_Package3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UNITY"))
        __sortingEnabled = self.tableWidget_Package3.isSortingEnabled()
        self.tableWidget_Package3.setSortingEnabled(False)
        item = self.tableWidget_Package3.item(0, 0)
        item.setText(_translate("MainWindow", "Battery Voltage"))
        item = self.tableWidget_Package3.item(0, 2)
        item.setText(_translate("MainWindow", "Volts"))
        item = self.tableWidget_Package3.item(1, 0)
        item.setText(_translate("MainWindow", "Break Temp. (F)"))
        item = self.tableWidget_Package3.item(1, 2)
        item.setText(_translate("MainWindow", "ºC"))
        item = self.tableWidget_Package3.item(2, 0)
        item.setText(_translate("MainWindow", "Break Temp. (R)"))
        item = self.tableWidget_Package3.item(2, 2)
        item.setText(_translate("MainWindow", "ºC"))
        item = self.tableWidget_Package3.item(3, 0)
        item.setText(_translate("MainWindow", "Engine Temp."))
        item = self.tableWidget_Package3.item(3, 2)
        item.setText(_translate("MainWindow", "ºC"))
        item = self.tableWidget_Package3.item(4, 0)
        item.setText(_translate("MainWindow", "Fan Realy"))
        item = self.tableWidget_Package3.item(4, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget_Package3.item(5, 0)
        item.setText(_translate("MainWindow", "Fuel Pump Relay"))
        item = self.tableWidget_Package3.item(5, 2)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget_Package3.item(6, 0)
        item.setText(_translate("MainWindow", "Relay Box T"))
        item = self.tableWidget_Package3.item(6, 2)
        item.setText(_translate("MainWindow", "ºC"))
        item = self.tableWidget_Package3.item(7, 0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget_Package3.item(7, 2)
        item.setText(_translate("MainWindow", "ms"))
        self.tableWidget_Package3.setSortingEnabled(__sortingEnabled)
        self.pushButton_SaveSetupValues.setText(_translate("MainWindow", "SAVE VALUES"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUpdate_Serial_Ports.setText(_translate("MainWindow", "Update Serial Ports"))

        # cores do gráfico
        self.checkBox_Voltage.setText(_translate("MainWindow", "Voltage"))
        self.checkBox_OilPressure.setStyleSheet('color:blue')
        self.checkBox_FuelPressure.setText(_translate("MainWindow", "Fuel Pressure"))
        self.checkBox_FuelPressure.setStyleSheet('color:green')
        self.checkBox_EngineTemperature.setText(_translate("MainWindow", "Engine Temp."))
        self.checkBox_EngineTemperature.setStyleSheet('color:red')
        self.checkBox_OilPressure.setText(_translate("MainWindow", "Oil Pressure "))
        self.checkBox_OilPressure.setStyleSheet('color:yellow')

        # A função update_values atualiza os campos que já haviam sido definidos em utilizações ateriores da interface
        # Ela serve para que não seja necessário atualizar todos os campos sempre que for necessária o reinício da interface

    def update_values(self, spinBox_WheelPosMax, spinBox_WheelPosMin, lineEdit_CalibrationConstant, lineEdit_SetupCar,
                      lineEdit_SetupTrack, lineEdit_SetupDriver,
                      lineEdit_SetupTemperature, lineEdit_SetupAntiroll, lineEdit_SetupTirePressureFront,
                      lineEdit_SetupTirePressureRear, lineEdit_SetupWingAttackAngle, lineEdit_SetupEngineMap,
                      lineEdit_SetupBalanceBar,
                      lineEdit_SetupDifferential, textEdit_SetupComments):
        try:
            self.setup = open('setup.txt', 'r')
            self.values = self.setup.readlines()
            self.i = 0
            while (self.i <= len(self.values) - 1):
                # caso o valor da lista na posição i seja \n significa que não foi setado, anteriormente, um valor nesse campo,
                # ou seja, ao redefinir os valores dos campos utilizando os valores salvos anteriormente, os campos devem receber ''
                self.values[self.i] = self.values[self.i].replace('\n', '')
                self.i = self.i + 1
            print(self.values)
            if (len(self.values) > 0):
                self.spinBox_WheelPosMax.setValue(int(self.values[0]))
                self.spinBox_WheelPosMin.setValue(int(self.values[1]))
                self.lineEdit_CalibrationConstant.setText(str(self.values[2]))
                self.lineEdit_SetupCar.setText(str(self.values[3]))
                self.lineEdit_SetupTrack.setText(str(self.values[4]))
                self.lineEdit_SetupDriver.setText(str(self.values[5]))
                self.lineEdit_SetupTemperature.setText(str(self.values[6]))
                self.lineEdit_SetupAntiroll.setText(str(self.values[7]))
                self.lineEdit_SetupTirePressureFront.setText(str(self.values[8]))
                self.lineEdit_SetupTirePressureRear.setText(str(self.values[9]))
                self.lineEdit_SetupWingAttackAngle.setText(str(self.values[10]))
                self.lineEdit_SetupEngineMap.setText(str(self.values[11]))
                self.lineEdit_SetupBalanceBar.setText(str(self.values[12]))
                self.lineEdit_SetupDifferential.setText(str(self.values[13]))
                self.lineEdit_SetupAcquisitionRate.setText(str(self.values[14]))
                self.textEdit_SetupComments.setText(str(self.values[15]))
            self.setup.close()
        except:
            print("ERRO")

        # As 3 funções a seguir realizam a configuração de qual porta serial será utilizada

        # função que atualiza as portas seriais disponíveis

    def update_ports(self):
        self.comboBox_SerialPorts.addItems(self.serial_ports())
        self.comboBox_SerialPorts.currentIndexChanged.connect(self.selection_port)

        # função que seleciona qual porta será utilizada

    def selection_port(self, i):
        return self.comboBox_SerialPorts.itemText(i)

        # Função que atualiza as portas seriais utilizadas

    def serial_ports(self):
        self.comboBox_SerialPorts.clear()
        """ Lists serial port names
            :raises EnvironmentError:
             On unsupported or unknown platforms
            :returns:
             A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            self.ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            self.ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            self.ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        self.result = []
        for self.port in self.ports:
            try:
                self.dados = serial.Serial(self.port)
                self.dados.close()
                self.result.append(self.port)
            except (OSError, serial.SerialException):
                pass
        return self.result

    def selection_baudrate(self, i):
        return self.comboBox_Baudrate.itemText(i)

        # Função que inicia a execução da interface

    def start_program(self):
        try:
            self.stop = 0
            self.time = self.doubleSpinBox_UpdateTime.value() * 1000
            # abre e configura a porta serial utilizando os valores definidos pelo usuário através da interface
            self.dados = serial.Serial()
            self.dados.baudrate = int(self.comboBox_Baudrate.currentText())
            self.dados.port = str(self.comboBox_SerialPorts.currentText())
            self.dados.timeout = None
            self.dados.open()
            self.now = datetime.now()
            self.arquivo = "tempos_de_volta_" + str(self.now.hour) + "_" + str(self.now.minute) + ".txt"
            self.arq_laptime = open(self.arquivo, 'w')
            self.program(self.program(self.stop))  # chama a função programa e passa por parãmetro o valor de stop
        # O erro de porta serial é analisado pela exceção serial.SerialException. Esse erro é tratado pausando o programa e
        # utilizando uma caixa de diálogo, a qual informa ao usuário o erro encontrado
        except serial.serialutil.SerialException:
            self.stop_program()
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Error!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.setText(
                "<center>Failed to receive data!<center> \n\n <center>Check Serial Ports and Telemetry System.<center>")
            dlg.exec_()

        # Função que executa o programa. Essa função verifica se o programa deve ser executado. Em caso afirmativo, é feita
        # a leitura da porta serial e é chamada a função que inicia o tratamento dos dados

    def program(self, stop):
        try:
            if (self.stop == 0):
                # A variável self.sec recebe o primeiro tempo
                # A função tempo retorna um valor o qual refere-se a quantos segundos se passaram desde um data pre-estabelecida pelo SO
                # Sendo assim, para obter o tempo de execução deve-se fazer tempofinal-tempoinicial. Isso é feito após a outra chamada da função tempo, a qual retorna o tempo final
                self.sec = time.time()

                # O loop verifica quantos bytes estão sendo recebidos pela porta serial. Enquanto esse valor for igual a
                # 0 o programa permanece no loop o qual não realiza nenhum comando
                # As duas variáveis a seguir são usadas para guardar os valores lidos na porta serial
                # São usadas duas variáveis pois é necessário converter os valores lidos para inteiro antes de saber quais dados eles represetam
                # Alguns dados são usados como unsigned e outro como signed, por isso alguns dados são gravados das duas maneiras
                self.leitura = np.array([]).astype('int')
                self.leiturasigned = np.array([]).astype('int')

                # As linhas a seguir realizam a leitura da porta serial byte a byte
                while True:
                    while (self.dados.inWaiting() == 0):
                        pass
                    self.byte = self.dados.read(1)  # dado com formato de byte
                    self.byteunsigned = int.from_bytes(self.byte, byteorder='big',
                                                       signed=False)  # dado com formato de int
                    self.bytesigned = int.from_bytes(self.byte, byteorder='big',
                                                     signed=True)  # dado com formato de int
                    self.leitura = np.append(self.leitura, self.byteunsigned)

                    # Apenas alguns dados do pacote 1 são usados como signed.
                    # Dessa forma, apenas quando estiver começando a leitura de um pacote ou se o pacote que está sendo lido é o pacote 1 é dada continuidade na definição do vetor de dados signed
                    if (self.leiturasigned.size == 0 or (self.leiturasigned[0]) == 1):
                        self.leiturasigned = np.append(self.leiturasigned, self.bytesigned)
                    self.tamanho = self.leitura.size

                    # Definimos o término de cada pacote pela sequência 9 \n (9 10). Logo, ao econtrar essa sequência a leitura de um pacote e finalizada
                    if (((self.leitura.size > 1)) & (
                            (self.leitura[self.tamanho - 2] == 9) & (self.leitura[self.tamanho - 1] == 10))):
                        break
                # chamada da função updateLabel para analisar os dados recebidos atualizar os mostradores da interface
                QtCore.QTimer.singleShot(self.time,
                                         lambda: self.updateLabel(self.textBrowser_Buffer,
                                                                  self.spinBox_IndexBattery,
                                                                  self.spinBox_IndexEngineTemperature,
                                                                  self.save, self.arq, self.graphicsView_EngineData,
                                                                  self.array_temp, self.array_fuel_p,
                                                                  self.array_oil_p, self.array_battery,
                                                                  self.array_leitura, self.tableWidget_Package1,
                                                                  self.tableWidget_Package2,
                                                                  self.tableWidget_Package3,
                                                                  self.graphicsView_DiagramaGG, self.x,
                                                                  self.y, self.w1, self.s, self.lineEdit_SetupCar,
                                                                  self.divisor, self.arq_laptime, self.buffer1,
                                                                  self.buffer2, self.buffer3, self.buffer4,
                                                                  self.buffer5, self.buffer6, self.cont,
                                                                  self.exe_time, self.sec))


        except (ValueError, serial.SerialException):
            self.stop_program()
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Error!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.setText(
                "<center>Failed to receive data!<center> \n\n <center>Check Serial Ports and Telemetry System.<center>")
            dlg.exec_()

        # Função que recebe novos dados, analisa sua consistência, verifica qual pacote foi recebido, realiza operações
        # necessárias com os dados e chama as funções de atualização de pacotes. Além disso, a função realiza a escrita
        # dos dados no arquivo txt. Isso é feito dentro de cada if para que só sejam gravados dados que foram recebidos corretamente.
        # A função recebe o vetor "leitura", realiza as operações binárias, deslocamento e soma, e cria o vetor "lista".
        # Dessa forma, o vetor "leitura" contém os bytes convertidos para inteiro, porém não os valores das variáveis que trabalhamos.
        # Já o vetor "lista", possui os valores corretos para serem mostrados

    def updateLabel(self, textBrowser_Buffer, spinBox, spinBox_IndexEngineTemperature, save, arq, graphicsView,
                    array_temp, array_fuel_p,
                    array_oil_p, array_battery, array_leitura, tableWidget, tableWidget_2,
                    tableWidget_3, graphicsView_DiagramaGG, x, y, w1, s, lineEdit_SetupDifferential, constante,
                    arq_laptime, buffer1, buffer2, buffer3, buffer4, buffer5, buffer6, cont, exe_time, sec):
        self.lista = np.array([]).astype('int')  # cria uma lista chamada "lista"
        self.lista = np.append(self.lista, self.leitura[0])
        if self.lineEdit_CalibrationConstant.text() == "":  # Caso a constante de calibração não seja definida é utilizado o valor 1
            self.constante = 1
        else:
            self.constante = float(self.lineEdit_CalibrationConstant.text())
        #print("tamanho", self.leitura.size)
        #print("tipo", type(self.leitura))
        #print(self.leitura)
        try:
            if ((int(self.leitura[0]) == 1) and (self.leitura.size == 16)):  # testa se é o pacote 1 e está completo
                self.x_accel = (int(self.leiturasigned[2]) << 8) + int(self.leiturasigned[
                                                                           3])  # recebe o valor contido na lista de dados(leitura) em suas respectivas posições e realiza as operações de deslocamento e soma binária
                self.lista = np.append(self.lista, self.x_accel)  # concatena o valor de x_accel na lista
                self.x_accel = round(float(self.x_accel / 16384), 3)  #
                self.y_accel = (int(self.leiturasigned[4]) << 8) + int(self.leiturasigned[5])
                self.lista = np.append(self.lista, self.y_accel)
                self.y_accel = round(float(self.y_accel / 16384), 3)
                self.z_accel = (int(self.leiturasigned[6]) << 8) + int(self.leiturasigned[7])
                self.lista = np.append(self.lista, self.z_accel)
                self.z_accel = round(float(self.z_accel / 16384), 3)
                self.vel_dianteira = int(self.leitura[8])
                self.lista = np.append(self.lista, self.vel_dianteira)
                self.vel_traseira = int(self.leitura[9])
                self.lista = np.append(self.lista, self.vel_traseira)
                self.rele_sparkcut = ((self.leitura[10]) & 128) >> 7
                self.lista = np.append(self.lista, self.rele_sparkcut)
                self.susp = (((self.leitura[10]) & 127) << 8) + int(self.leitura[11])
                self.lista = np.append(self.lista, self.susp)
                self.time1 = ((self.leitura[12]) << 8) + int(self.leitura[13])
                self.lista = np.append(self.lista, self.time1)
                self.time1 = 25 * self.time1

                if self.save == 1:
                    self.string = str(self.lista[0]) + ' ' + str(self.lista[1]) + ' ' + str(
                        self.lista[2]) + ' ' + str(self.lista[3]) + ' ' + str(self.lista[4]) + ' ' + str(
                        self.lista[5]) + ' ' + str(self.lista[6]) + ' ' + str(self.lista[7]) + ' ' + str(self.lista[8])
                    # print("string", self.string)
                    self.arq.write(self.string)  # escreve no arquivo txt a lista de dados recebidos
                    self.arq.write("\n")  # escreve no arquivo txt uma quebra de linha
                self.update_p1(self.x_accel, self.y_accel, self.z_accel, self.vel_dianteira, self.vel_traseira,
                               self.rele_sparkcut, self.susp,
                               self.time1, self.graphicsView_DiagramaGG, self.x, self.y, self.w1, self.s,
                               self.array_lap)
            elif ((int(self.leitura[0]) == 2) and (self.leitura.size == 22)):  # testa se é o pacote 2 e está completo
                self.oil_p = (int(self.leitura[2]) << 8) + int(self.leitura[3])
                self.lista = np.append(self.lista, self.oil_p)
                self.oil_p = round(float(self.oil_p * 0.001), 2)
                self.pcomb = (int(self.leitura[4]) << 8) + int(self.leitura[5])
                self.lista = np.append(self.lista, self.pcomb)
                self.pcomb = round(float(self.pcomb * 0.001), 2)
                self.tps = (int(self.leitura[6]) << 8) + int(self.leitura[7])
                self.lista = np.append(self.lista, self.tps)
                self.tps = round(float(self.tps * 0.1), 2)
                self.p_freio_t = (int(self.leitura[8]) << 8) + int(self.leitura[9])
                self.lista = np.append(self.lista, self.p_freio_t)
                self.p_freio_t = round(self.p_freio_t * 0.02536, 1)
                self.p_freio_d = (int(self.leitura[10]) << 8) + int(self.leitura[11])
                self.lista = np.append(self.lista, self.p_freio_d)
                self.p_freio_d = round(self.p_freio_d * 0.02536, 1)
                self.wheel_pos = (int(self.leitura[12]) << 8) + int(self.leitura[13])
                self.lista = np.append(self.lista, self.wheel_pos)
                self.lineEdit_CurrentWheelPos.setText(str(self.wheel_pos))
                self.wheel_pos = round(((self.wheel_pos - (self.spinBox_WheelPosMin.value())) / (
                        (self.spinBox_WheelPosMax.value() - self.spinBox_WheelPosMin.value()) / 240) - 120), 2)
                self.beacon = (int(self.leitura[14])) >> 7
                self.lista = np.append(self.lista, self.beacon)
                self.current = ((int(self.leitura[14]) & 127) << 8) + int(self.leitura[15])
                self.lista = np.append(self.lista, self.current)
                self.rpm = (int(self.leitura[16]) << 8) + int(self.leitura[17])
                self.lista = np.append(self.lista, self.rpm)
                self.time2 = (int(self.leitura[18]) << 8) + int(self.leitura[19])
                self.lista = np.append(self.lista, self.time2)
                self.time2 = 25 * self.time2

                if ((self.beacon == 1) and ((self.time2 - self.aux_time[self.aux_time.size - 1]) >= 200)):
                    if (self.aux_time.size == 0):
                        self.aux_time = np.append(self.aux_time, self.time2)
                    else:
                        self.array_lap = np.append(self.array_lap,self.time2 - self.aux_time[self.aux_time.size - 1])
                        self.aux_time = np.append(self.aux_time, self.time2)
                        self.laptime = str(self.array_lap[self.array_lap.size - 1])
                        self.arq_laptime.write(self.laptime)
                        self.arq_laptime.write("\n")

                self.array_oil_p = np.append(self.array_oil_p, self.oil_p)
                # print(self.lista)
                if self.save == 1:
                    self.string = str(self.lista[0]) + ' ' + str(self.lista[1]) + ' ' + str(self.lista[2]) + ' ' + str(
                        self.lista[3]) + ' ' + str(self.lista[4]) + ' ' + str(self.lista[5]) + ' ' + str(
                        self.lista[6]) + ' ' + str(self.lista[7]) + ' ' + str(self.lista[8]) + ' ' + str(
                        self.lista[9])+ ' ' + str(self.lista[10])
                    # print("string", self.string)
                    self.arq.write(self.string)
                    self.arq.write("\n")
                self.update_p2(self.oil_p, self.pcomb, self.tps, self.p_freio_d, self.p_freio_t, self.wheel_pos,
                               self.beacon, self.current,self.rpm, self.time2)

            elif ((int(self.leitura[0]) == 3) and (self.leitura.size == 15)):  # testa se é o pacote 3 e está completo
                self.temp = (int(self.leitura[(self.spinBox_IndexEngineTemperature.value())]) << 8) + int(
                    self.leitura[(self.spinBox_IndexEngineTemperature.value()) + 1])
                self.lista = np.append(self.lista, self.temp)
                self.temp = round(float(self.temp * 0.1), 2)
                self.battery = ((self.leitura[(self.spinBox_IndexBattery.value()) + 1]) << 8) + (
                    self.leitura[(self.spinBox_IndexBattery.value()) + 2])
                self.lista = np.append(self.lista, self.battery)
                self.battery = round(float(self.battery * 0.01), 2)
                self.rele_bomba = (int(self.leitura[(self.spinBox_IndexFuelPumpRelay.value()) + 2]) & 128) >> 7
                self.lista = np.append(self.lista, self.rele_bomba)
                self.rele_vent = (int(self.leitura[(self.spinBox_IndexFanRelay.value()) + 1]) & 32) >> 5
                self.lista = np.append(self.lista, self.rele_vent)
                self.temp_caixaR = (self.leitura[(self.spinBox_IndexRelayBoxTemperature.value())] << 8) + \
                                   self.leitura[
                                       (self.spinBox_IndexRelayBoxTemperature.value()) + 1]
                self.lista = np.append(self.lista, self.temp_caixaR)
                self.temp_caixaR = round(float(self.temp_caixaR), 2)
                self.temp_freiot = (self.leitura[(self.spinBox_IndexBreakTempRear.value()) + 1] << 8) + (
                    self.leitura[(self.spinBox_IndexBreakTempRear.value()) + 2])
                self.lista = np.append(self.lista, self.temp_freiot)
                self.temp_freiot = round(float(self.temp_freiot), 2)
                self.temp_freiod = (self.leitura[(self.spinBox_IndexBreakTempFront.value()) + 2] << 8) + (
                    self.leitura[(self.spinBox_IndexBreakTempFront.value()) + 3])
                self.lista = np.append(self.lista, self.temp_freiod)
                self.temp_freiod = round(float(self.temp_freiod), 2)
                self.time3 = (int(self.leitura[(self.spinBox_IndexTime3.value()) + 3]) << 8) + int(
                    self.leitura[(self.spinBox_IndexTime3.value()) + 4])
                self.lista = np.append(self.lista, self.time3)
                self.time3 = 25 * self.time3
                self.array_temp = np.append(self.array_temp, self.temp)
                self.array_battery = np.append(self.array_battery, self.battery)
                # print(self.lista)
                if self.save == 1:
                    self.string = str(self.lista[0]) + ' ' + str(self.lista[1]) + ' ' + str(
                        self.lista[2]) + ' ' + str(
                        self.lista[3]) + ' ' + str(self.lista[4]) + ' ' + str(self.lista[5]) + ' ' + str(
                        self.lista[6]) + ' ' + str(self.lista[7]) + ' ' + str(self.lista[8])
                    # print("string", self.string)
                    self.arq.write(self.string)
                    self.arq.write("\n")
                self.update_p3(self.temp, self.battery, self.rele_bomba, self.rele_vent, self.temp_caixaR,
                               self.temp_freiot, self.temp_freiod, self.time3)
            elif ((int(self.leitura[0]) == 4) and (self.leitura.size == 30)):  # testa se é o pacote 4 e está completo
                self.p1_ext = ((self.leitura[2] << 16) + (self.leitura[3] << 8) + self.leitura[4])
                self.lista = np.append(self.lista, self.p1_ext)
                self.p2_ext = ((self.leitura[5] << 16) + (self.leitura[6] << 8) + self.leitura[7])
                self.lista = np.append(self.lista, self.p2_ext)
                self.p3_ext = ((self.leitura[8] << 16) + (self.leitura[9] << 8) + self.leitura[10])
                self.lista = np.append(self.lista, self.p3_ext)
                self.p4_ext = ((self.leitura[11] << 16) + (self.leitura[12] << 8) + self.leitura[13])
                self.lista = np.append(self.lista, self.p4_ext)
                self.p5_ext = ((self.leitura[14] << 16) + (self.leitura[15] << 8) + self.leitura[16])
                self.lista = np.append(self.lista, self.p5_ext)
                self.p6_ext = ((self.leitura[17] << 16) + (self.leitura[18] << 8) + self.leitura[19])
                self.lista = np.append(self.lista, self.p6_ext)
                self.p7_ext = ((self.leitura[20] << 16) + (self.leitura[21] << 8) + self.leitura[22])
                self.lista = np.append(self.lista, self.p7_ext)
                self.p8_ext = ((self.leitura[23] << 16) + (self.leitura[24] << 8) + self.leitura[25])
                self.lista = np.append(self.lista, self.p8_ext)
                self.time4 = ((self.leitura[26] << 8) + (self.leitura[27]))
                self.lista = np.append(self.lista, self.time4)
                self.time4 = 25 * self.time4
                # self.array_temp= np.append(self.array_temp,self.temp)
                if self.save == 1:
                    self.string = str(self.lista[0]) + ' ' + str(self.lista[1]) + ' ' + str(
                        self.lista[2]) + ' ' + str(
                        self.lista[3]) + ' ' + str(self.lista[4]) + ' ' + str(self.lista[5]) + ' ' + str(
                        self.lista[6]) + ' ' + str(self.lista[7]) + ' ' + str(self.lista[8]) + ' ' + str(
                        self.lista[9])
                    # print("string", self.string)
                    self.arq.write(self.string)
                    self.arq.write("\n")
                self.update_p4(self.p1_ext, self.p2_ext, self.p3_ext, self.p4_ext, self.p5_ext, self.p6_ext,
                               self.p7_ext, self.p8_ext, self.time4)
            else:
                print ("Erro")
        except:
            print("Erro 2")

        # as linhas a seguir plotam os gráficos selecionados atráves dos checkBox e define as cores de cada gráfico.
        # Os gráficos são compostos pelos últimos 50 pontos do dado contidos nos arrays de cada dado.

        self.graphicsView_EngineData.clear()
        if self.checkBox_EngineTemperature.isChecked() == 1:
            self.graphicsView_EngineData.plot(self.array_temp[self.array_temp.size - 50:self.array_temp.size], pen='r')
        if self.checkBox_FuelPressure.isChecked() == 1:
            self.graphicsView_EngineData.plot(self.array_fuel_p[self.array_fuel_p.size - 50:self.array_fuel_p.size],
                                              pen='g')
        if self.checkBox_Voltage.isChecked() == 1:
            self.graphicsView_EngineData.plot(self.array_battery[self.array_battery.size - 50:self.array_battery.size],
                                              pen='b')
        if self.checkBox_OilPressure.isChecked() == 1:
            self.graphicsView_EngineData.plot(self.array_oil_p[self.array_oil_p.size - 50:self.array_oil_p.size],
                                              pen='y')

        # as linhas a seguir atualizam o mostrador textBrowser_Buffer com as ultimas 6 listas de dados recebidas.
        # Caso o número de listas recebidas seja menor que 6, são mostradas apenas estas
        self.buffer6 = self.buffer5
        self.buffer5 = self.buffer4
        self.buffer4 = self.buffer3
        self.buffer3 = self.buffer2
        self.buffer2 = self.buffer1
        self.buffer1 = self.leitura
        self.textBrowser_Buffer.setText(
            str(self.buffer1) + "\n" + str(self.buffer2) + "\n" + str(self.buffer3) + "\n" + str(
                self.buffer4) + "\n" + str(self.buffer5) + "\n" + str(self.buffer6))

        try:
            if (self.stop == 0):
                # As seguintes linhas contam o tempo de uma execução do programa e quantas execuções foram realizadas
                self.time_init = self.sec
                self.sec = time.time()
                self.milli_sec = (
                                         self.sec - self.time_init) * 1000  # tempo final - tempo inicial convertido para milissegundos
                self.exe_time = self.exe_time + self.milli_sec  # tempo total de execução
                self.cont = self.cont + 1  # número de execuções

                # As linhas a seguir printam no prompt o tempo médio de execução a cada mil execuções até 5000
                if (
                        self.cont == 1 or self.cont == 1000 or self.cont == 2000 or self.cont == 3000 or self.cont == 4000 or self.cont == 5000):
                    print("tempo médio:", self.exe_time / self.cont)
                    print("qtd de execuções", self.cont)

                # As duas variáveis a seguir são usadas para guardar os valores lidos na porta serial
                # São usadas duas variáveis pois é necessário converter os valores lidos para inteiro antes de saber quais dados eles represetam
                # Alguns dados são usados como unsigned e outro como signed, por isso alguns dados são gravados das duas maneiras
                self.leitura = np.array([]).astype('int')
                self.leiturasigned = np.array([]).astype('int')

                # As linhas a seguir realizam a leitura da porta serial byte a byte
                while True:
                    while (self.dados.inWaiting() == 0):
                        pass
                    self.byte = self.dados.read(1)  # dado com formato de byte
                    self.byteunsigned = int.from_bytes(self.byte, byteorder='big',
                                                       signed=False)  # dado com formato de int
                    self.bytesigned = int.from_bytes(self.byte, byteorder='big',
                                                     signed=True)  # dado com formato de int
                    self.leitura = np.append(self.leitura, self.byteunsigned)

                    # Apenas alguns dados do pacote 1 são usados como signed.
                    # Dessa forma, apenas quando estiver começando a leitura de um pacote ou se o pacote que está sendo lido é o pacote 1 é dada continuidade na definição do vetor de dados signed
                    if (self.leiturasigned.size == 0 or (self.leiturasigned[0]) == 1):
                        self.leiturasigned = np.append(self.leiturasigned, self.bytesigned)
                    self.tamanho = self.leitura.size

                    # Definimos o término de cada pacote pela sequência 9 \n (9 10). Logo, ao econtrar essa sequência a leitura de um pacote e finalizada
                    if (((self.leitura.size > 1)) & (
                            (self.leitura[self.tamanho - 2] == 9) & (self.leitura[self.tamanho - 1] == 10))):
                        break

                # Chamada da função updateLabel para tratamento dos dados
                QtCore.QTimer.singleShot(self.time,
                                         lambda: self.updateLabel(self.textBrowser_Buffer,
                                                                  self.spinBox_IndexBattery,
                                                                  self.spinBox_IndexEngineTemperature,
                                                                  self.save, self.arq,
                                                                  self.graphicsView_EngineData,
                                                                  self.array_temp, self.array_fuel_p,
                                                                  self.array_oil_p, self.array_battery,
                                                                  self.array_leitura, self.tableWidget_Package1,
                                                                  self.tableWidget_Package2,
                                                                  self.tableWidget_Package3,
                                                                  self.graphicsView_DiagramaGG, self.x,
                                                                  self.y, self.w1, self.s,
                                                                  self.lineEdit_SetupCar,
                                                                  self.divisor, self.arq_laptime, self.buffer1,
                                                                  self.buffer2, self.buffer3, self.buffer4,
                                                                  self.buffer5, self.buffer6, self.cont,
                                                                  self.exe_time, self.sec))

                # O erro de porta serial é analisado pela exceção serial.SerialException. Esse erro é tratado pausando o programa e
                # utilizando uma caixa de diálogo, a qual informa ao usuário o erro encontrado
        except (ValueError, serial.SerialException):
            self.stop_program()
            dlg = QMessageBox(None)
            dlg.setWindowTitle("Error!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.setText(
                "<center>Failed to receive data!<center> \n\n <center>Check Serial Ports and Telemetry System.<center>")
            dlg.exec_()

        # Função que atualiza os mostradores relacionados aos dados do pacote 1
        # Pacote 1: X_Accelerometer, Y_Accelerometer, Z_Accelerometer, Sparcut Relay, Speed, Suspension Course, time
        # Para atualizar as células da tabela tableWidget_Package1 é necessário definir o valor da variável item como o
        # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item

    def update_p1(self, x_accel, y_accel, z_accel, vel_dianteira, vel_traseira, rele_sparkcut, susp, time1, graphicsView_DiagramaGG, x, y, w1,
                  s, array_lap):
        item = QTableWidgetItem(str(self.x_accel))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(0, 1, item)
        self.x = np.append(self.x,self.x_accel)  # concatena o valor de x_accel no vetor x e este é utilizado para plotar o diagramaGG na função update_diagramagg
        item = QTableWidgetItem(str(self.y_accel))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(1, 1, item)
        self.y = np.append(self.y,self.y_accel)  # concatena o valor de y_accel no vetor y e este é utilizado para plotar o diagramaGG na função update_diagramagg
        item = QTableWidgetItem(str(self.z_accel))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(2, 1, item)
        item = QTableWidgetItem(str(self.vel_dianteira))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(3, 1, item)
        item = QTableWidgetItem(str(self.vel_traseira))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(4, 1, item)
        item = QTableWidgetItem(str(self.rele_sparkcut))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(5, 1, item)
        if (int(self.rele_sparkcut) == 1):
            self.radioButton_SparkcutRelay.setChecked(False)
        else:
            self.radioButton_SparkcutRelay.setChecked(True)

        item = QTableWidgetItem(str(self.susp))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(6, 1, item)
        item = QTableWidgetItem(str(self.time1))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package1.setItem(7, 1, item)
        if (self.array_lap.size == 1):
            self.lineEdit_LastLap.setText(str(self.array_lap[self.array_lap.size - 1]))
        elif (self.array_lap.size > 1):
            self.lineEdit_LastLap.setText(str(self.array_lap[self.array_lap.size - 1]))
            self.lineEdit_LastLap2.setText(str(self.array_lap[self.array_lap.size - 2]))
        self.update_diagramagg(self.graphicsView_DiagramaGG, self.w1, self.s, self.x,
                               self.y)  # Chamada da função update_diagramagg

        # função que mee      ostra o diagrama gg

    def update_diagramagg(self, graphicsView_DiagramaGG, w1, s, x, y):
        self.s = np.append(self.s, pg.ScatterPlotItem([self.y[self.y.size - 1]], [self.x[self.x.size - 1]], size=5,
                                                      pen=pg.mkPen(None)))
        self.s[self.x.size - 1].setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        self.w1.addItem(self.s[self.x.size - 1])

        # Função que atualiza os mostradores relacionados aos dados do pacote 2
        # Pacote 2: Oil pressure, fuel pressure, TPS, break pressure(rear), break pressute(front), wheel position, beacon, current, time
        # Para atualizar as células da tabela tableWidget_Package2 é necessário definir o valor da variável item como o
        # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item

    def update_p2(self, oil_p, pcomb, tps, p_freio_d, p_freio_t, wheel_pos, beacon, current,rpm, time2):
        item = QTableWidgetItem(str(self.beacon))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(0, 1, item)
        item = QTableWidgetItem(str(self.p_freio_d))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(1, 1, item)
        if ((self.p_freio_t + self.p_freio_d) != 0):  # Verificação necessária para que não ocorra divisão por zero
            self.progressBar_FrontBreakBalance.setValue(100 * self.p_freio_d / (
                        self.p_freio_t + self.p_freio_d))  # porcentagem da pressão referente ao freio dianteiro
        self.progressBar_FrontBreakPressure.setValue(self.p_freio_d)
        self.label_65.setText(str(self.p_freio_d))
        item = QTableWidgetItem(str(self.p_freio_t))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(2, 1, item)
        if ((self.p_freio_t + self.p_freio_d) != 0):  # Verificação necessária para que não ocorra divisão por zero
            self.progressBar_RearBreakBalance.setValue(100 * self.p_freio_t / (
                        self.p_freio_t + self.p_freio_d))  # porcentagem da pressão referente ao freio traseiro
        self.label_69.setText(str(self.p_freio_t))
        self.progressBar_RearBreakPressure.setValue(self.p_freio_t)
        item = QTableWidgetItem(str(self.current))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(3, 1, item)
        item = QTableWidgetItem(str(self.pcomb))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(4, 1, item)
        self.array_fuel_p = np.append(self.array_fuel_p, self.pcomb)
        self.progressBar_FuelPressure.setValue(self.pcomb)
        self.label_17.setText(str(self.pcomb))
        self.progressBar_OilPressure.setValue(self.oil_p)
        self.label_10.setText(str(self.oil_p))
        item = QTableWidgetItem(str(self.oil_p))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(5, 1, item)
        item = QTableWidgetItem(str(self.rpm))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(6, 1, item)
        item = QTableWidgetItem(str(self.time2))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(7, 1, item)
        self.progressBar_TPS.setValue(self.tps)
        self.progressBar_TPS.setProperty("value", self.tps)
        item = QTableWidgetItem(str(self.tps))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(8, 1, item)
        self.dial_WheelPos.setValue(self.wheel_pos)
        self.label_19.setText(str(self.wheel_pos))
        item = QTableWidgetItem(str(self.wheel_pos))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package2.setItem(9, 1, item)

        # Função que atualiza os mostradores relacionados aos dados do pacote 3
        # Pacote 3: Engine Temp, battery, fuel pump relay, fan relay, relay box temperature, break temperature rear, break temperature front, time
        # Para atualizar as células da tabela tableWidget_Package3 é necessário definir o valor da variável item como o
        # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item

    def update_p3(self, temp, battery, rele_bomba, rele_vent, temp_caixaR, temp_freiot, temp_freiod, time3):
        self.progressBar_BatteryVoltage.setValue(int(self.battery))
        self.label_15.setText(str(self.battery))
        # alarme bateria: o fundo da linha da tabela referente à tensão na bateria recebe a cor vermelha
        if (self.battery <= 11.5):
            item = self.tableWidget_Package3.item(0, 0)
            item.setBackground(QtGui.QColor(255, 0, 0))
            item = self.tableWidget_Package3.item(0, 2)
            item.setBackground(QtGui.QColor(255, 0, 0))
            item = QTableWidgetItem(str(self.battery))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setBackground(QtGui.QColor(255, 0, 0))
            self.tableWidget_Package3.setItem(0, 1, item)
        else:
            item = self.tableWidget_Package3.item(0, 0)
            item.setBackground(QtGui.QColor(255, 255, 255))
            item = self.tableWidget_Package3.item(0, 2)
            item.setBackground(QtGui.QColor(255, 255, 255))
            item = QTableWidgetItem(str(self.battery))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget_Package3.setItem(0, 1, item)
        item = QTableWidgetItem(str(self.temp_freiod))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(1, 1, item)
        item = QTableWidgetItem(str(self.temp_freiot))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(2, 1, item)
        self.progressBar_EngineTemperature.setValue(self.temp)
        self.label_6.setText(str(self.temp))
        # alarme temperatura: o fundo da linha da tabela referente à temperatura do motor recebe a cor vermelha
        if (self.temp >= 95.0):
            item = self.tableWidget_Package3.item(3, 0)
            item.setBackground(QtGui.QColor(255, 0, 0))
            item = self.tableWidget_Package3.item(3, 2)
            item.setBackground(QtGui.QColor(255, 0, 0))
            item = QTableWidgetItem(str(self.temp))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setBackground(QtGui.QColor(255, 0, 0))
            self.tableWidget_Package3.setItem(3, 1, item)
        else:
            item = self.tableWidget_Package3.item(3, 0)
            item.setBackground(QtGui.QColor(255, 255, 255))
            item = self.tableWidget_Package3.item(3, 2)
            item.setBackground(QtGui.QColor(255, 255, 255))
            item = QTableWidgetItem(str(self.temp))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setBackground(QtGui.QColor(255, 255, 255))
            self.tableWidget_Package3.setItem(3, 1, item)
            item = QTableWidgetItem(str(self.rele_vent))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(4, 1, item)
        if (int(self.rele_vent) == 1):
            self.radioButton_FanRelay.setChecked(False)
        else:
            self.radioButton_FanRelay.setChecked(True)
        item = QTableWidgetItem(str(self.rele_bomba))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(5, 1, item)
        if (int(self.rele_bomba) == 1):
            self.radioButton_FuelPumpRelay.setChecked(False)
        else:
            self.radioButton_FuelPumpRelay.setChecked(True)
        item = QTableWidgetItem(str(self.temp_caixaR))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(6, 1, item)
        item = QTableWidgetItem(str(self.time3))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_Package3.setItem(7, 1, item)

        # Função que atualiza os mostradores relacionados aos dados do pacote 4
        # Pacote 4: P1, P2, P3, P4, P5, P6, P7 e P8 strain gauges, time
        # Para atualizar as células da tabela tableWidget_StrainGauge é necessário definir o valor da variável item como o
        # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item

    def update_p4(self, p1_ext, p2_ext, p3_ext, p4_ext, p5_ext, p6_ext, p7_ext, p8_ext, time4):
        # extensometros
        item = QTableWidgetItem(str(self.p1_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(0, 1, item)
        item = QTableWidgetItem(str(self.p2_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(1, 1, item)
        item = QTableWidgetItem(str(self.p3_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(2, 1, item)
        item = QTableWidgetItem(str(self.p4_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(3, 1, item)
        item = QTableWidgetItem(str(self.p5_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(4, 1, item)
        item = QTableWidgetItem(str(self.p6_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(5, 1, item)
        item = QTableWidgetItem(str(self.p7_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(6, 1, item)
        item = QTableWidgetItem(str(self.p8_ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(7, 1, item)
        item = QTableWidgetItem(str(self.time4))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_StrainGauge.setItem(8, 1, item)

        # função para atualizar o arquivo setup com novos valores

    def update_setup(self, spinBox_WheelPosMax, spinBox_WheelPosMin, lineEdit_CalibrationConstant, lineEdit_SetupCar,
                     lineEdit_SetupTrack, lineEdit_SetupDriver,
                     lineEdit_SetupTemperature, lineEdit_SetupAntiroll, lineEdit_SetupTirePressureFront,
                     lineEdit_SetupTirePressureRear, lineEdit_SetupWingAttackAngle, lineEdit_SetupEngineMap,
                     lineEdit_SetupBalanceBar,
                     lineEdit_SetupDifferential,lineEdit_SetupAcquisitionRate, textEdit_SetupComments):
        self.setup = open('setup.txt', 'w')
        # if((spinBox_WheelPosMax.value()!=self.setup.readline(0)) or (spinBox_WheelPosMin.value() != self.setup.readline(1)) or (spinBox_IndexEngineTemperature6.value() != self.setup.readline(2)) or (lineEdit_SetupDifferential.text()!=self.setup.readline(3))or (lineEdit_SetupCar.text()!=self.setup.readline(3))or (lineEdit_SetupTrack.text()!=self.setup.readline(3))or (lineEdit_CalibrationConstant.text()!=self.setup.readline(3))or (lineEdit_SetupDriver.text()!=self.setup.readline(3))or (lineEdit_SetupTemperature.text()!=self.setup.readline(3))or (lineEdit_FileName6.text()!=self.setup.readline(3))or (lineEdit_SetupBalanceBar.text()!=self.setup.readline(3))or (lineEdit_SetupTirePressureFront.text()!=self.setup.readline(3))or (lineEdit_SetupTirePressureRear.text()!=self.setup.readline(3))or (lineEdit_SetupWingAttackAngle.text()!=self.setup.readline(3))or (lineEdit_SetupEngineMap.text()!=self.setup.readline(3))or (textEdit_SetupComments.toPlainText()!=self.setup.readline(3))):
        self.setup.write(str(spinBox_WheelPosMax.value()) + "\n")  # grava wheel_pos max
        self.setup.write(str(spinBox_WheelPosMin.value()) + "\n")  # grava wheel_pos min
        self.setup.write(str(lineEdit_CalibrationConstant.text()) + "\n")  # grava constante de calibração
        self.setup.write(str(lineEdit_SetupCar.text()) + "\n")  # grava car
        self.setup.write(str(lineEdit_SetupTrack.text()) + "\n")  # grava track
        self.setup.write(str(lineEdit_SetupDriver.text()) + "\n")  # grava driver
        self.setup.write(str(lineEdit_SetupTemperature.text()) + "\n")  # grava temperature
        self.setup.write(str(lineEdit_SetupAntiroll.text()) + "\n")  # grava antiroll
        self.setup.write(str(lineEdit_SetupTirePressureFront.text()) + "\n")  # grava tire pressure front
        self.setup.write(str(lineEdit_SetupTirePressureRear.text()) + "\n")  # grava tire pressure rear
        self.setup.write(str(lineEdit_SetupWingAttackAngle.text()) + "\n")  # grava wing attack angle
        self.setup.write(str(lineEdit_SetupEngineMap.text()) + "\n")  # grava engine map
        self.setup.write(str(lineEdit_SetupBalanceBar.text()) + "\n")  # grava balance bar
        self.setup.write(str(lineEdit_SetupDifferential.text()) + "\n")  # grava differential
        self.setup.write(str(lineEdit_SetupAcquisitionRate.text()) + "\n")  # grava taxa de aquisição
        self.setup.write(str(textEdit_SetupComments.toPlainText()) + "\n")  # grava comments
        self.setup.close()

        # Funcao para atualizar campos através dos valores contidos no arquivo setup. A função lê o arquivo e define os valores dos campos relacionados aos dados do arquivo

        # Função para definir nome do arquivo txt no qual os dados serão gravados, abrir este arquivo e gravar dados de setup e os dados recebidos através na porta serial

    def gravacao(self):
        self.arquivo = self.lineEdit_FileName.text()  # variável arquivo recebe o nome que o usuário informa na interface do arquivo a ser criado
        self.now = datetime.now()
        # define o nome do arquivo concatenando o nome definido pelo usuário e hora e minuto do início da gravação
        self.arquivo = self.arquivo + "_" + str(self.now.hour) + "_" + str(self.now.minute) + ".txt"
        print(self.arquivo)
        self.arq = open(self.arquivo, 'w')
        # escreve os valores de setup no início do arquivo
        self.arq.write("***\nCARRO: " + str(self.lineEdit_SetupCar.text()) + "\nPISTA: " + str(
            self.lineEdit_SetupTrack.text()) + "\nPILOTO: " + str(
            self.lineEdit_SetupDriver.text()) + "\nTEMPERATURA AMBIENTE: " + str(
            self.lineEdit_SetupTemperature.text()) + "\nANTIROLL: " + str(
            self.lineEdit_SetupAntiroll.text()) + "\nPRESSÃO PNEUS DIANTEIROS: " + str(
            self.lineEdit_SetupTirePressureFront.text()) + "\nPRESSÃO PNEUS TASEIROS: " + str(
            self.lineEdit_SetupTirePressureRear.text()) + "\nÂNGULO DE ATAQUE DA ASA: " + str(
            self.lineEdit_SetupWingAttackAngle.text()) + "\nMAPA MOTOR: " + str(
            self.lineEdit_SetupEngineMap.text()) + "\nBALANCE BAR: " + str(
            self.lineEdit_SetupBalanceBar.text()) + "\nDIFERENCIAL: " + str(
            self.lineEdit_SetupDifferential.text()) + "\nTAXA DE AQUISIÇÃO: " + str(
            self.lineEdit_SetupAcquisitionRate.text()) + "\nCOMENTÁRIOS: " + str(
            self.textEdit_SetupComments.toPlainText()) + "\nPOSIÇÃO MÁXIMA DO VOLANTE: " + str(
            self.spinBox_WheelPosMax.value()) + "\nPOSIÇÃO MÍNIMA DO VOLANTE: " + str(
            self.spinBox_WheelPosMin.value()) + "\nSUSPENSÃO: " + str(
            self.lineEdit_CalibrationConstant.text()) + "\n***\n\n")
        self.save = 1  # atualiza o valor da variavel save, a qual é usada para verificar se está ocorrendo ou não não gravação dos dados
        self.label_12.setText("Saving...")  # informa ao usuário a situação atual de gravação de dados

        # Função para parar a gravação dos dados no arquivo txt

    def stop_gravacao(self):
        self.save = 0  # atualiza o valor da variavel save, a qual é usada para verificar se está ocorrendo ou não não gravação dos dados
        self.label_12.setText("No saving...")  # informa ao usuário a situação atual de gravação de dados
        self.arq.close()

        # Função para pausar o funcionamento da interface

    def stop_program(self):
        self.stop = 1  # atualiza o valor da variavel stop, a qual é usada para verificar o funcionamento da interface
        self.arq_laptime.close()
        if self.dados.isOpen():
            self.dados.flushInput()
            self.dados.close()
        else:
            pass

        # função que fecha a interface

    def exit(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
