from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class RoboYoutube():
	def _init_(self):
		driver = webdriver.Chrome("/Users/rafaelholland/Desktop/robos/chromedriver")
