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

# Start webdriver
driver = webdriver.Chrome(PATH)
driver.get(URL)
time.sleep(5)

# Check if there is stock
stock = driver.find_elements_by_link_text("AGOTADO")

if stock == []:
    # Create message object instance
    msg = MIMEMultipart()
    message = "El enlace del articulo es el siguiente:"
    
    # Setup the parameters of the message
    msg['From'] = sender_addr
    msg['To'] = receiver_addr
    msg['Subject'] = "STOCK DE LA RTX 3080"
    
    # Add in the message body
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(URL, 'plain'))
    
    # Create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    # Login Credentials for sending the mail
    server.login(sender_addr, pwd)
    
    
    # Send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("THE BOMB HAS BEEN PLANTED")

    server.quit()

time.sleep(5)
driver.quit()