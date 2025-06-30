import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.parametrize("name,email,phone,message", [
    ("John Doe", "john@example.com", "1234567890", "Hello, this is a test message."),
    ("Jane Smith", "jane@example.com", "9876543210", "Another test message."),
])
def test_form_submission(driver, name, email, phone, message):
    url = "https://www.firstbittech.com/contact"  # Replace with your form URL
    driver.get(url)

    # Fill the form
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(phone)
    driver.find_element(By.ID, "message").send_keys(message)

    # Submit form
    driver.find_element(By.ID, "submitButton").click()  # Replace with actual button ID

    # Example check: Look for a success message or thank you page
    success_element = driver.find_element(By.ID, "successMessage")  # Replace with real ID
    assert success_element.is_displayed(), "Success message not displayed after form submission"
