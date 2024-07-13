from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import json

with open('config.json', 'r') as url:
    config = json.load(url)
    #Scenario 1    
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
    #Here code crashes
    @then('the subtitle "New User Signup!" should be visible')
    def step_imp(context):
        text = context.driver.find_element(By.XPATH, "//h2[contains(.,'New User Signup!')]")
        try :
            if text.is_displayed() and text.is_enabled():
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False
        
    @when('user fill in the name and email address fields')
    def step_imp(context):
        name_field = context.driver.find_element(By.XPATH, "//input[@name='name']")
        email_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'signup-email')]")
        name_field.send_keys(config["register_credentials"]["account_information"]["name"])
        email_field.send_keys(config["register_credentials"]["account_information"]["email"])
    
    @when('user fill name field only')
    def step_imp(context):
        name_field = context.driver.find_element(By.XPATH, "//input[@name='name']")
        name_field.send_keys(config["register_credentials"]["account_information"]["name"])
           
    @when('the user clicks the signup button')
    def step_imp(context):
        sign_up_button = context.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Signup')]")
        sign_up_button.click()
        time.sleep(2)
    
    @then('the "Enter Account Information" should be visible')
    def step_imp(context):
        text = context.driver.find_element(By.XPATH, "//b[contains(.,'Enter Account Information')]")
        try :
            if text.is_displayed() and text.is_enabled():
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False
    
    @then('the account registration should fail')
    def step_imp(context):
        context.driver.quit()
    
    @when('the user fills in the account information fields')
    def step_imp(context):
        try:
            radio_button = context.driver.find_element(By.XPATH, "//input[@type='radio'][contains(@id,'gender1')]")
            if radio_button.is_selected():
                pass
            else:
                radio_button.click()
        except NoSuchElementException:
            return False
        input = context.driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        input.send_keys(config["register_credentials"]["account_information"]["password"])
        
        select_drop_downlist_days = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'days')]"))
        select_drop_downlist_month = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'month')]"))
        select_drop_downlist_year = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'year')]"))
        
        select_drop_downlist_days.select_by_value("1")
        select_drop_downlist_month.select_by_value("1")
        select_drop_downlist_year.select_by_value("2000")
    
    
    @then("the ADDRESS INFORMATION section should be visible")
    def step_imp(context):
        try :
            text = context.driver.find_element(By.XPATH, "//b[contains(.,'Address Information')]")
            if text.is_displayed() and text.is_enabled():
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False
    #AQUI ESTA FALLANDO
    @when("the user fills the address information fields")
    def step_imp(context):
        first_name_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'first_name')]")
        last_name_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'last_name')]")
        company_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'company')]")
        address_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'address')]")
        country_dropdown = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'country')]"))
        state_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'state')]")
        city_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'city')]")
        zipcode_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'zipcode')]")
        mobile_number_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'mobile_number')]")
        
        
        first_name_field.send_keys( config["register_credentials"]["address_information"]["first_name"])
        last_name_field.send_keys( config["register_credentials"]["address_information"]["last_name"])
        company_field.send_keys( config["register_credentials"]["address_information"]["company"])
        address_field.send_keys( config["register_credentials"]["address_information"]["address"])
        context.driver.execute_script("window.scrollTo(0, 720);")
        country_dropdown.select_by_value(config["register_credentials"]["address_information"]["country"])
        state_field.send_keys( config["register_credentials"]["address_information"]["state"])
        city_field.send_keys( config["register_credentials"]["address_information"]["city"])
        zipcode_field.send_keys( config["register_credentials"]["address_information"]["zipcode"])
        mobile_number_field.send_keys( config["register_credentials"]["address_information"]["mobile_number"])
        
    @when("the user clicks the Create Account button")
    def step_imp(context):
        try: 
            button = WebDriverWait(context.driver, .3).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Create Account')]")))
            button.click()
        except ElementClickInterceptedException:
            try:
                context.driver.execute_script("window.scrollTo(0, 900);")
                button.click()
                time.sleep(.3)
            except:
                return False
    
    @then('the "Account Created!" message should be visible')
    def step_imp(context):
        try :
            text = context.driver.find_element(By.XPATH, "//b[contains(.,'Account Created!')]")
            if text.is_displayed() and text.is_enabled():
                return True
            return text.is_displayed()
        except NoSuchElementException:
                return False
    
    @then("the account should be created successfully")
    def step_imp(context):
        context.driver.quit()