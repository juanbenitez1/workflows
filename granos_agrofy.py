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
driver.get("https://news.agrofy.com.ar/granos")
time.sleep(10)

tabla = driver.find_elements_by_tag_name("td")
tab = []
for dato in tabla:
    tab.append(dato.text)
tab

time.sleep(2)
driver.find_element_by_xpath('/html/body/div/header/nav/a/div/i').click()
time.sleep(5)
dolar = driver.find_element_by_xpath("//span[@class='price']").text
dolar = dolar.replace("$ ","").replace(",",".")

desc_soja = [tab[0]+" "+tab[2],tab[18]+" "+tab[20].replace(" dispo","")]
soja_pesos = [tab[3].replace("$ ","").replace(".",""),tab[21].replace("$/ton ","").replace(".","")]
soja_fecha = [tab[5],tab[23]]
s = {'descripcion':desc_soja,'pesosxtn':soja_pesos}
soja = pd.DataFrame(data=s)
soja["tipo_cambio"] = dolar
soja["fecha"] = soja_fecha
soja["tipo_cambio"] = soja["tipo_cambio"].astype(float)
soja["pesosxtn"] = soja["pesosxtn"].astype(float)
soja['usdxtn'] = soja["pesosxtn"]/soja["tipo_cambio"]
soja["fecha"] = pd.to_datetime(soja["fecha"], format='%d/%m/%Y %H:%M:%S')
soja["fecha"] = soja["fecha"].dt.strftime('%d/%m/%Y')
print(soja['fecha'])
soja = soja.reindex(columns=['fecha','descripcion','pesosxtn','usdxtn'])

desc_maiz = [tab[36]+" "+tab[38],tab[54]+" "+tab[56].replace(" dispo","")]
maiz_pesos = [tab[39].replace("$ ","").replace(".",""),tab[57].replace("$/ton ","").replace(".","")]
maiz_fecha = [tab[41],tab[59]]
m = {'descripcion':desc_maiz,'pesosxtn':maiz_pesos}
maiz = pd.DataFrame(data=m)
maiz["tipo_cambio"] = dolar
maiz["fecha"] = maiz_fecha
maiz["tipo_cambio"] = maiz["tipo_cambio"].astype(float)
maiz["pesosxtn"] = maiz["pesosxtn"].astype(float)
maiz['usdxtn'] = maiz["pesosxtn"]/maiz["tipo_cambio"]
maiz["fecha"] = pd.to_datetime(maiz["fecha"], format='%d/%m/%Y %H:%M:%S')
maiz["fecha"] = maiz["fecha"].dt.strftime('%d/%m/%Y')
maiz = maiz.reindex(columns=['fecha','descripcion','pesosxtn','usdxtn'])

desc_trigo = [tab[72]+" "+tab[74],tab[90]+" "+tab[92].replace(" dispo","")]
trigo_pesos = [tab[75].replace("$ ","").replace(".",""),tab[93].replace("$/ton ","").replace(".","")]
trigo_fecha = [tab[77],tab[95]]
t = {'descripcion':desc_trigo,'pesosxtn':trigo_pesos}
trigo = pd.DataFrame(data=t)
trigo["tipo_cambio"] = dolar
trigo["fecha"] = trigo_fecha
trigo["tipo_cambio"] = trigo["tipo_cambio"].astype(float)
if trigo["pesosxtn"][0] != 'S/C':
    trigo["pesosxtn"] = trigo["pesosxtn"].astype(float)
    trigo['usdxtn'] = trigo["pesosxtn"]/trigo["tipo_cambio"]
else:
    trigo["pesosxtn"] = 'N/D'
    trigo['usdxtn'] = 'N/D'
trigo["fecha"] = pd.to_datetime(trigo["fecha"], format='%d/%m/%Y %H:%M:%S')
trigo["fecha"] = trigo["fecha"].dt.strftime('%d/%m/%Y')
trigo = trigo.reindex(columns=['fecha','descripcion','pesosxtn','usdxtn'])


granos = pd.concat([maiz,soja,trigo])
granos['fecha'] = granos['fecha'].astype(str)
granos = granos[granos['descripcion'].str.contains('FAS') == False]

time.sleep(0.5)
driver.quit()

gc = pygsheets.authorize(service_file='creds.json')
df = pd.DataFrame()
sh = gc.open('CampoaCampo')

wks = sh[4]
cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False)
num = len(cells)

granos1 = pd.concat([df,granos])
granos1

probando = granos1.values.tolist()
wks.insert_rows(num, values=probando, inherit=True)
