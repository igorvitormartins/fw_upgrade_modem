from filecmp import clear_cache
from io import BufferedReader
from multiprocessing.connection import wait
from turtle import clear, color
import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os


#definição de campos para busca

user_name = '//*[@id="txtUserName"]'
password = '//*[@id="pwdUserPasswd"]'
login_button = '//*[@id="btnLogin"]'
upgrade_button = '//*[@id="btnUpgradeByHTTP"]'
whatdoyousee = '//*[@id="txtCaptcha"]'


serial = '/html/body/jhi-main/div/div[3]/div/jhi-op-transfer/div/div[2]/table/tbody/tr[indice]/td[3]/span'
check = '/html/body/jhi-main/div/div[3]/div/jhi-op-transfer/div/div[2]/table/tbody/tr[indice]/td[1]/label' 
pesquisar = '//*[@id="fileUpgradeByHTTP"]'
arquivo = "C:/Users/igor.martins/Desktop/Testes_Developer/Askey_Testes/firm_update/ASP_RTF8209VW_TLSC_V1.0.2_V002/ASP_RTF8209VW_TLSC_V1.0.2_V002"


#execução do sellenium




def fwupdate():
    error_code = ['FAIL', 'FWU']
    try:
        driver = webdriver.Chrome()
        driver.get("http://192.168.1.1/login.asp")
        time.sleep(3)
        os.system('cls')
        captcha = input("INSIRA VALOR CAPTHA: ")

        driver.find_element_by_xpath(whatdoyousee).send_keys(captcha)
        driver.find_element_by_xpath(user_name).send_keys('system')
        driver.find_element_by_xpath(password).send_keys('system')
        driver.find_element_by_xpath(login_button).send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get("http://192.168.1.1/fw_upgrade.asp")
        time.sleep(3)
        driver.find_element_by_xpath(pesquisar).send_keys(arquivo)
        driver.find_element_by_xpath(upgrade_button).send_keys(Keys.ENTER)
        time.sleep(1)
        #inicio = input("ENTER: ")
        return 'FW UPDATE PASS'
    except:
        return error_code