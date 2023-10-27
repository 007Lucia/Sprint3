
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
import data
from data import evidencia

class Test_1055(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge() 
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://shop.thonet-vander.com/")


    def test_1055(self):
        self.driver.find_element(By.CSS_SELECTOR,"#menuUsuarioDiv > li.m-register.m-prod > a").click()
        self.driver.implicitly_wait(5)
        nombre = self.driver.find_element(By.ID,"usuario_registro_nombre").send_keys("Lucia")
        apellido = self.driver.find_element(By.ID,"usuario_registro_apellido").send_keys("Rosso")
        telefono = self.driver.find_element(By.ID,"usuario_registro_telefono").send_keys("3537569874")
        email = self.driver.find_element(By.ID,"usuario_registro_email").send_keys("lupi_747@live.com.ar")
        password = self.driver.find_element(By.ID,"usuario_registro_plainPassword").send_keys("39970545")
        registrar_button = self.driver.find_element(By.ID,"usuario_registro_registrar").click()
        time.sleep(5)
        
        assert nombre.is_enabled(), "El campo de nombre no está habilitado"
        nombre.send_keys("Lucia")

        assert apellido.is_enabled(), "El campo de apellido no está habilitado"
        apellido.send_keys("Rosso")

        assert telefono.is_enabled(), "El campo de teléfono no está habilitado"
        telefono.send_keys("3537569874")

        assert email.is_enabled(), "El campo de correo electrónico no está habilitado"
        email.send_keys("lupi_747@live.com.ar")

        assert password.is_enabled(), "El campo de contraseña no está habilitado"
        password.send_keys("39970545")
                      
        assert registrar_button.is_enabled(), "El botón de registro no está habilitado"
        registrar_button.click()    
        
                   
        self.driver.save_screenshot("../data/evidencia/captura.png")
        
    def tearDown(self):
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()