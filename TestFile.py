import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
time.sleep(5)

AlertWindow=driver.switch_to.alert
print(AlertWindow.text) #print Popup text
AlertWindow.send_keys("Welcome to Python")

time.sleep(5)
#AlertWindow.accept() #Close alert window by using OK button
AlertWindow.dismiss() #Close alert window by using Cancel button