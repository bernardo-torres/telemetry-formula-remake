self.tps
import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
# pacotes necessários
import sys
import pyqtgraph as pg
from time import time
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

from interface_generated import *

# inicializações
global save, stop, arq, arq_laptime, sec, cont, porta, x, y, s
save = 0  # variável que define se salva dados no txt 0= não salva, 1=salva
stop = 1  # variável que define se o programa está pausado/parado 0= não parado, 1= parado
arq = 0
arq_laptime = 0
array_temp = np.array([]).astype('int')
array_fuel_p = np.array([]).astype('int')
array_oil_p = np.array([]).astype('int')
array_battery = np.array([]).astype('int')
array_leitura = np.array([]).astype('int')
x = np.array([]).astype('int')
y = np.array([]).astype('int')
s = np.array([]).astype('int')
divisor = 1
array_lap = np.array([]).astype('int')
aux_time = np.array([0]).astype('int')
# Vetores para mostrar últimos dados recebidos (TEMPORARIO)
buffer1 = np.array([]).astype('int')
buffer2 = np.array([]).astype('int')
buffer3 = np.array([]).astype('int')
buffer4 = np.array([]).astype('int')
buffer5 = np.array([]).astype('int')
buffer6 = np.array([]).astype('int')
sec = 0
cont = 0
exe_time = 0

porta = serial.Serial()


# Classe values é utilizada para armazenar valores das grandezas apos a separacao
# delas dentro do buffer e processamento
class data:
    def __init__(self):
        self.acelY = 0
        self.acelX = 0
        self.acelZ = 0
        self.velDD = 0
        self.velT = 0
        self.sparkCut = 0
        self.suspPos = 0
        self.time = 0
        self.oleoP = 0
        self.fuelP = 0
        self.tps = 0
        self.rearBrakeP = 0
        self.frontBrakeP = 0
        self.volPos = 0
        self.beacon = 0
        self.correnteBat = 0
        self.rpm = 0
        self.time2 = 0
        self.batVoltage = 0
        self.ect = 0
        self.releBomba = 0
        self.releVent = 0
        self.pduTemp = 0
        self.tempDiscoD = 0
        self.tempDiscoE = 0
        self.time3 = 0

    def updateP1(self, buffer):
        if ((int(buffer[0]) == 1) and (len(buffer) == 15)):  # testa se é o pacote 1 e está completo
            self.acelX = (int(buffer[2]) << 8) + int(buffer[3])  # recebe o valor contido na lista de dados(leitura) em suas respectivas posições e realiza as operações de deslocamento e soma binária
            self.acelX = round(float(x_accel / 16384), 3)  #
            self.acelY = (int(buffer[4]) << 8) + int(buffer[5])
            self.acelY = round(float(y_accel / 16384), 3)
            self.acelZ = (int(buffer[6]) << 8) + int(buffer[7])
            self.acelZ = round(float(z_accel / 16384), 3)
            self.velDD = int(buffer[8])
            self.velT = int(buffer[9])
            self.sparkCut = ((buffer[10]) & 128) >> 7
            self.suspPos = (((buffer[10]) & 127) << 8) + int(buffer[11])
            self.time = ((buffer[12]) << 8) + int(buffer[13])
            self.time = 25 * self.time

    def updateP2(self, buffer):
        if ((int(buffer[0]) == 2) and (len(buffer) == 22)):  # testa se é o pacote 2 e está completo
            self.oleoP = (int(buffer[2]) << 8) + int(buffer[3])
            oself.oleoP = round(float(self.oleoP * 0.001), 2)
            self.fuelP = (int(buffer[4]) << 8) + int(buffer[5])
            self.fuelP = round(float(self.fuelP * 0.001), 2)
            self.tps = (int(buffer[6]) << 8) + int(buffer[7])
            #buffer = round(float(buffer * 0.1), 2)
            self.rearBrakeP = (int(buffer[8]) << 8) + int(buffer[9])
            self.rearBrakeP = round(self.rearBrakeP * 0.02536, 1)
            self.frontBrakeP = (int(buffer[10]) << 8) + int(buffer[11])
            self.frontBrakeP = round(self.frontBrakeP * 0.02536, 1)
            self.volPos = (int(buffer[12]) << 8) + int(buffer[13])
            self.volPos = round(((self.volPos - (ui.spinBox_WheelPosMin.value())) / ((ui.spinBox_WheelPosMax.value() - ui.spinBox_WheelPosMin.value()) / 240) - 120), 2)
            self.beacon = (int(buffer[14])) >> 7
            self.correnteBat = ((int(buffer[14]) & 127) << 8) + int(buffer[15])
            self.rpm = (int(buffer[16]) << 8) + int(buffer[17])
            self.time2 = (int(buffer[18]) << 8) + int(buffer[19])
            self.time2 = 25 * time2

    def updateP3(self):
        if ((int(buffer[0]) == 3) and (len(buffer) == 15)):  # testa se é o pacote 3 e está completo
            self.ect = (int(buffer[(ui.spinBox_IndexEngineTemperature.value())]) << 8) + int(buffer[(ui.spinBox_IndexEngineTemperature.value()) + 1])
            self.ect = round(float(self.ect * 0.1), 2)
            self.batVoltage = ((buffer[(ui.spinBox_IndexBattery.value()) + 1]) << 8) + (buffer[(ui.spinBox_IndexBattery.value()) + 2])
            self.batVoltage = round(float(battery * 0.01), 2)
            self.releBomba = (int(buffer[(ui.spinBox_IndexFuelPumpRelay.value()) + 2]) & 128) >> 7
            self.releVent = (int(buffer[(ui.spinBox_IndexFanRelay.value()) + 1]) & 32) >> 5
            self.pduTemp = (buffer[(ui.spinBox_IndexRelayBoxTemperature.value())] << 8) + buffer[(ui.spinBox_IndexRelayBoxTemperature.value()) + 1]
            self.pduTemp = round(float(self.pduTemp), 2)
            self.tempDiscoE = (buffer[(ui.spinBox_IndexBreakTempRear.value()) + 1] << 8) + (buffer[(ui.spinBox_IndexBreakTempRear.value()) + 2])
            self.tempDiscoE = round(float(self.tempDiscoE), 2)
            self.tempDiscoD = (buffer[(ui.spinBox_IndexBreakTempFront.value()) + 2] << 8) + (buffer[(ui.spinBox_IndexBreakTempFront.value()) + 3])
            self.tempDiscoD = round(float(self.tempDiscoD), 2)
            self.time3 = (int(buffer[(ui.spinBox_IndexTime3.value()) + 3]) << 8) + int(buffer[(ui.spinBox_IndexTime3.value()) + 4])
            self.time3 = 25 * self.time3


# A função update_values atualiza os campos que já haviam sido definidos em utilizações ateriores da interface
# Ela serve para que não seja necessário atualizar todos os campos sempre que for necessária o reinício da interface
def update_values():
    try:
        setup = open('setup.txt', 'r')
        values = setup.readlines()
        i = 0
        while (i <= len(values) - 1):
            # caso o valor da lista na posição i seja \n significa que não foi setado, anteriormente, um valor nesse campo,
            # ou seja, ao redefinir os valores dos campos utilizando os valores salvos anteriormente, os campos devem receber ''
            values[i] = values[i].replace('\n', '')
            i = i + 1
        print(values)
        if (len(values) > 0):
            ui.spinBox_WheelPosMax.setValue(int(values[0]))
            ui.spinBox_WheelPosMin.setValue(int(values[1]))
            ui.lineEdit_CalibrationConstant.setText(str(values[2]))
            ui.lineEdit_SetupCar.setText(str(values[3]))
            ui.lineEdit_SetupTrack.setText(str(values[4]))
            ui.lineEdit_SetupDriver.setText(str(values[5]))
            ui.lineEdit_SetupTemperature.setText(str(values[6]))
            ui.lineEdit_SetupAntiroll.setText(str(values[7]))
            ui.lineEdit_SetupTirePressureFront.setText(str(values[8]))
            ui.lineEdit_SetupTirePressureRear.setText(str(values[9]))
            ui.lineEdit_SetupWingAttackAngle.setText(str(values[10]))
            ui.lineEdit_SetupEngineMap.setText(str(values[11]))
            ui.lineEdit_SetupBalanceBar.setText(str(values[12]))
            ui.lineEdit_SetupDifferential.setText(str(values[13]))
            ui.lineEdit_SetupAcquisitionRate.setText(str(values[14]))
            ui.textEdit_SetupComments.setText(str(values[15]))
        setup.close()
    except:
        print("ERRO")


# As 3 funções a seguir realizam a configuração de qual porta serial será utilizada
# função que atualiza as portas seriais disponíveis
# Atualiza portas seriais disponiveis
def update_ports():
    ui.comboBox_SerialPorts.clear()
    ui.comboBox_SerialPorts.addItems(serial_ports())


# Lista as portas seriais disponiveis. Retorna uma lista com os nomes das portas
def serial_ports():
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


# Função que inicia a execução da interface
def start_program():
    try:
        global stop, tim, arq_laptime
        stop = 0
        tim = ui.doubleSpinBox_UpdateTime.value() * 1000
        # abre e configura a porta serial utilizando os valores definidos pelo usuário através da interface
        porta.baudrate = int(ui.comboBox_Baudrate.currentText())
        porta.port = str(ui.comboBox_SerialPorts.currentText())
        porta.timeout = 1
        porta.open()
        now = datetime.now()
        arquivo = "tempos_de_volta_" + str(now.hour) + "_" + str(now.minute) + ".txt"
        arq_laptime = open(arquivo, 'w')
        print("0.45")
        program()
        print("1") # chama a função programa e passa por parãmetro o valor de stop
# O erro de porta serial é analisado pela exceção serial.SerialException. Esse erro é tratado pausando o programa e
# utilizando uma caixa de diálogo, a qual informa ao usuário o erro encontrado
    except serial.serialutil.SerialException:
        stop_program()
        dlg = QMessageBox(None)
        dlg.setWindowTitle("Error!")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText(
         "<center>Failed to receive data!<center> \n\n <center>Check Serial Ports and Telemetry System.<center>")
        dlg.exec_()


# Le buffer da porta serial
def read_all():
    while True:
        while (porta.inWaiting() == 0):
            pass
        read_buffer = b''
        firstByte = porta.read()
        if int.from_bytes(firstByte, byteorder='big') == 1:
            read_buffer += firstByte
            # Le o segundo byte de inicio
            a = porta.read()
            if int.from_bytes(a, byteorder='big') == 5:
                read_buffer += a
                break
            else:
                print('Erro na leitura2')
        # Se o byte lido nao for 1, quer dizer que perdeu algum dado.
        else:
            print('Erro na leitura1')
    while True:
        byte = porta.read(size=13)  # dado com formato de byte
        read_buffer += byte

        if(len(read_buffer) == 15):
            break
        else:
            print('AQQQQ')
    return read_buffer


# Função que executa o programa. Essa função verifica se o programa deve ser executado. Em caso afirmativo, é feita
# a leitura da porta serial e é chamada a função que inicia o tratamento dos dados
def program():
    global stop, sec
    try:
        if (stop == 0):
            # A variável sec recebe o primeiro tempo
            # A função tempo retorna um valor o qual refere-se a quantos segundos se passaram desde um data pre-estabelecida pelo SO
            # Sendo assim, para obter o tempo de execução deve-se fazer tempofinal-tempoinicial. Isso é feito após a outra chamada da função tempo, a qual retorna o tempo final
            print("2")
            sec = time()
            print("3")

            buffer = read_all()
            print(buffer)
            test = np.zeros(15)
            for i in range(0, 15):
                test[i] = buffer[i]
            print(test)
            updateLabel(test)
            # chamada da função updateLabel para analisar os dados recebidos atualizar os mostradores da interface
    finally:
        QtCore.QTimer.singleShot(tim, program)


# Função que recebe novos dados, analisa sua consistência, verifica qual pacote foi recebido, realiza operações
# necessárias com os dados e chama as funções de atualização de pacotes. Além disso, a função realiza a escrita
# dos dados no arquivo txt. Isso é feito dentro de cada if para que só sejam gravados dados que foram recebidos corretamente.
# A função recebe o vetor "leitura", realiza as operações binárias, deslocamento e soma, e cria o vetor "lista".
# Dessa forma, o vetor "leitura" contém os bytes convertidos para inteiro, porém não os valores das variáveis que trabalhamos.
# Já o vetor "lista", possui os valores corretos para serem mostrados
def updateLabel(buffer):
    lista = np.array([]).astype('int')  # cria uma lista chamada "lista"
    lista = np.append(lista, buffer[0])
    print("5")
    if ui.lineEdit_CalibrationConstant.text() == "":  # Caso a constante de calibração não seja definida é utilizado o valor 1
        constante = 1
    else:
        constante = float(ui.lineEdit_CalibrationConstant.text())
    # print("tamanho", leitura.size)
    # print("tipo", type(leitura))
    # print(leitura)
    try:
        global aux_time, array_lap, array_oil_p, array_temp, array_battery, buffer1, buffer2, buffer3, buffer4, buffer5, buffer6, sec, cont, exe_time

            if save == 1:
                string = str(lista[0]) + ' ' + str(lista[1]) + ' ' + str(lista[2]) + ' ' + str(lista[3]) + ' ' + str(lista[4]) + ' ' + str(lista[5]) + ' ' + str(lista[6]) + ' ' + str(lista[7]) + ' ' + str(lista[8])
            # print("string", string)
                arq.write(string)  # escreve no arquivo txt a lista de dados recebidos
                arq.write("\n")  # escreve no arquivo txt uma quebra de linha

            ui.lineEdit_CurrentWheelPos.setText(str(wheel_pos))


            if ((beacon == 1) and ((time2 - aux_time[aux_time.size - 1]) >= 200)):
                if (aux_time.size == 0):
                    aux_time = np.append(aux_time, time2)
                else:
                    array_lap = np.append(array_lap, time2 - aux_time[aux_time.size - 1])
                    aux_time = np.append(aux_time, time2)
                    laptime = str(array_lap[array_lap.size - 1])
                    arq_laptime.write(laptime)
                    arq_laptime.write("\n")

            array_oil_p = np.append(array_oil_p, oil_p)
            # print(lista)
            if save == 1:
                string = str(lista[0]) + ' ' + str(lista[1]) + ' ' + str(lista[2]) + ' ' + str(lista[3]) + ' ' + str(lista[4]) + ' ' + str(lista[5]) + ' ' + str(lista[6]) + ' ' + str(lista[7]) + ' ' + str(lista[8]) + ' ' + str(lista[9])+ ' ' + str(lista[10])
            # print("string", string)
                arq.write(string)
                arq.write("\n")


            array_temp = np.append(array_temp, temp)
            array_battery = np.append(array_battery, battery)
            # print(lista)
            if save == 1:
                string = str(lista[0]) + ' ' + str(lista[1]) + ' ' + str(lista[2]) + ' ' + str(lista[3]) + ' ' + str(lista[4]) + ' ' + str(lista[5]) + ' ' + str(lista[6]) + ' ' + str(lista[7]) + ' ' + str(lista[8])
                # print("string", string)
                arq.write(string)
                arq.write("\n")

        elif ((int(buffer[0]) == 4) and (buffer.size == 30)):  # testa se é o pacote 4 e está completo
            p1_ext = ((buffer[2] << 16) + (buffer[3] << 8) + buffer[4])
            lista = np.append(lista, p1_ext)
            p2_ext = ((buffer[5] << 16) + (buffer[6] << 8) + buffer[7])
            lista = np.append(lista, p2_ext)
            p3_ext = ((buffer[8] << 16) + (buffer[9] << 8) + buffer[10])
            lista = np.append(lista, p3_ext)
            p4_ext = ((buffer[11] << 16) + (buffer[12] << 8) + buffer[13])
            lista = np.append(lista, p4_ext)
            p5_ext = ((buffer[14] << 16) + (buffer[15] << 8) + buffer[16])
            lista = np.append(lista, p5_ext)
            p6_ext = ((buffer[17] << 16) + (buffer[18] << 8) + buffer[19])
            lista = np.append(lista, p6_ext)
            p7_ext = ((buffer[20] << 16) + (buffer[21] << 8) + buffer[22])
            lista = np.append(lista, p7_ext)
            p8_ext = ((buffer[23] << 16) + (buffer[24] << 8) + buffer[25])
            lista = np.append(lista, p8_ext)
            time4 = ((buffer[26] << 8) + (buffer[27]))
            lista = np.append(lista, time4)
            time4 = 25 * time4
            # array_temp= np.append(array_temp,temp)
            if save == 1:
                string = str(lista[0]) + ' ' + str(lista[1]) + ' ' + str(lista[2]) + ' ' + str(lista[3]) + ' ' + str(lista[4]) + ' ' + str(lista[5]) + ' ' + str(lista[6]) + ' ' + str(lista[7]) + ' ' + str(lista[8]) + ' ' + str(lista[9])
            # print("string", string)
                arq.write(string)
                arq.write("\n")
        else:
            print("Erro")
    except:
        print("Erro 2")
    # as linhas a seguir plotam os gráficos selecionados atráves dos checkBox e define as cores de cada gráfico.
    # Os gráficos são compostos pelos últimos 50 pontos do dado contidos nos arrays de cada dado.
    ui.graphicsView_EngineData.clear()
    if ui.checkBox_EngineTemperature.isChecked() == 1:
        ui.graphicsView_EngineData.plot(array_temp[array_temp.size - 50:array_temp.size], pen='r')
    if ui.checkBox_FuelPressure.isChecked() == 1:
        ui.graphicsView_EngineData.plot(array_fuel_p[array_fuel_p.size - 50:array_fuel_p.size], pen='g')
    if ui.checkBox_Voltage.isChecked() == 1:
        ui.graphicsView_EngineData.plot(array_battery[array_battery.size - 50:array_battery.size], pen='b')
    if ui.checkBox_OilPressure.isChecked() == 1:
        ui.graphicsView_EngineData.plot(array_oil_p[array_oil_p.size - 50:array_oil_p.size], pen='y')
    # as linhas a seguir atualizam o mostrador textBrowser_Buffer com as ultimas 6 listas de dados recebidas.
    # Caso o número de listas recebidas seja menor que 6, são mostradas apenas estas
    buffer6 = buffer5
    buffer5 = buffer4
    buffer4 = buffer3
    buffer3 = buffer2
    buffer2 = buffer1
    buffer1 = buffer
    ui.textBrowser_Buffer.setText(str(buffer1) + "\n" + str(buffer2) + "\n" + str(buffer3) + "\n" + str(buffer4) + "\n" + str(buffer5) + "\n" + str(buffer6))
    if (stop == 0):
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

  # Função que atualiza os mostradores relacionados aos dados do pacote 1
  # Pacote 1: X_Accelerometer, Y_Accelerometer, Z_Accelerometer, Sparcut Relay, Speed, Suspension Course, time
  # Para atualizar as células da tabela tableWidget_Package1 é necessário definir o valor da variável item como o
  # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def update_p1():
    item = QTableWidgetItem(str(x_accel))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(0, 1, item)
    x = np.append(x,x_accel)  # concatena o valor de x_accel no vetor x e este é utilizado para plotar o diagramaGG na função update_diagramagg
    item = QTableWidgetItem(str(y_accel))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(1, 1, item)
    y = np.append(y,y_accel)  # concatena o valor de y_accel no vetor y e este é utilizado para plotar o diagramaGG na função update_diagramagg
    item = QTableWidgetItem(str(z_accel))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(2, 1, item)
    item = QTableWidgetItem(str(vel_dianteira))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(3, 1, item)
    item = QTableWidgetItem(str(vel_traseira))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(4, 1, item)
    item = QTableWidgetItem(str(rele_sparkcut))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(5, 1, item)
    if (int(rele_sparkcut) == 1):
        ui.radioButton_SparkcutRelay.setChecked(False)
    else:
        ui.radioButton_SparkcutRelay.setChecked(True)
    item = QTableWidgetItem(str(susp))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(6, 1, item)
    item = QTableWidgetItem(str(time1))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package1.setItem(7, 1, item)
    if (array_lap.size == 1):
        ui.lineEdit_LastLap.setText(str(array_lap[array_lap.size - 1]))
    elif (array_lap.size > 1):
        ui.lineEdit_LastLap.setText(str(array_lap[array_lap.size - 1]))
        ui.lineEdit_LastLap2.setText(str(array_lap[array_lap.size - 2]))
    update_diagramagg(ui.graphicsView_DiagramaGG, w1, s, x, y)  # Chamada da função update_diagramagg

  # função que meeostra o diagrama gg
def update_diagramagg(self, graphicsView_DiagramaGG, w1, s, x, y):
    s = np.append(s, pg.ScatterPlotItem([y[y.size - 1]], [x[x.size - 1]], size=5,
                                        pen=pg.mkPen(None)))
    s[x.size - 1].setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
    w1.addItem(s[x.size - 1])


  # Função que atualiza os mostradores relacionados aos dados do pacote 2
  # Pacote 2: Oil pressure, fuel pressure, TPS, break pressure(rear), break pressute(front), wheel position, beacon, current, time
  # Para atualizar as células da tabela tableWidget_Package2 é necessário definir o valor da variável item como o
  # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def update_p2(oil_p, pcomb, tps, p_freio_d, p_freio_t, wheel_pos, beacon, current,rpm, time2):
    item = QTableWidgetItem(str(beacon))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(0, 1, item)
    item = QTableWidgetItem(str(p_freio_d))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(1, 1, item)
    if ((p_freio_t + p_freio_d) != 0):  # Verificação necessária para que não ocorra divisão por zero
        ui.progressBar_FrontBreakBalance.setValue(100 * p_freio_d / (p_freio_t + p_freio_d))  # porcentagem da pressão referente ao freio dianteiro
    ui.progressBar_FrontBreakPressure.setValue(p_freio_d)
    ui.label_65.setText(str(p_freio_d))
    item = QTableWidgetItem(str(p_freio_t))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(2, 1, item)
    if ((p_freio_t + p_freio_d) != 0):  # Verificação necessária para que não ocorra divisão por zero
        ui.progressBar_RearBreakBalance.setValue(100 * p_freio_t / (p_freio_t + p_freio_d))  # porcentagem da pressão referente ao freio traseiro
    ui.label_69.setText(str(p_freio_t))
    ui.progressBar_RearBreakPressure.setValue(p_freio_t)
    item = QTableWidgetItem(str(current))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(3, 1, item)
    item = QTableWidgetItem(str(pcomb))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(4, 1, item)
    array_fuel_p = np.append(array_fuel_p, pcomb)
    ui.progressBar_FuelPressure.setValue(pcomb)
    ui.label_17.setText(str(pcomb))
    ui.progressBar_OilPressure.setValue(oil_p)
    ui.label_10.setText(str(oil_p))
    item = QTableWidgetItem(str(oil_p))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(5, 1, item)
    item = QTableWidgetItem(str(rpm))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(6, 1, item)
    item = QTableWidgetItem(str(time2))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(7, 1, item)
    ui.progressBar_TPS.setValue(tps)
    ui.progressBar_TPS.setProperty("value", tps)
    item = QTableWidgetItem(str(tps))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(8, 1, item)
    dial_WheelPos.setValue(wheel_pos)
    ui.label_19.setText(str(wheel_pos))
    item = QTableWidgetItem(str(wheel_pos))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package2.setItem(9, 1, item)


  # Função que atualiza os mostradores relacionados aos dados do pacote 3
  # Pacote 3: Engine Temp, battery, fuel pump relay, fan relay, relay box temperature, break temperature rear, break temperature front, time
  # Para atualizar as células da tabela tableWidget_Package3 é necessário definir o valor da variável item como o
  # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def update_p3(self, temp, battery, rele_bomba, rele_vent, temp_caixaR, temp_freiot, temp_freiod, time3):
    ui.progressBar_BatteryVoltage.setValue(int(battery))
    ui.label_15.setText(str(battery))
  # alarme bateria: o fundo da linha da tabela referente à tensão na bateria recebe a cor vermelha
    if (battery <= 11.5):
        item = ui.tableWidget_Package3.item(0, 0)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = ui.tableWidget_Package3.item(0, 2)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = QTableWidgetItem(str(battery))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 0, 0))
        ui.tableWidget_Package3.setItem(0, 1, item)
    else:
        item = ui.tableWidget_Package3.item(0, 0)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = ui.tableWidget_Package3.item(0, 2)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QTableWidgetItem(str(battery))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 255, 255))
    ui.tableWidget_Package3.setItem(0, 1, item)
    item = QTableWidgetItem(str(temp_freiod))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(1, 1, item)
    item = QTableWidgetItem(str(temp_freiot))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(2, 1, item)
    ui.progressBar_EngineTemperature.setValue(temp)
    ui.label_6.setText(str(temp))
  # alarme temperatura: o fundo da linha da tabela referente à temperatura do motor recebe a cor vermelha
    if (temp >= 95.0):
        item = ui.tableWidget_Package3.item(3, 0)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = ui.tableWidget_Package3.item(3, 2)
        item.setBackground(QtGui.QColor(255, 0, 0))
        item = QTableWidgetItem(str(temp))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 0, 0))
        ui.tableWidget_Package3.setItem(3, 1, item)
    else:
        item = ui.tableWidget_Package3.item(3, 0)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = ui.tableWidget_Package3.item(3, 2)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QTableWidgetItem(str(temp))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 255, 255))
        ui.tableWidget_Package3.setItem(3, 1, item)
        item = QTableWidgetItem(str(rele_vent))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(4, 1, item)
    if (int(rele_vent) == 1):
        ui.radioButton_FanRelay.setChecked(False)
    else:
        ui.radioButton_FanRelay.setChecked(True)
    item = QTableWidgetItem(str(rele_bomba))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(5, 1, item)
    if (int(rele_bomba) == 1):
        ui.radioButton_FuelPumpRelay.setChecked(False)
    else:
        ui.radioButton_FuelPumpRelay.setChecked(True)
    item = QTableWidgetItem(str(temp_caixaR))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(6, 1, item)
    item = QTableWidgetItem(str(time3))
    item.setTextAlignment(QtCore.Qt.AlignCenter)
    ui.tableWidget_Package3.setItem(7, 1, item)

  # Função que atualiza os mostradores relacionados aos dados do pacote 4
  # Pacote 4: P1, P2, P3, P4, P5, P6, P7 e P8 strain gauges, time
  # Para atualizar as células da tabela tableWidget_StrainGauge é necessário definir o valor da variável item como o
  # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def update_p4(p1_ext, p2_ext, p3_ext, p4_ext, p5_ext, p6_ext, p7_ext, p8_ext, time4):
  # extensometros
  item = QTableWidgetItem(str(p1_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(0, 1, item)
  item = QTableWidgetItem(str(p2_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(1, 1, item)
  item = QTableWidgetItem(str(p3_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(2, 1, item)
  item = QTableWidgetItem(str(p4_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(3, 1, item)
  item = QTableWidgetItem(str(p5_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(4, 1, item)
  item = QTableWidgetItem(str(p6_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(5, 1, item)
  item = QTableWidgetItem(str(p7_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(6, 1, item)
  item = QTableWidgetItem(str(p8_ext))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(7, 1, item)
  item = QTableWidgetItem(str(time4))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_StrainGauge.setItem(8, 1, item)

  # função para atualizar o arquivo setup com novos valores
def update_setup():
    setup = open('setup.txt', 'w')
  # if((spinBox_WheelPosMax.value()!=setup.readline(0)) or (spinBox_WheelPosMin.value() != setup.readline(1)) or (spinBox_IndexEngineTemperature6.value() != setup.readline(2)) or (lineEdit_SetupDifferential.text()!=setup.readline(3))or (lineEdit_SetupCar.text()!=setup.readline(3))or (lineEdit_SetupTrack.text()!=setup.readline(3))or (lineEdit_CalibrationConstant.text()!=setup.readline(3))or (lineEdit_SetupDriver.text()!=setup.readline(3))or (lineEdit_SetupTemperature.text()!=setup.readline(3))or (lineEdit_FileName6.text()!=setup.readline(3))or (lineEdit_SetupBalanceBar.text()!=setup.readline(3))or (lineEdit_SetupTirePressureFront.text()!=setup.readline(3))or (lineEdit_SetupTirePressureRear.text()!=setup.readline(3))or (lineEdit_SetupWingAttackAngle.text()!=setup.readline(3))or (lineEdit_SetupEngineMap.text()!=setup.readline(3))or (textEdit_SetupComments.toPlainText()!=setup.readline(3))):
    setup.write(str(ui.spinBox_WheelPosMax.value()) + "\n")  # grava wheel_pos max
    setup.write(str(ui.spinBox_WheelPosMin.value()) + "\n")  # grava wheel_pos min
    setup.write(str(ui.lineEdit_CalibrationConstant.text()) + "\n")  # grava constante de calibração
    setup.write(str(ui.lineEdit_SetupCar.text()) + "\n")  # grava car
    setup.write(str(ui.lineEdit_SetupTrack.text()) + "\n")  # grava track
    setup.write(str(ui.lineEdit_SetupDriver.text()) + "\n")  # grava driver
    setup.write(str(ui.lineEdit_SetupTemperature.text()) + "\n")  # grava temperature
    setup.write(str(ui.lineEdit_SetupAntiroll.text()) + "\n")  # grava antiroll
    setup.write(str(ui.lineEdit_SetupTirePressureFront.text()) + "\n")  # grava tire pressure front
    setup.write(str(ui.lineEdit_SetupTirePressureRear.text()) + "\n")  # grava tire pressure rear
    setup.write(str(ui.lineEdit_SetupWingAttackAngle.text()) + "\n")  # grava wing attack angle
    setup.write(str(ui.lineEdit_SetupEngineMap.text()) + "\n")  # grava engine map
    setup.write(str(ui.lineEdit_SetupBalanceBar.text()) + "\n")  # grava balance bar
    setup.write(str(ui.lineEdit_SetupDifferential.text()) + "\n")  # grava differential
    setup.write(str(ui.lineEdit_SetupAcquisitionRate.text()) + "\n")  # grava taxa de aquisição
    setup.write(str(ui.textEdit_SetupComments.toPlainText()) + "\n")  # grava comments
    setup.close()

  # Funcao para atualizar campos através dos valores contidos no arquivo setup. A função lê o arquivo e define os valores dos campos relacionados aos dados do arquivo
  # Função para definir nome do arquivo txt no qual os dados serão gravados, abrir este arquivo e gravar dados de setup e os dados recebidos através na porta serial
def gravacao():
    arquivo = ui.lineEdit_FileName.text()  # variável arquivo recebe o nome que o usuário informa na interface do arquivo a ser criado
    now = datetime.now()
    # define o nome do arquivo concatenando o nome definido pelo usuário e hora e minuto do início da gravação
    arquivo = arquivo + "_" + str(now.hour) + "_" + str(now.minute) + ".txt"
    print(arquivo)
    arq = open(arquivo, 'w')
    # escreve os valores de setup no início do arquivo
    arq.write("***\n")
    arq.write("CARRO: " + str(ui.lineEdit_SetupCar.text()) + "\n")
    arq.write("PISTA: " + str(ui.lineEdit_SetupTrack.text()) + "\n")
    arq.write("PILOTO: " + str(ui.lineEdit_SetupDriver.text()) + "\n")
    arq.write("TEMPERATURA AMBIENTE: " + str(ui.lineEdit_SetupTemperature.text()) + "\n")
    arq.write("ANTIROLL: " +str(ui.lineEdit_SetupAntiroll.text()) + "\n")
    arq.write("PRESSÃO PNEUS DIANTEIROS: " +str(ui.lineEdit_SetupTirePressureFront.text()) + "\n")
    arq.write("PRESSÃO PNEUS TASEIROS: " +str(ui.lineEdit_SetupTirePressureRear.text()) + "\n")
    arq.write("ÂNGULO DE ATAQUE DA ASA: " +str(ui.lineEdit_SetupWingAttackAngle.text()) + "\n")
    arq.write("MAPA MOTOR: " +str(ui.lineEdit_SetupEngineMap.text()) + "\n")
    arq.write("BALANCE BAR: " +str(ui.lineEdit_SetupBalanceBar.text()) + "\n")
    arq.write("DIFERENCIAL: " +str(ui.lineEdit_SetupDifferential.text()) + "\n")
    arq.write("TAXA DE AQUISIÇÃO: " +str(ui.lineEdit_SetupAcquisitionRate.text()) + "\n")
    arq.write("COMENTÁRIOS: " +str(ui.textEdit_SetupComments.toPlainText()) + "\n")
    arq.write("POSIÇÃO MÁXIMA DO VOLANTE: " +str(ui.spinBox_WheelPosMax.value()) + "\n")
    arq.write("POSIÇÃO MÍNIMA DO VOLANTE: " +str(ui.spinBox_WheelPosMin.value()) + "\n")
    arq.write("SUSPENSÃO: " +str(ui.lineEdit_CalibrationConstant.text()) + "\n")
    arq.write("PACOTE1 40 acelY acelX acelZ velDD velT sparkCut suspPos time\n")
    arq.write("PACOTE2 20 oleoP fuelP tps rearBrakeP frontBrakeP volPos beacon correnteBat rpm time2\n")
    arq.write("PACOTE3 2 ect batVoltage releBomba releVent pduTemp tempDiscoD tempDiscoE time3\n")
    arq.write("***\n\n")

    save = 1  # atualiza o valor da variavel save, a qual é usada para verificar se está ocorrendo ou não não gravação dos dados
    ui.label_12.setText("Saving...")  # informa ao usuário a situação atual de gravação de dados

      # Função para parar a gravação dos dados no arquivo txt
def stop_gravacao():
    save = 0  # atualiza o valor da variavel save, a qual é usada para verificar se está ocorrendo ou não não gravação dos dados
    ui.label_12.setText("No saving...")  # informa ao usuário a situação atual de gravação de dados
    arq.close()
    # Função para pausar o funcionamento da interface

def stop_program():
    stop = 1  # atualiza o valor da variavel stop, a qual é usada para verificar o funcionamento da interface
    arq_laptime.close()
    if porta.isOpen():
        porta.flushInput()
        porta.close()
    else:
        pass

def exit():
    sys.exit(app.exec_())

# Roda janela
app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# ações
ui.pushButton_Exit.clicked.connect(exit)  # botão para fechar a interface
ui.pushButton_PauseProgram.clicked.connect(stop_program)  # botão para pausar o programa
ui.pushButton_StartProgram.clicked.connect(start_program)  # botão para iniciar o programa
ui.pushButton_SaveFile.clicked.connect(gravacao)  # botão para iniciar gravação de dados no txt
ui.pushButton_StopSaveFile.clicked.connect(stop_gravacao)  # botão para parar a gravação de dados txt
ui.pushButton_UpdatePorts.clicked.connect(update_ports)  # botão para atualizar as portas seriis disponíveis
ui.pushButton_SaveSetupValues.clicked.connect(update_setup)  # botão para atualizar os dados de setup no arquivo txt
ui.actionExit.triggered.connect(exit)  # realiza a ação para fechar a interface
ui.comboBox_SerialPorts.addItems(serial_ports())  # mostra as portas seriais disponíveis
ui.comboBox_Baudrate.addItems(["38400", "1200", "2400", "9600", "19200", "57600", "115200"])  # mostra os baudrates disponíveis
#ui.comboBox_Baudrate.currentIndexChanged.connect(selection_baudrate)
#pixmap = QPixmap("image1.png")
#ui.label_28.setPixmap(pixmap)
update_values()  # inicializa os valores de setup de acordo com o arquivo setup
ui.label_12.setText("No saving...")  # informa na interface que os dados não estão sendo salvos
w1 = ui.graphicsView_DiagramaGG.addPlot()
w1.setRange(xRange=[-2, 2])
w1.setRange(yRange=[-2, 2])

# cores do gráfico
#ui.checkBox_Voltage.setText(_translate("MainWindow", "Voltage"))
ui.checkBox_OilPressure.setStyleSheet('color:blue')
#ui.checkBox_FuelPressure.setText(_translate("MainWindow", "Fuel Pressure"))
ui.checkBox_FuelPressure.setStyleSheet('color:green')
#ui.checkBox_EngineTemperature.setText(_translate("MainWindow", "Engine Temp."))
ui.checkBox_EngineTemperature.setStyleSheet('color:red')
#ui.checkBox_OilPressure.setText(_translate("MainWindow", "Oil Pressure "))
ui.checkBox_OilPressure.setStyleSheet('color:yellow')

# Mostra a janela e fecha o programa quando ela é fechada (?)
MainWindow.show()
sys.exit(app.exec_())
