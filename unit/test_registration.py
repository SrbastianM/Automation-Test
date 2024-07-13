from funciones.global_functions import GlobalFunctions
import unittest
import json
import time

with open('config.json', 'r') as url:
    config = json.load(url)
class TestRegistration(unittest.TestCase):
        
    def test_web_is_open(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.teardown()
    
    def test_signup_link_exists(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        driver.teardown()
    
    def test_visible_text_signup(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        time.sleep(2)
        driver.text_is_visible("//h2[contains(.,'New User Signup!')]", .3)
        driver.teardown()
        
    def test_set_name_and_email_in_signup(self):
        driver = GlobalFunctions()
        driver.setUp(.3)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        time.sleep(2)
        driver.select_name_signup_input_field("//input[@name='name']", .2, config["register_credentials"]["account_information"]["name"])
        driver.select_email_signup_input_field("//input[contains(@data-qa,'signup-email')]", .2, config["register_credentials"]["account_information"]["email"])
        driver.select_and_click_button_by_xpath("//button[@type='submit'][contains(.,'Signup')]", .3)
        driver.teardown()
    
    def test_set_account_information(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        time.sleep(1.5)
        driver.select_name_signup_input_field("//input[@name='name']", .2, config["register_credentials"]["account_information"]["name"])
        driver.select_email_signup_input_field("//input[contains(@data-qa,'signup-email')]", .2, config["register_credentials"]["account_information"]["email"])
        driver.select_and_click_button_by_xpath("//button[@type='submit'][contains(.,'Signup')]", .3)
        driver.select_radio_button_by_xpath("//input[@type='radio'][contains(@id,'gender1')]", .3)
        driver.select_password_input("//input[contains(@type,'password')]", .3, config["register_credentials"]["account_information"]["password"])
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'days')]", .5, config["register_credentials"]["account_information"]["date_of_birth"].split("/")[0])
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'months')]", .5, config["register_credentials"]["account_information"]["date_of_birth"].split("/")[1])
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'years')]", .5, config["register_credentials"]["account_information"]["date_of_birth"].split("/")[2])
        time.sleep(2)
        driver.teardown()
    
    def test_set_address_information(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        time.sleep(1.5)
        driver.select_name_signup_input_field("//input[@name='name']", .2, config["register_credentials"]["account_information"]["name"])
        driver.select_email_signup_input_field("//input[contains(@data-qa,'signup-email')]", .2, config["register_credentials"]["account_information"]["email"])
        driver.select_and_click_button_by_xpath("//button[@type='submit'][contains(.,'Signup')]", .3)
        driver.text_is_visible("//b[contains(.,'Address Information')]", .3)
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'first_name')]", .3, config["register_credentials"]["address_information"]["first_name"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'last_name')]", .3, config["register_credentials"]["address_information"]["last_name"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'company')]", .3, config["register_credentials"]["address_information"]["company"])
        driver.select_input_field_by_xpath("//input[contains(@name,'address1')]", .3, config["register_credentials"]["address_information"]["address"])
        driver.scroll_down_page()
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'country')]", .3, config["register_credentials"]["address_information"]["country"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'state')]", .3, config["register_credentials"]["address_information"]["state"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'city')]", .3, config["register_credentials"]["address_information"]["city"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'zipcode')]", .3, config["register_credentials"]["address_information"]["zipcode"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'mobile_number')]", .3, config["register_credentials"]["address_information"]["mobile_number"])
        driver.teardown()
        
    def test_register_successfully(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        time.sleep(1.5)
        driver.select_name_signup_input_field("//input[@name='name']", .2, config["register_credentials"]["account_information"]["name"])
        driver.select_email_signup_input_field("//input[contains(@data-qa,'signup-email')]", .2, config["register_credentials"]["account_information"]["email"])
        driver.select_and_click_button_by_xpath("//button[@type='submit'][contains(.,'Signup')]", .3)
        driver.select_radio_button_by_xpath("//input[@type='radio'][contains(@id,'gender1')]", .3)
        driver.select_password_input("//input[contains(@type,'password')]", .3, config["register_credentials"]["account_information"]["password"])
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'days')]", .5, config["register_credentials"]["account_information"]["date_of_birth"].split("/")[0])
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'months')]", .5, config["register_credentials"]["account_information"]["date_of_birth"].split("/")[1])
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'years')]", .5, config["register_credentials"]["account_information"]["date_of_birth"].split("/")[2])
        driver.text_is_visible("//b[contains(.,'Address Information')]", .3)
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'first_name')]", .3, config["register_credentials"]["address_information"]["first_name"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'last_name')]", .3, config["register_credentials"]["address_information"]["last_name"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'company')]", .3, config["register_credentials"]["address_information"]["company"])
        driver.select_input_field_by_xpath("//input[contains(@name,'address1')]", .3, config["register_credentials"]["address_information"]["address"])
        driver.scroll_down_page()
        driver.select_element_in_dropdown_by_value_xpath("//select[contains(@data-qa,'country')]", .3, config["register_credentials"]["address_information"]["country"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'state')]", .3, config["register_credentials"]["address_information"]["state"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'city')]", .3, config["register_credentials"]["address_information"]["city"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'zipcode')]", .3, config["register_credentials"]["address_information"]["zipcode"])
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'mobile_number')]", .3, config["register_credentials"]["address_information"]["mobile_number"])
        driver.select_and_click_button_by_xpath("//button[@type='submit'][contains(.,'Create Account')]", .3)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()