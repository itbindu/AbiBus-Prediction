import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.redbus.in/")
time.sleep(3)  # Allow page to load

# Enter 'From' location
from_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "src")))
from_input.send_keys("Hyderabad")
time.sleep(2)
from_input.send_keys(Keys.ENTER)

# Enter 'To' location
to_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "dest")))
to_input.send_keys("Goa")
time.sleep(2)
to_input.send_keys(Keys.ENTER)

# Click on the date picker div
date_picker = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "labelCalendarContainer"))
)
date_picker.click()
time.sleep(2)

# Select the desired date (e.g., 5th of the month)
desired_date = "5"  # Change this to your preferred date
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//span[text()='{desired_date}']"))
).click()
time.sleep(2)

# Click the search button
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search_button")))
search_button.click()
time.sleep(5)  # Wait for the next page to load

print("Successfully navigated to the next page!")

# Keep the browser open for some time (optional)
time.sleep(10)

# Close the browser
driver.quit()
