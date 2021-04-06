from selenium import webdriver
import time  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

fullname = "Rakshit Nayak"
email = "abc@gmail.com"
PATH = "E:\RAKSHIT FILES\WEB DEVLOPMENT\INternship works\selenium-tests\Browsers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()  
driver.get("https://www.thesparksfoundationsingapore.org/join-us/why-join-us/#")
element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]")
element.send_keys(fullname)
time.sleep(3)  

element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]")
element.send_keys(email)
time.sleep(3)  

driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[2]").click()
element.send_keys(Keys.RETURN)
time.sleep(3)  
print("The test is completed Successfully By submitting form data")
driver.close()