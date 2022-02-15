import pyvisa as visa
import time

rm = visa.ResourceManager('@py')
rm.list_resources()
scope = rm.open_resource('USB0::1689::925::C011433::0::INSTR')
print(scope.query('*IDN?'))

scope.write("*RST")
time.sleep(2.5)

scope.write("SELect:CH2 1")
scope.write("SELect:CH1 1")
scope.write("AUTOSet EXECute")
time.sleep(5)

# Setup Search and Marks
scope.write("SEARCH:SEARCH1:TRIGger:A:EDGE:SOUrce CH1")
scope.write("SEARCH:SEARCH1:TRIGger:A:TYPe EDGe")
scope.write("SEARCH:SEARCH1:TRIGger:A:EDGE:SLOpe FALL")
scope.write("SEARCH:SEARCH1:TRIGger:A:LEVel:CH1 2.5")
scope.write("SEARCH:SEARCH1:STATE ON")

# Give the search and marks time to search and mark
time.sleep(1)

# Use FPAnel:PRESS NEXt and FPAnel:PRESS PREv as many times as necessary to select the correct mark
scope.write("FPAnel:PRESS PREv")

# MARK:SELected:STARt? and MARK:SELected:END? return where the mark starts and ends.  Even for an edge event the start and end are different because the scope uses hysteresis to detect edge transitions, otherwise the edge detection would be affected by noise.  For this reason you'll want to retrieve the start and end and average the two to get the position that is right in the middle.
start = scope.query("MARK:SELected:STARt?")
end = scope.query("MARK:SELected:END?")
position_in_percent = (float(end) + float(start))/float(2)
