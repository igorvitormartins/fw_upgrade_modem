from ast import arg
from cProfile import run
from cgi import test
from filecmp import clear_cache
from http.client import OK
from io import BufferedReader
from multiprocessing.connection import wait
from os import kill
from turtle import clear, color
from typing import Any
from unittest import result
import PySimpleGUI as sg
import function
import time
from datetime import datetime
import math
from pygame import mixer
import threading
import fwupdate
import os

while True:
    entermode = input("Aperte Enter para Iniciar: ")
    os.system('cls')
    mac = '000000000000'
    print(mac)
    inicio = time.time()

    result = function.startpingtest()
    if result[0] == 'FAIL':
        #window.find_element('RESULT').Update(result[1])
        print('Result: ' + result[0] + ' ' + result[1])
    else:
        result = function.Version_ISP()
        if result[0] == 'FAIL':
            #window.find_element('RESULT').Update(result[1])
            print('Result: ' + result[0] + ' ' + result[1])
        else:
            print(result)

    fim = time.time()
    tempo = math.trunc(fim - inicio)
    print('Total Time: ' + str(tempo) + ' seconds')

    if(result[0] == 'FAIL'):
        mixer.init()
        mixer.music.load('smw_fireball.wav')
        mixer.music.play()
        arq = open("pass.txt")
        linhas = arq.readlines()
        for linha in linhas:
            print(linha)

    else:
        mixer.init()
        mixer.music.load('mario.mp3')
        mixer.music.play()
        arq = open("pass.txt")
        linhas = arq.readlines()
        for linha in linhas:
            print(linha)
    arq.close()

#codigo OK
'''
mac = '000000000000'
inicio = time.time()
result = function.startpingtest()
if result[0] == 'FAIL':
    #window.find_element('RESULT').Update(result[1])
    print('Result: ' + result[0] + ' ' + result[1])                        
else:
    print('PASS')
    result = fwupdate.fwupdate()
    if result[0] == 'FAIL':
        print('Result: ' + result[0] + ' ' + result[1])
    else:
        print('PASS')
fim = time.time()
tempo = math.trunc(fim - inicio)
print('Total Time: ' + str(tempo) + ' seconds')
resumo = result[0]
function.saveLog(mac, resumo)
print(resumo)
'''
#FIM codigo OK



'''
global var
var = False

sg.theme('Dark Grey 13')



def interface():

    layout = [ [sg.Text('')],
          [sg.Text('MAC: '), sg.Input('', key='MAC', justification='true', size=(25,10)), sg.Text('RUN: '), sg.Text('', key='lastmac')],
          [sg.Text('')],
          [sg.Button('1', key='1', size=(4, 1)), sg.Button('2', key='2', size=(4, 1)), sg.Button('3', key='3', size=(4, 1)), sg.Button('4', key='4', size=(4, 1)), sg.Submit('START', key='START', size=(6, 3)), sg.Text('RESULT', key='RESULT')],
          [sg.Output(key='_output_' ,size=(60,25))]]

    window = sg.Window('PRETEST', layout, resizable = False)


    while True:
        eventos, valores = window.read()
        if eventos == sg.WINDOW_CLOSED:
            break
            
        if eventos == '1':
            window.find_element(key='1').Update(disabled=True)
            window.find_element('_output_').Update('')
            window.find_element('RESULT').Update('USB TEST PROCESSING...')
            time.sleep(1)
            print('USB TEST 1')
            time.sleep(2)
            print('USB TEST 2')
            time.sleep(3)
            print('USB TEST 3')
            window.find_element('RESULT').Update('USB TEST FINISHED...')
            window.find_element(key='1').Update(disabled=False)
            
            #window[key] or window.find_element are recommended. **
        if eventos == '2':
            
            window.find_element(key='2').Update(disabled=True)
            window.find_element(key='START').Update(disabled=True)
            window.find_element('_output_').Update('')
            window.find_element('RESULT').Update('USB TEST PROCESSING...')
            #decisao = sg.popup_ok_cancel('ARE THE LEDs ON?')
            time.sleep(1)
            print('USB TEST 1')
            time.sleep(2)
            print('USB TEST 2')
            time.sleep(3)
            print('USB TEST 3')
            window.find_element('RESULT').Update('USB TEST FINISHED...')
            window.find_element(key='2').Update(disabled=False)
            window.find_element(key='START').Update(disabled=False)
            #window[key] or window.find_element are recommended. **

        if eventos == '4':
            
            window.find_element(key='2').Update(disabled=True)
            window.find_element(key='START').Update(disabled=True)
            window.find_element('_output_').Update('')
            window.find_element('RESULT').Update('LED TEST PROCESSING...')
            result = hitron.Check_Led()
            decisao = sg.popup_ok_cancel('ARE THE LEDs ON?')
            if(decisao == 'OK'):
                window.find_element('RESULT').Update('LED TEST PASS')
            else: 
                window.find_element('RESULT').Update('LED TEST FAIL')
            
        if eventos == 'START':
            
            def running():
                         
                inicio = time.time()
                
                window.find_element('RESULT').Update('PROCESSING...')
                window.find_element(key='START').Update(disabled=True)
                window.find_element(key='MAC').Update(disabled=True)
                window.find_element('_output_').Update('')
                window.find_element('lastmac').Update(valores['MAC'])
                print('Date Time: ' + str(datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')))
                result = hitron.input_string(valores['MAC'])
                if result[0] == 'FAIL':
                    window.find_element('RESULT').Update(result[1])
                else:
                    print("MAC: "+valores['MAC'])
                    print("TEST CHECK PING")
                    #result = threading.Thread(target=hitron.startpingtest()).start()
                    result = hitron.startpingtest()
                    if result[0] == 'FAIL':
                        window.find_element('RESULT').Update(result[1])
                        print('Result: ' + result[0] + ' ' + result[1])
                        
                    else:
                        print('--TELNET TEST START--')
                        result = hitron.Telnet_valid()
                        if result[0] == 'FAIL':
                            window.find_element('RESULT').Update(result[1])
                            print('Result: ' + result[0] + ' ' + result[1])
                        else:
                            print('--TELNET TEST PASS--')
                            print('--USB MOUNT TEST--')
                            result = hitron.USB_Test_Mount()
                            if result[0] == 'FAIL':
                                window.find_element('RESULT').Update(result[1])
                                print('Result: ' + result[0] + ' ' + result[1])
                            else:
                                print('USB MOUNT PASS')
                                print('USB FAST TEST')
                                result = hitron.USB_Test_Fast()
                                if result[0] == 'FAIL':
                                    window.find_element('RESULT').Update(result[1])
                                    print('Result: ' + result[0] + ' ' + result[1])
                                else:
                                    print('USB 3.0 FAST PASS')
                                    
                                    print('START CHECK BUTTONS')
                                    result = hitron.WpsButton()
                                    if result[0] == 'FAIL':
                                        window.find_element('RESULT').Update(result[1])
                                        print('Result: ' + result[0] + ' ' + result[1])
                                    
                                    else:
                                        print('--CHECK WPS PASS--')
                                        result = hitron.ResetButton()
                                        if result[0] == 'FAIL':
                                            window.find_element('RESULT').Update(result[1])
                                            print('Result: ' + result[0] + ' ' + result[1])
                                        else:
                                            print('--CHECK Reset Button PASS--')
                                            
                                            #result = ['PASS', '']
                                    
                fim = time.time()
                tempo = math.trunc(fim - inicio)
                print('Total Time: ' + str(tempo) + ' seconds')      
                window.find_element(key='START').Update(disabled=False)
                window.find_element(key='MAC').Update(disabled=False)
                window.find_element(key='MAC').Update('')
                resume = window.find_element(key='_output_').Get()
                hitron.saveLog(valores['MAC'], resume)
                
                if (result[0] == 'FAIL'):
                    sg.theme('DarkGreen3')
                    mixer.init()
                    mixer.music.load('smw_fireball.wav')
                    mixer.music.play()
                else:
                    window.find_element(key='RESULT').Update('PASS')
                    mixer.init()
                    mixer.music.load('mario.mp3')
                    mixer.music.play()
            
            t1 = threading.Thread(target=running, daemon=True, kwargs={})
            t1.start()
            
interface()
'''