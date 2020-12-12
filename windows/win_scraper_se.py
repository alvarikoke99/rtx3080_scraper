from selenium import webdriver
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import traceback

PATH = "C:\Program Files (x86)\chromedriver.exe"
URL_NVIDIA = "https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080"
URL_ASUS = "https://www.pccomponentes.com/asus-tuf-geforce-rtx-3080-10gb-gddr6x"
sender_addr = "alert-mail@gmail.com"
receiver_addr = "personal-mail@gmail.com"
pwd = "password"
N = 1

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

def checkStockNvidia(driver):
    stock = driver.find_elements_by_link_text("AGOTADO")
    if stock == []:
        message = "El enlace del articulo es el siguiente: " + URL_NVIDIA
        sendMsg(sender_addr, receiver_addr, "STOCK DE RTX 3080", message)
        print("Mail sent at: ", time.ctime(time.time()))
        print("")

def checkStockPcComp(driver, subject, URL):
    notify = driver.find_elements_by_id("notify-me")
    if notify == []:
        message = "El enlace del articulo es el siguiente: " + URL
        sendMsg(sender_addr, receiver_addr, subject, message)
        print("Mail sent at: ", time.ctime(time.time()))
        print("")

try:
    # Start webdriver
    driver = webdriver.Chrome(PATH)
    
    for i in range(N):
        # Check if there is stock of FE
        driver.get(URL_NVIDIA)
        time.sleep(1)
        checkStockNvidia(driver)

        # Check if there is stock of ASUS TUF
        driver.get(URL_ASUS)
        time.sleep(1)
        checkStockPcComp(driver, "STOCK DE ASUS TUF RTX 3080", URL_ASUS)
        
    print("Running - ", time.ctime(time.time()))
    print("")

except Exception as e:
    error_trace = traceback.format_exc()
    sendMsg(sender_addr, receiver_addr, "Error en el servidor", error_trace)
    print("ERROR - ", time.ctime(time.time()))
    print(error_trace)
    print("")

finally:
    # Close webdriver
    driver.close()
    driver.quit()