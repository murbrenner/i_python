from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

filename = 'C:\\Users\\Murilo Brenner\\Downloads\\CREDITO - SEDUC.csv'
df = pd.read_csv(filename)

driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    for i in df.index:
        url = ("http://gsan.caema.ma.gov.br:8080/gsan/exibirFiltrarRegistroAtendimentoAction.do?menu=sim")
        driver.get(url)
        driver.find_element(By.NAME, "numeroRA").send_keys(str(df['RA'][i]), Keys.ENTER)
        print((str(df['RA'][i])), end=" ")
        play()

def play():
    try:
        driver.find_element(By.NAME, "Submit").click()
        driver.find_element(By.NAME, "ButtonEncerrar").click()
        driver.find_element(By.NAME, "motivoEncerramentoId").send_keys('CANCELADO PELA CAEMA')
        driver.find_element(By.NAME, "parecerEncerramento").send_keys('CANCELAR R.A. NAO HA DUPLICIDADE DE PAGAMENTO DO MÊS 10/2022 PARA ESTA MATRICULA')
        driver.find_element(By.NAME, "botaoConcluir").click()
        print('ENCERRADO')
    except NoSuchElementException:
        print('DEU ALGUM ERRO')

enter()

while True:
    pass

