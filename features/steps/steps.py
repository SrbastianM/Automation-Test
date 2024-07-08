from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json

with open('config.json', 'r') as url:
    config = json.load(url)

@given('El usuario ingresó a la plataforma')
def webDriver(context):
    context.driver = webdriver.Firefox()
    context.driver.get(config["url"])
    context.driver.maximize_window()
    time.sleep(10)
     
    try:
        cookieAlert = context.driver.find_element(By.XPATH, "//button[contains(text(),'Aceptar')]")
        
        if cookieAlert.is_displayed() and cookieAlert.is_enabled():
            try:
                cookieAlert.click()
                print("Cookie accepted with selenium click")
            except:
                 context.driver.execute_script("arguments[0].click();", cookieAlert)
                 print("Cookie accepted with selenium click")
            print("Cookies is accepted")
    except Exception as e:
        print("Element Not found or not clickable", str(e))
        context.driver.quit()
    
    

@when('El usuario ingresa sus credenciales')
def credentials(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.ID,"userName").send_keys(config["correctUser"]["username"])
    context.driver.find_element(By.ID,"password").send_keys(config["correctUser"]["password"])
    
@when('El usuario ingresa sus credenciales de manera incorrecta')
def incorrect_credentials(context):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.XPATH,"//input[@id='userName']").send_keys(config["incorrectUser"]["username"])
    context.driver.find_element(By.XPATH,"//input[contains(@type,'password')]").send_keys(config["incorrectUser"]["password"])
    
@when('El usuario hace clic en el botón ingresar')
def click_login_button(context):
    time.sleep(2)
    btnLogin = context.driver.find_element(By.XPATH, "//button[contains(text(),'Entrar')]")
    if btnLogin.is_displayed() and btnLogin.is_enabled():
        btnLogin.click()
    
@then('El usuario visualiza el mensaje de credenciales incorrectas')
def login_fail(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//p[@class='first-body'][contains(.,'Usuario o contraseña incorrectos.')]")
    assert " Usuario o contraseña incorrectos. " in context.driver.page_source
    context.driver.find_element(By.XPATH, "//button[@class='btn'][contains(.,'Regresar')]").click()
    context.driver.quit()

@then('El usuario es redirigido a la página de inicio o home')
def login_success(context):
    assert "P AAutomated Company Pass and User" in context.driver.title 

@then('El usuario visualiza el mensaje de bienvenida')
def show_welcome_message(context):
    context.driver.find_element(By.XPATH, "//p[@class='name-menu'][contains(.,'Hola, User')]")
    time.sleep(2)
    

@then('El usuario cierra sesión')
def user_logout(context):
    context.driver.find_element(By.XPATH,"//img[contains(@class,'icon-close-s')]").click()
    time.sleep(2)
    context.driver.quit()