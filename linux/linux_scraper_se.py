from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

URL = "https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080&manufacturer=NVIDIA&manufacturer_filter=NVIDIA~1,ASUS~4,EVGA~5,GAINWARD~0,GIGABYTE~3,MSI~2,PNY~2,ZOTAC~2"
PATH = "/usr/local/bin/geckodriver"
sender_addr = "alert-mail@gmail.com"
receiver_addr = "personal-mail@gmail.com"
pwd = "password"
N = 3

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

def checkStock(driver):
    stock = driver.find_elements_by_link_text("AGOTADO")
    if stock == []:
        message = "El enlace del articulo es el siguiente: " + URL
        sendMsg(sender_addr, receiver_addr, "STOCK DE LA RTX 3080", message)
        print("Mail sent at: ", time.ctime(time.time()))
        print("")

try:
    # Start webdriver
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=PATH)
    driver.get(URL)
    time.sleep(5)

    # Check if there is stock
    checkStock(driver)

    for i in range(N):
        driver.refresh()
        time.sleep(5)
        checkStock(driver)
        
    # Close webdriver
    driver.close()
    driver.quit()
    print("Running - ", time.ctime(time.time()))
    print("")

except Exception as e:
    message = str(e)
    sendMsg(sender_addr, receiver_addr, "Error en el servidor", message)
    print("ERROR - ", time.ctime(time.time()))
    print(e)