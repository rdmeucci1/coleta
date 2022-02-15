
#encontrando instrumentos nas portas usb

import pyvisa as visa
rm = visa.ResourceManager()
print(rm.list_resources()) # Prints "()" => No instruments found!

