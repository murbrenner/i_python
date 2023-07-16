import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import pyautogui
from selenium.common import NoSuchElementException

filename = 'D:\\teste.csv'
df = pd.read_csv(filename)

driver = webdriver.Chrome()

def login():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirInserirRegistroAtendimentoAction.do?menu=sim")
        driver.find_element(By.NAME, "tipoSolicitacao").send_keys("ATENDIMENTO RAPIDO")
        driver.find_element(By.NAME, "especificacao").send_keys("COMENTARIO")
        driver.find_element(By.NAME, "observacao").send_keys(str(df['OBSERVACAO'][i]))
        driver.find_element(By.NAME, "avancar").click()
        driver.find_element(By.NAME, "idImovel").send_keys(str(df['MATRICULA'][i]), Keys.ENTER)
        pyautogui.press('esc')
        pyautogui.keyUp('esc')
        driver.find_element(By.NAME, "avancar").click()
        try:
            driver.find_element(By.CSS_SELECTOR, ".centercoltext > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > input:nth-child(1)").click()
        except NoSuchElementException:
            driver.find_element(By.NAME, "avancar").click()
            driver.find_element(By.NAME, 'concluir').click()
            retorno = driver.find_element(By.CSS_SELECTOR, ".centercoltext > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text
            retorno1 = re.sub('[^0-9]', '', retorno)
            print((str(df['MATRICULA'][i])), end=',')
            print(("R.A:"), retorno1)

login()

while True:
    pass