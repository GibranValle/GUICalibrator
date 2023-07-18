import subprocess


def getLocalMAC():
    call = 'chcp 65001 | getmac /fo csv /v /nh'
    output = subprocess.check_output(call, shell=True)
    output = output.decode('utf-8').split('\r\n')
    ethernet = []
    for index, line in enumerate(output):
        items = line.split(',')
        if "Ethernet" in items[0]:
            ethernet.append(items[0].replace('"', '') + ': ' + items[2].replace('"', '').replace('-', ':'))
    return ethernet


def getMac(ip):
    call = 'arp', '-a', ip
    output = subprocess.check_output(call)
    output = output.decode('latin-1').strip().split('\r\n')
    try:
        lastLine = output[2:][0].split(' ')
        for item in lastLine:
            if len(item) > 0 and '-' in item:
                return item.upper().replace('-', ':')
        return 'IP not found'
    except IndexError:
        return 'IP not found'


def getMCUMac():
    return getMac('192.168.0.101')


def getMUMac():
    return getMac('192.168.0.100')


def saveMACs():
    other = '\n'.join(getLocalMAC())
    mu = getMUMac()
    mcu = getMCUMac()
    f = open('macList.txt', 'w')
    f.writelines(other + '\n')
    f.writelines('MU0: ')
    f.writelines(mu + '\n')
    f.writelines('MCU0: ')
    f.writelines(mcu)
    f.close()
    temp = other, 'MU0: ' + mu, 'MCUO: ' + mcu
    return '\n'.join(temp)


def createWOLsetupFile(adaptername):
    macList = getLocalMAC()
    mac = '00:00:00:00:00:00'
    for item in macList:
        temp = item.split(': ')
        name = temp[0]
        if name == adaptername:
            mac = temp[1]
            break

    ip = '192.168.0.2'
    hostname = getHostname()
    submask = '255.255.255.0'

    macmu = getMUMac()
    ipmu = '192.168.0.100'

    macmcu = getMCUMac()
    ipmcu = '192.168.0.101'

    row1 = [mac, ip, hostname, submask]
    line1 = ",".join(row1)

    row2 = [mac, ip, hostname, '1']
    line2 = ','.join(row2)

    row3 = [macmu, ipmu, 'mu0', '0']
    line3 = ','.join(row3)

    row4 = [macmcu, ipmcu, 'mcu0', '0']
    line4 = ','.join(row4)

    f = open('setup.ini', 'w')
    end = '\n'
    f.write(line1 + end)
    f.write(line2 + end)
    f.write(line3 + end)
    f.write(line4 + end)
    f.close()


def getHostname():
    call = 'hostname'
    output = subprocess.check_output(call, shell=True)
    hostname = output.decode('utf-8').split('\r\n')[0]
    return hostname
