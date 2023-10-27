from Functions.Functions import Functions
from Functions.Inicializar import Inicializar 

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException

#from Pages.registro import Registro
class Test_1054(unittest.TestCase, Functions):


    def setUp(self):
        self.driver = Functions.abrir_navegador(self)
        print(self.driver)
        self.driver.get(Inicializar.URL)
        time.sleep(5)

    def test_1054(self):
        Functions.get_json_file(self, "registro")
        Functions.get_elements(self, "Registrate").click()
        nombre = Functions.get_elements(self, "Nombre")
        apellido = Functions.get_elements(self, "Apellido")
        telefono = Functions.get_elements(self, "Telefono")
        email = Functions.get_elements(self, "Email")
        password = Functions.get_elements(self, "Password")
        registrar_button = Functions.get_elements(self, "Registrar_button")
        time.sleep(5)
        
        assert nombre.is_enabled(), "El campo de nombre no está habilitado" 
        nombre.send_keys("Lucia")

        assert apellido.is_enabled(), "El campo de apellido no está habilitado"
        apellido.send_keys("Rosso")

        assert telefono.is_enabled(), "El campo de teléfono no está habilitado" 
        telefono.send_keys("3537569874")

        assert email.is_enabled(), "El campo de correo electrónico no está habilitado"
        email.send_keys("dbjifgf516@tormails.com")

        assert password.is_enabled(), "El campo de contraseña no está habilitado"
        password.send_keys("12345")
                      
        assert registrar_button.is_enabled(), "El botón de registro no está habilitado"
        registrar_button.click()         
        
        pass
                                 
    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()