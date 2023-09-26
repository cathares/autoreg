from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from getNumber import purchaseNumber
from tokenInfo import TOKEN
from getNumber import getSMS
from util import randInt

"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.get("https://www.tiktok.com/signup/phone-or-email/phone")

arrows = driver.find_elements(By.CLASS_NAME, "tiktok-gz151e-StyledArrowTriangleDownLargeFill")
arrows[0].click()

month = driver.find_element(By.ID, f"Month-options-item-{randInt(0,12)}")
month.click()
time.sleep(3)

arrows[1].click()
day = driver.find_element(By.ID, f"Day-options-item-{randInt(0,30)}")
day.click()
time.sleep(3)
arrows[2].click()
year = driver.find_element(By.ID, f"Year-options-item-{randInt(32,43)}")
year.click()
time.sleep(3)

purchaseData = dict.fromkeys(['Country', 'Operator'])
purchaseData['Country'] = "usa"
purchaseData['Operator'] = "Virtual40"

#numberInfo = purchaseNumber(TOKEN, purchaseData)  # number, country, id

numberInfo = dict.fromkeys(['Number'])
numberInfo['Number'] = "+7632332485"
numberArrow = driver.find_element(By.CLASS_NAME, "tiktok-so52kr-StyledArrowIcon")
numberArrow.click()
time.sleep(3)
country = driver.find_element(By.ID, "US-1")
country.click()
time.sleep(3)


numberField = driver.find_element(By.CLASS_NAME, "tiktok-af1p2k-InputContainer")
numberField.send_keys(numberInfo['Number'][2:])
time.sleep(3)

sendCodeButton = driver.find_element(By.CLASS_NAME, "tiktok-1jjb4td-ButtonSendCode")
sendCodeButton.click()
time.sleep(20)
#smsCode = getSMS(TOKEN, numberInfo[2])
smsCode = "111222"
print(smsCode)

while smsCode is None:
    time.sleep(30)
    print(smsCode)
    smsCode = getSMS(TOKEN, numberInfo[2])

print(smsCode)
smsField = driver.find_element(By.CLASS_NAME, "tiktok-11to27l-InputContainer")
smsField.send_keys(smsCode)
time.sleep(5)

nextButton = driver.find_element(By.CLASS_NAME, "tiktok-11sviba-Button-StyledButton")
nextButton.click()

driver.quit()
"""

import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER = Path('chromedriver.exe')


def start_driver():
    driver = webdriver.Chrome()
    delete_cache(driver)
    return driver


def delete_cache(driver):
    driver.execute_script("window.open('')")  # Create a separate tab than the main one
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    perform_actions(driver, Keys.TAB * 2 + Keys.DOWN * 4 + Keys.TAB * 5 + Keys.ENTER)  # Tab to the time select and key down to say "All Time" then go to the Confirm button and press Enter
    driver.close()  # Close that window
    driver.switch_to.window(driver.window_handles[0])  # Switch Selenium controls to the original tab to continue normal functionality.


def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    print('Performing Actions!')
    actions.perform()



if __name__ == '__main__':
    driver = start_driver()
    driver.get("https://www.tiktok.com/signup/phone-or-email/phone")

    arrows = driver.find_elements(By.CLASS_NAME, "tiktok-gz151e-StyledArrowTriangleDownLargeFill")
    arrows[0].click()

    month = driver.find_element(By.ID, f"Month-options-item-{randInt(0, 12)}")
    month.click()
    time.sleep(3)

    arrows[1].click()
    day = driver.find_element(By.ID, f"Day-options-item-{randInt(0, 30)}")
    day.click()
    time.sleep(3)
    arrows[2].click()
    year = driver.find_element(By.ID, f"Year-options-item-{randInt(32, 43)}")
    year.click()
    time.sleep(3)

    purchaseData = dict.fromkeys(['Country', 'Operator'])
    purchaseData['Country'] = "usa"
    purchaseData['Operator'] = "Virtual40"

    numberInfo = purchaseNumber(TOKEN, purchaseData)  # number, country, id

    numberInfo = dict.fromkeys(['Number'])
    #numberInfo['Number'] = "+9884343324"
    numberArrow = driver.find_element(By.CLASS_NAME, "tiktok-so52kr-StyledArrowIcon")
    numberArrow.click()
    time.sleep(3)
    country = driver.find_element(By.ID, "US-1")
    country.click()
    time.sleep(3)

    numberField = driver.find_element(By.CLASS_NAME, "tiktok-af1p2k-InputContainer")
    numberField.send_keys(numberInfo['Number'][2:])
    time.sleep(3)

    sendCodeButton = driver.find_element(By.CLASS_NAME, "tiktok-1jjb4td-ButtonSendCode")
    sendCodeButton.click()
    time.sleep(20)
    smsCode = getSMS(TOKEN, numberInfo[2])
    print(smsCode)

    while smsCode is None:
        time.sleep(30)
        print(smsCode)
        smsCode = getSMS(TOKEN, numberInfo[2])

    print(smsCode)
    smsField = driver.find_element(By.CLASS_NAME, "tiktok-11to27l-InputContainer")
    smsField.send_keys(smsCode)
    time.sleep(20)

    nextButton = driver.find_element(By.CLASS_NAME, "tiktok-11sviba-Button-StyledButton")
    nextButton.click()

    driver.quit()