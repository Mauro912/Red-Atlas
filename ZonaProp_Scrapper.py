from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd




driver = webdriver.Chrome()
driver.get("https://www.zonaprop.com.ar/departamentos-alquiler-moreno-orden-precio-ascendente.html")

data_list = []

posts_container = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'sc-1tt2vbg-5.GcsXo')))
for posteo in posts_container:
        price_element = posteo.find_element(By.CLASS_NAME, 'sc-12dh9kl-3.iqNJlX')
        expenses_element = posteo.find_element(By.CLASS_NAME, 'sc-12dh9kl-1.chzHQe') if posteo.find_elements(By.CLASS_NAME, 'sc-12dh9kl-1.chzHQe') else None
        adress_element = posteo.find_element(By.CLASS_NAME, 'sc-ge2uzh-0.eWOwnE.postingAddress')
        area_element = posteo.find_element(By.CLASS_NAME, 'sc-ge2uzh-2.foowHA')
        rooms_element = posteo.find_element(By.CLASS_NAME, 'sc-1uhtbxc-0.jHlxXg')
        unit_details_element = posteo.find_element(By.CLASS_NAME, 'sc-i1odl-11.dnPeFf')

        price = price_element.text
        expenses = expenses_element.text.replace("Expensas", "").replace("expensas", "") if expenses_element else "Listing has no expenses"
        adress = adress_element.text
        area = area_element.text
        rooms = rooms_element.text.replace("\n", " | ")
        details = unit_details_element.text

        data_list.append({'Monthly Rent': price, 'Expenses': expenses, 'Address': adress, 'Area': area, 'Rooms': rooms, 'Unit Details':details})

df = pd.DataFrame(data_list)
df.to_csv("ZonaProp_Data.csv", encoding='utf-8-sig', index=False, sep=';')
print("CSV file created successfully.")

driver.quit()