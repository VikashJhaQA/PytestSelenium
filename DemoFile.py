
#webdriver is module
from selenium import webdriver
from selenium.webdriver.common.by import By

#driver= webdriver.Chrome()
#driver.get("https://opensource-demo.orangehrmlive.com/")
driver = webdriver.Firefox()

driver.get("https://profile.w3schools.com/")

driver.find_element(By.NAME,"email").send_keys("vikash@gmrwebteam.com")
driver.find_element(By.NAME,"current-password").send_keys("Asdf@1234")
driver.find_element(By.XPATH,"//button[@class='Button_button__URNp+ Button_primary__d2Jt3 Button_fullwidth__0HLEu']").click()


#driver.title

driver.maximize_window() #maximize window
#driver.close() #quit()- for all windows
