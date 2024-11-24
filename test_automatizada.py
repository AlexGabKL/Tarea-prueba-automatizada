import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import HtmlTestRunner  # Import para generar los reportes HTML

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial de la prueba"""
        service = Service(executable_path="./chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_login_process(self):
        """Prueba de proceso de login con capturas de pantalla"""
        driver = self.driver
        
        # Captura de estado inicial
        driver.save_screenshot("inicio_pagina.png")

        # Navega a Form Authentication
        driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        time.sleep(2)  

        # Captura después de tocar Form Authentication
        driver.save_screenshot("form_authentication.png")
        
        # Completa automáticamente los formularios de name y pass
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Código para ingresar los datos automáticamente
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")

        # Captura del login
        driver.save_screenshot("login_completado.png")

        submit_button.click()

        time.sleep(2)

        # Captura después del login
        driver.save_screenshot("despues_de_login.png")

        success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
        self.assertIn("You logged into a secure area!", success_message.text)

        # Captura de mensaje éxito
        driver.save_screenshot("mensaje_exito.png")
    
    def tearDown(self):
        """Cierra el navegador después de cada prueba"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
