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
time.sleep(3)
driver.find_element_by_link_text('Ver más').click()
time.sleep(2)


driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div[1]/div/button[2]').click()
time.sleep(2)

datclase2 = driver.find_elements_by_xpath("//td[@class='td_precios categoria_precios']")
time.sleep(2)
dataclas2 = []
for dato in datclase2:
    dataclas2.append(dato.text)

dfclas2 = pd.DataFrame(dataclas2)
dfclas2.columns=['Clase']

datprec2 = driver.find_elements_by_xpath("//span[@class='entero_y_coma']")
time.sleep(4)
datprecio2 = []
for dato in datprec2:
    datprecio2.append(dato.text)

dfprecio2 = pd.DataFrame(datprecio2)

n = dfprecio2.index
par = n % 2 == 0
impar = n % 2 != 0

precionuev2 = []
for n in dfprecio2:
    precionu2 = dfprecio2.iloc[par]
    precionuev2.append(precionu2)
precionuevo2 = pd.DataFrame(np.row_stack(precionuev2))
precionuevo2.columns = ['Precio_nuevo']
precionuevo2

datcan12 = driver.find_elements_by_xpath("//td[@class='td_precios cantidad_precios']")
time.sleep(2)
datcant12 = []
for dato in datcan12:
    datcant12.append(dato.text)

cantidadnu2 = pd.DataFrame(datcant12)
cantidadnu2.columns=['Cantidad_nueva']
cantidadnu2

time.sleep(3)
driver.quit()

gc = pygsheets.authorize(service_file='creds.json')
df = pd.DataFrame()
sh = gc.open('CampoaCampo')

wks = sh[1]
cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False)
num = len(cells)

datosss = dfclas2.merge(precionuevo2,right_index=True,left_index=True)
datosss = datosss.merge(cantidadnu2,right_index=True,left_index=True)

fecha_nueva = datetime.today()
fecha_nueva = str(fecha_nueva.strftime('%d/%m/%Y'))

datosss['Fecha'] = fecha_nueva
datosss = datosss.reindex(columns=['Fecha','Clase','Precio_nuevo','Cantidad_nueva'])
datosss = datosss.rename(columns={'Precio_nuevo':'Precio_prom_sem','Cantidad_nueva':'Cantidad_acum_sem'})

datosss['Precio_prom_sem'] = datosss['Precio_prom_sem'].squeeze()

datoss2 = pd.concat([df,datosss])
datoss2

probando = datoss2.values.tolist()
wks.insert_rows(num, values=probando, inherit=True)
