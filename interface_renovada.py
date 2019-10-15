import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# pacotes necessários
import sys
from time import time
import glob
import numpy as np
# Se for instalar um pacote, NÃO instalar o serial, apenas o pyserial
import serial
from serial import Serial
from serial import SerialException
from classData import Data, File, ErrorLog
from interface_generated import *

# settings armazena os campos de configuracao na interface
settings = QtCore.QSettings('test', 'interface_renovada')
array_lap = np.array([]).astype('int')
aux_time = np.array([0]).astype('int')
# Vetores para mostrar últimos dados recebidos (TEMPORARIO)

sec = 0
cont = 0
exe_time = 0

porta = serial.Serial()


# Concatena vetor em uma string separada por delimiter
def vectorToString(line, delimiter):
    string = delimiter.join(str(x) for x in line)
    string = string + '\n'
    return string


# A função updateInitValues atualiza os campos que já haviam sido definidos em utilizações ateriores da interface
# Ela serve para que não seja necessário atualizar todos os campos sempre que for necessária o reinício da interface
def updateInitValues():
    global settings, errorLog
    try:
        filename = settings.value('filename')
        ui.lineEdit_FileName.setText(filename)
    except:
        errorLog.writeErrorLog("Erro ao carregar config do arquivo")
    try:
        ui.textEdit_SetupComments.setText(settings.value('setupComments'))
        ui.spinBox_WheelPosMax.setValue(int(settings.value('wheelPosMax')))
        ui.spinBox_WheelPosMin.setValue(int(settings.value('wheelPosMin')))
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
        ui.lineEdit_SetupAcquisitionRate.setText(settings.value('sampleRate'))
        ui.textEdit_SetupComments.setText(settings.value('setupComments'))
    except:
        errorLog.writeErrorLog("Erro ao carregar configs")


# Atualiza portas seriais disponiveis
def updatePorts():
    ui.comboBox_SerialPorts.clear()
    ui.comboBox_SerialPorts.addItems(serialPorts())


# Lista as portas seriais disponiveis. Retorna uma lista com os nomes das portas
def serialPorts():
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
        porta.baudrate = int(ui.comboBox_Baudrate.currentText())
        porta.port = str(ui.comboBox_SerialPorts.currentText())
        porta.timeout = None
        porta.open()
        # Inicializa programa
        program.data.wheelPosMax = ui.spinBox_WheelPosMax.value()
        program.data.wheelPosMin = ui.spinBox_WheelPosMin.value()
        program.stop = 0
        program.lapTimeFile.startDataSave("tempos_de_volta")
        program.program()

        print("Saiu do programa")

# O erro de porta serial é analisado pela exceção serial.SerialException. Esse erro é tratado pausando o programa e
# utilizando uma caixa de diálogo, a qual informa ao usuário o erro encontrado
    except serial.serialutil.SerialException:
        errorLog.writeErrorLog("startProgram: SerialException")
        stopProgram()
        dlg = QMessageBox(None)
        dlg.setWindowTitle("Error!")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText(
         "<center>Failed to receive data!<center> \n\n <center>Check Serial Ports and Telemetry System.<center>")
        dlg.exec_()


# Le buffer da porta serial. bufferSize é uma lista com os tamanhos dos pacotes e firstByteValues
# é uma lista com os numeros dos pacotes (1,2,3,4)
def readAll(bufferSize, firstByteValues):
    while True:
        # Espera receber algo na porta serial
        while (porta.inWaiting() == 0):
            pass
        read_buffer = b''
        # Le primeiro e segundo bytes
        firstByte = porta.read()
        if int.from_bytes(firstByte, byteorder='big') in firstByteValues:
            read_buffer += firstByte
            # Le o segundo byte de inicio
            a = porta.read()
            if int.from_bytes(a, byteorder='big') == 5:
                read_buffer += a
                break
            else:
                errorLog.writeErrorLog("Leitura: segundo byte com valor inesperado. Leu-se " + str(firstByte) + ", esperava-se 5")
        # Se o byte lido nao for 1, 2 3 ou 4,, quer dizer que perdeu algum dado.
        else:
            errorLog.writeErrorLog("Leitura: primeiro byte com valor inesperado. Leu-se " + str(firstByte) + ", esperava-se de 1 a 4")
    while True:
        # Le resto do buffer
        index = int.from_bytes(firstByte, byteorder='big') - 1
        byte = porta.read(size=int(bufferSize[index] - 2))
        read_buffer += byte

        if(len(read_buffer) == bufferSize[index]):
            if int(read_buffer[bufferSize[index]-2]) == 9:
                # Chegou no fim do pacote
                if int(read_buffer[bufferSize[index]-1]) == 10:
                    break
                else:
                    errorLog.writeErrorLog("Leitura: ultimo dado diferente de byte 10")
                    return []
            else:
                errorLog.writeErrorLog("Leitura: penultimo dado diferente de byte 9")
                return []

    return read_buffer


# Função que executa o programa
class Program():
    def __init__(self):
        ui.pushButton_SaveFile.clicked.connect(self.beginDataSave)  # botão para iniciar gravação de dados no txt
        ui.pushButton_StopSaveFile.clicked.connect(self.stopDataFileSave)  # botão para parar a gravação de dados txt
        ui.pushButton_PauseProgram.clicked.connect(self.stopProgram)  # botão para pausar o programa
        self.updateTime = ui.doubleSpinBox_UpdateTime.value() * 1000

        self.data = Data()
        self.dataFile = File()
        self.lapTimeFile = File()
        self.lastBuffers = np.array(['', '', '', '', '', ''], dtype=object)
        # Dicionario de funcoes: permite chamar funcoes fazendo updateInterfaceFunctions[key], onde key é 1,2,3 ou 4
        self.updateInterfaceFunctions = {1: updateP1Interface, 2: updateP2Interface, 3: updateP3Interface, 4: updateP4Interface}
        self.stop = 1

    def stopProgram(self):
        self.stop = 1  # atualiza o valor da variavel stop, a qual é usada para verificar o funcionamento da interface
        self.lapTimeFile.stopDataSave()
        # Fecha arquivo file e porta serial
        self.stopDataFileSave()
        if porta.isOpen():
            porta.flushInput()
            porta.close()
        else:
            pass

    # program() roda em loop
    def program(self):
        global sec
        if (self.stop == 0):
            sec = time()
            # Le dados da porta serial
            packIndexes = [1, 2, 3, 4]
            packSizes = [16, 22, 15, 30]
            self.buffer = readAll(packSizes, packIndexes)

            if len(self.buffer) != 0:
                # chamada da função updateLabel para analisar os dados recebidos atualizar os mostradores da interface
                self.updateLabel(self.buffer)

            # Apos updateTime segundos, chama funcao program() novamente
            QtCore.QTimer.singleShot(self.updateTime, lambda: self.program())

    # Função para definir nome do arquivo txt no qual os dados serão gravados,
    # abrir este arquivo e gravar dados de setup e os dados recebidos através na porta seria
    def beginDataSave(self):

        arquivo = ui.lineEdit_FileName.text()  # variável arquivo recebe o nome que o usuário informa na interface do arquivo a ser criado
        self.dataFile.startDataSave(arquivo)
        self.dataFile.writeRow("***\n")
        self.dataFile.writeRow("CARRO: " + str(ui.lineEdit_SetupCar.text()) + "\n")
        self.dataFile.writeRow("PISTA: " + str(ui.lineEdit_SetupTrack.text()) + "\n")
        self.dataFile.writeRow("PILOTO: " + str(ui.lineEdit_SetupDriver.text()) + "\n")
        self.dataFile.writeRow("TEMPERATURA AMBIENTE: " + str(ui.lineEdit_SetupTemperature.text()) + "\n")
        self.dataFile.writeRow("ANTIROLL: " +str(ui.lineEdit_SetupAntiroll.text()) + "\n")
        self.dataFile.writeRow("PRESSAO PNEUS DIANTEIROS: " +str(ui.lineEdit_SetupTirePressureFront.text()) + "\n")
        self.dataFile.writeRow("PRESSAO PNEUS TASEIROS: " +str(ui.lineEdit_SetupTirePressureRear.text()) + "\n")
        self.dataFile.writeRow("ANGULO DE ATAQUE DA ASA: " +str(ui.lineEdit_SetupWingAttackAngle.text()) + "\n")
        self.dataFile.writeRow("MAPA MOTOR: " +str(ui.lineEdit_SetupEngineMap.text()) + "\n")
        self.dataFile.writeRow("BALANCE BAR: " +str(ui.lineEdit_SetupBalanceBar.text()) + "\n")
        self.dataFile.writeRow("DIFERENCIAL: " +str(ui.lineEdit_SetupDifferential.text()) + "\n")
        self.dataFile.writeRow("TAXA DE AQUISICAO: " +str(ui.lineEdit_SetupAcquisitionRate.text()) + "\n")
        self.dataFile.writeRow("COMENTARIOS: " +str(ui.textEdit_SetupComments.toPlainText()) + "\n")
        self.dataFile.writeRow("POSICAO MAXIMA DO VOLANTE: " +str(ui.spinBox_WheelPosMax.value()) + "\n")
        self.dataFile.writeRow("POSICAO MINIMA DO VOLANTE: " +str(ui.spinBox_WheelPosMin.value()) + "\n")
        self.dataFile.writeRow("SUSPENSAO: " +str(ui.lineEdit_CalibrationConstant.text()) + "\n")
        self.dataFile.writeRow("PACOTE1 40 " + vectorToString(self.data.p1Order, ' '))
        self.dataFile.writeRow("PACOTE2 20 " + vectorToString(self.data.p2Order, ' '))
        self.dataFile.writeRow("PACOTE3 2 " + vectorToString(self.data.p3Order, ' '))
        self.dataFile.writeRow("PACOTE4 20 " + vectorToString(self.data.p4Order, ' '))
        # self.dataFile.writeRow("PACOTE1 40 acelY acelX acelZ velDD velT sparkCut suspPos time\n")
        # self.dataFile.writeRow("PACOTE2 20 oleoP fuelP tps rearBrakeP frontBrakeP volPos beacon correnteBat rpm time2\n")
        # self.dataFile.writeRow("PACOTE3 2 ect batVoltage releBomba releVent pduTemp tempDiscoD tempDiscoE time3\n")
        self.dataFile.writeRow("***\n\n")

        ui.label_12.setText("Saving...")  # informa ao usuário a situação atual de gravação de dados

    def stopDataFileSave(self):
        self.dataFile.stopDataSave()
        ui.label_12.setText("Not saving...")  # informa ao usuário a situação atual de gravação de dados

    def updateLabel(self, buffer):
        global aux_time, sec, cont, exe_time

        packID = buffer[0]
        # Atualiza dados em Data e atualiza campos respectivos na interface
        if (self.data.updateDataFunctions[packID](buffer) == 0):
            errorLog.writeErrorLog(" updateData: Pacote " + str(packID) + "com tamanho diferente do configurado")
        self.updateInterfaceFunctions[packID](self.data)

        # Grava linha buffer no arquivo
        if self.dataFile.save == 1:
            string = self.data.createPackString(buffer[0])
            self.dataFile.writeRow(string)

        # Atualiza graficos
        updatePlot(self.data)

        # Atualiza o mostrador textBrowser_Buffer com as ultimas 6 listas de dados recebidas.
        string = vectorToString(self.lastBuffers, '\n')
        self.lastBuffers = np.roll(self.lastBuffers, 1)
        self.lastBuffers[0] = vectorToString(buffer, ' ')
        ui.textBrowser_Buffer.setText(string)

        if (self.stop == 0):
            # As seguintes linhas contam o tempo de uma execução do programa e quantas execuções foram realizadas
            time_init = sec
            sec = time()
            milli_sec = (sec - time_init) * 1000  # tempo final - tempo inicial convertido para milissegundos
            exe_time = exe_time + milli_sec  # tempo total de execução
            cont = cont + 1  # número de execuções
            # As linhas a seguir printam no prompt o tempo médio de execução a cada mil execuções até 5000
            if (cont == 1 or cont == 1000 or cont == 2000 or cont == 3000 or cont == 4000 or cont == 5000):
                print("tempo médio:", exe_time / cont)
                print("qtd de execuções", cont)


def updatePlot(data):
    # as linhas a seguir plotam os gráficos selecionados atráves dos checkBox e define as cores de cada gráfico.
    # Os gráficos são compostos pelos últimos 50 pontos do dado
    # Arrasta vetor pto lado para que novo valor possa ser inserido
    data.rollArrays()

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

    # Gauge da bateria
    ui.progressBar_BatteryVoltage.setValue(int(data.dic['batVoltage']))
    ui.label_15.setText(str(data.dic['batVoltage']))

  # alarme bateria: o fundo da linha da tabela referente à tensão na bateria recebe a cor vermelha
    if (data.dic['batVoltage'] <= 11.5):
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
        item.setBackground(QtGui.QColor(255, 255, 255))

    ui.progressBar_EngineTemperature.setValue(data.dic['ect'])
    ui.label_6.setText(str(data.dic['ect']))

    # alarme temperatura: o fundo da linha da tabela referente à temperatura do motor recebe a cor vermelha
    if (data.dic['ect'] >= 95.0):
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
        item.setBackground(QtGui.QColor(255, 255, 255))

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


# função para atualizar o arquivo setup com novos valores
def updateSetup():

    global settings, errorLog
    settings.setValue('wheelPosMax',str(ui.spinBox_WheelPosMax.value()))
    settings.setValue('wheelPosMin',str(ui.spinBox_WheelPosMin.value()))
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
    settings.setValue('sampleRate' ,str(ui.lineEdit_SetupAcquisitionRate.text()))
    settings.setValue('setupComments' ,str(ui.textEdit_SetupComments.toPlainText()))
    settings.setValue('filename', ui.lineEdit_FileName.text())

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


# Roda janela
app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Classes globais
errorLog = ErrorLog(ui.errorLog)
program = Program()

# ações
ui.pushButtonOpenFile.clicked.connect(selectFile)
ui.pushButton_Exit.clicked.connect(exit)  # botão para fechar a interface
ui.pushButton_StartProgram.clicked.connect(startProgram)  # botão para iniciar o programa
ui.pushButton_UpdatePorts.clicked.connect(updatePorts)  # botão para atualizar as portas seriis disponíveis
ui.pushButton_SaveSetupValues.clicked.connect(updateSetup)  # botão para atualizar os dados de setup no arquivo txt
ui.actionExit.triggered.connect(exit)  # realiza a ação para fechar a interface
ui.comboBox_SerialPorts.addItems(serialPorts())  # mostra as portas seriais disponíveis
ui.comboBox_Baudrate.addItems(["115200", "38400", "1200", "2400", "9600", "19200", "57600" ])  # mostra os baudrates disponíveis
#ui.comboBox_Baudrate.currentIndexChanged.connect(selection_baudrate)
#pixmap = QPixmap("image1.png")
#ui.label_28.setPixmap(pixmap)
updateInitValues()  # inicializa os valores de setup de acordo com o arquivo setup
ui.label_12.setText("Not saving...")  # informa na interface que os dados não estão sendo salvos
ui.graphicsView_DiagramaGG.setXRange(-2, 2)
ui.graphicsView_DiagramaGG.setYRange(-2, 2)

# cores do gráfico
ui.checkBox_OilPressure.setStyleSheet('color:blue')
ui.checkBox_FuelPressure.setStyleSheet('color:green')
ui.checkBox_EngineTemperature.setStyleSheet('color:red')
ui.checkBox_OilPressure.setStyleSheet('color:black')

# Mostra a janela e fecha o programa quando ela é fechada (?)
MainWindow.show()
sys.exit(app.exec_())
