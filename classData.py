import numpy as np
import copy
from datetime import datetime


class Data:
    windowUi = []

    def __init__(self):
        self.wheelPosMax = 0
        self.wheelPosMin = 0
        self.p1Size = 16
        self.p2Size = 22
        self.p3Size = 15
        self.p4Size = 30
        self.p1Order = ['acelX', 'acelY', 'acelZ', 'velDD', 'velT', 'sparkCut', 'suspPos', 'time']
        self.p2Order = ['oleoP', 'fuelP', 'tps', 'rearBrakeP', 'frontBrakeP', 'volPos', 'beacon', 'correnteBat', 'rpm', 'time2']
        self.p3Order = ['ect', 'batVoltage', 'releBomba', 'releVent', 'pduTemp', 'tempDiscoD', 'tempDiscoE', 'time3']
        self.p4Order = ['ext1', 'ext2', 'ext3', 'ext4', 'ext5', 'ext6', 'ext7', 'ext8', 'time4']
        self.updateDataFunctions = {1: self.updateP1Data, 2: self.updateP2Data, 3: self.updateP3Data, 4: self.updateP4Data}

        self.dic = {
            'acelX': 0,
            'acelY': 0,
            'acelZ': 0,
            'velDD': 0,
            'velT': 0,
            'sparkCut': 0,
            'suspPos': 0,
            'oleoP': 0,
            'fuelP': 0,
            'tps': 0,
            'rearBrakeP': 0,
            'frontBrakeP': 0,
            'volPos': 0,
            'beacon': 0,
            'correnteBat': 0,
            'rpm': 0,
            'ect': 0,
            'batVoltage': 0,
            'releBomba': 0,
            'releVent': 0,
            'pduTemp': 0,
            'tempDiscoD': 0,
            'tempDiscoE': 0,
            'ext': np.zeros(8),
            'time': 0,
            'time2': 0,
            'time3': 0,
            'time4': 0,
        }

        self.dicRaw = copy.deepcopy(self.dic)
        self.arrayTemp = np.zeros(50)
        self.arrayFuelP = np.zeros(50)
        self.arrayOilP = np.zeros(50)
        self.arrayBattery = np.zeros(50)
        self.arrayTime2 = np.zeros(50)
        self.arrayTime3 = np.zeros(50)

    # Caso valor seja signed, é necessario trata-lo como complemento de 2
    def twosComp(self, number, bits):
        if (number & (1 << (bits - 1))) != 0:
            number = number - (1 << bits)        # compute negative value
        return number

    def updateP1Data(self, buffer):
        # recebe o valor contido na lista de dados(leitura) em suas respectivas posições e realiza as operações de deslocamento e soma binária
        if ((int(buffer[0]) == 1) and (len(buffer) == self.p1Size)):  # testa se é o pacote 1 e está completo
            self.dicRaw['acelX'] = (int(buffer[2]) << 8) + int(buffer[3])
            self.dicRaw['acelX'] = self.twosComp(self.dicRaw['acelX'], 16)
            self.dic['acelX'] = round(float(self.dicRaw['acelX'] / 16384), 3)

            self.dicRaw['acelY'] = (int(buffer[4]) << 8) + int(buffer[5])
            self.dicRaw['acelY'] = self.twosComp(self.dicRaw['acelY'], 16)
            self.dic['acelY'] = round(float(self.dicRaw['acelY'] / 16384), 3)

            self.dicRaw['acelZ'] = (int(buffer[6]) << 8) + int(buffer[7])
            self.dicRaw['acelZ'] = self.twosComp(self.dicRaw['acelZ'], 16)
            self.dic['acelZ'] = round(float(self.dicRaw['acelZ'] / 16384), 3)

            self.dic['velDD'] = int(buffer[8])
            self.dicRaw['velDD'] = int(buffer[8])
            self.dic['velT'] = int(buffer[9])
            self.dicRaw['velT'] = int(buffer[9])
            self.dicRaw['sparkCut'] = ((buffer[10]) & 128) >> 7
            self.dic['sparkCut'] = self.dicRaw['sparkCut']
            self.dicRaw['suspPos'] = (((buffer[10]) & 127) << 8) + int(buffer[11])
            self.dic['suspPos'] = self.dicRaw['suspPos']
            self.dicRaw['time'] = ((buffer[12]) << 8) + int(buffer[13])
            self.dic['time'] = 25 * self.dicRaw['time']
            return 1
        else:
            return 0

    def updateP2Data(self, buffer):
        if ((int(buffer[0]) == 2) and (len(buffer) == self.p2Size)):  # testa se é o pacote 2 e está completo
            self.dicRaw['oleoP'] = (int(buffer[2]) << 8) + int(buffer[3])
            self.dic['oleoP'] = round(float(self.dicRaw['oleoP'] * 0.001), 4)
            self.dicRaw['fuelP'] = (int(buffer[4]) << 8) + int(buffer[5])
            self.dic['fuelP'] = round(float(self.dicRaw['fuelP'] * 0.001), 4)
            self.dicRaw['tps'] = (int(buffer[6]) << 8) + int(buffer[7])
            self.dic['tps'] = self.dicRaw['tps']
            self.dicRaw['rearBrakeP'] = (int(buffer[8]) << 8) + int(buffer[9])
            self.dic['rearBrakeP'] = round(self.dicRaw['rearBrakeP'] * 0.02536, 1)
            self.dicRaw['frontBrakeP'] = (int(buffer[10]) << 8) + int(buffer[11])
            self.dic['frontBrakeP'] = round(self.dicRaw['frontBrakeP'] * 0.02536, 1)
            self.dicRaw['volPos'] = (int(buffer[12]) << 8) + int(buffer[13])
            if self.wheelPosMax - self.wheelPosMin != 0:
                self.dic['volPos'] = round(((self.dicRaw['volPos'] - self.wheelPosMin) * 240 / (self.wheelPosMax - self.wheelPosMin) - 120), 2)
            self.dicRaw['beacon'] = int(buffer[14] >> 7)
            self.dic['beacon'] = self.dicRaw['beacon']
            self.dicRaw['correnteBat'] = ((int(buffer[14]) & 127) << 8) + int(buffer[15])
            self.dic['correnteBat'] = self.dicRaw['correnteBat']
            self.dicRaw['rpm'] = (int(buffer[16]) << 8) + int(buffer[17])
            self.dic['rpm'] = self.dicRaw['rpm']
            self.dicRaw['time2'] = (int(buffer[18]) << 8) + int(buffer[19])
            self.dic['time2'] = 25 * self.dicRaw['time2']
            return 1
        else:
            return 0

    def updateP3Data(self, buffer):
        if ((int(buffer[0]) == 3) and (len(buffer) == self.p3Size)):  # testa se é o pacote 3 e está completo

            self.dicRaw['ect'] = (buffer[3] << 8) + buffer[4]
            self.dic['ect'] = round(float(self.dicRaw['ect'] * 0.1), 2)
            self.dicRaw['batVoltage'] = (buffer[5] << 8) + (buffer[6])
            self.dic['batVoltage'] = round(float(self.dicRaw['batVoltage'] * 0.01), 2)
            self.dicRaw['releBomba'] = int((buffer[7] & 128) >> 7)
            self.dic['releBomba'] = self.dicRaw['releBomba']
            self.dicRaw['releVent'] = int((buffer[7] & 32) >> 5)
            self.dic['releVent'] = self.dicRaw['releVent']
            self.dicRaw['pduTemp'] = (buffer[8] << 8) + buffer[8]
            self.dic['pduTemp'] = round(float(self.dicRaw['pduTemp']), 2)
            self.dicRaw['tempDiscoE'] = (buffer[9] << 8) + buffer[10]
            self.dic['tempDiscoE'] = round(float(self.dicRaw['tempDiscoE']), 2)
            self.dicRaw['tempDiscoD'] = (buffer[11] << 8) + buffer[12]
            self.dic['tempDiscoD'] = round(float(self.dicRaw['tempDiscoD']), 2)
            self.dicRaw['time3'] = (buffer[13] << 8) + buffer[14]
            self.dic['time3'] = 25 * self.dicRaw['time3']
            return 1
        else:
            return 0

    def updateP4Data(self, buffer):
        if ((int(buffer[0]) == 4) and (len(buffer) == self.p4Size)):  # testa se é o pacote 3 e está completo
            for i in range(0, 8):
                j = 2 + 3*i
                self.dicRaw['ext'][i] = (buffer[j] << 16) + (buffer[j+1] << 8) + buffer[j+2]
                self.dic['ext'][i] = self.dicRaw['ext'][i]
            self.dicRaw['time4'] = (buffer[26] << 8) + (buffer[27])
            self.dic['time4'] = 25 * self.dicRaw['time4']
            return 1
        else:
            return 0

    def rollArrays(self):
        self.arrayBattery = np.roll(self.arrayBattery, -1)
        self.arrayBattery[-1] = self.dic['batVoltage']
        self.arrayOilP = np.roll(self.arrayOilP, -1)
        self.arrayOilP[-1] = self.dic['oleoP']
        self.arrayTemp = np.roll(self.arrayTemp, -1)
        self.arrayTemp[-1] = self.dic['ect']
        self.arrayFuelP = np.roll(self.arrayFuelP, -1)
        self.arrayFuelP[-1] = self.dic['fuelP']
        self.arrayTime2 = np.roll(self.arrayTime2, -1)
        self.arrayTime2[-1] = self.dic['time2']
        self.arrayTime3 = np.roll(self.arrayTime3, -1)
        self.arrayTime3[-1] = self.dic['time3']

    def createPackString(self, packNo):
        if packNo == 1:
            list = self.p1Order
        elif packNo == 2:
            list = self.p2Order
        elif packNo == 3:
            list = self.p3Order
        elif packNo == 4:
            list = self.p4Order

        delimiter = ' '
        vec = [packNo]
        for key in list:
            vec.append(self.dicRaw[key])
        string = delimiter.join(str(x) for x in vec)
        string = string + '\n'
        return string


class File:
    def __init__(self):
        self.save = 0

    def startDataSave(self, arquivo):
        now = datetime.now()
        # define o nome do arquivo concatenando o nome definido pelo usuário e hora e minuto do início da gravação
        arquivo = arquivo + "_" + str(now.hour) + "_" + str(now.minute) + ".txt"
        print(arquivo)
        self.arq = open(arquivo, 'w')
        self.save = 1
        # escreve os valores de setup no início do arquivo

    def writeRow(self, string):
        self.arq.write(string)

    # Função para parar a gravação dos dados no arquivo txt
    def stopDataSave(self):
        if self.save != 0:
            self.save = 0  # atualiza o valor da variavel save, a qual é usada para verificar se está ocorrendo ou não não gravação dos dados
            self.arq.close()


class ErrorLog():
    def __init__(self, logInstance):
        self.errorLog = []
        self.logInstance = logInstance

    # Insere novo texto de erro na primeira posicao do vetor
    def writeErrorLog(self, text):
        self.errorLog.append(" ")
        self.errorLog = self.errorLog[-1:] + self.errorLog[:-1]
        self.errorLog[0] = text
        string = '\n'.join(str(x) for x in self.errorLog)
        string = string + '\n'
        self.logInstance.setText(string)
        print(text)
