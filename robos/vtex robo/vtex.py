from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd
print("iniciando nosso robô...")
arq = "categorys.txt"



def pegarSubCategorias():
    with open(arq, 'r') as file:
        lines = [line.strip().split(';') for line in file.readlines()]
        print(lines)


pegarSubCategorias()





