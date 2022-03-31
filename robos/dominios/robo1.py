from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd
print("iniciando nosso robô...")
arq = open("resultado.txt", "w")
dominios = []
#Lendo Excel
workbook = xlrd.open_workbook('dominios.xlsx')
sheet = workbook.sheet_by_index(0)

for linha in range(0,8):
	dominios.append(sheet.cell_value(linha,0))

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get('https://registro.br')



for dominio in dominios:
	pesquisa = driver.find_element_by_id("is-avail-field")
	pesquisa.clear() #Limpando a barra de pesquisa
	pesquisa.send_keys(dominio)
	pesquisa.send_keys(Keys.RETURN)
	time.sleep(2)
	resultados = driver.find_elements_by_tag_name("strong")
	texto = ("Domínio %s %s\n" % (dominio, resultados[4].text))
	arq.write(texto)

arq.close()
time.sleep(5) #Dormindo
driver.close()

