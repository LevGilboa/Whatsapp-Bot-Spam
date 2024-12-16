#program by LevGilboa
#version 1.00
#testing date: December , 14 , 2024

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By


import os
import time
service = ChromeService((ChromeDriverManager().install()))
options = webdriver.ChromeOptions()
options.add_argument('--profile-directory=Profile NUM_HERE') #You can find the dir in chrome://version/
options.add_argument("--user-data-dir=enter user data here") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
try:
    driver = webdriver.Chrome(service=service,options=options)
except:
    os.system("taskkill /im chrome.exe /f")
    driver = webdriver.Chrome(service=service,options=options)
driver.get('https://web.whatsapp.com/')

#Chrome opens
#Scan the QR code
print("\n\nPlease MAXIMIZE the WhatsApp window before proceeding...")
print("\n\nPlease ignore all warnings and enter name of user or group...\n\n")

name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').upper()

input('Enter anything after scanning QR code...')
try:
    user = driver.find_element(by=By.XPATH,value='//span[@title = "{}"]'.format(name))
    user.click()

    #Entered the chat

    msg_box = driver.find_element(by=By.XPATH,value='//div[@data-tab = "10"]')    #updated from last version: @data-tab = "10"   #May require further updates based on Chrome version.

    for i in range(count):
        if bot_prompt == 'Y':
            msg_final = '<Status: ' + str(i+1) + '/' + str(count) + '>' + msg
        else:
            msg_final = msg
        msg_box.send_keys(msg_final)
        button = driver.find_element(by=By.XPATH,value="//span[@data-icon='send']")          
        button.click()
        if gap > 0:
            time.sleep(gap)

    msg_final = 'Spaming Complete!'
    msg_box.send_keys(msg_final)
    button = driver.find_element(by=By.XPATH,value="//span[@data-icon='send']")
                  
    button.click()

    time.sleep(30)#update: gives time for messages to be sent before closing the window
except:
    driver.quit()
try:
    driver.quit()
except:
    print("Already closed::ERROR")

