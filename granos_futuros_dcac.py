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

driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
driver.get("https://www.decampoacampo.com/__dcac/")
time.sleep(3)

mail = 'jpbenitez1997@gmail.com'
contraseña = 'Juan40044678'

driver.find_element_by_id("btn_login").click()
time.sleep(2)
driver.find_element_by_id("maillog").send_keys(mail)
time.sleep(2)
driver.find_element_by_id("password").send_keys(contraseña)
time.sleep(2)
driver.find_element_by_id("ingresar_login").click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/span/a[3]/span/span').click()
time.sleep(30)

denom = driver.find_elements_by_xpath("//td[@data-label='Categoria']")
time.sleep(20)
datadenom = []
for dato in denom:
    datadenom.append(dato.text)

dfdenom = pd.DataFrame(datadenom)
dfdenom.columns = ['Denominacion']

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

dfprecioxtn = pd.DataFrame(dats)

maiz = dfdenom.merge(dfprecioxtn,right_index=True,left_index=True)
maiz.columns = ['Denominacion','Precio']

driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/button[2]').click()
time.sleep(5)

denom1 = driver.find_elements_by_xpath("//td[@data-label='Categoria']")
time.sleep(2)
datadenom1 = []
for dato in denom1:
    datadenom1.append(dato.text)

dfdenom1 = pd.DataFrame(datadenom1)
dfdenom1.columns=['Denominacion']

datprecxtn11 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]")
datprecxtn21 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
datprecxtn31 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]")
datprecxtn41 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[4]/td[2]")
datprecxtn51 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[5]/td[2]")
datprecxtn61 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[6]/td[2]")
datprecxtn71 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[7]/td[2]")
datprecxtn81 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[8]/td[2]")
datprecxtn91 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[9]/td[2]")

time.sleep(4)

datpxt11 = []
for dato in datprecxtn11:
    datpxt11.append(dato.text)

datpxt21 = []
for dato in datprecxtn21:
    datpxt21.append(dato.text)

datpxt31 = []
for dato in datprecxtn31:
    datpxt31.append(dato.text)

datpxt41 = []
for dato in datprecxtn41:
    datpxt41.append(dato.text)
    
datpxt51 = []
for dato in datprecxtn51:
    datpxt51.append(dato.text)
    
datpxt61 = []
for dato in datprecxtn61:
    datpxt61.append(dato.text)
    
datpxt71 = []
for dato in datprecxtn71:
    datpxt71.append(dato.text)
    
datpxt81 = []
for dato in datprecxtn81:
    datpxt81.append(dato.text)
    
datpxt91 = []
for dato in datprecxtn91:
    datpxt91.append(dato.text)

dats1 = datpxt11,datpxt21,datpxt31,datpxt41,datpxt51,datpxt61,datpxt71,datpxt81,datpxt91

dfprecioxtn1 = pd.DataFrame(dats1)

soja = dfdenom1.merge(dfprecioxtn1,right_index=True,left_index=True)
soja.columns = ['Denominacion','Precio']

driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/button[3]').click()
time.sleep(5)

denom11 = driver.find_elements_by_xpath("//td[@data-label='Categoria']")
time.sleep(2)

datadenom11 = []
for dato in denom11:
    datadenom11.append(dato.text)

dfdenom11 = pd.DataFrame(datadenom11)
dfdenom11.columns=['Denominacion']

datprecxtn111 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]")
datprecxtn211 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[2]")
datprecxtn311 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[3]/td[2]")
datprecxtn411 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[4]/td[2]")
datprecxtn511 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[5]/td[2]")
datprecxtn611 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[6]/td[2]")
datprecxtn711 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[7]/td[2]")
datprecxtn811 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[8]/td[2]")
datprecxtn911 = driver.find_elements_by_xpath("/html/body/div[6]/div/div[2]/div/div/div[2]/table/tbody/tr[9]/td[2]")

time.sleep(4)

datpxt111 = []
for dato in datprecxtn111:
    datpxt111.append(dato.text)

datpxt211 = []
for dato in datprecxtn211:
    datpxt211.append(dato.text)

datpxt311 = []
for dato in datprecxtn311:
    datpxt311.append(dato.text)

datpxt411 = []
for dato in datprecxtn411:
    datpxt411.append(dato.text)
    
datpxt511 = []
for dato in datprecxtn511:
    datpxt511.append(dato.text)
    
datpxt611 = []
for dato in datprecxtn611:
    datpxt611.append(dato.text)
    
datpxt711 = []
for dato in datprecxtn711:
    datpxt711.append(dato.text)
    
datpxt811 = []
for dato in datprecxtn811:
    datpxt811.append(dato.text)
    
datpxt911 = []
for dato in datprecxtn911:
    datpxt911.append(dato.text)

dats11 = datpxt111,datpxt211,datpxt311,datpxt411,datpxt511,datpxt611,datpxt711,datpxt811,datpxt911

dfprecioxtn11 = pd.DataFrame(dats11)

trigo = dfdenom11.merge(dfprecioxtn11,right_index=True,left_index=True)
trigo.columns = ['Denominacion','Precio']

granos = pd.concat([maiz,soja,trigo])

fecha = datetime.today()
fecha = str(fecha.strftime('%d/%m/%Y'))

granos['Fecha'] = fecha
granos = granos.reindex(columns=['Fecha','Denominacion','Precio'])
granos['Precio'] = granos['Precio'].squeeze()
granos['Precio'] = granos['Precio'].map(lambda x: str(x).replace(',','.')).astype(float)

time.sleep(0.5)
driver.quit()

gc = pygsheets.authorize(service_file='creds.json')
df = pd.DataFrame()
sh = gc.open('CampoaCampo')

wks = sh[2]
cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False)
num = len(cells)

granos1 = pd.concat([df,granos])
granos1

probando = granos1.values.tolist()
wks.insert_rows(num, values=probando, inherit=True)
