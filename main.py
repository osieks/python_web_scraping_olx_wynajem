import time
from venv import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

urlpage = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/gliwice/?search%5Bfilter_float_price:to%5D=2500&search%5Bfilter_float_m:from%5D=45'
driver.get(urlpage)

# get the title of the webpage
title = driver.title
print('Title: ', title)

data = []

iterator = 1
while True:
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, 'mainContent'))
        )
    except:
        driver.quit()

    ogloszenia = driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')

    break

driver.quit()

df = pd.DataFrame(data, columns=['id','Link','Title', 'Price', 'Additional Rent', 'Description'])
#df = pd.DataFrame(data, columns=['Link'])
print("zapisuje")
df.to_excel('output.xlsx', index=False)
print("done")
