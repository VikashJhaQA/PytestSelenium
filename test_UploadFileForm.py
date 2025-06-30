import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    #driver.quit()


@pytest.mark.parametrize("name,institution,department,course,year,email,phone,wish,about,resume_file", [
    (
            "Vikash Kumar",
            "XYZ Institute of Technology",
            "Development",
            "MCA",
            "2000",
            "vikash@example.com",
            "9876543210",
            "I want to master automation testing.",
            "I am a final year student passionate about QA.",
            "PytestQA.pdf"  # Make sure this file exists locally
    ),
])
def test_application_form(driver, name, institution, department, course, year, email, phone, wish, about, resume_file):
    url = "https://www.firstbittech.com/internship"  # Replace with your actual form URL
    driver.get(url)

    # Fill text fields
    driver.find_element(By.ID, "Name").send_keys(name)
    driver.find_element(By.ID, "NameoftheInstitution").send_keys(institution)
    driver.find_element(By.ID, "Email").send_keys(email)
    driver.find_element(By.ID, "Phone").send_keys(phone)
    driver.find_element(By.ID, "learn").send_keys(wish)
    driver.find_element(By.ID, "Writeaboutyourself").send_keys(about)

    # Select dropdowns
    Select(driver.find_element(By.ID, "DepartmentName")).select_by_visible_text(department)
    Select(driver.find_element(By.ID, "NatureOfCourses")).select_by_visible_text(course)
    Select(driver.find_element(By.ID, "year")).select_by_visible_text(year)

    # Upload resume
    if resume_file:
        file_path = os.path.abspath(r"C:\Users\Vikash Jha\Downloads\PytestQA.pdf")
        driver.find_element(By.ID, "Resumeupload").send_keys(file_path)

    # Submit form
    driver.find_element(By.ID, "Submit1").click()

    # Verify success (update locator for your form’s success element)
    success = driver.find_element(By.ID, "successMessage")
    assert success.is_displayed(), "Form submission failed or success message not shown"

#"C:\Users\Vikash Jha\Downloads\PytestQA.pdf"
#excel_file = r"C:\\Users\\Vikash Jha\\Desktop\\PythonTestReportFile\\TitleTest.xlsx"