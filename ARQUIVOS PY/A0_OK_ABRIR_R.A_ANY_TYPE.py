import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pyautogui
import re
from selenium.common import NoSuchElementException

df = pd.read_csv('D:\\PYTHON\\ARQUIVOS CSV\\abrirRA.csv')

driver = webdriver.Chrome()

def login():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('LUIZD')
    driver.find_element(By.NAME, 'senha').send_keys('260154')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        driver.get('http://gsan.caema.ma.gov.br:8080/gsan/exibirInserirRegistroAtendimentoAction.do?menu=sim')
        driver.find_element(By.NAME, "tipoSolicitacao").send_keys('2.02')
        driver.find_element(By.NAME, "especificacao").send_keys('INSERIR REVISAO PROCESSO JUDICIAL')
        driver.find_element(By.NAME, "observacao").send_keys(str(df['OBSERVACAO'][i]))
        driver.find_element(By.NAME, "avancar").click()
        driver.find_element(By.NAME, "idImovel").send_keys(str(df['MATRICULA'][i]), Keys.ENTER)
        time.sleep(0.5)
        pyautogui.keyDown('ESC')
        pyautogui.keyUp('ESC')
        driver.find_element(By.NAME, "avancar").click()
        time.sleep(0.3)
        try:
            driver.find_element(By.XPATH, f"//*[@value='Avançar']").click()
        except NoSuchElementException:
            continue
        driver.find_element(By.NAME, "concluir").click()
        print(str(df['MATRICULA'][i]), end=',')
        txt = driver.find_element(By.CSS_SELECTOR, 'body > table:nth-child(5) > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child(1) > td:nth-child(2) > div > span').text
        num = re.findall(r'\d+', txt)
        num_ra = ' '.join(num).replace("'", '').replace('[', '').replace(']', '')

        print(str(num_ra))

login()