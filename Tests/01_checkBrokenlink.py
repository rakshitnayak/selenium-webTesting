import requests
from selenium import webdriver
import time
PATH = "E:\RAKSHIT FILES\WEB DEVLOPMENT\INternship works\selenium-tests\Browsers\chromedriver.exe"

driver=webdriver.Chrome(PATH)
driver.maximize_window()
driver.get('https://www.thesparksfoundationsingapore.org/programs/student-scholarship-program/')

links = driver.find_elements_by_css_selector("a") # Selecting all the links (Anchor Tag <a> tag) as all links are elements.
print("Total number of links --", len(links))

for link in links:
    req = requests.head(link.get_attribute('href'))  # requesting the href attribute to get status code
    if req.status_code >= 400:    # link is broken if status code is greater than 400 eg. error code 404, 503 etc
        print(link.get_attribute('href'), req.status_code)
    else:
        print(link.get_attribute('href') + " -- OK")
time.sleep(2)
driver.quit()
print ("The test is completed")