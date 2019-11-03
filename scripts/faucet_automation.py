# part of the bot that actually crawls the provided Alza url
# uses Selenium and Chrome
# dependencies:
#   pip install selenium
# Chrome needs chromedriver with specified path
# doc for Selenium + Python: https://selenium-python.readthedocs.io

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# run headless
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome('./chromedriver/chromedriverForWin.exe')

url = 'http://bonusbitcoin.co/faucet'
driver.get(url)

# driver.maximize_window()

searchPickupPlace = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#PageContent_SignInButton')))
searchPickupPlace.click()

time.sleep(1)
setPickupPlace = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-results__seznam .pickup_box')))
setPickupPlace.click()

time.sleep(1)
setPickupPlace2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Kulhavého 669/2, Praha 4"]')))
setPickupPlace2.click()

time.sleep(1)
confirmPickupPlace = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pickupPlace-0-739 .selected-pickup-place-confirm')))
confirmPickupPlace.click()

time.sleep(1)
setPaymentMethod = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#paymentContainer-101')))
setPaymentMethod.click()

time.sleep(1)
confirmOrder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#confirmOrder2Button')))
confirmOrder.click()

# set email and phone
time.sleep(1)
setEmail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#userEmail')))
setEmail.clear() # clear predefined value ('@')
setEmail.send_keys('hamcouz@gmail.com')

setPhoneNumber = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#userPhone')))
setPhoneNumber.send_keys('666555444')

# finalize order
finalize = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.js-order3-continue')))
finalize.click()

# close browser
driver.quit()

