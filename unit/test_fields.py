from funciones.global_functions import GlobalFunctions
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
        
if __name__ == '__main__':
    unittest.main()