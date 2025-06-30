#
# import pytest
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# #driver= webdriver.Chrome()
# #driver.get("https://opensource-demo.orangehrmlive.com/")
# driver = webdriver.Firefox()
#
# driver.get("https://www.dictaai.com/account/")
# driver.find_element(By.ID,"ContentPlaceHolder1_Clientlogin_txtemail").send_keys("vikash@gmrwebteam.com")
# driver.find_element(By.ID,"ContentPlaceHolder1_Clientlogin_txtpwd").send_keys("Asdf@123")
# driver.find_element(By.ID,"ContentPlaceHolder1_Clientlogin_Signin").click()
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()  # Adjust if using another browser
    driver.implicitly_wait(5)  # Optional: wait up to 5s for elements
    yield driver
    driver.quit()

def test_login(driver):
    url = "https://www.dictaai.com/account/"  # Replace with your login URL
    driver.get(url)

    # Locate username and password fields and login button
    driver.find_element(By.ID,"ContentPlaceHolder1_Clientlogin_txtemail").send_keys("vikash@gmrwebteam.com")
    driver.find_element(By.ID,"ContentPlaceHolder1_Clientlogin_txtpwd").send_keys("Asdf@123")
    driver.find_element(By.ID,"ContentPlaceHolder1_Clientlogin_Signin").click()

    # Verify login success, example: check URL or element
    assert "home" in driver.current_url #or driver.find_element(By.ID, "logoutButton"), "Login failed"
