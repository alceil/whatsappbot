import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
username = 'xc9dv4d4vyb9'
password = '#Alleycafe123'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com/')
time.sleep(15)
contact = "sid"
msg = "msg by lala bot"
search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
search_box.send_keys(contact)
search_box.send_keys(Keys.ENTER)
msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
msg_box.send_keys(msg)
msg_box.send_keys(Keys.ENTER)
