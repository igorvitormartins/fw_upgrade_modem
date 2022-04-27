import inicial, ping
import time
import getpass
import telnetlib
import random
import threading
import PySimpleGUI as sgq

dados = inicial.data_inicial()
diretorio = inicial.dir()

def ping_test(ip):
    for x in range(1):
        print('Trying ping... '+str(x)+' '+ip)
        #res_ping = threading.Thread(target=ping.myping_test, args=(ip,)).start()
        res_ping = ping.myping_test(ip)
        #ping_test_ip = threading.Thread(target=ping_test).start()
        if(res_ping == True):
            return True
        else:
            print('PING FAIL...TRYING AGAIN!')
            time.sleep(1)
    return 'VG8 ' + ip
    
def chk_version(version, version_gabarito):
    if version == version_gabarito:
        return True
    else:
        return 'FW02 ' + version
        
def input_string(valor):
    error_code = ['FAIL', 'SR0']
    if len(valor) != 12:
        return error_code
    else:
        if (dados[3] != valor[:6]):
            return error_code
        else:
            if (valor[11]!= dados[4]):
                return error_code
            else:
                return 'PASS MAC CHECK'

def startpingtest():
    error_code = ['FAIL', 'VG8']
    
    ping_test_ip = ping_test(dados[0])
    if ping_test_ip == True: 
        print('PING PASS: '+ dados[0])
        return 'TEST PING PASS'
        #ping_test_second = ping_test(dados[1])
        #if ping_test_second == True:
            #print('PING PASS: '+ dados[1])
            #return 'TEST PING PASS'
        #else:
            #print(ping_test_second)
            #return error_code
    else:
        print(ping_test_ip)
        return error_code


def USB_Test_Mount():
    error_code = ['FAIL', 'USBM']
    for x in range(3):
        try:
            tn = telnetlib.Telnet(dados[1])
            time.sleep(3)
            pendrive = tn.write(b"mount\n\n")
            tn.write(b"exit\n")
            crash = tn.read_all()
            #print(crash)
            
            #inicio de verificacao de montagem:
            findit = "/tmp/mnt/diska1"

            if findit in str(crash):
                return 'USB TEST MOUNT PASS'
                break
            else: 
                print("ERROR USB MOUNT...")
                time.sleep(1)
                print("TYING AGAIN...")
        except:
            print("ERROR USB MOUNT...")
            time.sleep(1)
            print("TYING AGAIN...")
    return error_code

def USB_Test_Fast():
    error_code = ['FAIL', 'USBT']
    for x in range(3):
        try:
            tn = telnetlib.Telnet(dados[1])
            time.sleep(3)
            pendrive = tn.write(b"lsusb -t\n\n")
            tn.write(b"exit\n")
            crash = tn.read_all()
            #print(crash)
            findit = "usb-storage, 5000M"

            if findit in str(crash):
                print("3.0 PASS")
                return 'USB 3.0 TEST MOUNT PASS'
                break
            else:
                print("ERROR USB FAST...")
                time.sleep(1)
                print("TRYING AGAIN...")
        except:
            print("ERROR USB FAST...")
            time.sleep(1)
            print("TRYING AGAIN...")
    return error_code
    
def Telnet_valid():
    error_code = ['FAIL', 'TLN']
    for x in range(3):
        try:
            tn = telnetlib.Telnet(dados[0])
            tn.read_until(b"login:")
            tn.write(b"system\n")
            tn.read_until(b"Password:")
            tn.write(b"system\n")
            time.sleep(3)
            tn.write(b"exit\n")
            #crash = tn.read_all().decode('ascii')
            return 'TELNET TEST PASS'  
            break
        except:
            print("ERROR TELNET TEST...")
            time.sleep(1)
            print("TRYING AGAIN...")
    return error_code        

def Check_Led():
    error_code = ['FAIL', 'CHL']
    
    
    for x in range(2):
        try:
            tn = telnetlib.Telnet(dados[0])
            tn.read_until(b"puma login:")
            tn.write(b"mso\n")
            tn.read_until(b"Password:")
            tn.write(b"msopassword\n")
            time.sleep(3)
            tn.write(b"Manufacture\n")
            time.sleep(1)
            tn.write(b"setLed 99 1\n")
            time.sleep(3)
            tn.write(b"exit\n")
            return 'LED CHECK TEST PASS'  
            break
        except:
            print("LED CHECK TEST FAIL...")
            time.sleep(1)
            print("TRYING AGAIN...")
    return error_code 

def saveLog(mac, resumo):
    
    keytest = random.randint(1000,9999)
    filename = diretorio + mac + '_' + str(keytest) + '.fwu'
    #print(filename)
    if(input_string(mac)[0] != 'FAIL'):
        with open(filename, "w") as logfile:
            #print(resumo)
            logfile.write(resumo)
            logfile.close()
    return 

def WpsButton():
    validator = 0
    error_code = ['FAIL', 'WPS']
    for x in range(1):
        try:
            tn = telnetlib.Telnet(dados[1])
            #print('Telnet OK')
            time.sleep(1)
            validator = 1
        except:
            validator = 0
        for y in range(10):
            if(validator == 1):
                print('Waiting Press WPS Button ' + str(y) + ' ...')
                time.sleep(3)
                output = tn.read_very_eager()
                output_formatted = output.decode('utf-8')
                findit = "WPS Button"
                if findit in str(output_formatted):
                    tn.write(b"exit\n")
                    print("WPS TEST PASS")
                    return 'WPS TEST PASS'
                    break
                else:
                    print("WPS TEST FAIL...")
                    print("TRYING AGAIN...")
    return error_code
    
def ResetButton():
    validator = 0
    error_code = ['FAIL', 'RST']
    for x in range(1):
        try:
            tn = telnetlib.Telnet(dados[1])
            #print('Telnet OK')
            time.sleep(1)
            validator = 1
        except:
            validator = 0
        for y in range(10):
            if(validator == 1):
                print('Waiting Press Reset Button ' + str(y) + ' ...')
                time.sleep(3)
                output = tn.read_very_eager()
                output_formatted = output.decode('utf-8')
                findit = "Reset Button"
                if findit in str(output_formatted):
                    tn.write(b"exit\n")
                    print("Reset TEST PASS")
                    return 'Reset TEST PASS'
                    break
                else:
                    print("Reset TEST FAIL...")
                    print("TRYING AGAIN...")
    return error_code
    
    
def Version_ISP():
    validator = 0
    error_code = ['FAIL', 'FW02']
    for x in range(1):
        try:
            tn = telnetlib.Telnet(dados[0])
            tn.read_until(b"login:")
            tn.write(b"system\n")
            tn.read_until(b"Password:")
            tn.write(b"system\n")
            time.sleep(3)
            tn.write(b"sys_info show\n")
            time.sleep(1)
            #print('Telnet OK')
            time.sleep(1)
            validator = 1
            
        except:
            validator = 0
        try:
            for y in range(5):
                if(validator == 1):
                    print('Finding... ' + str(y) + ' ...')
                    time.sleep(3)
                    output = tn.read_very_eager()
                    output_formatted = output.decode('utf-8')
                    findit = "V1.0.2"
                    if findit in str(output_formatted):
                        tn.write(b"exit\n")
                        return 'Version TEST PASS'
                        break
                    else:
                        print("Version TEST FAIL...")
                        print("TRYING AGAIN...")
        except:
            return error_code
    return error_code
    
    
    
