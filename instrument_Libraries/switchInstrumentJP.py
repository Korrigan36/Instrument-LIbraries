# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 10:28:08 2017

@author: beschanz
"""
import time

class SwitchInstrument3497XX():
    
    def __init__(self, switchObject):
        self.switchObject = switchObject
        self.tcScanList = []
        self.vScanList = []
        self.measurementDict = dict()     
        self.switchObject.write("ABORt")
        
    def get_scan_list_str(self, scanList):
        return str(str(scanList)[1:(len(str(scanList))-1)])
        
    def add_voltage_channel(self, channel):
        self.switchObject.clear()
        self.vScanList.append(channel)
        tempString = "CONF:VOLTage:DC AUTO,MAX,(@" + self.get_scan_list_str(self.vScanList) + ")"
        print(tempString)
        self.switchObject.write(tempString)
        time.sleep(.05)
        self.setup_switch()
        
    def add_tc_channel(self, channel):
        self.switchObject.clear()
        self.tcScanList.append(channel)
        tempString = "CONF:TEMPerature TCouple, T, (@" + self.get_scan_list_str(self.tcScanList) + ")"
        print(tempString)
        self.switchObject.write(tempString)
        time.sleep(.05)
        self.setup_switch()
        
    def setup_switch(self):
        self.switchObject.clear()
        tempString = "ROUTE:SCAN (@" + self.get_scan_list_str(sorted(self.vScanList + self.tcScanList, key = int)) + ")"
        print(tempString)
        self.switchObject.write(tempString)
        time.sleep(1)
        tempString = "TRIGger:COUNT 1"
        self.switchObject.write(tempString)
        tempString = "TRIGger:SOURce IMMediate"
        self.switchObject.write(tempString)
    
    def trigger_measurement(self, numTriggers):
        self.switchObject.clear()
        
        tempString = "TRIGger:COUNT " + str(numTriggers)
        self.switchObject.write(tempString)
        
        numReadings = int(self.switchObject.query("ROUTe:SCAN:SIZE?"))
        
        tempString = "INITIATE"
        self.switchObject.write(tempString)
        
        while self.switchObject.query("DATA:POINTS?") < numReadings:
          time.sleep(.1)
        
        #tempString = "INIT;*OPC?"
        #self.switchObject.write(tempString)

        tempString = "FETCH?"
        result = self.switchObject.query(tempString)

        print(result)
        return result
        
#        #split result into numeric values
#        #result = result[2:len(result)] #first 2 character is not valid for some reason
#        result = result.split(",")
#       
#        for i in range(0, len(result)):
#            result[i] = float(result[i])
#        
#        #build complete channel list and sort it for entry into dictionary
#        channelList = self.tcScanList + self.vScanList
#        channelList = sorted(channelList, key=int)
#        
#        #put channel,measurement pairs into dictionary for access later
#        self.measurementDict = dict()   #clear existing measurement/channel dictionary
#        for i in range(0, len(channelList)):
#            self.measurementDict[channelList[i]] = result[i]
    
    def get_triggered_measurement(self, channelIndex):
        #try to lookup given channel in measurementDictionary from last trigger
        try:
            result = self.measurementDict[channelIndex]
            return result
        except:
            raise ValueError('Given channelIndex not in switch channel list')
