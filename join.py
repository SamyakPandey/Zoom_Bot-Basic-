link = "https://class link" # May be multiple , according to your time table
import time
from selenium import webdriver

driver = webdriver.Chrome('path')

def join1():
    driver.get(link)
    time.sleep(30) 
    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(3600) # 1 hour = 3600 seconds
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

    
