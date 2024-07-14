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
    
    @then('the subtitle "Login to your account" should be visible')
    def step_imp(context):
        text = context.driver.find_element(By.XPATH, "//h2[contains(.,'Login to your account')]")
        try :
            if text.is_displayed() and text.is_enabled():
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False
    @when('user fill in the email and password fields')
    def step_imp(context):
        email_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'login-email')]")
        password_field = context.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        email_field.send_keys(config["login_credentials"]["correct_user"]["email"])
        password_field.send_keys(config["login_credentials"]["correct_user"]["password"])
    
    @when('user fill with wrong information the email and password fields')
    def step_imp(context):
        email_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'login-email')]")
        password_field = context.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        email_field.send_keys(config["login_credentials"]["incorrect_user"]["email"])
        password_field.send_keys(config["login_credentials"]["correct_user"]["password"])

    
    @when('the user clicks the Login button')
    def step_imp(context):
        sign_up_button = context.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Login')]")
        sign_up_button.click()
        time.sleep(8)
    
    @then('the "Logout" message should be visible')
    def step_imp(context):
        try :
            text = context.driver.find_element(By.XPATH, "//a[contains(.,'Logout')]")
            delete_account = context.driver.find_element(By.XPATH, "//a[contains(.,'Delete Account')]")
            if text.is_displayed() and text.is_enabled():
                delete_account.click()
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False

    @then('the "Your email or password is incorrect!" message should be visible')
    def step_imp(context):
        try :
            text = context.driver.find_element(By.XPATH, "//p[contains(.,'Your email or password is incorrect!')]")
            if text.is_displayed() and text.is_enabled():
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False
    
    @then('the account should not be logged in successfully')
    def step_imp(context):
        context.driver.quit()
    
    @then("the account should be logged in successfully")
    def step_imp(context):
        context.driver.quit()