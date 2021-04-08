
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH = "E:\RAKSHIT FILES\WEB DEVLOPMENT\INternship works\selenium-tests\Browsers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()  

driver.get("https://www.thesparksfoundationsingapore.org/")
time.sleep(5)
driver.find_element_by_link_text("KNOW MORE").click()
time.sleep(5)
driver.find_element_by_link_text("Executive Team").click()

print ("The test is completed")