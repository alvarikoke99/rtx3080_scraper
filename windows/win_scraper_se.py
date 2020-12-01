from selenium import webdriver
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "https://www.nvidia.com/es-es/shop/geforce/gpu/?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080&manufacturer=NVIDIA&gpu_filter=RTX%203090~1,RTX%203080~1,RTX%203070~1,RTX%202080%20Ti~0,RTX%202080%20SUPER~0,RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0,GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20SUPER~0,GTX%201650~0"
sender_addr = "alert-mail@gmail.com"
receiver_addr = "personal-mail@gmail.com"
pwd = "password"
N = 4

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
    driver = webdriver.Chrome(PATH)
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
    print("")