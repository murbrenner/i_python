from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

df = pd.read_csv('C:\\Users\\ocmvc45555\\Documents\\iMacros\\Datasources\\visu.csv')

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
        driver.find_element(By.NAME, "idImovelDebitos").send_keys(str(df['MAT'][i]), Keys.ENTER)
        try:
            txt1 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td[5]/font/a/font").text
            txt2 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[5]/font/a/font").text
            txt3 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td[5]/font/a/font").text
            "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td[5]/font/a/font"
            print((str(df['MAT'][i])), end=" ")
            print((str(txt1)), end=" ")
            print((str(txt2)), end=" ")
            print((str(txt3)))

        except NoSuchElementException:
            try:
                txt1 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td[5]/font/a/font").text
                txt2 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[5]/font/a/font").text
                print((str(df['MAT'][i])), end=" ")
                print((str(txt1)), end=" ")
                print((str(txt2)))

            except NoSuchElementException:
                try:
                    txt2 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr[1]/td[5]/font/a/font").text
                    txt3 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td[5]/font/a/font").text
                    print((str(df['MAT'][i])), end=" ")
                    print((str(txt2)), end=" ")
                    print((str(txt3)))
                except NoSuchElementException:
                    try:
                        txt3 = driver.find_element(By.XPATH, "/html/body/form/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td[5]/font/a/font").text
                        print((str(df['MAT'][i])), end=" ")
                        print((str(txt3)))
                    except NoSuchElementException:
                        print((str(df['MAT'][i])), end=" ")
                        print("NONE")


enter()

while True:
    pass