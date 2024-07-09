from funciones.convert_to_upper import to_upper
import unittest
import json


with open('config.json', 'r') as url:
    config = json.load(url)

class TestMain(unittest.TestCase):
    
    def test_main(self):
        result = "HELLO"
        self.assertEqual(result, to_upper("hello"))
        
    def test_url_exists(self):
        self.assertIn("url", config)
        self.assertIsInstance(config["url"], str)
    
    def test_correct_user(self):
        correctUser = config.get("correctUser", {})
        self.assertIn('username', correctUser)
        self.assertIn('password', correctUser)
        self.assertIsInstance(correctUser["username"], str)
        self.assertIsInstance(correctUser["password"], str) 
        
    
if __name__ == '__main__':
    unittest.main()