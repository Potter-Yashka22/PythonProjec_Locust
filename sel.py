
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def toFind(driver,by,item):
    print(f'Ищу элемент {item}')
    #e0=driver.find_element()
    e1=WebDriverWait(driver,5).until(
        EC.presence_of_element_located((by,item))
    )
    print(f'Нашёл элемент {item}')
    try:
        driver.execute_script("arguments[0].scrollIntoView();",e1)
    except:
        print('прокрутка не робит')
    return e1

def toClick(driver,by,item):
    toFind(driver,by,item)
    print(f'проверка на клик {item}')
    e1=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((by, item))
    )
    e1.click()
    print(f'кликнул на элемент {item}')
    return True

def toSend(driver,by,item,text):
    e1=toFind(driver,by,item)
    e1.send_keys(text)
    e1.send_keys(Keys.ENTER)
    print(f'вписал текст в {item}')
    try:
        t1=e1.get_attribute('value')
        print(f'текст виден  {t1}')
    except:
        print('текс не виден')
    return True
def toSendNoEnter(driver,by,item,text):
    e1=toFind(driver,by,item)
    e1.send_keys(text)
    # e1.send_keys(Keys.ENTER)
    print(f'вписал текст в {item}')
    try:
        t1=e1.get_attribute('value')
        print(f'текст виден  {t1}')
    except:
        print('текс не виден')
    return True

def getScreen(driver,num):
    time.sleep(3)
    driver.get_screenshot_as_file(f'{num}.png')
    print('Сделал скриншот')
    return True

def toSelect(driver,by,item,value):
    toFind(driver,by,item)
    print(f'проверка на select {item}')
    e1=WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((by, item))
    )
    Select(e1).select_by_value(value)
    print(f'кликнул на элемент {item}')





























