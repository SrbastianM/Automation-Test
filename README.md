# Automation Project
---
Small project to improve my automation skills using selenium and behave
---
## Points of interest:
- Remember install ```behave``` using the following command: ```pip install selenium behave``` if you don't have it  
- To start the robot, you need to use the following command: ```behave``` in your terminal. This command runs all the scenarios in the folder features
- To use the robot you need to set your own settings for the page, remember create your json file and change it for your own properties beacuse if you dont do it the robot wasn't run. Using a config.json file like this:
```json
{
    "url": "https://www.automationexercise.com/",
    "login_credentials": {
        "correct_user": {
            "username": "jhon@example.com",
            "password": "Cutepassword1*"
        },
        "incorrect_user": {
            "username": "usertecvac2",
            "password": "UserTest2*"
        }
    },
    "register_credentials": {
        "account_information": {
            "name": "John",
            "email": "jhon@example.com",
            "password": "Cutepassword1*",
            "date_of_birth": "1/1/2000"
        },
        "address_information": {
            "first_name": "John",
            "last_name": "Doe",
            "company": "Example Inc",
            "address": "123 Main 5t",
            "country": "United States",
            "state": "CA",
            "city": "Los Angeles",
            "zipcode": "90001",
            "mobile_number": "123789"
        }
    }
}
```
- The unit test's are checking if the robot is normally or have some problem. To use it you need to use the following command ```py -m unittest .\unit\test_registration.py -v``` or ```py -m unittest .\unit\test_registration.py```
---
Thanks for watching my project! Follow me if you want
