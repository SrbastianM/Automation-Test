from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json
 
with open('config.json', 'r') as url:
    config = json.load(url) 
    @given('the browser is launched')
    def step_imp(context):
        context.driver = webdriver.Firefox()
        context.driver.maximize_window()
        
    @when('the user navigates to the website')
    def step_imp(context):
        context.driver.get(config["url"])
        time.sleep(2)
    
    @then('the home page should be visible')
    def step_imp(context):
        assert "Website for automation practice" in context.driver.page_source
    
    @when('the user clicks on the signup link page')
    def step_imp(context):
        sign_up_button_page =  context.driver.find_element(By.XPATH, "//a[contains(.,'Signup / Login')]")
        sign_up_button_page.click()
        time.sleep(2)