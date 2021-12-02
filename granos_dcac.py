from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from openpyxl import load_workbook
import time
import datetime
from datetime import datetime, timedelta
import pandas as pd
from selenium.webdriver.support.ui import Select
import numpy as np
import pandas as pd
import gspread
import df2gspread as d2g
import pygsheets

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.decampoacampo.com/__dcac/")
time.sleep(3)

mail = 'jpbenitez1997@gmail.com'
contraseña = 'Juan40044678'

driver.find_element_by_id("btn_login").click()
time.sleep(0.25)
driver.find_element_by_id("maillog").send_keys(mail)
time.sleep(0.25)
driver.find_element_by_id("password").send_keys(contraseña)
time.sleep(0.25)
driver.find_element_by_id("ingresar_login").click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/span/a[3]/span/span').click()
time.sleep(3)

denom = driver.find_elements_by_xpath("//td[@data-label='Categoria']")
time.sleep(2)
datadenom = []
for dato in denom:
    datadenom.append(dato.text)

dfdenom = pd.DataFrame(datadenom)
dfdenom.columns=['Denominacion']
dfdenom 

