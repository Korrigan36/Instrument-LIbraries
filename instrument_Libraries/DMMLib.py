import time


def dmm_ConfigureDCVoltage(dmmObject, voltRange, precision):
    dmmObject.clear()
    tempString = "*RST"
    dmmObject.write(tempString)
    tempString = "VOLTage:DC:NPLCycles 10"
    dmmObject.write(tempString)
#    tempString = "CONF:VOLTage:DC " + str(voltRange) + ", " + str(precision)
#    dmmObject.write(tempString)
    tempString = "TRIGger:COUNT 1"
    dmmObject.write(tempString)
    tempString = "TRIGger:SOURce BUS"
#    tempString = "TRIGger:SOURce IMM"
    dmmObject.write(tempString)
    tempString = "SAMPle:COUNT 1"
    dmmObject.write(tempString)
    tempString = "DATA:FEED RDG_STORE, " + '""'
    dmmObject.write(tempString)
    tempString = "CALCulate:FUNCtion AVERage"
    dmmObject.write(tempString)
    tempString = "SYSTem:BEEPer:STATe OFF"
    dmmObject.write(tempString)

def dmm_ArmTrigger(dmmObject):
#    dmmObject.clear()
#    tempString = "INIT;*OPC?"
    tempString = "INIT"
    dmmObject.write(tempString)
    tempString = "CALCulate:STATe ON"
    dmmObject.write(tempString)

def dmm_TriggerDevice(dmmObject):
    tempString = "*TRG"
    dmmObject.write(tempString)

def dmm_DeviceClear(dmmObject):
    tempString = "CALCulate:STATe OFF"
    dmmObject.write(tempString)
    dmmObject.clear()

#def dmm_BusTrigger(dmmObject):
##    dmmObject.clear()
#    tempString = "TRIGGER 722"
#    dmmObject.write(tempString)

def dmm_FetchMeasurement(dmmObject):
        
    tempString = "DATA:POINTS?"
    returnString = dmmObject.query(tempString)
    time.sleep(2)
    tempString = "Fetch?"
#    tempString = "DATA:REMOVE? 500"
        
    return dmmObject.query(tempString)

def dmm_GetAverage(dmmObject):
        
#    tempString = "CALCulate:AVERage:COUNt?"
#    returnString = dmmObject.query(tempString)
#    print returnString
#    
    tempString = "CALCulate:AVERage:AVERage?"
#    dmmObject.timeout = 2500
    average = dmmObject.query(tempString)

#    dmmObject.write(tempString)
#    average = dmmObject.read()
 
    return average
