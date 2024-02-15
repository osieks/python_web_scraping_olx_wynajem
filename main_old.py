from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

urlpage = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/gliwice/?search%5Bfilter_float_price:to%5D=2500'
driver.get(urlpage)

# get the title of the webpage
title = driver.title
print('Title: ', title)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'mainContent'))
    )
except:
    driver.quit()

#mainContent = driver.find_element(By.ID, 'mainContent')
ogloszenia = driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')

for ogloszenie in ogloszenia:
    print(ogloszenie.text)
    
    a = ogloszenie.find_element(By.CSS_SELECTOR, 'a')
    print(a.get_attribute('href'))

    driver.get(a.get_attribute('href'))
    
    offer = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1wws9er'))
    )
    dane_container = offer[0].find_element(By.TAG_NAME, 'ul')
    dane = dane_container.find_elements(By.CLASS_NAME, 'css-1r0si1e')
    for dana in dane:
        print(dana.text)
    driver.back()
    

driver.quit()
