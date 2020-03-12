def setLoad(loadObject, loadNumber, loadValue):
    tempString = "CHAN:LOAD " + str(loadNumber)
    loadObject.write(tempString)
    loadObject.write("CURR:STAT:L1 0\n")
    loadObject.write("CONFigure:AUTO:ON 0\n")
    loadObject.write("CHANnel:ACTive 1\n")
    tempString = "CURR:STAT:L1 " + str(loadValue) 
    loadObject.write(tempString)
    
def setLoadOn(loadObject, channel):
    tempString = "CHAN:LOAD " + str(channel)
    loadObject.write(tempString)
    tempString = "LOAD:STATe ON\n" 
    loadObject.write(tempString)
        
def setLoadOff(loadObject, channel):
    tempString = "CHAN:LOAD " + str(channel)
    loadObject.write(tempString)
    tempString = "LOAD:STATe OFF\n" 
    loadObject.write(tempString)
  
def getLoad(loadObject, channel):
    tempString = "CHAN:LOAD " + str(channel)
    loadObject.write(tempString)
    tempString = "CURR:STAT:L1?"  
    return loadObject.query(tempString)
  
def load_DigSampleTime(loadObject, number):
    tempString = "DIG:SAMP:TIME " + str(number) 
    loadObject.write(tempString)

def load_DigSamplePoints(loadObject, number):
    tempString = "DIG:SAMP:POIN " + str(number) 
    loadObject.write(tempString)

def load_DigTriggerPoint(loadObject, number):
    tempString = "DIG:TRIG:POIN " + str(number) 
    loadObject.write(tempString)

def load_DigTriggerSource(loadObject, text):
    tempString = "DIG:TRIG:SOUR " + text 
    loadObject.write(tempString)

def load_SelectChannel(loadObject, channel):
    tempString = "CHAN " + str(channel) 
    loadObject.write(tempString)

