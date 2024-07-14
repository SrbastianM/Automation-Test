from functions.global_functions import GlobalFunctions
import unittest
import json
import time

with open('config.json', 'r') as url:
    config = json.load(url)
class TestFields(unittest.TestCase):
        
    def test_web_is_open(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.teardown()
    def test_login_email_field_accept_only_email(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'login-email')]", .3, "123123")
        driver.select_input_field_by_xpath("//input[contains(@type,'password')]", .3, config["login_credentials"]["correct_user"]["password"])
        alert_is_visible =driver.text_is_visible("//p[contains(.,'Your email or password is incorrect!')]", .3)
        
        if alert_is_visible == True:
            pass
        else:
            return False
        driver.teardown()
    def test_login_password_field_accept_only_password(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'login-email')]", .3, config["login_credentials"]["correct_user"]["email"])
        driver.select_input_field_by_xpath("//input[contains(@type,'password')]", .3, config["login_credentials"]["correct_user"]["password"])
        alert_is_visible =driver.text_is_visible("//p[contains(.,'Your email or password is incorrect!')]", .3)
        
        if alert_is_visible == True:
            pass
        else:
            return False
        driver.teardown()
    def test_email_login_form_alert_is_visible(self):
        driver = GlobalFunctions()
        driver.setUp(.2)
        driver.select_signup_link("//a[contains(.,'Signup / Login')]", .3)
        driver.select_input_field_by_xpath("//input[contains(@data-qa,'login-email')]", .3, config["login_credentials"]["correct_user"]["email"])
        driver.select_input_field_by_xpath("//input[contains(@type,'password')]", .3, config["login_credentials"]["correct_user"]["password"])
        driver.select_and_click_button_by_xpath("//button[@type='submit'][contains(.,'Login')]", .3)
        alert_is_visible =driver.text_is_visible("//p[contains(.,'Your email or password is incorrect!')]", .3)
        
        if alert_is_visible == True:
            pass
        else:
            return False
        driver.teardown()

if __name__ == '__main__':
    unittest.main()