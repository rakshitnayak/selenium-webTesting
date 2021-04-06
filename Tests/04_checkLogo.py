# Selenium to Check whether logo exist or not in Homepage thesparksfoundationsingapore.org

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "E:\RAKSHIT FILES\WEB DEVLOPMENT\INternship works\selenium-tests\Browsers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()  

driver.get("https://www.thesparksfoundationsingapore.org/")
elem = bool
elem=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/h1/a/img")
if elem:
    print("Logo Exist in Homepage")
else:
    print("Logo Missing from Homepage")

time.sleep(2)
driver.quit()
print ("The test is completed")