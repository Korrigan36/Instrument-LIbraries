import time


def switch_SetDCVoltageScan(switchObject):
    switchObject.clear()
    tempString = "*RST"
    switchObject.write(tempString)
    tempString = "CONF:VOLTage:DC 1,MAX,(@101, 102)"
    switchObject.write(tempString)
    tempString = "ROUTE:SCAN (@101, 102)"
    switchObject.write(tempString)
    #This delay necessary for some reason?
    time.sleep(1)
    tempString = "TRIGger:COUNT 500"
#    tempString = "TRIGger:COUNT INFINITY"
    switchObject.write(tempString)
    tempString = "TRIGger:SOURce IMMediate"
    switchObject.write(tempString)

def switch_SetTcScan(switchObject):
    switchObject.clear()
    tempString = "*RST"
    switchObject.write(tempString)
    tempString = "CONF:TEMPerature TCouple, T, (@101, 102, 103, 104, 105)"
    switchObject.write(tempString)
    tempString = "ROUTE:SCAN (@101, 102, 103, 104, 105)"
    switchObject.write(tempString)
    #This delay necessary for some reason?
    time.sleep(1)
#    tempString = "TRIGger:COUNT 500"
#    tempString = "TRIGger:COUNT INFINITY"
    switchObject.write(tempString)
    tempString = "TRIGger:SOURce IMMediate"
    switchObject.write(tempString)

def switch_TriggerMeasurement(switchObject):
    switchObject.clear()
    tempString = "INIT;*OPC?"
    switchObject.query(tempString)
#    tempString = "*OPC?"
#    switchObject.query(tempString)
    
   
#    tempString = switchObject.read()

def switch_FetchMeasurement(switchObject):
        
#    tempString = "DATA:POINTS?"
#    returnString = switchObject.query(tempString)
#    print returnString
    tempString = "Fetch?"
#    tempString = "DATA:REMOVE? 500"
        
    return switchObject.query(tempString)

def switch_GetAverage(switchObject):
        
    tempString = "DATA:POINTS?"
    returnString = switchObject.query(tempString)
    print returnString
    
    tempString = "CALC:AVER:AVER? (@101, 102, 103, 104, 105)"
    average = switchObject.query(tempString)
 
    tempString = "CALC:AVER:CLEAR (@101, 102, 103, 104, 105)"
    switchObject.write(tempString)

    return average

