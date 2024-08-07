# Selenium Registration Test Automation

This project automates the registration process on the Torjoman website using Selenium. The script interacts with various web elements, uploads a file, fills out the registration form, and verifies the process completion.

## Prerequisites

- Python 3.x
- Selenium
- PyAutoGUI
- Chrome WebDriver

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium pyautogui
    ```

3. Ensure you have the ChromeDriver executable in your PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Usage

1. Update the `main.py` script with the correct path for the file upload.

2. Run the script:
    ```sh
    python main.py
    ```

## main.py

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

driver = webdriver.Chrome()
driver.get("https://torjoman.com/quotation-test/?service_id=28")

# Select Source Language:
source_language_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='source_language_id_chosen']/a/span"))
)
source_language_dropdown.click()
time.sleep(1)

language_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='source_language_id_chosen']/div/ul"))
)
language_option.click()
time.sleep(1)

# Select Target Languages:
target_language_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='target_language_ids_chosen']/ul"))
)
target_language_dropdown.click()
time.sleep(1)

target_language_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='target_language_ids_chosen']/div/ul"))
)
target_language_option.click()
time.sleep(5)

# Enter Subject Matter:
subject_matter_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='subject_matter_id_chosen']/a/span"))
)
subject_matter_dropdown.click()
time.sleep(1)

subject_matter_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='subject_matter_id_chosen']/div/ul"))
)
subject_matter_option.click()
time.sleep(5)

# Uploading files
element_present = EC.presence_of_element_located((By.ID, "file_upload_button"))
WebDriverWait(driver, 10).until(element_present).click()

time.sleep(5)

element_present = EC.presence_of_element_located((By.CLASS_NAME, "file-upload-modal"))
WebDriverWait(driver, 10).until(element_present).click()
time.sleep(5)

pyautogui.write("C:\\Users\\soft_eng9\\Downloads\\registeration\\upload.docx")
pyautogui.press('enter')
time.sleep(30)

element_present = EC.presence_of_element_located((By.ID, "upload_done_btn"))
WebDriverWait(driver, 10).until(element_present).click()
time.sleep(5)

# Enter Your Information:
name_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='first_name']"))
)
name_input.send_keys("Abdelhamid Khamis")

company_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='prospect_type']"))
)
company_dropdown.click()

company_dropdown_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='individual']"))
)
company_dropdown_option.click()

email_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
)
email_input.send_keys("engab55k@alexu.edu.eg")

phone_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='phone']"))
)
phone_input.send_keys("01204984543")

# Submitting the Form:
show_price_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='btn_proceed_prospect']"))
)
show_price_button.click()
time.sleep(10)

# Next Page
order_now_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='btn_proceed']"))
)
order_now_button.click()
time.sleep(1)

# SignUp form
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='registration_password']"))
)
password.send_keys("AbdelhamidKhamis.8000")

confirm_password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='confirm']"))
)
confirm_password.send_keys("AbdelhamidKhamis.8000")

signup_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='btn_sign_up']"))
)
signup_button.click()
time.sleep(60)

# Getting current URL source code
title = driver.title
assert title == "Order Details"

# Printing the title of this URL
print(title)

driver.quit()
