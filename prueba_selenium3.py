from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled') 

ruta_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver.exe")
driver = webdriver.Chrome(service=Service(ruta_driver), options=options)

empresa = "microsoft"
driver.get(f"https://www.google.com/search?q=precio+acción+{empresa}")
try:
    empresa = driver.find_element(By.CSS_SELECTOR, "div[class='PZPZlf ssJ7i B5dxMb']").text
    precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='L3mUVe']").text
    print(f"{empresa}: ${precio}")
except Exception as e:
    print("No se pudo obtener el precio de la acción en este momento.")