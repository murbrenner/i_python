from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

df = pd.read_csv('E:\\PYTHON\\ARQUIVOS CSV\\teste.csv')

driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirConsultarImovelAction.do?menu=sim")
        driver.find_element(By.ID, '1').click()
        driver.find_element(By.NAME, "idImovelDadosCadastrais").send_keys(str(df['MATRICULA'][i]), Keys.ENTER)
        txt = driver.find_element(By.NAME, "tipoHabitacaoDadosCadastrais").get_attribute('value')
        # #txt = driver.find_element(By.NAME, "tipoHabitacaoDadosCadastrais").text
        # driver.find_element(By.NAME, "idOrdemServico").send_keys(str(df['OS'][i]), Keys.ENTER)
        print((str(df['MATRICULA'][i])), end=" ")
        print((str(txt)))
        # play()

# def play():
#     try:
#         driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[2]/td/strong[2]/input[2]").click()
#         driver.find_element(By.NAME, "situacaoLigacaoEsgotoNova").send_keys('FACTIVEL')
#         driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[5]/td/table/tbody/tr/td[2]/input").click()
#         print('Alterado')
#     except NoSuchElementException:
#         print('Inalterado')

enter()

while True:
    pass

