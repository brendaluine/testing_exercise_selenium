from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from os import path

#set up options
firefoxOptions = Options()

options = [
  # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors",
    "--private"
 
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

#service = Service(log_path=path.devnull)
service = Service('/usr/local/bin/geckodriver')

driver = webdriver.Firefox(service = service, options = firefoxOptions)
driver.get('https://www.giving.uts.edu.au/donate')

try:
  #fill out the form
  choose_amount = driver.find_element(By.ID, 'amount225').click()

  #designation_dropdown = driver.find_element(By.ID, 's2id_PC16725_ddlDesignation').click
  #designation_dropdown.send_keys('High Impact Research')
  #designation_dropdown.select_by_visible_text('High Impact Research')
  #designation_choice = driver.find_element(By.XPATH, '//*[@id="PC16725_ddlDesignations"]/option[15]').click()
  #designation_choice = driver.find_element(By.ID, 'select2-result-label-314').click()

  gift_type = driver.find_element(By.XPATH, '//*[@id="PC16725_rdoGiftType"]/tbody/tr[3]/td/label').click()

  driver.implicitly_wait(5) #wait for page to update

  instalments = driver.find_element(By.NAME, 'PC16725$txtInstallments')
  instalments.send_keys('3')

  title = Select(driver.find_element(By.ID, 'PC16725_DonationCapture1_cboTitle'))
  title.select_by_visible_text('Dr')

  fname = driver.find_element(By.ID, 'PC16725_DonationCapture1_txtFirstName')
  fname.send_keys('Jane')

  lname = driver.find_element(By.ID, 'PC16725_DonationCapture1_txtLastName')
  lname.send_keys('Doe')

  # country = Select(driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_AddressCtl_dd_Country"]'))
  # country.select_by_visible_text('Belgium')
  # driver.implicitly_wait(5) #wait for page to update

  address = driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_AddressCtl_tb_AddressLine"]')
  address.send_keys('123 Lalaland Street')

  suburb = driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_AddressCtl_tb_CityAUS"]')
  suburb.send_keys('Wonderland')

  state = Select(driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_AddressCtl_dd_StateAUS"]'))
  state.select_by_visible_text('VIC')

  postcode = driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_AddressCtl_tb_ZipAUS"]')
  postcode.send_keys('1234')

  phone = driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_txtPhone"]')
  phone.send_keys('123 456 789')


  email = driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_txtEmail"]')
  email.send_keys('this@email.com')

  #payment_method = driver.find_element(By.XPATH, '//*[@id="PC16725_DonationCapture1_rdoPaymentOption_1"]').click()
  #driver.implicitly_wait(5) #wait for page to update

  card_name = driver.find_element(By.NAME, 'PC16725$DonationCapture1$txtCardholder')
  card_name.send_keys('Jane Doe')

  card_number = driver.find_element(By.NAME, 'PC16725$DonationCapture1$txtCardNumber')
  card_number.send_keys('0000000000')

  card_type = Select(driver.find_element(By.NAME, 'PC16725$DonationCapture1$cboCardType'))
  card_type.select_by_visible_text('Visa')

#to submit and/or close the window
#driver.implicitly_wait(20) #wait for page to update

#donate_btn = driver.find_element(By.NAME, 'PC16725$btnNext').click()

finally:
  driver.quit()

