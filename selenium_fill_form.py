from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

# Optional: specify path to geckodriver if not in PATH
# service = Service(executable_path="/path/to/geckodriver")
# driver = webdriver.Firefox(service=service)

driver = webdriver.Firefox()

try:
    # Step 1: Open the website
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Optional: wait for page to load
    time.sleep(2)

    # Step 2: Locate the username input by ID and enter text
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("student")

    # Step 3: Locate the password input by ID and enter text
    for number in range(100, 124):
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        print(f"Trying password Password{number}")
        password_input.send_keys(f"Password{number}")
        time.sleep(0.5)

    # Step 4: Click the submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    print("✅ Username entered successfully.")

    # Keep browser open for a bit so you can see it
    time.sleep(5)

finally:
    driver.quit()
