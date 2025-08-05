import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

# Function to calculate days until a given date
def days_until(booking_date_str):
    date_format = "%d/%m/%Y"
    booking_date = datetime.strptime(booking_date_str, date_format)
    today = datetime.today()
    return (booking_date - today).days


# List of holidays
holiday_dates = [
    "06/04/2025", "10/04/2025", "13/04/2025", "14/04/2025", "18/04/2025",
    "20/04/2025", "27/04/2025", "01/05/2025", "04/05/2025", "09/05/2025",
    "11/05/2025", "18/05/2025", "25/05/2025", "01/06/2025", "07/06/2025",
    "08/06/2025", "15/06/2025", "22/06/2025", "29/06/2025"
]


# Function to check if a given date is a holiday
def is_holiday(date_str):
    return date_str in holiday_dates


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
to_input.send_keys("Mumbai")
time.sleep(2)
to_input.send_keys(Keys.ENTER)

# Click on the date picker div
date_picker = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "labelCalendarContainer"))
)
date_picker.click()
time.sleep(2)

# Select the desired date
desired_date = "11"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//span[text()='{desired_date}']"))
).click()
time.sleep(2)

# Click the search button
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search_button")))
search_button.click()
time.sleep(5)  # Wait for the next page to load

print("Successfully navigated to the next page!")

# Wait for the bus-items container to load
bus_container = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "bus-items"))
)

# Scroll to ensure all buses are loaded
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Find all bus listings
# buses = driver.find_elements(By.XPATH, "//ul[contains(@class, 'bus-items')]/li")
# Find all bus listings
buses = bus_container.find_elements(By.TAG_NAME, "li")


# Check if buses are available
if not buses:
    print("No buses found for the selected route and date.")
else:
    date = "11/04/2025"
    journey_date = datetime.strptime(date, "%d/%m/%Y")
    is_weekday = journey_date.weekday() < 5
    is_holiday_flag = is_holiday(date)

    for bus in buses:
        try:
            # Extract bus details safely
            bus_name = bus.find_element(By.XPATH, ".//div[contains(@class, 'travels lh-24 f-bold d-color')]").text
            bus_type = bus.find_element(By.XPATH,
                                        ".//div[contains(@class, 'bus-type f-12 m-top-16 l-color evBus')]").text.lower()
            departure = bus.find_element(By.XPATH, ".//div[contains(@class, 'dp-time f-19 d-color f-bold')]").text
            arrival = bus.find_element(By.XPATH, ".//div[contains(@class, 'bp-time f-19 d-color disp-Inline')]").text
            duration = bus.find_element(By.XPATH, ".//div[contains(@class, 'dur l-color lh-24')]").text
            price = bus.find_element(By.XPATH, ".//div[contains(@class, 'fare d-block')]").text
            seats = bus.find_element(By.XPATH, ".//div[contains(@class, 'seat-left m-top-30')]").text

            print("---------------------")
            print(f"Bus Name: {bus_name}")
            print(f"Bus Type: {bus_type}")
            print(f"Departure Time: {departure}")
            print(f"Arrival Time: {arrival}")
            print(f"Journey Duration: {duration}")
            print(f"Price: {price}")
            print(f"Available Seats: {seats}")

            is_NONAC = "non-ac" in bus_type
            is_AC = not is_NONAC
            is_sleeper = "sleeper" in bus_type
            is_seater = "seater" in bus_type

            print(f"Is AC: {is_AC}")
            print(f"Is NON-AC: {is_NONAC}")
            print(f"Is Sleeper: {is_sleeper}")
            print(f"Is Seater: {is_seater}")
            print(f"Is Weekday: {is_weekday}")
            print(f"Is Weekend: {not is_weekday}")
            print(f"Is Holiday: {is_holiday_flag}")
            print(f"Days Until Booking: {days_until(date)}")
            print("---------------------")
        except Exception as e:
            print(f"Error extracting bus data: {e}")

# Keep browser open for review
time.sleep(10)

# Close the browser
driver.quit()