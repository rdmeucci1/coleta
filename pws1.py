#localizando a fonte de potencia

import pyvisa as visa # pyvisa.org
import time
import matplotlib.pyplot as plt


rm = visa.ResourceManager('@py')
rm.list_resources()
pwr1 = rm.open_resource('USB0::1689::913::C010918::0::INSTR')
print(pwr1.query('*IDN?'))
pwr1.write("OUTPUT 0")
pwr1.write("*RST")

tensaoList = []
correnteList = []

plt.figure(figsize=(10,10))
plt.xlabel('Tensao(V)', fontsize=24)
plt.xticks(fontsize=18)
plt.ylabel('Corrente (A)', fontsize=24)
plt.yticks(fontsize=18)

n=0.0
pwr1.write("VOLTAGE 0V")
pwr1.write("CURRENT 3A")
pwr1.write("OUTPUT 1")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)

n = n + 5
pwr1.write("VOLTAGE 5V")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)

n = n + 5
pwr1.write("VOLTAGE 10V")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)

n = n + 5
pwr1.write("VOLTAGE 15V")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)

n = n + 5
pwr1.write("VOLTAGE 20V")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)


n = n + 5
pwr1.write("VOLTAGE 25V")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)

n = n + 5
pwr1.write("VOLTAGE 30v")
time.sleep(1)
currLeitura = float(pwr1.query('MEASure:CURRent:DC?'))
correnteList.append(currLeitura)
tensaoList.append(n)
time.sleep(1)
print(tensaoList, correnteList)


plt.plot(tensaoList, correnteList, color='blue', linewidth=10) # Plot the collected data with time on the x axis and temperature on the y axis.
plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.

pwr1.write("OUTPUT 0")



