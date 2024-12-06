from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Initialize WebDriver (so that it can run in a browser)
with webdriver.Chrome() as driver:
    # Open the Yahoo Finance World Indices page
    driver.get("https://ca.finance.yahoo.com/world-indices")

    # Wait for the table to render (ensuring that the table is loaded)
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )

    # Get each row in the table
    rows = table.find_elements(By.CSS_SELECTOR, "tbody > tr")

    # Extract data from each row, filtering out only the relevant columns
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = []
        for cell in cells:
            aria_label = cell.get_attribute("aria-label")
            if aria_label in ["Symbol", "Name", "Last Price", "Change"]:
                row_data.append(cell.text)
        if row_data:
            data.append(row_data)

    # Save the scraped data to a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol", "Name", "Last Price", "Change"])
        writer.writerows(data)
