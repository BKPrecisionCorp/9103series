import serial

ser = serial.Serial("/dev/ttyUSB0")
ser.timeout = 1

currMult = 100
voltMult = 100

def spdWrite(cmd):
    ser.write(cmd.encode())
    return ser.read_until(terminator=b'\r')

def spdQuery(cmd):
    resp = []
    notDone = True
    ser.write(cmd.encode())
    while(notDone):
        r = ser.read_until(terminator=b'\r')
        print(r.decode())
        if(not(len(r) > 0)):
           notDone = False
        else:
            resp.append(r)
    return resp

def setCurrent(value, preset=3):
    """Set the current. Val is a number in normal format. i.e. 1.0 = 1.0 A. preset, default 0, sets which preset to set."""
    val = int(value*currMult)
    print(spdWrite("CURR"+str(preset)+"%04d\r"%val))

def setVoltage(value, preset=3):
    """Set the voltage. value is a number in normal format. i.e. 1.0 = 1.0 V. preset, default 0, sets which preset to set."""
    val = int(value*voltMult)
    print(spdWrite("VOLT"+str(preset)+"%04d\r"%val))

def setOutput(value):
    """Set the output state. On (value = 1), Off (Value = 0) """
    print(spdWrite("SOUT"+str(value)+"\r"))

def getOutput():
    """Get the state of the output. 1 = On, 0 = Off """
    resp = spdQuery("GOUT\r")
    return int(resp[0])

def getPreset():
    """ Returns the preset in use. 0-2 or normal mode 3"""
    resp = spdQuery("GABC\r")
    return int(resp[0])

def setPreset(value):
    """ Set the active preset. value =  0-2 or normal mode 3 """
    print(spdWrite("SABC"+str(value)+"\r"))

def getDeltaTime(value):
    """ Get the "delta time". value = 0-5. Return is in seconds """
    resp = spdQuery("GDLT"+str(value)+"\r")
    return int(resp[0])

def setDeltaTime(deltaVal, time):
    """ Set the "delta time". deltaVal = 0-5. time is in seconds """
    print(spdWrite("SDLT"+str(deltaVal)+"%02d\r"%time))

def getSWTime(preset):
    """ Get the SW time of a preset. Returns the time in seconds.
        Not sure what this does now..."""
    return spdQuery("GSWT"+str(preset)+"\r")
    
def setSWTime(deltaVal, time):
    """ Set the "delta time". deltaVal = 0-5. time is in seconds """
    print(spdWrite("SDLT"+str(deltaVal)+"%02d\r"%time))

# create some commands for the transient mode...
# (Users please submit a support case at www.bkprecision.com if you need this)
# Adding the commands as they are in the programming manual for now.

def runProgram(firstNum, secondNum):
    """Set and start running first and last sequence (?)
    Value range 0-2"""
    print(spdWrite("RUNP"+str(firstNum)+str(secondNum)+"\r"))

def stopProgram():
    print(spdWrite("STOP\r"))

def disableKeypad():
    """ Disables keypad on PS. Use ENDS / enableKeypad() to re-enable"""
    print(spdWrite("SESS\r"))

def disableKeypad():
    """ Disables keypad on PS. Use ENDS / enableKeypad() to re-enable"""
    print(spdWrite("ENDS\r"))

def getAllData():
    """ Get all data from power supply
     see programming manual for array order and meaning
     page 7... """
    return spdQuery("GALL\r")

def setAllPresets(psA, psB, psC):
    """Set the values for each preset. See the programming manual for details"""
    print(spdWrite("SETM"+str(psA)+str(psB)+str(psC)+"\r"))
