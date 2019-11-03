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

# run headless
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome('./chromedrivers/chromedriverForWin.exe')

url = 'http://bonusbitcoin.co/faucet'
driver.get(url)

# driver.maximize_window()

try:
    # if a user is signed in, sign in process is skipped
    signIn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#PageContent_SignInButton')))
    signIn.click()

    time.sleep(1)
    setEmail = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#SignInEmailInput')))
    setEmail.clear()
    setEmail.send_keys('pospisil1vaclav@gmail.com')

    time.sleep(1)
    setPassw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#SignInPasswordInput')))
    setPassw.send_keys('childbycrystalcastle1+')

    time.sleep(1)
    reCaptcha = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.recaptcha-checkbox-border')))
    reCaptcha.click()

    time.sleep(1)
    signInConfirm = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-bind="click: signIn"]')))
    signInConfirm.click()
    
except Exception as e:
    print(e)
    pass

time.sleep(1)
reCaptchaClaimer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.recaptcha-checkbox-border')))
reCaptchaClaimer.click()

claimer = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-bind="click: delayedClaim, text: claimButtonText, enable: canClaimNow"]')))
ActionChains(driver).move_to_element(claimer).click()


# close browser
# driver.quit()

