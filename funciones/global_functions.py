import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver

with open('config.json', 'r') as url:
    config = json.load(url)
class GlobalFunctions():
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        
    def setUp(self, t):
        self.driver.get(config["url"])
        self.driver.maximize_window()
        time.sleep(t)
    
    def teardown(self):
        self.driver.quit()

    def time_sleep(t):
        set_time = time.sleep(t)
        return set_time

    def select_signup_link(self, xpath, t):
        link = self.driver.find_element(By.XPATH, xpath)
        time.sleep(t)
        link.click()
    
    def select_name_signup_input_field(self, xpath, t, input):
        input_field  = self.driver.find_element(By.XPATH, xpath)
        time.sleep(t)
        input_field.send_keys(input)
    
    def select_email_signup_input_field(self, xpath, t, input):
        input_field  = self.driver.find_element(By.XPATH, xpath)
        time.sleep(t)
        input_field.send_keys(input)
    
    def select_and_click_button_by_xpath(self, xpath, t):
        try: 
            button = WebDriverWait(self.driver, t).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            button.click()
        except ElementClickInterceptedException:
            try:
                self.driver.execute_script("window.scrollTo(0, 900);")
                button.click()
                time.sleep(t)
            except:
                return False
        
    
    def select_radio_button_by_xpath(self, xpath, t):
        try:
            radio_button = self.driver.find_element(By.XPATH, xpath)
            if radio_button.is_selected():
                pass
            else:
                radio_button.click()
                time.sleep(t)
        except NoSuchElementException:
            return False
    def select_password_input(self, xpath, t, password):
        input = self.driver.find_element(By.XPATH, xpath)
        time.sleep(t)
        input.send_keys(password)
        
    def select_element_in_dropdown_by_index_xpath(self, xpath, t, element):
        dropdown = self.driver.find_element(By.XPATH, xpath)
        select_dropdown = Select(dropdown)
        time.sleep(t)
        select_dropdown.select_by_index(element)
    
    def select_element_in_dropdown_by_value_xpath(self, xpath, t, element):
        dropdown = self.driver.find_element(By.XPATH, xpath)
        select_dropdown = Select(dropdown)
        time.sleep(t)
        select_dropdown.select_by_value(element)
    
    def select_input_field_by_xpath(self, xpath, t, input):
        input_field = self.driver.find_element(By.XPATH, xpath)
        time.sleep(t)
        input_field.send_keys(input)
        
    def text_is_visible(self, xpath, t):
        try :
            text = self.driver.find_element(By.XPATH, xpath)
            if text.is_displayed() and text.is_enabled():
                return True
            time.sleep(t)
            return text.is_displayed()
        except NoSuchElementException:
                return False
    
    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, 720);")