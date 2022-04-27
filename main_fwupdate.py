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
import socket


os.system('cls')
for x in range(3):
    arq = open("intro\intro"+str(x) +".txt")
    linhas = arq.readlines()
    for linha in linhas:
        print(linha)
        time.sleep(0.1)
    arq.close()
    time.sleep(2)
    os.system('cls')
for x in range(1):
    arq = open("intro/intro3.txt")
    linhas = arq.readlines()
    for linha in linhas:
        print(linha)
        time.sleep(0.1)
        os.system('cls')
    arq.close()
    os.system('cls')
#codigo OK
while True:
    mac = input("Insira Serial: ")
    os.system('cls')
    inicio = time.time()
    result = function.input_string(mac)
    if result[0] == 'FAIL':
        mac= 'AAAAAAAAAAAA'
        print('Result: ' + result[0] + ' ' + result[1])
        
    else:
        
        print(mac)
        result = function.startpingtest()
        if result[0] == 'FAIL':
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
    
    
    if(result[0] == 'FAIL'):
        mixer.init()
        mixer.music.load('smw_fireball.wav')
        mixer.music.play()
        result_test = 'FAIL'
        error_code = result[1]
        arq = open("fail.txt")
        linhas = arq.readlines()
        for linha in linhas:
            print(linha)

    else:
        mixer.init()
        mixer.music.load('mario.mp3')
        mixer.music.play()
        result_test = 'PASS'
        error_code = '00'
        arq = open("pass.txt")
        linhas = arq.readlines()
        for linha in linhas:
            print(linha)
        arq.close()

    resumo = mac + ' ' + result_test + ' ' + error_code + ' ' + 'FW_UPGRADE ' + socket.gethostname() + ' ' + str(tempo) + 'seconds'
    print(resumo)
    
    function.saveLog(mac, resumo)

#FIM codigo OK