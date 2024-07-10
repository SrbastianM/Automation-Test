from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import json

from funciones.global_functions import time_sleep

with open('config.json', 'r') as url:
    config = json.load(url)
    

    #Scenario 1    
    @given("the browser is launched")
    def step_imp(context):
        context.driver = webdriver.Firefox()
        context.driver.maximize_window()
    
    @when("the user navigates to the website")
    def step_imp(context):
        context.driver.get(config["url"])
        time_sleep(2)
    
    @then("the home page should be visible")
    def step_imp(context):
        assert "Website for automation practice" in context.driver.page_source
    
    @when("the user clicks on the signup button page")
    def step_imp(context):
        sign_up_button_page =  context.driver.find_element(By.XPATH, "//a[contains(.,'Signup / Login')]")
        sign_up_button_page.click()
        time_sleep(2)
    
    @when("the New User signup should be visible")
    def step_imp(context):
        signup_text = context.driver.find_element(By.XPATH, "//h2[contains(.,'New User Signup!')]")
        if signup_text.is_displayed() and signup_text.is_enabled():
            print("New User Signup is visible")
        time_sleep(2)
        
    @when("user fill in the name and email address with:")
    def step_imp(context):
        name_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'signup-name')]").send_keys(config["register_credentials"]["account_information"]["name"])
        email_field = context.driver.find_element(By.XPATH, "//input[contains(@data-qa,'signup-email')]")
        name_field.send_keys(Keys.TAB, config["register_credentials"]["account_information"]["name"])
        email_field.send_keys(Keys.TAB, config["register_credentials"]["account_information"]["email"])
        
           
    @when("the user clicks on the signup button")
    def step_imp(context):
        sign_up_button = context.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Signup')]")
        sign_up_button.click()
        time_sleep(2)
    
    @then("the 'Enter Account Information' should be visible")
    def step_imp(context):
        assert "Enter Account Information" in context.driver.page_source
    
    @when("the user fills in the account information with:")
    def step_imp(context):
        select_drop_downlist_days = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'days')]"))
        select_drop_downlist_month = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'month')]"))
        select_drop_downlist_year = Select(context.driver.find_element(By.XPATH, "//select[contains(@data-qa,'year')]"))
        
        select_drop_downlist_days.select_by_value("1")
        select_drop_downlist_month.select_by_value("1")
        select_drop_downlist_year.select_by_value("1990")
    
    @then("the 'Address Information' should be visible")
    def step_imp(context):
        assert "Address Information" in context.driver.page_source
    
    @when("the user fills in the address information with:")
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
        
        
        first_name_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["first_name"])
        last_name_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["last_name"])
        company_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["company"])
        address_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["address"])
        country_dropdown.select_by_value("UA")
        state_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["state"])
        city_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["city"])
        zipcode_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["zipcode"])
        mobile_number_field.send_keys(Keys.TAB, config["register_credentials"]["address_information"]["mobile_number"])
        
    @then("the user clicks the Create Account button")
    def step_imp(context):
        create_account_button = context.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Create Account')]")
        create_account_button.click()
        time_sleep(2)
    
    @then("the 'Account Created!' message should be visible")
    def step_imp(context):
        assert "Account Created!" in context.driver.page_source
    
    @then("the account should be created")
    def step_imp(context):
        context.driver.quit()