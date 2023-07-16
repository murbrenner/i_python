from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

df = pd.read_csv('C:\\Users\\ocmvc45555\\Documents\\iMacros\\Datasources\\reprint.csv')

driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirFiltrarRegistroAtendimentoAction.do?menu=sim")
        driver.find_element(By.NAME, "numeroRA").send_keys(str(df['RA'][i]), Keys.ENTER)
        driver.find_element(By.NAME, "Submit").click()
        print((str(df['RA'][i])), sep=' ')
        play()

def play():
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Anexos').click()
    try:
        driver.find_element(By.CSS_SELECTOR, '#layerShowAnexos > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > img').click()
        print('ANEXO 01 BAIXADO', sep=' ')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#layerShowAnexos > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > a > img').click()
        print('ANEXO 02 BAIXADO', sep=' ')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#layerShowAnexos > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > div > table > tbody > tr:nth-child(3) > td:nth-child(1) > a > img').click()
        print('ANEXO 03 BAIXADO', sep=' ')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#layerShowAnexos > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > a > img').click()
        print('ANEXO 04 BAIXADO', sep=' ')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#layerShowAnexos > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > div > table > tbody > tr:nth-child(5) > td:nth-child(1) > a > img').click()
        print('ANEXO 05 BAIXADO', sep=' ')
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#layerShowAnexos > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > div > table > tbody > tr:nth-child(6) > td:nth-child(1) > a > img').click()
        print('ANEXO 06 BAIXADO')
        time.sleep(1)
    except NoSuchElementException:
        print('DOWNLOAD DE ANEXOS FINALIZADO')
        time.sleep(1)

enter()

while True:
    pass






