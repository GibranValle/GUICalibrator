import time
import serial
import serial.tools.list_ports

arduino = None
buffer = ''
isListening = False
response = ''
waitingResponse = False
offline = True


def startListening():
    print('START LISTENING THREAD')
    global arduino, isListening, buffer, response, waitingResponse, offline
    arduino = advancedSerialInit()
    if arduino is None:
        print('NO ARDUINO IS CONNECTED')
        return

    if communicate("X"):
        offline = False
        isListening = True

    while isListening:
        if not arduino.isOpen():
            print(f" *** ARDUINO IS NO LONGER CONNECTED *** ")
            serialError = True
            break
        # data to send
        if buffer != '':
            arduino.write(f"{buffer}\n".encode())
            buffer = ''
        # data to read
        elif arduino.in_waiting:
            response = arduino.readline().decode('ascii').rstrip()
            if response != '':
                waitingResponse = False


def endListening():
    communicate("X")
    time.sleep(0.2)
    global isListening, offline
    offline = True
    isListening = False
    try:
        arduino.close()
        time.sleep(2)
        print(' *-- PORT CLOSED --* ')
    except AttributeError:
        print(' -- ABORTION ANORMALLY --')
        return


def write2Read(message):
    global buffer, waitingResponse, response
    waitingResponse = True
    buffer = message
    while waitingResponse:
        pass
    return response


def communicate(message):
    global offline
    if offline:
        return True
    res = write2Read(message)
    if res == message:
        return True
    print(" *** COMMUNICATION ERROR ***")
    return False


def getPorts():
    ports = serial.tools.list_ports.comports()
    return ports


def findItem(portsFound, matchingText):
    commPort = ''
    numConnections = len(portsFound)
    for i in range(0, numConnections):
        port = portsFound[i]
        strPort = str(port)
        if matchingText in strPort:
            splitPort = strPort.split(' ')
            commPort = splitPort[0]
    return commPort


def advancedSerialInit():
    portName = 'CH340'
    foundPorts = getPorts()
    connectPort = findItem(foundPorts, portName)
    if connectPort != '':
        arduino = serial.Serial(connectPort, 9600)
        return arduino
