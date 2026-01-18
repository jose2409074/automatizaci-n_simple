from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

ruta_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
driver = webdriver.Chrome(service=Service(ruta_driver))
driver.get("https://www.google.com")
sleep(2)
driver.get("https://hybridge.education")
sleep(2)
driver.get("https://openai.com")