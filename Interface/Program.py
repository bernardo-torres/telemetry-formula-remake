
import serial
from Classes import Data, File, Log, vectorToString
from PyQt5 import QtCore
import time


# Classe que executa o programa
class Program():
    def __init__(self, updateTime, errorLog, bufferLog, updateInterfaceFunctions, updateCounterMax=[0,0,0,0]):

        self.updateTime = updateTime

        self.data = Data()
        self.dataFile = File()
        # self.lapTimeFile = File()
        self.lastBuffers = bufferLog
        self.errorLog = errorLog

        # Dicionario de funcoes: permite chamar funcoes fazendo updateInterfaceFunctions[key], onde key é 1,2,3 ou 4
        self.updateInterfaceFunctions = updateInterfaceFunctions

        self.packIndexes = [1, 2, 3, 4]
        self.packSizes = self.data.pSizes

        self.updateCounterMax = updateCounterMax  # numero de pacotes recebidos at atualizar a interface
        self.updateCounter = [0, 0, 0, 0]
        self.updateInterfaceEnabled = True

    def openSerialPort(self, port, baudrate, timeout):
        self.porta = serial.Serial()
        self.porta.baudrate = baudrate
        self.porta.port = port
        self.porta.timeout = timeout
        self.porta.open()

    def stopProgram(self):
        self.stop = 1  # atualiza o valor da variavel stop, a qual é usada para verificar o funcionamento da interface
        # self.lapTimeFile.stopDataSave()
        # Fecha arquivo file e porta serial
        self.dataFile.stopDataSave()
        if self.porta.isOpen():
            self.porta.flushInput()
            self.porta.close()
        else:
            pass

    # program() roda em loop
    def program(self):
        if (self.stop == 0):
            # Le dados da porta serial

            self.buffer = self.readFromSerialPort(self.packSizes, self.packIndexes)
            if len(self.buffer) != 0:
                # chamada da função updateDataAndInterface para analisar os dados recebidos atualizar os mostradores da interface
                self.updateData(self.buffer, int(self.buffer[0]))
                if self.dataFile.save == 1:
                    self.saveLine(self.buffer, int(self.buffer[0]))
                if self.updateInterfaceEnabled:
                    self.updateInterface(self.buffer, int(self.buffer[0]))


            # Apos updateTime segundos, chama funcao program() novamente
            QtCore.QTimer.singleShot(self.updateTime, lambda: self.program())

    def updateData(self, buffer, packID):
        # Atualiza dados em Data e atualiza campos respectivos na interface
        if (self.data.updateDataFunctions[packID](buffer) == 0):
            self.errorLog.writeLog(" updateData: Pacote " + str(packID) + "com tamanho diferente do configurado")

        # Desloca vetores e chama funcao de atualizar graficos da interface
        if packID == 2 or packID == 3:
            self.data.rollArrays()

    def updateInterface(self, buffer, packID):

        # Chama funcao updatePxInterface, atribuida no dicionario updateInterfaceFunctions, para a chave x = packID
        if self.updateCounter[packID-1] >= self.updateCounterMax[packID-1]:
            self.updateInterfaceFunctions[packID](self.data)
            self.updateCounter[packID-1] = 0
        else:
            self.updateCounter[packID-1] += 1

        # Atualiza o mostrador textBrowser_Buffer com as ultimas listas de dados recebidas.
        self.lastBuffers.writeLog(vectorToString(buffer, ' ', addNewLine=False))

    def saveLine(self, buffer, packID):
        # Grava linha buffer no arquivo

        string = self.data.createPackString(packID)
        self.dataFile.writeRow(string)

    # Le buffer da porta serial. bufferSize é uma lista com os tamanhos dos pacotes e firstByteValues
    # é uma lista com os numeros dos pacotes (1,2,3,4)
    def readFromSerialPort(self, bufferSize, firstByteValues):
        while True:
            # Espera receber algo na porta serial
            while (self.porta.inWaiting() == 0):
                pass
            read_buffer = b''
            # Le primeiro e segundo bytes
            firstByte = self.porta.read()

            if int.from_bytes(firstByte, byteorder='big') in firstByteValues:
                read_buffer += firstByte
                # Le o segundo byte de inicio
                a = self.porta.read()
                if int.from_bytes(a, byteorder='big') == 5:
                    read_buffer += a
                    break
                else:
                    self.errorLog.writeLog("Leitura: segundo byte com valor inesperado. Leu-se " + str(firstByte) + ", esperava-se 5")
            # Se o byte lido nao for 1, 2 3 ou 4,, quer dizer que perdeu algum dado.
            else:
                self.errorLog.writeLog("Leitura: primeiro byte com valor inesperado. Leu-se " + str(firstByte) + ", esperava-se de 1 a 4")
        while True:
            # Le resto do buffer
            index = int.from_bytes(firstByte, byteorder='big') - 1
            byte = self.porta.read(size=int(bufferSize[index] - 2))
            read_buffer += byte

            if(len(read_buffer) == bufferSize[index]):
                if int(read_buffer[bufferSize[index]-2]) == 9:
                    # Chegou no fim do pacote
                    if int(read_buffer[bufferSize[index]-1]) == 10:
                        break
                    else:
                        self.errorLog.writeLog("Leitura: ultimo dado diferente de byte 10" + str(read_buffer))
                        return []
                else:
                    self.errorLog.writeLog("Leitura: penultimo dado diferente de byte 9")
                    return []
        return read_buffer
