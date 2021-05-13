from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "C:\Chorme Driver\chromedriver.exe"
chrome_options = Options()

chrome_options.add_argument("--window-size=500,400")

driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

driver.get("http://practice.automationtesting.in/")
# get current url
print(driver.page_source)

driver.quit()
