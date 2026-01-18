from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion

from utils.sanitizar import sanitizar
import os

# Configuración de Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Inicialización del driver
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_driver = os.path.join(ruta_actual, "chromedriver.exe")

driver = None

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None

def salir(driver_instancia):
    if driver_instancia:
        try:
            driver_instancia.quit()c
            pass

print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")

try:
    driver = webdriver.Chrome(service=Service(ruta_driver), options=options)
    
    while True:
        user_input = sanitizar(input("---> "))
        
        if user_input.lower() in ["salir", "exit", "quit", "adiós", "chao"]:
            print("Cerrando sesión... ¡Hasta luego! 👋")
            break
            
        funcion_agente = procesar_input(user_input)
        
        if funcion_agente is None:
            print("No entendí tu solicitud. Intenta nuevamente.")
        else:
            respuesta = funcion_agente(driver, user_input)
            print(f">>> {respuesta}")

except KeyboardInterrupt:
    print("\nInterrupción detectada.")
except Exception as e:
    print(f"Error inesperado: {e}")
finally:
    salir(driver)