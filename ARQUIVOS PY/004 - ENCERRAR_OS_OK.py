from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.common import NoSuchElementException

df = pd.read_csv("C:\\Users\\cereb\\OneDrive\\Área de Trabalho\\PLANILHA.csv")
driver = webdriver.Chrome()

def enter():
    driver.get("http://gsan.caema.ma.gov.br:8080/gsan")
    driver.find_element(By.NAME, 'login').send_keys('BRENNER')
    driver.find_element(By.NAME, 'senha').send_keys('7355')
    driver.find_element(By.NAME, 'buttonLogin').click()
    begin()

def begin():
    hoje = date.today()
    formatted_date = hoje.strftime("%d/%m/%Y")
    hoje = formatted_date
    motivo = "CONCLUSAO DO SERVICO"

    for i in df.index:
        driver.get("http://gsan.caema.ma.gov.br:8080/gsan/exibirFiltrarOrdemServicoAction.do?menu=sim")
        os = driver.find_element(By.NAME, "numeroOS").send_keys(str(df['OS'][i]), Keys.ENTER)
        print(str(df['OS'][i]), end=',')
        driver.find_element(By.XPATH, "//input[@value='Filtrar']").click()
        driver.find_element(By.XPATH, "//input[@value='Encerrar']").click()
        driver.find_element(By.NAME, "dataEncerramento").send_keys(hoje)
        driver.find_element(By.NAME, "idMotivoEncerramento").send_keys(motivo)
        driver.find_element(By.NAME, "observacaoEncerramento").send_keys(str(df['PARECER'][i]))
        driver.find_element(By.NAME, "ButtonAtividade").click()
        main_window_handle = driver.current_window_handle
        all_window_handles = driver.window_handles
        for handle in all_window_handles:
            if handle != main_window_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table[3]/tbody/tr[9]/td/table[2]/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr/td[4]/a/img').click()
                time.sleep(0.5)
                driver.find_element(By.NAME, 'horaInicioExecucao').send_keys("0800")
                driver.find_element(By.NAME, 'horaFimExecucao').send_keys("1800")
                driver.find_element(By.NAME, "idEquipeProgramada").send_keys("CAEMA CADASTRO-SEDE")
                driver.find_element(By.XPATH, "//input[@value='Adicionar']").click()
                driver.find_element(By.XPATH, "//input[@value='Voltar']").click()
                driver.find_element(By.XPATH, "//input[@value='Inserir']").click()
                print("ATIVIDADE INSERIDA")
        driver.switch_to.window(main_window_handle)
        driver.find_element(By.NAME, "ButtonEncerrar").click()
        print("OS {} ENCERRADA")
        try:
            driver.find_element(By.XPATH, "//input[@value='Cancelar']").click()
            driver.find_element(By.XPATH, "//input[@value='Voltar']").click()
            driver.find_element(By.XPATH, "//input[@value='ButtonCancelar']").click()
            driver.find_element(By.XPATH, "//input[@value='ButtonVoltar']").click()
        except NoSuchElementException:
            pass

enter()