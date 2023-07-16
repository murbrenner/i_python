from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

filename = 'C:\\Users\\ocmvc45555\\Documents\\iMacros\\Datasources\\encerrar.csv'
df = pd.read_csv(filename)

driver = webdriver.Chrome()

driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
driver.find_element(By.NAME, 'login').send_keys('BRENNER')
driver.find_element(By.NAME, 'senha').send_keys('7355')
driver.find_element(By.NAME, 'buttonLogin').click()

for i in df.index:
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirFiltrarOrdemServicoAction.do?menu=sim")
    driver.find_element(By.NAME, 'numeroOS').send_keys(str(df['OS'][i]))
    print((str(df['OS'][i])))
    driver.find_element(By.NAME, 'periodoGeracaoInicial').send_keys('')
    driver.find_element(By.NAME, 'periodoGeracaoFinal').send_keys('')
    driver.find_element(By.XPATH, '//*[@id="formDiv"]/form/table[3]/tbody/tr/td[2]/table[3]/tbody/tr[41]/td[2]/input').click()
    driver.find_element(By.NAME, 'btnEncerrar').click()

while True:
    pass



    # driver.find_element(By.NAME, 'observacao').send_keys('TESTE - ALTERAR ESGOTO PARA FACTIVEL - TESTE')
    # driver.find_element(By.NAME, 'avancar').click()
    # driver.find_element(By.NAME, 'idImovel').send_keys(str(df['MATRICULA'][i]), Keys.ENTER)
    # driver.find_element(By.NAME, 'avancar').click()
    # driver.find_element(By.NAME, 'avancar').click()
    # driver.find_element(By.NAME, 'concluir').click()
    #         #os = (driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/div/span/text()')).text
    #         os = (driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/span')).text
    #         divide = os.split(" ")[14]
    #         print(divide)
    #     except NoSuchElementException:
    #         os = (driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table[3]/tbody/tr[1]/td[2]/span')).text
    #         #divide = os.split(" ")[14]
    #         #print(divide)
    #         print("exception handled")





    # driver.find_element(By.NAME, 'cdRotaInicial').send_keys(str(df['ROTA'][i]), Keys.ENTER)
    # driver.find_element(By.NAME, 'ordenacaoRelatorio').send_keys('R')
    # driver.find_element(By.NAME, 'concluir').click()
    # driver.find_element(By.NAME, 'botao').click()

