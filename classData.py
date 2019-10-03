import numpy as np


class Data:
    windowUi = []

    def __init__(self):
        self.wheelPosMax = 0
        self.wheelPosMin = 0
        self.p1Size = 15
        self.p2Size = 22
        self.p3Size = 15
        self.p4Size = 30
        self.p1Order = ['acelX', 'acelY', 'acelZ', 'velDD', 'velT', 'sparkCut', 'suspPos', 'time']
        self.p2Order = ['oleoP', 'fuelP', 'tps', 'rearBrakeP', 'frontBrakeP', 'volPos', 'beacon', 'correnteBat', 'rpm', 'time2']
        self.p3Order = ['ect', 'batVoltage', 'releBomba', 'releVent', 'pduTemp', 'tempDiscoD', 'tempDiscoE', 'time3']

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

        self.array_temp = np.zeros(50)
        self.array_fuel_p = np.zeros(50)
        self.array_oil_p = np.zeros(50)
        self.array_battery = np.zeros(50)
        self.array_time2 = np.zeros(50)
        self.array_time2 = np.zeros(50)

    def updateP1Data(self, buffer):
        if ((int(buffer[0]) == 1) and (len(buffer) == self.p1Size)):  # testa se é o pacote 1 e está completo
            self.dic['acelX'] = (int(buffer[2]) << 8) + int(buffer[3])  # recebe o valor contido na lista de dados(leitura) em suas respectivas posições e realiza as operações de deslocamento e soma binária
            self.dic['acelX'] = round(float(self.dic['acelX'] / 16384), 3)  #
            self.dic['acelY'] = (int(buffer[4]) << 8) + int(buffer[5])
            self.dic['acelY'] = round(float(self.dic['acelY'] / 16384), 3)
            self.dic['acelZ'] = (int(buffer[6]) << 8) + int(buffer[7])
            self.dic['acelZ'] = round(float(self.dic['acelZ'] / 16384), 3)
            self.dic['velDD'] = int(buffer[8])
            self.dic['velT'] = int(buffer[9])
            self.dic['sparkCut'] = ((buffer[10]) & 128) >> 7
            self.dic['suspPos'] = (((buffer[10]) & 127) << 8) + int(buffer[11])
            self.dic['time'] = ((buffer[12]) << 8) + int(buffer[13])
            self.dic['time'] = 25 * self.dic['time']

    def updateP2Data(self, buffer):
        if ((int(buffer[0]) == 2) and (len(buffer) == self.p2Size)):  # testa se é o pacote 2 e está completo
            self.dic['oleoP'] = (int(buffer[2]) << 8) + int(buffer[3])
            self.dic['oleoP'] = round(float(self.dic['oleoP'] * 0.001), 2)
            self.dic['fuelP'] = (int(buffer[4]) << 8) + int(buffer[5])
            self.dic['fuelP'] = round(float(self.dic['fuelP'] * 0.001), 2)
            self.dic['tps'] = (int(buffer[6]) << 8) + int(buffer[7])
            self.dic['rearBrakeP'] = (int(buffer[8]) << 8) + int(buffer[9])
            self.dic['rearBrakeP'] = round(self.dic['rearBrakeP'] * 0.02536, 1)
            self.dic['frontBrakeP'] = (int(buffer[10]) << 8) + int(buffer[11])
            self.dic['frontBrakeP'] = round(self.dic['frontBrakeP'] * 0.02536, 1)
            self.dic['volPos'] = (int(buffer[12]) << 8) + int(buffer[13])
            self.dic['volPos'] = round(((self.dic['volPos'] - self.wheelPosMin) * 240 / (self.wheelPosMax - self.wheelPosMin) - 120), 2)
            self.dic['beacon'] = int(buffer[14] >> 7)
            self.dic['correnteBat'] = ((int(buffer[14]) & 127) << 8) + int(buffer[15])
            self.dic['rpm'] = (int(buffer[16]) << 8) + int(buffer[17])
            self.dic['time2'] = (int(buffer[18]) << 8) + int(buffer[19])
            self.dic['time2'] = 25 * self.dic['time2']

    def updateP3Data(self, buffer):
        if ((int(buffer[0]) == 3) and (len(buffer) == self.p3Size)):  # testa se é o pacote 3 e está completo

            self.dic['ect'] = (buffer[3] << 8) + buffer[4]
            self.dic['ect'] = round(float(self.dic['ect'] * 0.1), 2)
            self.dic['batVoltage'] = (buffer[5] << 8) + (buffer[6])
            self.dic['batVoltage'] = round(float(self.dic['batVoltage'] * 0.01), 2)
            self.dic['releBomba'] = int((buffer[7] & 128) >> 7)
            self.dic['releVent'] = int((buffer[7] & 32) >> 5)
            self.dic['pduTemp'] = (buffer[8] << 8) + buffer[8]
            self.dic['pduTemp'] = round(float(self.dic['pduTemp']), 2)
            self.dic['tempDiscoE'] = (buffer[9] << 8) + buffer[10]
            self.dic['tempDiscoE'] = round(float(self.dic['tempDiscoE']), 2)
            self.dic['tempDiscoD'] = (buffer[11] << 8) + buffer[12]
            self.dic['tempDiscoD'] = round(float(self.dic['tempDiscoD']), 2)
            self.dic['time3'] = (buffer[13] << 8) + buffer[14]
            self.dic['time3'] = 25 * self.dic['time3']

    def updateP4Data(self, buffer):
        if ((int(buffer[0]) == 4) and (len(buffer) == self.p4Size)):  # testa se é o pacote 3 e está completo
            for i in range(0, 8):
                j = 2 + 3*i
                self.dic['ext'][i] = (buffer[j] << 16) + (buffer[j+1] << 8) + buffer[j+2]
            self.dic['time4'] = (buffer[26] << 8) + (buffer[27])
            self.dic['time4'] = 25 * self.dic['time4']

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
