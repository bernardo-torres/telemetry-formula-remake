import numpy as np
import copy
from datetime import datetime


# Data armazena os dados atuais
class Data:
    def __init__(self):
        # Constantes
        self.wheelPosMax = 0
        self.wheelPosMin = 0
        self.pSizes = [37, 34, 42, 42]

        # Dados
        self.p1Order = ['acelX_DD', 'acelY_DD', 'acelZ_DD', 'acelX_DE', 'acelY_DE', 'acelZ_DE',
                        'acelX_TD', 'acelY_TD', 'acelZ_TD', 'acelX_TE', 'acelY_TE', 'acelZ_TE',
                        'velDE', 'velDD', 'velTE', 'velTD', 'rpm', 'beacon', 'time']
        self.p2Order = ['tps', 'oleoP', 'fuelP', 'injectors', 'suspDE', 'suspDD', 'suspTE', 'suspTD',
                        'volPos', 'correnteBat', 'correnteVent', 'correnteBomba', 'frontBrakeP',  'rearBrakeP', 'time2']
        self.p3Order = ['batVoltage', 'ect', 'oilTemp', 'tempDiscoDE', 'tempDiscoDD', 'tempDiscoTE', 'tempDiscoTD',
                        'tempVent', 'tempBomba', 'runners', 'releVent', 'releBomba', 'mata', 'gpsLat', 'gpsLong',
                        'gpsNS', 'gpsEW', 'time3']
        self.p4Order = ['ext1', 'ext2', 'ext3', 'ext4', 'ext5', 'ext6', 'ext7', 'ext8', 'ext9', 'ext10',
                        'ext11', 'ext12', 'time4']
        self.updateDataFunctions = {1: self.updateP1Data, 2: self.updateP2Data, 3: self.updateP3Data, 4: self.updateP4Data}

        self.dic = {
            'acelX_DD': 0, 'acelY_DD': 0, 'acelZ_DD': 0, 'acelX_DE': 0, 'acelY_DE': 0, 'acelZ_DE': 0,
            'acelX_TD': 0, 'acelY_TD': 0, 'acelZ_TD': 0, 'acelX_TE': 0, 'acelY_TE': 0, 'acelZ_TE': 0,
            'velDD': 0, 'velDE': 0, 'velTD': 0, 'velTE': 0, 'rpm': 0, 'beacon': 0, 'time': 0,

            'tps': 0, 'oleoP': 0, 'fuelP': 0, 'injectors': 0, 'suspDE': 0, 'suspDD': 0, 'suspTE': 0, 'suspTD': 0,
            'volPos': 0, 'correnteBat': 0, 'correnteVent': 0, 'correnteBomba': 0, 'frontBrakeP': 0,  'rearBrakeP': 0, 'time2': 0,

            'batVoltage': 0, 'ect': 0, 'oilTemp': 0, 'tempDiscoDE': 0, 'tempDiscoDD': 0, 'tempDiscoTE': 0, 'tempDiscoTD': 0,
            'tempVent': 0, 'tempBomba': 0, 'runners': 0, 'releVent': 0, 'releBomba': 0, 'mata': 0, 'gpsLat': 0, 'gpsLong': 0,
            'gpsNS': 0, 'gpsEW': 0, 'time3': 0,

            'ext1': 0, 'ext2': 0, 'ext3': 0, 'ext4': 0, 'ext5': 0, 'ext6': 0, 'ext7': 0, 'ext8': 0, 'ext9': 0, 'ext10': 0,
            'ext11': 0, 'ext12': 0, 'time4': 0,

        }

        self.dicRaw = copy.deepcopy(self.dic)
        self.alarms = copy.deepcopy(self.dic)
        # Configura alarmes padrao
        self.setDefaultAlarms()
        self.arrayTemp = np.zeros(50)
        self.arrayFuelP = np.zeros(50)
        self.arrayOilP = np.zeros(50)
        self.arrayBattery = np.zeros(50)
        self.arrayTime2 = np.zeros(50)
        self.arrayTime3 = np.zeros(50)

    def setDefaultAlarms(self):
        for key in self.alarms:
            self.alarms[key] = []
        self.alarms['batVoltage'] = [11.5, 'lesser than']
        self.alarms['ect'] = [95, 'greater than']

    # Caso valor seja signed, é necessario trata-lo como complemento de 2
    def twosComplement(self, number, bits):
        if (number & (1 << (bits - 1))) != 0:
            number = number - (1 << bits)        # compute negative value
        return number

    def updateP1Data(self, buffer):
        # recebe o valor contido na lista de dados(leitura) em suas respectivas posições e realiza as operações de deslocamento e soma binária
        if ((int(buffer[0]) == 1) and (len(buffer) == self.pSizes[0])):  # testa se é o pacote 1 e está completo.

            # Acelerometros
            for i in range(0, 12):
                j = 2 + 2*i
                key = self.p1Order[i]
                self.dicRaw[key] =  (buffer[j] << 8) + buffer[j+1]
                self.dicRaw[key] = self.twosComplement(self.dicRaw[key], 16) # Complemento de 2
                self.dic[key] = round(float(self.dicRaw[key] / 16384), 3)
            # self.dicRaw['acelX'] = (int(buffer[2]) << 8) + int(buffer[3])
            # self.dicRaw['acelX'] = self.twosComplement(self.dicRaw['acelX'], 16)
            # self.dic['acelX'] = round(float(self.dicRaw['acelX'] / 16384), 3)

            self.dicRaw['velDD'] = int(buffer[26])
            self.dicRaw['velDE'] = int(buffer[27])
            self.dicRaw['velTD'] = int(buffer[28])
            self.dicRaw['velTE'] = int(buffer[29])
            self.dicRaw['rpm'] = (int(buffer[30]) << 8) + int(buffer[31])
            self.dicRaw['beacon'] = int(buffer[32])
            self.dicRaw['time'] = ((buffer[33]) << 8) + int(buffer[34])

            self.dic['velDE'] = self.dicRaw['velDE']
            self.dic['velDD'] = self.dicRaw['velDD']
            self.dic['velTE'] = self.dicRaw['velTE']
            self.dic['velTD'] = self.dicRaw['velTD']
            self.dic['rpm'] = self.dicRaw['rpm']
            self.dic['beacon'] = self.dicRaw['beacon']
            self.dic['time'] = 25 * self.dicRaw['time']

            return 1
        else:
            return 0

    def updateP2Data(self, buffer):
        if ((int(buffer[0]) == 2) and (len(buffer) == self.pSizes[1])):  # testa se é o pacote 2 e está completo

            # Todos os dados do pacote 2 sao no formato byte1 << 8 | byte2
            for i in range(0, len(self.p2Order)):
                j = 2 + 2*i
                key = self.p2Order[i]
                self.dicRaw[key] =  (buffer[j] << 8) + buffer[j+1]

            self.dic['tps'] = self.dicRaw['tps']
            self.dic['oleoP'] = round(float(self.dicRaw['oleoP'] * 0.001), 4)
            self.dic['fuelP'] = round(float(self.dicRaw['fuelP'] * 0.001), 4)
            self.dic['rearBrakeP'] = round(self.dicRaw['rearBrakeP'] * 0.02536, 1)
            self.dic['frontBrakeP'] = round(self.dicRaw['frontBrakeP'] * 0.02536, 1)
            if self.wheelPosMax - self.wheelPosMin != 0:
                self.dic['volPos'] = round(((self.dicRaw['volPos'] - self.wheelPosMin) * 240 / (self.wheelPosMax - self.wheelPosMin) - 120), 2)
            self.dic['injectors'] = self.dicRaw['injectors']
            self.dic['correnteBat'] = self.dicRaw['correnteBat']
            self.dic['suspDE'] = self.dicRaw['suspDE']
            self.dic['suspDD'] = self.dicRaw['suspDD']
            self.dic['suspTE'] = self.dicRaw['suspTE']
            self.dic['suspTD'] = self.dicRaw['suspTD']
            self.dic['correnteVent'] = self.dicRaw['correnteVent']
            self.dic['correnteBomba'] = self.dicRaw['correnteBomba']
            self.dic['time2'] = 25 * self.dicRaw['time2']
            return 1
        else:
            return 0

    def updateP3Data(self, buffer):
        if ((int(buffer[0]) == 3) and (len(buffer) == self.pSizes[2])):  # testa se é o pacote 3 e está completo

            # os 10 primeiros dados sao no formato byte1 <<8 | byte2
            for i in range(0, 10):
                j = 2 + 2*i
                key = self.p3Order[i]
                self.dicRaw[key] =  (buffer[j] << 8) + buffer[j+1]

            self.dicRaw['releBomba'] = int((buffer[22] & 128) >> 7) #consertar
            self.dicRaw['releVent'] = int((buffer[6] & 8) >> 3)
            self.dicRaw['mata'] = int((buffer[22] & 32) >> 5)
            self.dicRaw['gpsLat'] = (buffer[23] << 16) + (buffer[24] << 8) + buffer[25]
            self.dicRaw['gpsLong'] = (buffer[26] << 16) + (buffer[27] << 8) + buffer[28]
            self.dicRaw['gpsNS'] = int(buffer[29])
            self.dicRaw['gpsEW'] = int(buffer[30])
            self.dicRaw['time3'] = (buffer[38] << 8) + buffer[39]

            # Falta gps hora, minuto, segundo, ms, ano, mes dia nessa ordem
            # buffer3[30] = hgps.hour;
            # buffer3[31] = hgps.minute;
            # buffer3[32] = hgps.seconds;
            # buffer3[33] = hgps.milliseconds;
            # buffer3[34] = hgps.year;
            # buffer3[35] = hgps.month;
            # buffer3[36] = hgps.day;

            self.dic['batVoltage'] = round(float(self.dicRaw['batVoltage'] * 0.01), 2)
            self.dic['ect'] = round(float(self.dicRaw['ect'] * 0.1), 2)
            self.dic['oilTemp'] = self.dicRaw['oilTemp']
            self.dic['tempDiscoDE'] = round(float(self.dicRaw['tempDiscoDE']), 2)
            self.dic['tempDiscoDD'] = round(float(self.dicRaw['tempDiscoDD']), 2)
            self.dic['tempDiscoTE'] = round(float(self.dicRaw['tempDiscoTE']), 2)
            self.dic['tempDiscoTD'] = round(float(self.dicRaw['tempDiscoTD']), 2)
            self.dic['tempVent'] = self.dicRaw['tempVent']
            self.dic['tempBomba'] = self.dicRaw['tempBomba']
            self.dic['runners'] = self.dicRaw['runners']
            self.dic['releVent'] = self.dicRaw['releVent']
            self.dic['releBomba'] = self.dicRaw['releBomba']
            self.dic['mata'] = self.dicRaw['mata']
            self.dic['gpsLat'] = self.dicRaw['gpsLat']
            self.dic['gpsLong'] = self.dicRaw['gpsLong']
            self.dic['gpsNS'] = self.dicRaw['gpsNS']
            self.dic['gpsEW'] = self.dicRaw['gpsEW']
            self.dic['time3'] = 25 * self.dicRaw['time3']

            return 1
        else:
            return 0

    def updateP4Data(self, buffer):
        if ((int(buffer[0]) == 4) and (len(buffer) == self.pSizes[3])):  # testa se é o pacote 3 e está completo
            for i in range(0, len(self.p4Order) -1):
                j = 2 + 3*i
                key = self.p4Order[i]
                self.dicRaw[key] = (buffer[j] << 16) + (buffer[j+1] << 8) + buffer[j+2]
                self.dic[key] = self.dicRaw[key]
            self.dicRaw['time4'] = (buffer[38] << 8) + (buffer[39])
            self.dic['time4'] = 25 * self.dicRaw['time4']
            return 1
        else:
            return 0

    # Arrasta para esquerda uma posicao os dados dos vetores e substitui ultimo valor com o dado mais recente
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

    # Cria string separada por espaco com os nomes dos dados do pacote X, definidos em pXOrder
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


# Classe armazena um arquivo
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


# Escrve mensagens na instancia logInstance.
# Nesse caso, logInstance é um campo da interface. Pode ser qualquer campo que aceite a
# Funcao setText
class Log():
    def __init__(self, logInstance, maxElements=200):
        self.Log = []
        self.logInstance = logInstance
        self.maxElements = maxElements
        self.on = 'on'

    # Insere novo texto de erro na primeira posicao do vetor
    def writeLog(self, text):
        if self.on == 'off':
            return
        self.Log.append(" ")
        # Faz o roll
        if len(self.Log) < self.maxElements:
            self.Log = self.Log[-1:] + self.Log[:-1]
            self.Log[0] = text
        else:
            self.Log = self.Log[-1:] + self.Log[:self.maxElements-1]
            self.Log[0] = text
        string = '\n'.join(str(x) for x in self.Log)
        #string = string + '\n'
        self.logInstance.setText(string)
        # print(text)


# Concatena vetor em uma string separada por delimiter
def vectorToString(line, delimiter, addNewLine=True):
    string = delimiter.join(str(x) for x in line)
    if addNewLine:
        string = string + '\n'
    return string
