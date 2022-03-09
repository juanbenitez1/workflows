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

mail = 'omarszampaca@gmail.com'
contraseña = '15_Chapu'

driver.find_element_by_id("btn_login").click()
time.sleep(2)
driver.find_element_by_id("maillog").send_keys(mail)
time.sleep(2)
driver.find_element_by_id("password").send_keys(contraseña)
time.sleep(2)
driver.find_element_by_id("ingresar_login").click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="submenu_desplegable_2"]/a[2]').click()
time.sleep(4)

data_maiz_usd = driver.find_elements_by_tag_name('td')
dmu = []
for d in data_maiz_usd:
    dmu.append(d.text)
desc_m = [dmu[0],dmu[4]]
prec_m_usd = [dmu[1],dmu[5]]
time.sleep(2)
driver.find_element_by_xpath('//*[@id="vue-app"]/div/div[2]/div[1]/div[2]/span/button[1]').click()
data_maiz_pes = driver.find_elements_by_tag_name('td')
dmp = []

for d in data_maiz_pes:
    dmp.append(d.text)
prec_m_pes = [dmp[1],dmp[5]]

time.sleep(5)

driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/button[2]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/span/button[2]").click()
time.sleep(4)

data_soja_usd = driver.find_elements_by_tag_name('td')
time.sleep(5)
dsu = []

for d in data_soja_usd:
    dsu.append(d.text)
desc_s = [dsu[0],dsu[4]]
prec_s_usd = [dsu[1],dsu[5]]
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/span/button[1]').click()
data_soja_pes = driver.find_elements_by_tag_name('td')
dsp = []

for d in data_soja_pes:
    dsp.append(d.text)
prec_s_pes = [dsp[1],dsp[5]]
        
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/button[3]").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/span/button[2]").click()
time.sleep(5)

data_trigo_usd = driver.find_elements_by_tag_name('td')
time.sleep(5)
dtu = []
for d in data_trigo_usd:
    dtu.append(d.text)
desc_t = [dtu[0],dtu[8]]
prec_t_usd = [dtu[1],dtu[9]]
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/span/button[1]').click()
data_trigo_pes = driver.find_elements_by_tag_name('td')
dtp = []

for d in data_trigo_pes:
    dtp.append(d.text)
prec_t_pes = [dtp[1],dtp[9]]

m = {'descripcion':desc_m,'pesosxtn':prec_m_pes,'usdxtn':prec_m_usd}
maiz = pd.DataFrame(data=m)

s = {'descripcion':desc_s,'pesosxtn':prec_s_pes,'usdxtn':prec_s_usd}
soja = pd.DataFrame(data=s)

t = {'descripcion':desc_t,'pesosxtn':prec_t_pes,'usdxtn':prec_t_usd}
trigo = pd.DataFrame(data=t)

granos = pd.concat([maiz,soja,trigo])

fecha = datetime.today()
fecha = str(fecha.strftime('%d/%m/%Y'))

granos['Fecha'] = fecha
granos = granos.reindex(columns=['Fecha','descripcion','pesosxtn','usdxtn'])

granos['usdxtn'] = granos['usdxtn'].squeeze()
granos['usdxtn'] = granos['usdxtn'].map(lambda x: str(x).replace(',','.'))
granos['usdxtn'] = pd.to_numeric(granos['usdxtn'], downcast='float', errors='coerce')
granos['usdxtn'] = granos['usdxtn'].apply(lambda x: round(x, 1) if type(x) is float else x)

granos['pesosxtn'] = granos['pesosxtn'].squeeze()
granos['pesosxtn'] = granos['pesosxtn'].map(lambda x: str(x).replace('.',''))
granos['pesosxtn'] = pd.to_numeric(granos['pesosxtn'], downcast='float', errors='coerce')
granos['pesosxtn'] = granos['pesosxtn'].apply(lambda x: round(x, 0) if type(x) is float else x)

try:
    granos['tipo_cambio'] = granos['pesosxtn']/granos['usdxtn']
    granos['tipo_cambio'] = granos['tipo_cambio']
except:
    granos['tipo_cambio'] = 'N/D'

time.sleep(5)
driver.quit()

gc = pygsheets.authorize(service_file='creds.json')
df = pd.DataFrame()
sh = gc.open('CampoaCampo')

wks = sh[3]
cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False)
num = len(cells)

granos1 = pd.concat([df,granos])
granos1

probando = granos1.values.tolist()
wks.insert_rows(num, values=probando, inherit=True)
