from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        site = "https://temptaking.ado.sg/group/1c58ca12560f9949694ba366c8a0f245"
        driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromdriver87\chromedriver.exe")
        driver.get(site)
        sleep(5)
        # XPath for select member://*[@id="member-select"]
        memberSelect = driver.find_element_by_xpath("//select[@id='member-select']")
        memberSelect.click()
        sleep(5)
        print("click test")
        for option in memberSelect.find_elements_by_tag_name('option'):

            print(option.text)
            if option.text == username:
                option.click()
            else:
                pass
        sleep(5)

        #PIN declarations
        code = password

        pin1 = driver.find_element_by_xpath("//input[@id='ep1']")
        pin2 = driver.find_element_by_xpath("//input[@id='ep2']")
        pin3 = driver.find_element_by_xpath("//input[@id='ep3']")
        pin4 = driver.find_element_by_xpath("//input[@id='ep4']")
        
        pinArray = [pin1, pin2, pin3, pin4]

        for pin in pinArray:
            i = len(code)
            pin.send_keys(code[range(0, i-1)])
            sleep(1)
            
        """ 
        pin1.send_keys(code[0])
        sleep(1)
        pin2.send_keys(code[1])
        sleep(1)
        pin3.send_keys(code[2])
        sleep(1)
        pin4.send_keys(code[3])
        sleep(1)
        """
        
        # Temperature
        temperatureArray = [3, 6, random.randint(0, 9)]

        tBox1 = driver.find_element_by_xpath("//input[@id='td1']")
        tBox2 = driver.find_element_by_xpath("//input[@id='td2']")
        tBox3 = driver.find_element_by_xpath("//input[@id='td3']")

        tBox1.send_keys(temperatureArray[0])
        sleep(1)
        tBox2.send_keys(temperatureArray[1])
        sleep(1)
        tBox3.send_keys(temperatureArray[2])
        sleep(1)

        #SUBMISSION

        submitButton = driver.find_element_by_xpath("//button[contains(text(),'SUBMIT')]")
        submitButton.click()
        sleep(2)
        confirmButton = driver.find_element_by_xpath("//button[@id='submit-temp-btn']")
        confirmButton.click()
        sleep(2)
        driver.close()



Bot("Kaushik", [6, 6, 6, 6])
