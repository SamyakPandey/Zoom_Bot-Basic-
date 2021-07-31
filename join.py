link = "https://us05web.zoom.us/j/9549146713?pwd=WjJjeXZxOVlwM2JDelFLdEEvMkxKdz09"
import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver')

def join1():
    driver.get(link)
    time.sleep(30) 
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600)
    driver.quit()

def join2():
    driver.get(link)
    time.sleep(30) 
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600)
    driver.quit()


def join3():
    driver.get(link)
    time.sleep(30) 
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600)
    driver.quit()

    
