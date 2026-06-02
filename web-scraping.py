from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
import json
from time import sleep
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.timeanddate.com/weather/')
sleep(2)
links = []
weather_data = []   

weather_rows = driver.find_elements(By.CSS_SELECTOR, 'table.zebra.fw.tb-theme tbody tr')
for row in weather_rows:
    weather_cells = row.find_elements(By.CSS_SELECTOR, 'td')
    for cell in weather_cells:
        city_a = cell.find_elements(By.CSS_SELECTOR, 'a')
        if city_a:
            link = city_a[0].get_attribute('href')
            if link:
                links.append(link)
        

 
for item in links:
    driver.get(item)
    sleep(2)
    location = driver.find_element(By.CSS_SELECTOR, 'h1.headline-banner__title').text
    glook = driver.find_element(By.ID, 'qlook')
    temperature = glook.find_element(By.CSS_SELECTOR, 'span[title="High and low forecasted temperature today"]').text
    description = glook.find_element(By.XPATH, 'p[1]').text
    p = glook.find_element(By.XPATH, 'p[2]').text
    wind = p.split("Wind:", 1)[1].strip()
    info_div = driver.find_element(By.CSS_SELECTOR, 'div.bk-focus__info')
    info_rows = info_div.find_elements(By.CSS_SELECTOR, 'table tbody tr td')
    time = info_rows[2].text
    visibility = info_rows[3].text
    pressure = info_rows[4].text
    humidity = info_rows[5].text
    dew_point = info_rows[6].text
    weather_data.append({'Location': location, 'Temperature': temperature, 'Description': description, 'Wind': wind, "Date": time, 'Visibility': visibility, 'Pressure': pressure, 'Humidity': humidity, 'Dew point': dew_point })

with open('weather_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Location', 'Temperature', 'Description', 'Wind', "Date", 'Visibility, miles', 'Pressure, "Hg', 'Humidity, %', 'Dew point, °F'])
    writer.writeheader()
    writer.writerows(weather_data)



