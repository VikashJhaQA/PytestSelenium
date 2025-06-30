import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Provide multiple sets of username/password
@pytest.mark.parametrize("username,password", [
    ("vikash@gmrwebteam.com", "Asdf@123"),
    ("skumar+789@gmrwebteam.com", "Asdf@123455"),
    ("vi@gmrwebteam.com", "Asdf@123"),
])
def test_login(driver, username, password):
    url = "https://www.dictaai.com/account/"  # Replace with your actual login URL
    driver.get(url)

    # Locate and interact with elements
    driver.find_element(By.ID, "ContentPlaceHolder1_Clientlogin_txtemail").send_keys(username)
    driver.find_element(By.ID, "ContentPlaceHolder1_Clientlogin_txtpwd").send_keys(password)
    driver.find_element(By.ID, "ContentPlaceHolder1_Clientlogin_Signin").click()

    # Example check: If valid, dashboard appears, else error message
    if "valid" in username:
        assert "home" in driver.current_url, f"Login failed for valid user: {username}"
    else:
        # Check for error message element or no dashboard redirect
        assert "dashboard" not in driver.current_url, f"Invalid user {username} should not log in"
