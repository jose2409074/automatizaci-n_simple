from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def obtener_clima(driver, consulta):

    driver.get(f"https://www.google.com/search?q=clima+{consulta.replace(' ', '+')}&hl=es")
    
    try:
        # Espera explícita para que cargue el widget de Google
        wait = WebDriverWait(driver, 10)
        
        try:

            ubicacion_el = wait.until(EC.visibility_of_element_located((By.ID, "wob_loc")))
            ubicacion = ubicacion_el.text
            
            if ubicacion.lower() == "clima":
                try:
                    ubicacion = driver.find_element(By.CSS_SELECTOR, "div.vk_gy.vk_h").text
                except:

                    ubicacion = consulta.replace("clima en ", "").replace("clima ", "").title()

            temperatura = driver.find_element(By.ID, "wob_tm").text
            condicion = driver.find_element(By.ID, "wob_dc").text

        except:
            # Probé más de un bloque como alternativa en caso de error
            try:
                ubicacion = driver.find_element(By.CSS_SELECTOR, "div[data-attrid='title']").text.replace("Clima en ", "")
                temperatura = driver.find_element(By.CSS_SELECTOR, "span[class*='wob_t']").text
                condicion = "No especificada"
            except:
                return "No se pudo encontrar información climática por el momento."

        return f"El clima en {ubicacion} es {condicion} con una temperatura de {temperatura}°C."
    
    except Exception as e:
        # En caso de error crítico, devolvemos un mensaje genérico
        return "No se pudo obtener el clima en este momento."