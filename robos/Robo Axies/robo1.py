# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("iniciando nosso robô...")
arq = open("resultado.txt", "w")

driver = webdriver.Chrome("/Users/rafaelholland/Desktop/robos/chromedriver")
driver.get('https://marketplace.axieinfinity.com/axie?class=Aquatic&part=tail-nimo&pureness=6&breedCount=0&breedCount=0')
time.sleep(5)
pesquisa = driver.find_element_by_id("is-avail-field")

print(pesquisa)

arq.close()
time.sleep(5) #Dormindo
driver.close()

