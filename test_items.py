import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser):
	browser.maximize_window()
	browser.get(link)	
	'''time.sleep(30)'''
	button_basket = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
	assert button_basket, "No basket :("
	