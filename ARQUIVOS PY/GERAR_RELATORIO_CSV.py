from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

filename = 'C:\\Users\\ocmvc45555\\Documents\\iMacros\\Datasources\\gerar_relat.csv'
df = pd.read_csv(filename)

driver = webdriver.Chrome()

driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
driver.find_element(By.NAME, 'login').send_keys('BRENNER')
driver.find_element(By.NAME, 'senha').send_keys('7355')
driver.find_element(By.NAME, 'buttonLogin').click()

for i in df.index:
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirFiltrarImovelOutrosCriteriosConsumidoresInscricao.do?menu=sim&gerarRelatorio=RelatorioCadastroConsumidoresInscricao")
    driver.find_element(By.NAME, 'localidadeOrigemID').send_keys(str(df['LOCAL'][i]), Keys.ENTER)
    driver.find_element(By.NAME, 'setorComercialOrigemCD').send_keys(str(df['GRUPO'][i]), Keys.ENTER)
    driver.find_element(By.NAME, 'cdRotaInicial').send_keys(str(df['ROTA'][i]), Keys.ENTER)
    driver.find_element(By.NAME, 'ordenacaoRelatorio').send_keys('R')
    driver.find_element(By.NAME, 'concluir').click()
    driver.find_element(By.XPATH, '//*[@id="demodiv"]/table/tbody/tr[4]/td/span/input').click()
    driver.find_element(By.NAME, 'botao').click()

while True:
    pass



