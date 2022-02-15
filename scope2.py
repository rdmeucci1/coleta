from datetime import datetime # std library
import pyvisa as visa # https://pyvisa.readthedocs.org/en/stable/
import time


fileSaveLocation = r'/home/ricardo/' # pasta onde a imagem serah salva

rm = visa.ResourceManager('@py')
rm.list_resources()
scope = rm.open_resource('USB0::1689::925::C011437::0::INSTR') #USBTMC configuracao
print(scope.query('*IDN?'))

print(scope.query('*LRN?'))
time.sleep(2.5)

scope.write("SAVe:IMAGe:FILEFormat PNG")
scope.write("SAVe:IMAGe:INKSaver OFF")
scope.write("HARDCopy STARt")
imgData = scope.read_raw()

# gerando nome do arquivo
dt = datetime.now()
fileName = dt.strftime("%Y%m%d_%H%M%S.png")

imgFile = open(fileSaveLocation + fileName, "wb")
imgFile.write(imgData)
imgFile.close()

scope.close()
rm.close()
