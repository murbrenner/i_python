import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pyautogui
import re
from selenium.common import NoSuchElementException


df = pd.read_csv('D:\\PYTHON\\ARQUIVOS CSV\\abrirRA.csv')

driver = webdriver.Chrome()

class Login:
    def __init__(self, url):
        self.url =
