import time
import serial
import serial.tools.list_ports
from serial import Serial

arduino: Serial | None = None  # type: ignore
buffer = ""
isListening = False
response: str = ""
waitingResponse = False
offline = True


def startListening():
    print("START LISTENING THREAD")
    global arduino, isListening, buffer, response, waitingResponse, offline
    arduino = advancedSerialInit()
    if arduino is not Serial:
        print("NO ARDUINO IS CONNECTED")
        return

    if communicate("X"):
        offline = False
        isListening = True

    while isListening:
        if not arduino.isOpen():
            print(f" *** ARDUINO IS NO LONGER CONNECTED *** ")
            break
        # data to send
        if buffer != "":
            arduino.write(f"{buffer}\n".encode())
            buffer = ""
        # data to read
        elif arduino.in_waiting:
            response = arduino.readline().decode("ascii").rstrip()
            if response != "":
                waitingResponse = False


def endListening():
    communicate("X")
    time.sleep(0.2)
    global isListening, offline
    offline = True
    isListening = False
    try:
        arduino.close()  # type: ignore
        time.sleep(2)
        print(" *-- PORT CLOSED --* ")
    except AttributeError:
        print(" -- ABORTION ANORMALLY --")
        return


def write2Read(message: str):
    global buffer, waitingResponse, response
    waitingResponse = True
    buffer = message
    while waitingResponse:
        pass
    return response


def communicate(message: str) -> bool:
    """Send message via SERIAL PORT to PC
    :param message: message added to buffer
    :return: True if OFFLINE MODE or MESSAGE CONFIRMATION RECEIVED
    :raise: Connection error
    ---------
    :arg: "T" for test communication
    :arg: "S" for short exposure - most used
    :arg: "L" for long exposure - mA calibration only
    """
    global offline
    if offline:
        return True
    res = write2Read(message)
    if res == message:
        return True
    raise ConnectionError


def getPorts():
    ports = serial.tools.list_ports.comports()
    return ports


def findItem(portsFound, matchingText: str):  # type: ignore
    commPort = ""
    numConnections = len(portsFound)  # type: ignore
    for i in range(0, numConnections):
        port = portsFound[i]  # type: ignore
        strPort = str(port)  # type: ignore
        if matchingText in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]
    return commPort


def advancedSerialInit() -> serial.Serial | None:
    portName = "CH340"
    foundPorts = getPorts()
    connectPort = findItem(foundPorts, portName)
    if connectPort != "":
        return serial.Serial(connectPort, 9600)
