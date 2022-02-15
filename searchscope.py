import pyvisa as visa
rm = visa.ResourceManager('@py')
rm.list_resources()
my_instrument = rm.open_resource('USB0::1689::925::C011433::0::INSTR')
print(my_instrument.query('*IDN?'))



