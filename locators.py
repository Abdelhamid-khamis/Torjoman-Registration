from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# create a new Chrome browser instance
driver = webdriver.Chrome()

# navigate to the webpage
driver.get("http://example.com/order_form")

# locate the source language dropdown menu
source_language_dropdown = driver.find_element(By.ID, "source_language_id")

# locate the target language dropdown menu
target_language_dropdown = driver.find_element(By.ID, "target_language_ids")

# select "Persian" from the source language dropdown menu
select_source_language = Select(source_language_dropdown)
select_source_language.select_by_value("26")

# select "English" from the target language dropdown menu
select_target_language = Select(target_language_dropdown)
select_target_language.select_by_value("2")

# add the selected languages to the summary
add_to_summary_button = driver.find_element(By.NAME, "add_to_summary")
add_to_summary_button.click()

# change the language summary
change_language_summary_button = driver.find_element(By.NAME, "change_language_summary")
change_language_summary_button.click()

# handle the change target language
handle_change_target_button = driver.find_element(By.NAME, "handle_change_target")
handle_change_target_button.click()

# close the browser
driver.quit()
