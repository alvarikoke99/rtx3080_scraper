import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

URL = "https://www.nvidia.com/es-es/shop/geforce/gpu/ \
?page=1&limit=9&locale=es-es&category=GPU&gpu=RTX%203080&manufacturer=NVIDIA \
&gpu_filter=RTX%203090~1,RTX%203080~1,RTX%203070~1,RTX%202080%20Ti~0,RTX%202080%20SUPER~0, \
RTX%202080~0,RTX%202070%20SUPER~0,RTX%202070~0,RTX%202060%20SUPER~0,RTX%202060~0, \
GTX%201660%20Ti~0,GTX%201660%20SUPER~0,GTX%201660~0,GTX%201650%20SUPER~0,GTX%201650~0"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())

session = HTMLSession()
r = session.get(URL)
r.html.render(sleep=1, keep_page=True, scrolldown=1)
palabra = r.html.find("featured-buy-link link-btn brand-green  cta-button stock-grey-out")
print(palabra)

                        