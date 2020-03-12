# -*- coding: utf-8 -*-

import time
import visa

def printf(x):
    '''
        Print function to allow a return of text
    '''
    print x

def lcr_Aperture(lcrObject, length):
    '''
        Sets the Aperture to Short, Medium, or Long
        Input: lcrObject, str SHORt, MEDium, or LONG
    '''
    tempString = length.lower()
    if tempString.find("short") != -1:
        lcrObject.write(":APERture SHORt")
    elif tempString.find("medium") != -1:
        lcrObject.write(":APERture MEDium")
    elif tempString.find("long") != -1:
        lcrObject.write(":APERture LONG")
    else:
        return printf("Please input Short, Medium, or Long")

def lcr_GetSettings(lcrObject):
    '''
        Checks current settings on meter
        Input: LCR Object
        Output: str
    '''
    returnString = lcrObject.query("*LRN?")
    print returnString

def lcr_SettingsReset(lcrObject):
    '''
        Resets Settings on LCR
        Input: LCR Object
    '''
    lcrObject.write("*RST")

def lcr_ClearError(lcrObject):
    '''
        Clears Error Queue
        Input: LCR Object
    '''
    lcrObject.write("*CLS")

def lcr_SetCableLength(lcrObject, cableLen):
    '''
        Set Cable Length
        Input: LCR Object, int cableLen (0,1,2,4)
    '''
    tempString = ":CORR:LENG " + str(cableLen)
    lcrObject.write(tempString)

def lcr_BiasState(lcrObject, onOff):
    '''
        Turns the DC Bias On or Off.
        Input: lcrObject, str "ON", "OFF", "1", "0"
    '''
    tempString = str(onOff)
    tempString = tempString.upper()
    if ("ON" or "1") in tempString:
        lcrObject.write(":BIAS:STATe ON")
    elif ("OFF" or "0") in tempString:
        lcrObject.write(":BIAS:STATe OFF")
    else:
        return printf("Please input On, Off, 0 or 1")

def lcr_SetDCBiasLevel(lcrObject, bias):
    ''' 
        Sets the DC Bias Level, 
        Input: LCR object, integer bias  
    '''
    tempString = ":BIAS:CURR:LEV " + str(bias)
    lcrObject.write(tempString)
    
def lcr_GetDCBiasLevel(lcrObject):
    '''
        Check DC Bias Level on meter.
        Input: LCR Object
        Output: str
    '''
    tempString = ":BIAS:CURR:LEV?"
    return lcrObject.query(tempString)

def lcr_OpenMeasurement(lcrObject):
    '''
        Turn on and un the Open Measurement Correction
        input: LCR Object
    '''
    lcrObject.write(":CORRection:OPEN:STATe ON")
    lcrObject.write(":CORR:OPEN:EXEC")


def lcr_ShortMeasurment(lcrObject):
    '''
        Run the Short Measurement Correction
        input: LCR Object
    '''
    lcrObject.write(":CORRection:SHORt:STATe ON")
    lcrObject.write(":CORR:SHORt:EXEC")

def lcr_SetFreq(lcrObject, freqSet):
    '''
        Set Frequency
        Input: LCR Object, integer freq
    '''
    lcrObject.write("FREQ:CW " + str(freqSet))
    
def lcr_GetFreq(lcrObject):
    '''
        Check Frequency
        Input: LCR Object
        Output: str
    '''
    returnString = lcrObject.query("FREQ:CW?")
    print returnString

def lcr_SetFunction(lcrObject, func):
    '''
        Set Function
        Input: lcrObject, str func
    '''
    lcrObject.write(":FUNC:IMP:TYPE "+str(func))

def lcr_SetBufferSize(lcrObject, bufferSize):
    '''
        Set the data buffer memory’s size. 1 - 201 size range, 1 steps.
        Input: lcrObject, int bufferSize
    '''
    lcrObject.write(":MEMory:DIM DBUF,"+str(bufferSize))

def lcr_FillMemory(lcrObject):
    '''
        Fill memory with values measured.
        Input: lcrObject
    '''
    lcrObject.write(":MEMory:FILL DBUF")

def lcr_ReadMemory(lcrObject):
    '''
        Read Memory. Returns long string separated by commas.
    '''
    returnString = lcrObject.query(":MEMory:READ? DBUF")
    return returnString

def lcr_FetchImpedance(lcrObject):
    '''
        Fetches Instantaneous Impedance. Returns string 
        with impedance separated by commas.
    '''
    returnString = lcrObject.query(":FETCh:IMPedance:FORMatted?")
    return returnString

def lcr_SetAnnotation(lcrObject, title):
    '''
        Set Title. Title needs all caps and no spaces.
    '''
    tempString = title.replace(" ","")
    tempString = tempString.upper()
    lcrObject.write(":DISPlay:LINE "+str(tempString))
    
def lcr_SetVoltageLevel(lcrObject, level):
    '''
        Set the voltage level for the measurement signal.
        Input: lcrObject
    '''
    lcrObject.write(":VOLTage:LEVel "+str(level))

def lcr_Abort(lcrObject):
    '''
        Abort resets the trigger system.
        Input: lcrObject
    '''
    lcrObject.write(":ABORt")

def lcr_Trigger(lcrObject):
    '''
        Issues a trigger to lcr.
        Input: lcrObject
    '''
    lcrObject.write("*TRG")

