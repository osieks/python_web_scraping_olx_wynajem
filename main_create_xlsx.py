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

    links = []
    for ogloszenie in ogloszenia:
        a_elements = ogloszenie.find_elements(By.CSS_SELECTOR, 'a')
        if a_elements:
            links.append(a_elements[0].get_attribute('href'))

    for link in links:
        print(iterator)
        iterator += 1
        
        #for fast debbuging
        #if(iterator > 3): break
        
        row = []
        row.append("=HYPERLINK({link}, 'LINK')")
        driver.get(link)
        if 'www.otodom.pl' in link:
            print("otodom")
            driver.back()
            continue
        
        offer = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1wws9er'))
        )
        
        title = offer[0].find_elements(By.CLASS_NAME, 'css-1yzzyg0')
        row.append(title[1].find_element(By.CLASS_NAME, 'css-77x51t').text)
        
        row.append(offer[0].find_element(By.CLASS_NAME, 'css-sxnu2o').find_element(By.CLASS_NAME, 'css-e2ir3r').find_element(By.TAG_NAME, 'h3').text)
        
        dane_container = offer[0].find_element(By.TAG_NAME, 'ul')
        dane = dane_container.find_elements(By.CLASS_NAME, 'css-1r0si1e')
        for dana in dane:
            if 'Czynsz (dodatkowo):' in dana.text:
                row.append(dana.text.split("Czynsz (dodatkowo):",1)[1])
        
        row.append(offer[0].find_element(By.CLASS_NAME, 'css-1m8mzwg').text)
        
        driver.back()
        
        data.append(row)
        
        for total_count in driver.find_elements(By.CSS_SELECTOR, "span[data-testid='total-count']"): 
            znaleziono_string = total_count.text
            print(znaleziono_string)
            lista_znaleziono = znaleziono_string.split()
            #lista_znaleziono[1]="2"
            print( int(lista_znaleziono[1]))
            if int(lista_znaleziono[1])<=iterator:
                break
        if int(lista_znaleziono[1])<=iterator:
            break
    if int(lista_znaleziono[1])<=iterator:
        break
    try:
        next_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-testid='pagination-forward']"))
        )
        for next_button in next_buttons:
            print(next_button.get_attribute('href'))
        
        driver.get(next_buttons[0].get_attribute('href'))
        time.sleep(5)
        #next_button.click()
    except Exception:
        logger.error('Failed to do something: ' + str(Exception))
        break

driver.quit()

df = pd.DataFrame(data, columns=['Link','Title', 'Price', 'Additional Rent', 'Description'])
#df = pd.DataFrame(data, columns=['Link'])
print("zapisuje")
df.to_excel('output.xlsx', index=False)
print("done")
