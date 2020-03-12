def pulseGen_Set_Volt_High_Low(waveFormObject, amplitude):

    offset = amplitude / 2.0 + 0.010
    
    waveFormObject.write("SOURCE1:VOLTAGE:OFFSET -" + str(offset))
    waveFormObject.write("OUTPUT1:POLarity INVerted")
        
    waveFormObject.write("SOURCE1:VOLTAGE +" + str(amplitude))
              
def pulseGen_Set_Freq(waveFormObject, freq):
    tempString = "SOURce1:FREQuency:MODE FIXED"
    waveFormObject.write(tempString)
    tempString = "SOURCE1:FREQUENCY " + str(freq)
    waveFormObject.write(tempString)
        
def pulseGen_Set_FreqSweep(waveFormObject, startFreq, stopFreq, sweepTime):
    tempString = "SOURce1:FREQuency:STARt " + str(startFreq)
    waveFormObject.write(tempString)
    tempString = "SOURce1:FREQuency:STOP " + str(stopFreq)
    waveFormObject.write(tempString)
    tempString = "SOURce1:SWEep:TIME " + str(sweepTime)
    waveFormObject.write(tempString)
    tempString = "TRIGger1:SOURce IMM"
    waveFormObject.write(tempString)
    tempString = "SOURce1:FREQuency:MODE SWE"
    waveFormObject.write(tempString)
        
def pulseGen_Set_Duty(waveFormObject, duty):
    tempString = "SOURce1:FUNCTION:PULSe:DCYCLE " + str(duty)
    waveFormObject.write(tempString)
      
def pulseGen_Check_OutputOn(waveFormObject):
    tempString = "OUTPUT1?"
    return waveFormObject.query(tempString)
  
def pulseGen_Set_OutputOn(waveFormObject):
    tempString = "OUTPUT1 ON"
    waveFormObject.write(tempString)
        
def pulseGen_Set_OutputOff(waveFormObject):
    tempString = "OUTPUT1 OFF"
    waveFormObject.write(tempString)
        
def pulseGen_Set_Mode_Pulse(waveFormObject):
    tempString = "SOURCE1:FUNCTION PULSE"
    waveFormObject.write(tempString)
    tempString = "SOURCE1:FUNCTION:PULSE:HOLD DCYCLE"
    waveFormObject.write(tempString)
       
def pulseGen_Zero_Output(waveFormObject):
    tempString = "SOURCE1:VOLTAGE MINIMUM"
    waveFormObject.write(tempString)
    tempString = "SOURCE1:VOLTAGE:OFFSET 0"
    waveFormObject.write(tempString)
      
def pulseGen_Set_Burst_Mode_Trig(waveFormObject):
    tempString = "SOURCE1:BURST:MODE TRIGGERED"
    waveFormObject.write(tempString)
         
def pulseGen_Set_Burst_NCycles(waveFormObject, numCycles):
    tempString = "SOURCE1:BURST:NCYCLES " + str(numCycles)
    waveFormObject.write(tempString)
         
def pulseGen_Set_Burst_Period(waveFormObject, burstPeriod):
    tempString = "SOURCE1:BURST:INTERNAL:PERIOD " + str(burstPeriod)
    waveFormObject.write(tempString)
         
def pulseGen_Set_Burst_On(waveFormObject):
    tempString = "SOURCE1:BURST:STATE ON "
    waveFormObject.write(tempString)
         
def pulseGen_Set_Burst_Off(waveFormObject):
    tempString = "SOURCE1:BURST:STATE OFF "
    waveFormObject.write(tempString)
         
def pulseGen_Set_Both_Edge(waveFormObject, time_ns):
    tempString = "SOURCE1:FUNCTION:PULSE:TRANSITION:BOTH " + str(time_ns) + " ns"
    waveFormObject.write(tempString)

def pulseGen_Config_Pulse_Waveform(waveFormObject, amplitude, frequency, offset):
    tempString = "SOURCE1:APPLy:PULSe " + str(frequency) + " , " + str(amplitude) + " , " + str(offset)
    waveFormObject.write(tempString)
