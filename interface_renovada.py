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
from classData import Data
from interface_generated import *

# inicializações
global save, stop, arq, arq_laptime, sec, cont, porta, x, y, s
save = 0  # variável que define se salva dados no txt 0= não salva, 1=salva
stop = 1  # variável que define se o programa está pausado/parado 0= não parado, 1= parado
arq = 0
arq_laptime = 0
array_leitura = np.array([]).astype('int')
x = np.array([]).astype('int')
y = np.array([]).astype('int')
s = np.array([]).astype('int')
divisor = 1
array_lap = np.array([]).astype('int')
aux_time = np.array([0]).astype('int')
# Vetores para mostrar últimos dados recebidos (TEMPORARIO)
buf = np.zeros(6)
sec = 0
cont = 0
exe_time = 0

porta = serial.Serial()


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
        data = Data()
        program(data)
        print("1")
        # chama a função programa e passa por parãmetro o valor de stop
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
def read_all(bufferSize, firstByteValue):
    while True:
        while (porta.inWaiting() == 0):
            pass
        read_buffer = b''
        firstByte = porta.read()
        if int.from_bytes(firstByte, byteorder='big') == firstByteValue:
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
        byte = porta.read(size=bufferSize - 2)  # dado com formato de byte
        read_buffer += byte

        if(len(read_buffer) == bufferSize):
            break
        else:
            print('AQQQQ')
    return read_buffer


# Função que executa o programa. Essa função verifica se o programa deve ser executado. Em caso afirmativo, é feita
# a leitura da porta serial e é chamada a função que inicia o tratamento dos dados
def program(data):
    global stop, sec
    try:
        if (stop == 0):
            # A variável sec recebe o primeiro tempo
            # A função tempo retorna um valor o qual refere-se a quantos segundos se passaram desde um data pre-estabelecida pelo SO
            # Sendo assim, para obter o tempo de execução deve-se fazer tempofinal-tempoinicial. Isso é feito após a outra chamada da função tempo, a qual retorna o tempo final
            print("Linha 276")
            sec = time()
            print("Linha 278")

            buffer = read_all(15, 1)
            print(buffer)
            test = np.zeros(15)
            for i in range(0, len(buffer)):
                test[i] = buffer[i]
            print(test)
            packIdent = buffer[0]

            updateLabel(test, data)
            # chamada da função updateLabel para analisar os dados recebidos atualizar os mostradores da interface
    finally:
        QtCore.QTimer.singleShot(tim, program(data))


def updatePlot(data):
    # as linhas a seguir plotam os gráficos selecionados atráves dos checkBox e define as cores de cada gráfico.
    # Os gráficos são compostos pelos últimos 50 pontos do dado contidos nos arrays de cada dado.

    data.rollArrays()

    ui.graphicsView_EngineData.clear()
    if ui.checkBox_EngineTemperature.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayTemp, pen='r')
    if ui.checkBox_FuelPressure.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayFuelP, pen='g')
    if ui.checkBox_Voltage.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayBattery, pen='b')
    if ui.checkBox_OilPressure.isChecked() == 1:
        ui.graphicsView_EngineData.plot(data.arrayTime2, data.arrayOilP, pen='y')


def vectorToString(line, delimiter):

    string = delimiter.join(str(x) for x in line)
    string = string + '\n'
    return string


# Função que recebe novos dados, analisa sua consistência, verifica qual pacote foi recebido, realiza operações
# necessárias com os dados e chama as funções de atualização de pacotes. Além disso, a função realiza a escrita
# dos dados no arquivo txt. Isso é feito dentro de cada if para que só sejam gravados dados que foram recebidos corretamente.
# A função recebe o vetor "leitura", realiza as operações binárias, deslocamento e soma, e cria o vetor "lista".
# Dessa forma, o vetor "leitura" contém os bytes convertidos para inteiro, porém não os valores das variáveis que trabalhamos.
# Já o vetor "lista", possui os valores corretos para serem mostrados
def updateLabel(buffer, data):
    if ui.lineEdit_CalibrationConstant.text() == "":  # Caso a constante de calibração não seja definida é utilizado o valor 1
        constante = 1
    else:
        constante = float(ui.lineEdit_CalibrationConstant.text())
    global aux_time, array_lap, array_oil_p, array_temp, array_battery, sec, cont, exe_time, arq, buf

    if buffer[0] == 1:
        data.updateP1Data(buffer)
        update_p1(data)
    elif buffer[0] == 2:
        data.updateP2Data(buffer)
        update_p2(data)
    elif buffer[0] == 3:
        data.updateP3Data(buffer)
        update_p3(data)
    elif buffer[0] == 4:
        data.updateP4Data(buffer)
        update_p4(data)

    if save == 1:
        string = vectorToString(buffer, ' ')
        arq.write(string)  # escreve no arquivo txt a lista de dados recebidos

    updatePlot(data)
    # as linhas a seguir atualizam o mostrador textBrowser_Buffer com as ultimas 6 listas de dados recebidas.
    # Caso o número de listas recebidas seja menor que 6, são mostradas apenas estas
    buf = np.roll(buf, -1)
    buf[5] = buffer
    string = vectorToString(buffer, '\n')
    ui.textBrowser_Buffer.setText(string)

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
def update_p1(data):

    elements = len(data.p1Order)
    for key, i in zip(data.p1Order, range(0, elements)):
        item = QTableWidgetItem(str(data.dic[key]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package1.setItem(i, 1, item)

    x = np.append(x,x_accel)  # concatena o valor de x_accel no vetor x e este é utilizado para plotar o diagramaGG na função update_diagramagg

    y = np.append(y,y_accel)  # concatena o valor de y_accel no vetor y e este é utilizado para plotar o diagramaGG na função update_diagramagg

    if (int(data.dic['sparkCut']) == 1):
        ui.radioButton_SparkcutRelay.setChecked(False)
    else:
        ui.radioButton_SparkcutRelay.setChecked(True)

    # if (array_lap.size == 1):
    #     ui.lineEdit_LastLap.setText(str(array_lap[array_lap.size - 1]))
    # elif (array_lap.size > 1):
    #     ui.lineEdit_LastLap.setText(str(array_lap[array_lap.size - 1]))
    #     ui.lineEdit_LastLap2.setText(str(array_lap[array_lap.size - 2]))

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
def update_p2(data):

    elements = len(data.p2Order)
    for key, i in zip(data.p2Order, range(0, elements)):
        item = QTableWidgetItem(str(data.dic[key]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package2.setItem(i, 1, item)


    if ((data.dic['rearBrakeP'] + data.dic['frontBrakeP']) != 0):  # Verificação necessária para que não ocorra divisão por zero
        ui.progressBar_FrontBreakBalance.setValue(100 * data.dic['frontBrakeP'] / (data.dic['rearBrakeP'] + data.dic['frontBrakeP']))  # porcentagem da pressão referente ao freio dianteiro
        ui.progressBar_FrontBreakBalance.setValue(100 * data.dic['rearBrakeP'] / (data.dic['rearBrakeP'] + data.dic['frontBrakeP'])) # traseiro

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

    dial_WheelPos.setValue(data.dic['volPos'])
    ui.label_19.setText(str(data.dic['volPos']))


  # Função que atualiza os mostradores relacionados aos dados do pacote 3
  # Pacote 3: Engine Temp, battery, fuel pump relay, fan relay, relay box temperature, break temperature rear, break temperature front, time
  # Para atualizar as células da tabela tableWidget_Package3 é necessário definir o valor da variável item como o
  # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def update_p3(data):

    elements = len(data.p3Order)
    for key, i in zip(data.p3Order, range(0, elements)):
        item = QTableWidgetItem(str(data.dic[key]))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget_Package3.setItem(i, 1, item)

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
  # Pacote 4: P1, P2, P3, P4, P5, P6, P7 e P8 strain gauges, time
  # Para atualizar as células da tabela tableWidget_StrainGauge é necessário definir o valor da variável item como o
  # desejado, definir a formatação, nesse caso centralizado, e inserir na posição (linha, coluna) a variável item
def update_p4(data):
  # extensometros

  elements = len(data.dic['ext'])
  for ext, i in zip(data.dic['ext'], range(0, elements)):
      item = QTableWidgetItem(str(ext))
      item.setTextAlignment(QtCore.Qt.AlignCenter)
      ui.tableWidget_Package3.setItem(i, 1, item)

      item = QTableWidgetItem(str(data.dic['time4']))
  item.setTextAlignment(QtCore.Qt.AlignCenter)
  ui.tableWidget_Package3.setItem(i+1, 1, item)

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
