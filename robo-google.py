from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# https://chromedriver.chromium.org/downloads #
browser = webdriver.Chrome(r'C:\chromedriver.exe')

browser.get('https://www.google.com/')

# Digita a Busca #
browser.find_element_by_xpath("//input[@title='Pesquisar']").send_keys('Bill Gates')

# Faz a busca Busca #
browser.find_element_by_xpath("//input[@title='Pesquisar']").send_keys(Keys.RETURN)