from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefoxOptions = Options()

options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    firefoxOptions.add_argument(option)

driver = webdriver.Firefox()
driver.get('https://www.giving.uts.edu.au/donate')

choose_amount = driver.find_element(By.ID, 'amount225').click()

#designation_dropdown = driver.find_element(By.ID, 'select2-drop-mask').click()
#designation_choice = driver.find_element(By.ID, 'select2-result-label-66').click()
gift_type = driver.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/div/article/div/div[1]/table/tbody[4]/tr[3]/td[2]/table/tbody/tr[2]/td/label').click()

# frequency = driver.find_element(By.ID, 'PC16725_Recurrence_ddlFrequency')
# frequency.select_by_visible_text('July 10 of every year')


#print('Title: %s' % browser.title)
#browser.quit()

