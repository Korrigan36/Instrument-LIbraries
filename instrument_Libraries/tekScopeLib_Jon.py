import time
import visa
from datetime import datetime

def scope_SetAnnotation(scopeObject, text, xPos, yPos):
    tempString = "MESSage:CLEAR"
    scopeObject.write(tempString)
    tempString = "MESSage:SHOW \"" + str(text) + "\""
    scopeObject.write(tempString)
    tempString = "MESSage:STATE ON"
    scopeObject.write(tempString)
#    tempString = "MESSAGE:BOX 650,720"
    tempString = "MESSAGE:BOX " + str(xPos) + "," + str(yPos)
    scopeObject.write(tempString)
    
def scope_SetChannel_Label(scopeObject, channel, text):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = str(channel) + ":LABel \"" + str(text) + "\""
    elif returnString.find("3014") != -1:
        tempString = str(channel) + ":LABel \"" + str(text) + "\""
    elif returnString.find("MSO58") != -1:
        tempString = str(channel) + ":LABel:NAMe \"" + str(text) + "\""
    scopeObject.write(tempString)

def scope_SetChannel_OnOff(scopeObject, channel, text):
    tempString = "SELect:" + str(channel) + " " + str(text)
    scopeObject.write(tempString)

def scope_SetChannel_Position(scopeObject, channel, text):
    tempString = str(channel) + ":POSition " + str(text) 
    scopeObject.write(tempString)
    
def scope_SetAcquisitionHiRes(scopeObject):
    tempString = "ACQuire:MODE HIRes"
    scopeObject.write(tempString)

def scope_SetAcquisitionEnvelope(scopeObject):
    tempString = "ACQuire:MODE ENVelope"
    scopeObject.write(tempString)
    tempString = "ACQuire:NUMEnv INFInite"
    scopeObject.write(tempString)

def scope_Setuprecordlength(scopeObject, value):
    tempString = "HORIZONTAL:RECORDLENGTH " + str(value)
    scopeObject.write(tempString)

def scope_SetTimescale(scopeObject, value):
    tempString = "HORizontal:MAIn:SCAle " + str(value)
    scopeObject.write(tempString)
    
def scope_Set_Trigger_Auto(scopeObject):
    tempString = "TRIGGER:A:MODE AUTO"
    scopeObject.write(tempString)
    
def scope_Set_Trigger_Normal(scopeObject):
    tempString = "TRIGGER:A:MODE NORMAL"
    scopeObject.write(tempString)
    
def scope_Clear_Statistics(scopeObject):
    tempString = "MEASUREMENT:STATISTICS RESET"
    scopeObject.write(tempString)
    
def scope_Stop(scopeObject):
    tempString = "ACQuire:STATE OFF"
    scopeObject.write(tempString)

def scope_Start(scopeObject):
    tempString = "ACQuire:STATE ON"
    scopeObject.write(tempString)
    
def scope_Clear_Persist(scopeObject):
    tempString = "DISplay:PERSistence CLEAR"
    scopeObject.write(tempString)
    
def scope_Force_Trigger(scopeObject):
    tempString = "TRIGger FORCe"
    scopeObject.write(tempString)
    
def scope_Set_Single_Capture(scopeObject):
    tempString = "ACQuire:STOPAfter SEQUENCE"
    scopeObject.write(tempString)
    
def scope_Set_Multiple_Capture(scopeObject):
    tempString = "ACQuire:STOPAfter RUNStop"
    scopeObject.write(tempString)
    
def scope_Reset_Persistance(scopeObject):
    tempString = "DISplay:PERSistence:RESET"
    scopeObject.write(tempString)
    tempString = "DISplay:PERSistence INFInite"
    scopeObject.write(tempString)
 
def scope_SetChannel_Bandwidth(scopeObject, channel, text):
    tempString = str(channel) + ":BANdwidth " + str(text)
    scopeObject.write(tempString)

def scope_List_Measurements(scopeObject):
    tempString = "MEASUrement:LIST?"
    returnString = scopeObject.query(tempString)
    print "Measurement List " + returnString

def scope_Delete_Measurements(scopeObject):
#This function is needed for MSO5 series otherwise measurements keep getting added on
#This command is strange because it requires the double quotation marks around the MEASx entry
    for loop in range (1,100):
        tempString = 'MEASUrement:DELete "MEAS' + str(loop) + '"'
        scopeObject.write(tempString)
        
def scope_Set_Measurement(scopeObject, measNumber, channel, measurement):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = "MEASUrement:MEAS" + str(measNumber) + ":SOURCE1 " + "CH" + str(channel)
        scopeObject.write(tempString)
    #    tempString = "MEASUrement:MEAS" + str(measNumber) + ":TYPe " + str(measurement)
        tempString = "MEASUrement:MEAS" + str(measNumber) + ":TYPe " + measurement
        scopeObject.write(tempString)
        tempString = "MEASUrement:MEAS" + str(measNumber) + ":STATE ON"
    elif returnString.find("MSO58") != -1:
        tempString = "MEASUrement:ADDMEAS " + measurement
        scopeObject.write(tempString)
        #This command is not documented correctly or completely. Source much have CH in front
        #and there must be a space after SOUrce. No double quotes are required for this one
        tempString = "MEASUrement:MEAS" + str(measNumber) + ":SOUrce " + "CH" + str(channel)
        scopeObject.write(tempString)
#        tempString = "MEASUrement::STATIstics:CYCLEMode ON"
#        scopeObject.write(tempString)

def scope_Get_Measurement(scopeObject, measNumber, meanMinOrMax):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = "MEASUrement:MEAS" + str(measNumber) + ":" + str(meanMinOrMax) + "?"
        return scopeObject.query(tempString)
    elif returnString.find("MSO58") != -1:
        tempString = "MEASUrement:MEAS" + str(measNumber) + ":RESUlts:ALLAcqs:MEAN?"
        return scopeObject.query(tempString)

    
    
    #    if meanMinOrMax == "VAL":
#        tempString = "MEASUrement:MEAS" +str(measNumber) + ":VALue?"
#        return scopeObject.query(tempString)
#    else:

def scope_SetUp_Trigger(scopeObject, channel, level, edge, position):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = "HORizontal:DELay:MODe OFF"
        scopeObject.write(tempString)
        tempString = "TRIGger:A:LEVel -" + str(level)
        scopeObject.write(tempString)
        tempString = "TRIGGER:A:EDGE:SOURCE " + str(channel)
        scopeObject.write(tempString)
        tempString = "TRIGger:A:EDGE:SLOpe " + str(edge)
        scopeObject.write(tempString)
        tempString = "HORizontal:MAIn:POSition " + str(position)
        scopeObject.write(tempString)
    elif returnString.find("MSO58") != -1:
        tempString = "TRIGger:A:TYPe EDGE"
        scopeObject.write(tempString)
        tempString = "TRIGGER:A:MODE NORMAL"
        scopeObject.write(tempString)
        tempString = "TRIGGER:A:EDGE:SLOPE " + str(edge)
        scopeObject.write(tempString)
        tempString = "TRIGGER:A:EDGE:SOURCE " + str(channel)
        scopeObject.write(tempString)
        tempString = "TRIGGER:A:LEVEL:"  + str(channel) + " -" + str(level)
        scopeObject.write(tempString)

def scope_ScreenShot_Copy(scopeObject, fileName):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = "*CLS"
        scopeObject.write(tempString)
        tempString = "SAVe:ASSIgn:TYPe IMAGe"
        scopeObject.write(tempString)
        tempString = "SAVe:IMAGe:FILEFormat PNG"
        scopeObject.write(tempString)
#        tempString = "HARDCOPY:PORT ETHERnet"
#        scopeObject.write(tempString)
        tempString = "HARDCOPY START"
        scopeObject.write(tempString)
        time.sleep(2)
                
        raw_data = scopeObject.read_raw()
    
#        print "before read raw"
##        raw_data = scopeObject.read_raw()
#        rm = visa.ResourceManager()
#        raw_data = rm.visalib.read(scopeObject.session, 262144)
#        raw_data = raw_data[0]
#        print raw_data
#        print "after read raw"
        fid = open(fileName, 'wb')
        fid.write(raw_data)
        fid.close()
        
    elif returnString.find("MSO58") != -1:
#        tempString = "SAVe:IMAGe:FILEFormat PNG"
#        scopeObject.write(tempString)
#        tempString = "SAVe:IMAGe " + fileName
#        scopeObject.write(tempString)
#        tempString = "FILESystem:READFile " + fileName
#        scopeObject.write(tempString)
#        print "before read raw"
#        raw_data = scopeObject.read()
#        print "after read raw"
        
#        tempString = "*CLS"
#        scopeObject.write(tempString)
#        tempString = "SAVe:ASSIgn:TYPe IMAGe"
#        scopeObject.write(tempString)
#        tempString = "SAVe:IMAGe:FILEFormat PNG"
#        scopeObject.write(tempString)
##        tempString = "HARDCOPY:PORT ETHERnet"
##        scopeObject.write(tempString)
#        tempString = "HARDCOPY START"
#        scopeObject.write(tempString)
#        time.sleep(2)

        scopeObject.write('SAVE:IMAGe \"C:/Temp.png\"')
        dt = datetime.now()
        fileName = dt.strftime("MSO5_%Y%m%d_%H%M%S.png")
        scopeObject.query('*OPC?')
        scopeObject.write('FILESystem:READFile \"C:/Temp.png\"')
        imgData = scopeObject.read_raw(1024*1024)
        file = open(fileName, "wb")
        file.write(imgData)
        file.close()
        scopeObject.write('FILESystem:DELEte \"C:/Temp.png\"')
        
#        print "before read raw"
##        #Save image on scope harddrive
##        scopeObject.write('SAVE:IMAGE \'c:/TEMP.PNG\'')
##        scopeObject.ask("*OPC?")  #Make sure the image has been saved before trying to read the file
##        #Read file data over
##        scopeObject.write('FILESYSTEM:READFILE \'c:/TEMP.PNG\'')
#        raw_data = scopeObject.read_raw()
###        raw_data = visa.visalib.read(scopeObject, 1024)
#        print "after read raw"
        


    print "Screen Captured"    
    
def scope_Set_Offset(scopeObject, channel, offset):
    tempString = str(channel) + ":OFFSet " + str(offset)
    scopeObject.write(tempString)
    
def scope_Set_Channel_Voltage(scopeObject, channel, voltage):
    tempString = str(channel) + ":SCAle " + str(voltage)
    scopeObject.write(tempString)
    
def scope_Set_Statistics_Off(scopeObject):
    tempString = "MEASUrement:STATIstics:MODe OFF"
    scopeObject.write(tempString)
    
def scope_Set_Statistics_On(scopeObject):
    tempString = "MEASUrement:STATIstics:MODe ON"
    scopeObject.write(tempString)
    
def scope_Set_HCursor(scopeObject, valA, valB):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = "CURSor:HBArs:POSITION1 " + str(valA)
        scopeObject.write(tempString)
        tempString = "CURSor:HBArs:POSITION2 " + str(valB)
        scopeObject.write(tempString)
        tempString = "CURSor:VBArs:POSITION1 -20"
        scopeObject.write(tempString)
        tempString = "CURSor:VBArs:POSITION2 -20"
        scopeObject.write(tempString)
    elif returnString.find("MSO58") != -1:
        tempString = "DISplay:WAVEView1:CURSor:CURSOR1:ASOUrce CH1" 
        scopeObject.write(tempString)
        tempString = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:FUNCTION HBArs" 
        scopeObject.write(tempString)
        tempString = "DISPLAY:WAVEVIEW1:CURSOR:CURSOR1:MODE INDEPENDENT" 
        scopeObject.write(tempString)
        tempString = "DISplay:WAVEView1:CURSor:CURSOR1:HBArs:APOSition " + str(valA) 
        scopeObject.write(tempString)
        tempString = "DISplay:WAVEView1:CURSor:CURSOR1:HBArs:BPOSition " + str(valB) 
        scopeObject.write(tempString)

def scope_Set_CursorOn(scopeObject, channel):
    returnString = scopeObject.query("*IDN?")
    if returnString.find("4104") != -1:
        tempString = "CURSor:SOUrce " + str(channel)
        scopeObject.write(tempString)
        tempString = "CURSor:FUNCtion SCREEN"
        scopeObject.write(tempString)
        tempString = "CURSor:STATE ON"
        scopeObject.write(tempString)
        tempString = "CURSor:VBArs:UNIts SECOnds"
        scopeObject.write(tempString)
     
    elif returnString.find("MSO58") != -1:
        tempString = "DISplay:WAVEView1:CURSor:CURSOR1:STATE ON" 
        scopeObject.write(tempString)
        
        

        
def scope_Get_HCursor_Delta(scopeObject):
    tempString = "CURSor:HBArs:DELTa?"
    return scopeObject.query(tempString)
    

    
