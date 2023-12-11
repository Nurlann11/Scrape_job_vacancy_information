# Import necessary libraries
import time
import csv
import psutil   # for measuring memory usage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Set up the Firefox webdriver
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)  # Set implicit wait time for 30 seconds
driver.get('https://browser.az/vakansiyalar/')
time.sleep(2)  # Wait for 2 seconds to allow the page to load

# Define a function to write a vacancy to a CSV file
def write_to_csv(vacancy):
    with open("vacancy_browser.csv", "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=vacancy.keys())
        if csv_file.tell() == 0:  # Check if the file is empty
            writer.writeheader()
        writer.writerow(vacancy)

# Measure initial memory usage
initial_memory = psutil.Process().memory_info().rss / 1024 / 1024  # in MB

# Set up an infinite loop to scrape and write data to CSV
while True:
    # Find elements on the page using XPath
    vacancy_name = driver.find_elements(By.XPATH, "//div[contains(@class,'lis_title')]//a[@target='_blank']")
    vacancy_date = driver.find_elements(By.XPATH, "//div[@class='ic-time']")
    vacancy_description = driver.find_elements(By.XPATH, '//div[contains(@class,"listing")]/div[@class="desc"]')
    company = driver.find_elements(By.XPATH, "//div[contains(@class,'lis_title')]//a[@target='_blank']")
    salary = driver.find_elements(By.XPATH, '//div[@class="lis_salary"]')

    # Loop through the found elements and extract information
    for i in range(len(vacancy_name)):
        try:
            salary_ = salary[i].text
        except:
            salary_ = None

        # Create a dictionary with vacancy information
        vacancy = {
            "vacancy_name": vacancy_name[i].text.split('/')[0].strip() if len(company[i].text.split('/')) > 1 else vacancy_name[i].text.strip(),
            "vacancy_date": vacancy_date[i].text.strip(),
            "salary": salary_,
            "vacancy_description": vacancy_description[i].text.strip(),
            "company": company[i].text.split('/')[1].strip() if len(company[i].text.split('/')) > 1 else None
        }

        # Write the vacancy to the CSV file using the defined function
        write_to_csv(vacancy)

    # Try to find and click the "Next" button to move to the next page
    try:
        following_page_button = WebDriverWait(driver, 30, poll_frequency=0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Növbəti →']")))
        following_page_button.click()
    except:
        # Break the loop if the "Next" button is not found
        break

# Measure final memory usage
final_memory = psutil.Process().memory_info().rss / 1024 / 1024  # in MB
print(f"Memory usage: {final_memory - initial_memory:.2f} MB")
print('Successfully finished')

# Quit the webdriver
driver.quit()
