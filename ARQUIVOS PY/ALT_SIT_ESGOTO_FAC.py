from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

df = pd.read_csv('C:\\Users\\ocmvc45555\\Documents\\iMacros\\Datasources\\alterar-sit-esg.csv')

driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('MARCO')
    driver.find_element(By.NAME, 'senha').send_keys('2323')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        url = ("http://gsan.caema.ma.gov.br:8080/gsan/exibirAlterarSituacaoLigacaoAction.do?menu=sim")
        driver.get(url)
        driver.find_element(By.NAME, "idOrdemServico").send_keys(str(df['OS'][i]), Keys.ENTER)
        print((str(df['MATRICULA'][i])), end=" ")
        play()

def play():
    try:
        driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[2]/td/strong[2]/input[2]").click()
        driver.find_element(By.NAME, "situacaoLigacaoEsgotoNova").send_keys('FACTIVEL')
        driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[5]/td/table/tbody/tr/td[2]/input").click()
        print('Alterado')
    except NoSuchElementException:
        print('Inalterado')

enter()

while True:
    pass

