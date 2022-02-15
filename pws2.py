#utilizando a fonte PWS para demonstrar a lei de Ohm
#Ricardo Dalke Meucci
#09/02/2022

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

#configurando a fonte nos parâmetros iniciais
pwr1.write("VOLTAGE 0V") #tensão inicial
pwr1.write("CURRENT 3A") #corrente inicial
pwr1.write("OUTPUT 1") #conectando a fonte à carga
time.sleep(1)

tensao_fonte = 0.0 #tensão inicial da fonte
incr_tensão = 1 #incremento da tensão
while tensao_fonte < 10:

    corrLeitura = float(pwr1.query('MEASure:CURRent:DC?')) # leitura corrente
    tensLeitura = float(pwr1.query('MEASure:VolTage:DC?')) # leitura tensão
    correnteList.append(corrLeitura) #anexando dados à lista corrente
    tensaoList.append(tensLeitura) #anexadno dados à lista tensão
    time.sleep(1) #tempo de espera
    print(tensaoList, correnteList)
    #incrementado a tensão
    tensao_fonte = tensao_fonte + incr_tensão
    print(tensao_fonte)
    pwr1.write("VOLTAGE %d % tensao_fonte %d % tensao_fonte V") #tensão inicial


#criando o gráfico
plt.plot(tensaoList, correnteList, color='blue', linewidth=10) # Plot the collected data with time on the x axis and temperature on the y axis.
plt.pause(0.01) # This command is required for live plotting. This allows the code to keep running while the plot is shown.

pwr1.write("OUTPUT 0")



