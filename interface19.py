import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# pacotes necessários
import sys
import glob
import numpy as np

import serial
from classes import Data, File, Log, vectorToString
from Program import Program
from interface_generated import Ui_MainWindow


# A função loadSetup atualiza os campos que já haviam sido definidos em utilizações ateriores da interface
# Ela serve para que não seja necessário atualizar todos os campos sempre que for necessária o reinício da interface
def loadSetup():
    global settings, errorLog
    try:
        filename = settings.value('filename')
        ui.lineEdit_FileName.setText(filename)
    except:
        errorLog.writeLog("Erro ao carregar config do arquivo")
    try:
        ui.textEdit_SetupComments.setText(settings.value('setupComments'))
        ui.lineEdit_WheelPosMax.setText(settings.value('wheelPosMax'))
        ui.lineEdit_WheelPosMin.setText(settings.value('wheelPosMin'))
        ui.lineEdit_CalibrationConstant.setText(settings.value('calibConstant'))
        ui.lineEdit_SetupCar.setText(settings.value('setupCar'))
        ui.lineEdit_SetupTrack.setText(settings.value('setupTrack'))
        ui.lineEdit_SetupDriver.setText(settings.value('setupDriver'))
        ui.lineEdit_SetupTemperature.setText(settings.value('setupTemp'))
        ui.lineEdit_SetupAntiroll.setText(settings.value('setupAntiroll'))
        ui.lineEdit_SetupTirePressureFront.setText(settings.value('tirePFront'))
        ui.lineEdit_SetupTirePressureRear.setText(settings.value('tirePRear'))
        ui.lineEdit_SetupWingAttackAngle.setText(settings.value('aeroAngle'))
        ui.lineEdit_SetupEngineMap.setText(settings.value('engineMap'))
        ui.lineEdit_SetupBalanceBar.setText(settings.value('balanceBar'))
        ui.lineEdit_SetupDifferential.setText(settings.value('setupDrexler'))
        ui.textEdit_SetupComments.setText(settings.value('setupComments'))
        ui.lineEdit_SampleRate1.setText(settings.value('sampleRate1'))
        ui.lineEdit_SampleRate2.setText(settings.value('sampleRate2'))
        ui.lineEdit_SampleRate3.setText(settings.value('sampleRate3'))
        ui.lineEdit_SampleRate4.setText(settings.value('sampleRate4'))

    except:
        errorLog.writeLog("Erro ao carregar configs")
    try:
        for key in program.data.alarms:
            if settings.contains('alarm'+key):
                store = settings.value('alarm'+key)
                store[0] = float(store[0])
                program.data.alarms[key] = store
    except:
        errorLog.writeLog("Erro ao carregar config de alarme")


# Atualiza portas seriais disponiveis
def updatePorts():
    ui.comboBox_SerialPorts.clear()
    ui.comboBox_SerialPorts.addItems(listSerialPorts())


# Lista as portas seriais disponiveis. Retorna uma lista com os nomes das portas
def listSerialPorts():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


# Função que inicia a execução do programa
def startProgram():
    try:
        global errorLog, program
        # abre e configura a porta serial utilizando os valores definidos pelo usuário através da interface
        baudrate = int(ui.comboBox_Baudrate.currentText())
        port = str(ui.comboBox_SerialPorts.currentText())
        timeout = None
        program.openSerialPort(port, baudrate, timeout)

        # Inicializa programa e coloca constantes
        updateConstants()
        program.stop = 0
        # program.lapTimeFile.startDataSave("tempos_de_volta")
        program.updateTime = ui.doubleSpinBox_UpdateTime.value() * 1000
        program.program()

        print("Saiu do programa")

# O erro de porta serial é analisado pela exceção serial.SerialException. Esse erro é tratado pausando o programa e
# utilizando uma caixa de diálogo, a qual informa ao usuário o erro encontrado
    except serial.serialutil.SerialException:
        errorLog.writeLog("startProgram: SerialException")
        program.stopProgram()
        dlg = QMessageBox(None)
        dlg.setWindowTitle("Error!")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText(
         "<center>Failed to receive data!<center> \n\n <center>Check Serial Ports and Telemetry System.<center>")
        dlg.exec_()


# Atualiza constantes com os valores lidos na interface
def updateConstants():
    program.data.wheelPosMax = int(ui.lineEdit_WheelPosMax.text())
    program.data.wheelPosMin = int(ui.lineEdit_WheelPosMin.text())


# Função para definir nome do arquivo txt no qual os dados serão gravados,
# abrir este arquivo e gravar dados de setup e os dados recebidos através na porta seria
def beginDataSave():
    fileInstance = program.dataFile
    if fileInstance.save == 1:
        errorLog.writeLog("Arquivo já inicializado ")
        return
    # arquivo e a variável arquivo recebe o nome que o usuário informa na interface do arquivo a ser criado
    arquivo = ui.lineEdit_FileName.text()
    fileInstance.startDataSave(arquivo)
    fileInstance.writeRow("***\n")
    fileInstance.writeRow("CARRO: " + str(ui.lineEdit_SetupCar.text()) + "\n")
    fileInstance.writeRow("PISTA: " + str(ui.lineEdit_SetupTrack.text()) + "\n")
    fileInstance.writeRow("PILOTO: " + str(ui.lineEdit_SetupDriver.text()) + "\n")
    fileInstance.writeRow("TEMPERATURA AMBIENTE: " + str(ui.lineEdit_SetupTemperature.text()) + "\n")
    fileInstance.writeRow("ANTIROLL: " +str(ui.lineEdit_SetupAntiroll.text()) + "\n")
    fileInstance.writeRow("PRESSAO PNEUS DIANTEIROS: " +str(ui.lineEdit_SetupTirePressureFront.text()) + "\n")
    fileInstance.writeRow("PRESSAO PNEUS TASEIROS: " +str(ui.lineEdit_SetupTirePressureRear.text()) + "\n")
    fileInstance.writeRow("ANGULO DE ATAQUE DA ASA: " +str(ui.lineEdit_SetupWingAttackAngle.text()) + "\n")
    fileInstance.writeRow("MAPA MOTOR: " +str(ui.lineEdit_SetupEngineMap.text()) + "\n")
    fileInstance.writeRow("BALANCE BAR: " +str(ui.lineEdit_SetupBalanceBar.text()) + "\n")
    fileInstance.writeRow("DIFERENCIAL: " +str(ui.lineEdit_SetupDifferential.text()) + "\n")
    fileInstance.writeRow("TAXA DE AQUISICAO: "  + "\n")
    fileInstance.writeRow("COMENTARIOS: " +str(ui.textEdit_SetupComments.toPlainText()) + "\n")
    fileInstance.writeRow("POSICAO MAXIMA DO VOLANTE: " +str(ui.lineEdit_WheelPosMax.text()) + "\n")
    fileInstance.writeRow("POSICAO MINIMA DO VOLANTE: " +str(ui.lineEdit_WheelPosMin.text()) + "\n")
    fileInstance.writeRow("SUSPENSAO: " +str(ui.lineEdit_CalibrationConstant.text()) + "\n")
    fileInstance.writeRow("PACOTE1 " + ui.lineEdit_SampleRate1.text() + ' ' + vectorToString(program.data.p1Order, ' '))
    fileInstance.writeRow("PACOTE2 " + ui.lineEdit_SampleRate2.text() + ' ' + vectorToString(program.data.p2Order, ' '))
    fileInstance.writeRow("PACOTE3 " + ui.lineEdit_SampleRate3.text() + ' ' + vectorToString(program.data.p3Order, ' '))
    fileInstance.writeRow("PACOTE4 " + ui.lineEdit_SampleRate4.text() + ' ' + vectorToString(program.data.p4Order, ' '))
    # fileInstance.writeRow("PACOTE1 40 acelY acelX acelZ velDD velT sparkCut suspPos time\n")
    # fileInstance.writeRow("PACOTE2 20 oleoP fuelP tps rearBrakeP frontBrakeP volPos beacon correnteBat rpm time2\n")
    # fileInstance.writeRow("PACOTE3 2 ect batVoltage releBomba releVent pduTemp tempDiscoD tempDiscoE time3\n")
    fileInstance.writeRow("***\n\n")

    ui.label_12.setText("Saving...")  # informa ao usuário a situação atual de gravação de dados


def stopDataSave():
    fileInstance = program.dataFile
    fileInstance.stopDataSave()
    ui.label_12.setText("Not saving...")  # informa ao usuário a situação atual de gravação de dados


def updatePlot(data):
    # as linhas a seguir plotam os gráficos selecionados atráves dos checkBox e define as cores de cada gráfico.
    # Os gráficos são compostos pelos últimos 50 pontos do dado
    # Arrasta vetor pto lado para que novo valor possa ser inserid

    # Atualiza graficos
    ui.graphicsView_EngineData.clear()
    if ui.checkBox_EngineTemperature.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayTemp, pen='r')
    if ui.checkBox_FuelPressure.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayFuelP, pen='g')
    if ui.checkBox_Voltage.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayBattery, pen='b')
    if ui.checkBox_OilPressure.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayOilP, pen='k')


# Coloca o background da linha da lista na cor color, onde color e do tipo QtGui.QColor(r, g, b)
def setFieldBackground(tableWidget, color, i):
    for j in range(0, 3):
        item = tableWidget.item(i, j)
        item.setBackground(color)


# Confere se alarme deve ser ativado e colore bacgrond caso seja o caso
def checkAlarm(data, key, tableWidget, i):
    op = data.alarms[key][1]
    threshold = data.alarms[key][0]
    if op == 'greater then':
        if data.dic[key] > threshold:
            setFieldBackground(tableWidget, QtGui.QColor(255, 0, 0), i)
        else:
            setFieldBackground(tableWidget, QtGui.QColor(255, 255, 255), i)
    elif op == 'lesser then':
        if data.dic[key] < threshold:
            setFieldBackground(tableWidget, QtGui.QColor(255, 0, 0), i)
        else:
            setFieldBackground(tableWidget, QtGui.QColor(255, 255, 255), i)
    elif op == 'equals':
        if data.dic[key] == threshold:
            setFieldBackground(tableWidget, QtGui.QColor(255, 0, 0), i)
        else:
            setFieldBackground(tableWidget, QtGui.QColor(255, 255, 255), i)


# Função que atualiza os mostradores relacionados aos dados do pacote 1
# Pacote 1: X_Accelerometer, Y_Accelerometer, Z_Accelerometer, Sparcut Relay, Speed, Suspension Course, time
# Para atualizar as células da tabela tableWidget_Package1 é necessário definir o valor da variável item como o
# desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def updateP1Interface(data):

    elements = len(data.p1Order)

    # Itera na variavel que contem a ordem dos pacotes para pegar as respectivas chaves do dicionario
    for key, i in zip(data.p1Order, range(0, elements)):
        # Cria elemento da tabela, faz o alinhamento e coloca valor
        item = QTableWidgetItem(str(data.dic[key]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package1.setItem(i, 1, item)
        # Alarmes
        if data.alarms[key] != []:
            checkAlarm(data, key, ui.tableWidget_Package1, i)
        else:
            setFieldBackground(ui.tableWidget_Package1, QtGui.QColor(255, 255, 255), i)

    # print(data.dic['acelX'])
    if (int(data.dic['sparkCut']) == 1):
        ui.radioButton_SparkcutRelay.setChecked(False)
    else:
        ui.radioButton_SparkcutRelay.setChecked(True)

    update_diagramagg(data)  # Chamada da função update_diagramagg


# função que atualiza o diagrama gg
def update_diagramagg(data):
    ui.graphicsView_DiagramaGG.clear()
    ui.graphicsView_DiagramaGG.plot([data.dic['acelX']], [data.dic['acelY']], pen=None, symbol='o')


# Função que atualiza os mostradores relacionados aos dados do pacote 2
# Funcionaento semelhante ao do pacote 1
def updateP2Interface(data):

    elements = len(data.p2Order)
    for key, i in zip(data.p2Order, range(0, elements)):
        item = QTableWidgetItem(str(data.dic[key]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package2.setItem(i, 1, item)

        if data.alarms[key] != []:
            checkAlarm(data, key, ui.tableWidget_Package2, i)
        else:
            setFieldBackground(ui.tableWidget_Package2, QtGui.QColor(255, 255, 255), i)

    if ((data.dic['rearBrakeP'] + data.dic['frontBrakeP']) != 0):  # Verificação necessária para que não ocorra divisão por zero
        ui.progressBar_FrontBreakBalance.setValue(100 * data.dic['frontBrakeP'] / (data.dic['rearBrakeP'] + data.dic['frontBrakeP']))  # porcentagem da pressão referente ao freio dianteiro
        ui.progressBar_FrontBreakBalance.setValue(100 * data.dic['rearBrakeP'] / (data.dic['rearBrakeP'] + data.dic['frontBrakeP'])) # traseiro

    # atualiza gauges
    ui.progressBar_FrontBreakPressure.setValue(data.dic['frontBrakeP'])
    ui.label_65.setText(str(data.dic['frontBrakeP']))
    ui.label_69.setText(str(data.dic['rearBrakeP']))
    ui.progressBar_RearBreakPressure.setValue(data.dic['rearBrakeP'])

    ui.progressBar_FuelPressure.setValue(data.dic['fuelP'])
    ui.label_17.setText(str(data.dic['fuelP']))

    ui.progressBar_OilPressure.setValue(data.dic['oleoP'])
    ui.label_10.setText(str(data.dic['oleoP']))

    ui.progressBar_TPS.setValue(data.dic['tps'])
    ui.progressBar_TPS.setProperty("value", data.dic['tps'])

    ui.dial_WheelPos.setValue(data.dic['volPos'])
    ui.label_19.setText(str(data.dic['volPos']))


# Função que atualiza os mostradores relacionados aos dados do pacote 3
# Funcionaento semelhante ao do pacote 1
def updateP3Interface(data):

    elements = len(data.p3Order)
    for key, i in zip(data.p3Order, range(0, elements)):
        item = QTableWidgetItem(str(data.dic[key]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package3.setItem(i, 1, item)

        if data.alarms[key] != []:
            checkAlarm(data, key, ui.tableWidget_Package3, i)
        else:
            setFieldBackground(ui.tableWidget_Package3, QtGui.QColor(255, 255, 255), i)

    # Gauge da bateria
    ui.progressBar_BatteryVoltage.setValue(int(data.dic['batVoltage']))
    ui.label_15.setText(str(data.dic['batVoltage']))

  # alarme bateria: o fundo da linha da tabela referente à tensão na bateria recebe a cor vermelha
    """if (data.dic['batVoltage'] <= 11.5):
        item = ui.tableWidget_Package3.item(0, 0)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = ui.tableWidget_Package3.item(0, 2)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = ui.tableWidget_Package3.item(0, 1)
        item.setBackground(QtGui.QColor(255, 0, 0))
    else:
        item = ui.tableWidget_Package3.item(0, 0)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = ui.tableWidget_Package3.item(0, 2)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = ui.tableWidget_Package3.item(0, 1)
        item.setBackground(QtGui.QColor(255, 255, 255))"""

    ui.progressBar_EngineTemperature.setValue(data.dic['ect'])
    ui.label_6.setText(str(data.dic['ect']))

    # alarme temperatura: o fundo da linha da tabela referente à temperatura do motor recebe a cor vermelha
    """if (data.dic['ect'] >= 95.0):
        item = ui.tableWidget_Package3.item(3, 0)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = ui.tableWidget_Package3.item(3, 2)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = ui.tableWidget_Package3.item(3, 1)
        item.setBackground(QtGui.QColor(255, 0, 0))
    else:
        item = ui.tableWidget_Package3.item(3, 0)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = ui.tableWidget_Package3.item(3, 2)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = ui.tableWidget_Package3.item(3, 1)
        item.setBackground(QtGui.QColor(255, 255, 255))"""

    if (int(data.dic['releVent']) == 1):
        ui.radioButton_FanRelay.setChecked(False)
    else:
        ui.radioButton_FanRelay.setChecked(True)

    if (int(data.dic['releBomba']) == 1):
        ui.radioButton_FuelPumpRelay.setChecked(False)
    else:
        ui.radioButton_FuelPumpRelay.setChecked(True)


# Função que atualiza os mostradores relacionados aos dados do pacote 4
# Funcionaento semelhante ao do pacote 1
def updateP4Interface(data):

    elements = len(data.dic['ext'])
    for ext, i in zip(data.dic['ext'], range(0, elements)):
        item = QTableWidgetItem(str(ext))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package3.setItem(i, 1, item)

    item = QTableWidgetItem(str(data.dic['time4']))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(i+1, 1, item)


def saveAlarm():
    global settings
    key = ui.alarmComboBox.currentText()
    type = ui.alarmTypeComboBox.currentText()
    val = ui.alarmlineEdit.text()
    if val == '' or type == '':
        if settings.contains('alarm'+key):
            settings.remove('alarm'+key)
        program.data.alarms[key] = []
    else:
        store = [float(val), type]
        settings.setValue('alarm' + key, store)
        program.data.alarms[key] = store


# Chama funcao que reseta alarms dentro da instancia de Data em program e reseta settings
def setDefaultAlarms():
    global settings
    program.data.setDefaultAlarms()
    for key in program.data.alarms:
        if settings.contains('alarm'+key):
            settings.remove('alarm'+key)


# Funcao responsavel por atualizar os campos na parte de configuracao dos alarmes.
# Ela é chamada qnd o usuario escolhe algum dado no comboBox dos alarmes
def displayAlarm(types):

    # Pega qual dado esta selecionado no combobox e acessa dicionario de Data
    text = ui.alarmComboBox.currentText()
    val = program.data.alarms[text]
    # Caso o alarme exista, mostra ele no campo tipo e valor
    if val != []:
        index = types.index(val[1])
        ui.alarmlineEdit.setText(str(val[0]))
        ui.alarmTypeComboBox.setCurrentIndex(index)
    else:
        ui.alarmlineEdit.setText('')
        ui.alarmTypeComboBox.setCurrentIndex(0)


# função para atualizar settings com novos valores de setup
def saveSetup():
    global settings, errorLog
    settings.setValue('wheelPosMax',str(ui.lineEdit_WheelPosMax.text()))
    settings.setValue('wheelPosMin',str(ui.lineEdit_WheelPosMin.text()))
    settings.setValue('calibConstant',str(ui.lineEdit_CalibrationConstant.text()))
    settings.setValue('setupCar',str(ui.lineEdit_SetupCar.text()))
    settings.setValue('setupTrack' ,str(ui.lineEdit_SetupTrack.text()))
    settings.setValue('setupDriver' ,str(ui.lineEdit_SetupDriver.text()))
    settings.setValue('setupTemp' ,str(ui.lineEdit_SetupTemperature.text()))
    settings.setValue('setupAntiroll' ,str(ui.lineEdit_SetupAntiroll.text()))
    settings.setValue('tirePFront' ,str(ui.lineEdit_SetupTirePressureFront.text()))
    settings.setValue('tirePRear' ,str(ui.lineEdit_SetupTirePressureRear.text()))
    settings.setValue('aeroAngle' ,str(ui.lineEdit_SetupWingAttackAngle.text()))
    settings.setValue('engineMap' ,str(ui.lineEdit_SetupEngineMap.text()))
    settings.setValue('balanceBar' ,str(ui.lineEdit_SetupBalanceBar.text()))
    settings.setValue('setupDrexler' ,str(ui.lineEdit_SetupDifferential.text()))
    settings.setValue('setupComments' ,str(ui.textEdit_SetupComments.toPlainText()))
    settings.setValue('filename', ui.lineEdit_FileName.text())
    settings.setValue('sampleRate1', ui.lineEdit_SampleRate1.text())
    settings.setValue('sampleRate2', ui.lineEdit_SampleRate2.text())
    settings.setValue('sampleRate3', ui.lineEdit_SampleRate3.text())
    settings.setValue('sampleRate4', ui.lineEdit_SampleRate4.text())


# Abre dialogo para escolher arquivo
def selectFile():
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, "Escolha arquivo .txt",
                                                        "", "All Files (*);;Text Files (*.txt)")

    if len(fileName) > 5:
        ui.lineEdit_FileName.setText(fileName)
        return fileName
    else:
        return


def exit():
    sys.exit(app.exec_())


# settings armazena os campos de configuracao na interface
settings = QtCore.QSettings('test', 'interface_renovada')

# Roda janela
app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Classes globais
errorLog = Log(ui.errorLog)
bufferLog = Log(ui.textBrowser_Buffer, maxElements=6)

# updateInterfaceFunctions é um dicionario que contem algumas funcoes de atualizacao da interface
# ele é passado como parametro na criacao da classe program, para que essas funcoes possam ser chamadas por ela
updateInterfaceFunctions = {1: updateP1Interface, 2: updateP2Interface, 3: updateP3Interface, 4: updateP4Interface, 'updatePlot': updatePlot}
program = Program(ui.doubleSpinBox_UpdateTime.value() * 1000, errorLog, bufferLog, updateInterfaceFunctions)
updateConstants()


ui.pushButton_SaveFile.clicked.connect(beginDataSave)  # botão para iniciar gravação de dados no txt
ui.pushButton_StopSaveFile.clicked.connect(stopDataSave)  # botão para parar a gravação de dados txt
ui.pushButton_PauseProgram.clicked.connect(program.stopProgram)  # botão para pausar o programa
ui.restoreDefaultAlarmPushButton.clicked.connect(setDefaultAlarms)
ui.lineEdit_WheelPosMin.editingFinished.connect(updateConstants)
ui.lineEdit_WheelPosMax.editingFinished.connect(updateConstants)

# ações
ui.pushButtonOpenFile.clicked.connect(selectFile)
ui.pushButton_Exit.clicked.connect(exit)  # botão para fechar a interface
ui.pushButton_StartProgram.clicked.connect(startProgram)  # botão para iniciar o programa
ui.pushButton_UpdatePorts.clicked.connect(updatePorts)  # botão para atualizar as portas seriis disponíveis
ui.pushButton_SaveSetupValues.clicked.connect(saveSetup)  # botão para atualizar os dados de setup no arquivo txt
ui.saveAlarmPushButton.clicked.connect(saveAlarm)
ui.actionExit.triggered.connect(exit)  # realiza a ação para fechar a interface
ui.comboBox_SerialPorts.addItems(listSerialPorts())  # mostra as portas seriais disponíveis
ui.comboBox_Baudrate.addItems(["115200", "38400", "1200", "2400", "9600", "19200", "57600" ])  # mostra os baudrates disponíveis
#ui.comboBox_Baudrate.currentIndexChanged.connect(selection_baudrate)
#pixmap = QPixmap("image1.png")
#ui.label_28.setPixmap(pixmap)
loadSetup()  # inicializa os valores de setup de acordo com o arquivo setup
ui.label_12.setText("Not saving...")  # informa na interface que os dados não estão sendo salvos
ui.graphicsView_DiagramaGG.setXRange(-2, 2)
ui.graphicsView_DiagramaGG.setYRange(-2, 2)

# cores do gráfico
ui.checkBox_OilPressure.setStyleSheet('color:blue')
ui.checkBox_FuelPressure.setStyleSheet('color:green')
ui.checkBox_EngineTemperature.setStyleSheet('color:red')
ui.checkBox_OilPressure.setStyleSheet('color:black')

ui.alarmComboBox.addItems(program.data.alarms)
alarmTypes = ['', 'greater then', 'lesser then', 'equal to']
ui.alarmComboBox.activated.connect(lambda: displayAlarm(alarmTypes))
ui.alarmTypeComboBox.addItems(alarmTypes)

# Mostra a janela e fecha o programa quando ela é fechada (?)
MainWindow.show()
sys.exit(app.exec_())
