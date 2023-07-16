import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

df = pd.read_csv('F:\\ATUALIZACAO.csv')

driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        #PREENCHER TUDO
        driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirConsultarImovelAction.do?menu=sim")
        driver.find_element(By.ID, '1').click()
        driver.find_element(By.NAME, "idImovelDadosCadastrais").send_keys(str(df['MATRICULA'][i]), Keys.ENTER)
        try:
            driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/a/strong").click()
        except NoSuchElementException:
            driver.find_element(By.CSS_SELECTOR, "body > form > table:nth-child(10) > tbody > tr > td.centercoltext > table:nth-child(4) > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td > a > strong").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/form/table[3]/tbody/tr/td[2]/table[4]/tbody/tr[2]/td[2]/a[2]/img").click()
        driver.find_element(By.NAME, "idLocalidade").click()
        driver.find_element(By.NAME, "idLocalidade").send_keys(str(df['LOCALIDADE'][i]), Keys.ENTER)
        driver.find_element(By.XPATH, "/html/body/div[1]/form/table[3]/tbody/tr/td[2]/table[4]/tbody/tr[3]/td[2]/a[2]/img").click()
        driver.find_element(By.NAME, "idSetorComercial").click()
        driver.find_element(By.NAME, "idSetorComercial").send_keys(str(df['SETOR'][i]), Keys.ENTER)
        driver.find_element(By.XPATH, "/html/body/div[1]/form/table[3]/tbody/tr/td[2]/table[4]/tbody/tr[4]/td[2]/a[2]/img").click()
        driver.find_element(By.NAME, "idQuadra").click()
        driver.find_element(By.NAME, "idQuadra").send_keys(str(df['QUADRA'][i]), Keys.ENTER)

        driver.find_element(By.NAME, "lote").click()
        driver.find_element(By.NAME, "lote").clear()
        driver.find_element(By.NAME, "lote").send_keys(str(df['SEQUENCIA'][i]), Keys.ENTER)

        driver.find_element(By.NAME, "subLote").clear()
        driver.find_element(By.NAME, "subLote").send_keys("000")

        driver.find_element(By.NAME, "testadaLote").clear()
        driver.find_element(By.NAME, "testadaLote").send_keys(str(df['TESTADA'][i]), Keys.ENTER)

        driver.find_element(By.NAME, "sequencialRota").clear()
        driver.find_element(By.NAME, "sequencialRota").send_keys(str(df['SEQUENCIA'][i]), Keys.ENTER)

        #AVANÇAR
        driver.find_element(By.NAME, "avancar").click()
        #time.sleep(60)

        try:
            driver.find_element(By.NAME, "confirmar").click()
        except NoSuchElementException:
            driver.find_element(By.NAME, "avancar").click()
            try:
                driver.find_element(By.NAME, "voltar").click()
            except NoSuchElementException:
                print("DEU ERRO")
                continue


        driver.find_element(By.NAME, "concluir").click()
        print((str(df['MATRICULA'][i])), end=',')
        print("CODIFICACAO ALTERADA")
        try:
            driver.find_element(By.NAME, "cancelar").click()
        except NoSuchElementException:
            continue





enter()

while True:
    pass

