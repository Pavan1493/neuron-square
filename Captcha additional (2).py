from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary

url="https://safebrowsing.google.com/safebrowsing/report_phish/"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
sleep(2)
driver.maximize_window()
sleep(2.1)
driver.get(url)
sleep(5)
url_name=driver.find_element_by_id('url')
More_info=txt=driver.find_element_by_id('dq')
submit=driver.find_element_by_xpath("//input[@type='submit']")

url_name.send_keys("https://www.midsouthshooterssupply.com/dept/reloading/primers")

sleep(4.6)
txt.send_keys('This is a very suspicious website and is not recomended')
sleep(5.4)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
sleep(15)
driver.switch_to.default_content()
sleep(2.2)
submit.click()
sleep(10)
driver.close()