from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_precio_accion(driver, consulta):
    driver.get(f"https://www.google.com/search?q=precio+acción+{consulta}")
    
    try:
        # Pequeña pausa para cargar
        time.sleep(1)
        
        wait = WebDriverWait(driver, 10)
        

        empresa = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='PZPZlf ssJ7i B5dxMb']"))).text
        
        precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").text
        
        divisa = driver.find_element(By.CSS_SELECTOR, "span[jsname='T3Us2d']").text
        
        ticker = driver.find_element(By.CSS_SELECTOR, "div[class='iAIpCb PZPZlf']").text
        
        return f"{empresa} [{ticker}]  ${precio} {divisa.upper()}."
    except Exception as e:
        return "No se pudo obtener el precio de la acción en este momento."