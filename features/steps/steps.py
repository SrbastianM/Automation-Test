from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open('config.json', 'r') as url:
    config = json.load(url)

@given('El usuario ingresó a la plataforma')
def webDriver(context):
    context.driver = webdriver.Firefox()
    context.driver.get(config["url"])
    context.driver.maximize_window()
    context.driver.execute_script("window.scrollTo(0, 800)")

@when('El usuario ingresa sus credenciales')
def credentials(context):
    context.driver.find_element(By.ID,"username").send_keys(config["username"])
    context.driver.find_element(By.ID,"password").send_keys(config["password"])
    
@when('El usuario ingresa sus credenciales de manera incorrecta')
def incorrect_credentials(context):
    context.driver.find_element(By.ID,"username").send_keys("practice incorrect")
    context.driver.find_element(By.ID,"password").send_keys("SuperSecretPasswordIncorrect!")
    
@when('El usuario hace clic en el botón ingresar')
def click_login_button(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Login')]").click()
    
@then('El usuario visualiza el mensaje de credenciales incorrectas')
def login_fail(context):
    assert "Your username is invalid!" in context.driver.page_source
    context.driver.quit()

@then('El usuario es redirigido a la página de inicio o home')
def login_success(context):
    assert "Secure Page page for Automation Testing Practice" in context.driver.title 

@then('El usuario visualiza el mensaje de bienvenida')
def login_success(context):
    assert "Welcome to the Secure Area. When you are done click logout below." in context.driver.page_source

@then('El usuario cierra sesión')
def login_success(context):
    context.driver.find_element(By.XPATH,"//i[@class='icon-2x icon-signout'][contains(.,'Logout')]").click()
    context.driver.quit()