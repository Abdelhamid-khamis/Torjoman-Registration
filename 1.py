from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import os

class Torjoman():

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_website(self):
        self.driver.get("https://torjoman.com/quotation-test/?service_id=28")

    def select_service_type(self, service_type):
        try:
            service_type_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'service-item') and contains(., '{service_type}')]"))
            )
            service_type_element.click()
        except TimeoutException:
            print(f"Service type '{service_type}' not found.")




    def select_source_language(self, source_language):
        try:

            source_language_dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Source Language *']"))
            )
            source_language_dropdown.click()
            time.sleep(1)
            language_option = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//li[contains(text(), '{source_language}')]"))
            )
            language_option.click()
            

        except TimeoutException:
            print(f"Source language '{source_language}' not found.")

    def select_target_languages(self, target_languages):
        try:
            target_languages_dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Target Languages *']"))
            )
            target_languages_dropdown.click()
            time.sleep(1)
            for language in target_languages:
                language_option = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//li[contains(text(), '{language}')]"))
                )
                language_option.click()
        except TimeoutException:
            print(f"Target language '{target_languages}' not found.")

    def enter_subject_matter(self, subject_matter):
        try:
            subject_matter_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Subject Matter']"))
            )
            subject_matter_input.send_keys(subject_matter)
        except TimeoutException:
            print(f"Subject matter input not found.")

    def enter_word_count(self, word_count):
        try:
            word_count_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Word Count *']"))
            )
            word_count_input.send_keys(word_count)
        except TimeoutException:
            print(f"Word count input not found.")

    def upload_files(self, file_paths):
        try:
            upload_button = WebDriverWait(self.driver, 10).until(
                # EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Upload Files')]"))
                EC.presence_of_element_located((By.ID,"file_upload_button"))
            )
            upload_button.click()
            time.sleep(1)
            for file_path in file_paths:
                self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
        except TimeoutException:
            print(f"Upload files button not found.")

    def enter_name(self, name):
        try:
            name_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name *']"))
            )
            name_input.send_keys(name)
        except TimeoutException:
            print(f"Name input not found.")

    def enter_email(self, email):
        try:
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E-mail *']"))
            )
            email_input.send_keys(email)
        except TimeoutException:
            print(f"Email input not found.")

    def enter_company_name(self, company_name):
        try:
            company_name_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Company name *']"))
            )
            company_name_input.send_keys(company_name)
        except TimeoutException:
            print(f"Company name input not found.")

    def get_quote(self):
        try:
            show_price_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Show Price')]"))
            )
            show_price_button.click()
            time.sleep(2)  # Allow time for the quote to load
            # Extract and return the quote details (e.g., price, delivery time)
            # ...
        except TimeoutException:
            print("Show Price button not found.")

    def close_browser(self):
        self.driver.close()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    torjoman_bot = Torjoman(driver)

    torjoman_bot.navigate_to_website()

    # Example usage:
    # torjoman_bot.select_service_type("Translation")
    # torjoman_bot.select_source_language("English")
    # torjoman_bot.select_target_languages("Persian")
    torjoman_bot.enter_subject_matter("Consumer Electronics")
    torjoman_bot.enter_word_count("1000")
    torjoman_bot.upload_files(["upload.docx", "upload.pdf"])
    torjoman_bot.enter_name("Abdelhamid Khamis")
    torjoman_bot.enter_email("abdelhameedkhamis50@alexu.edu.eg")
    torjoman_bot.enter_company_name("Future Group.")

    # torjoman_bot.get_quote()

    # torjoman_bot.close_browser()