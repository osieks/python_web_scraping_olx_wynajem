from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

urlpage = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/gliwice/?search%5Bfilter_float_price:to%5D=2500&search%5Bfilter_float_m:from%5D=45'
driver.get(urlpage)

# get the title of the webpage
title = driver.title
print('Title: ', title)

iterator = 1

while True:
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, 'mainContent'))
        )
    except:
        driver.quit()

    #mainContent = driver.find_element(By.ID, 'mainContent')
    ogloszenia = driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')

    links = []
    for ogloszenie in ogloszenia:
        a_elements = ogloszenie.find_elements(By.CSS_SELECTOR, 'a')
        if a_elements:
            links.append(a_elements[0].get_attribute('href'))

    for link in links:
        print(iterator)
        iterator += 1

        print(link)
        """
        driver.get(link)
        if 'www.otodom.pl' in link:
            print("OTO DOM")
            continue
        
        offer = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1wws9er'))
        )
        
        title = offer[0].find_elements(By.CLASS_NAME, 'css-1yzzyg0')
        print(title[1].find_element(By.CLASS_NAME, 'css-77x51t').text)
        
        print(offer[0].find_element(By.CLASS_NAME, 'css-sxnu2o').find_element(By.CLASS_NAME, 'css-e2ir3r').find_element(By.TAG_NAME, 'h3').text)
        
        
        dane_container = offer[0].find_element(By.TAG_NAME, 'ul')
        dane = dane_container.find_elements(By.CLASS_NAME, 'css-1r0si1e')
        for dana in dane:
            if 'Czynsz (dodatkowo):' in dana.text:
                print(dana.text.split("Czynsz (dodatkowo):",1)[1])
        
        print(offer[0].find_element(By.CLASS_NAME, 'css-1m8mzwg').text)
        driver.back()
        """
    try:
        next_button = driver.find_element(By.XPATH, '//button[@class="pagination-forward"]')
        print('Clicking next page')
        next_button.click()
    except Exception:
        print('No more pages')
        print('Exception', Exception.__name__)
        break  # If the "pagination-forward" button is not available, break the loop

driver.quit()
