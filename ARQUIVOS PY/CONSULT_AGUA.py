from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

#df = pd.read_csv('C:\\Users\\ocmvc45555\\Documents\\iMacros\\Datasources\\visu.csv')
df = pd.read_csv('G:\\teste.csv')

driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        url = ("http://gsan.caema.ma.gov.br:8080/gsan/exibirConsultarImovelAction.do?menu=sim")
        driver.get(url)
        driver.find_element(By.ID, "1").click()
        driver.find_element(By.NAME, "idImovelDadosCadastrais").send_keys(str(df['MATRICULA'][i]), Keys.ENTER)
        agua = driver.find_element(By.NAME, "situacaoAguaDadosCadastrais").get_attribute('value')
        print((str(df['MATRICULA'][i])), end=" "), print((str(agua)))

enter()

while True:
    pass