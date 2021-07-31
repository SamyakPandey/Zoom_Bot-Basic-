firstClass =  ("16:10")
secondClass = ("17:20")
thirdClass = ("18:30")



import datetime
from selenium import webdriver
import schedule
import time
from join import *
e = datetime.datetime.now()


def saturday():
    schedule.every().saturday.at(firstClass).do(join1())
    schedule.every().saturday.at(secondClass).do(join2())
    schedule.every().saturday.at(thirdClass).do(join3())

day = (e.strftime("%a"))
print(day)

if day == "Sat":
    saturday()

else:
    print("No Class")
