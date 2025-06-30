from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_open_browser():
    # Open Chrome browser
   # driver = webdriver.Chrome()
    driver = webdriver.Firefox()


    # Navigate to a URL
    driver.get("https://www.google.com")

    # Wait for 2 seconds
    time.sleep(2)

    # Assert the page title contains "Google"
    assert "Google" in driver.title

    # Close the browser
    driver.quit()
