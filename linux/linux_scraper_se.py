from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

URL_1 = "https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080"
URL_2 = "https://www.pccomponentes.com/asus-tuf-geforce-rtx-3080-10gb-gddr6x"
PATH = "/usr/local/bin/geckodriver"
sender_addr = "alert-mail@gmail.com"
receiver_addr = "personal-mail@gmail.com"
pwd = "password"
N = 0

# code to use in crontab scheduler
# SHELL=/bin/bash
# * 8-23,0-3 * * * DISPLAY=:0 /usr/bin/python3 /home/ubuntu/scraper/linux_scraper_se.py >> /home/ubuntu/Documentos/Scraper/log.out

def sendMsg(sender_addr, receiver_addr, subject, body):
    # Create message object instance
    msg = MIMEMultipart()
        
    # Setup the parameters of the message
    msg['From'] = sender_addr
    msg['To'] = receiver_addr
    msg['Subject'] = subject
        
    # Add in the message body
    msg.attach(MIMEText(body, 'plain'))
        
    # Create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
        
    # Login Credentials for sending the mail
    server.login(sender_addr, pwd)
        
    # Send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def checkStockFE(driver):
    stock = driver.find_elements_by_link_text("AGOTADO")
    if stock == []:
        message = "El enlace del articulo es el siguiente: " + URL_1
        sendMsg(sender_addr, receiver_addr, "STOCK DE RTX 3080", message)
        print("Mail sent at: ", time.ctime(time.time()))
        print("")

def checkStockASUS(driver):
    notify = driver.find_elements_by_id("notify-me")
    if notify == []:
        message = "El enlace del articulo es el siguiente: " + URL_2
        sendMsg(sender_addr, receiver_addr, "STOCK DE ASUS TUF RTX 3080", message)
        print("Mail sent at: ", time.ctime(time.time()))
        print("")

try:
    # Start webdriver
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=PATH)
    driver.get(URL_1)
    time.sleep(5)

    # Check if there is stock of FE
    checkStockFE(driver)

    # Check if there is stock of ASUS TUF
    driver.get(URL_2)
    time.sleep(5)
    checkStockASUS(driver)

    #for i in range(N):
    #    driver.refresh()
    #    time.sleep(5)
    #    checkStockFE(driver)
        
    # Close webdriver
    driver.quit()
    print("Running - ", time.ctime(time.time()))
    print("")

except Exception as e:
    message = str(e)
    sendMsg(sender_addr, receiver_addr, "Error en el servidor", message)
    print("ERROR - ", time.ctime(time.time()))
    print(e)