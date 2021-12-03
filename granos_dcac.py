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

datprecxtn1 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]")
datprecxtn2 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
datprecxtn3 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]")
datprecxtn4 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[4]/td[2]")
datprecxtn5 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[5]/td[2]")
datprecxtn6 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[6]/td[2]")
datprecxtn7 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[7]/td[2]")
datprecxtn8 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[8]/td[2]")
datprecxtn9 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[9]/td[2]")

time.sleep(4)

datpxt1 = []
for dato in datprecxtn1:
    datpxt1.append(dato.text)
datpxt1

datpxt2 = []
for dato in datprecxtn2:
    datpxt2.append(dato.text)

datpxt3 = []
for dato in datprecxtn3:
    datpxt3.append(dato.text)

datpxt4 = []
for dato in datprecxtn4:
    datpxt4.append(dato.text)
    
datpxt5 = []
for dato in datprecxtn5:
    datpxt5.append(dato.text)
    
datpxt6 = []
for dato in datprecxtn6:
    datpxt6.append(dato.text)
    
datpxt7 = []
for dato in datprecxtn7:
    datpxt7.append(dato.text)
    
datpxt8 = []
for dato in datprecxtn8:
    datpxt8.append(dato.text)
    
datpxt9 = []
for dato in datprecxtn9:
    datpxt9.append(dato.text)

dats = datpxt1,datpxt2,datpxt3,datpxt4,datpxt5,datpxt6,datpxt7,datpxt8,datpxt9
dats

dfprecioxtn = pd.DataFrame(dats)
dfprecioxtn

maiz = dfdenom.merge(dfprecioxtn,right_index=True,left_index=True)
maiz.columns = ['Denominacion','Precio']

driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/button[2]').click()
time.sleep(5)


