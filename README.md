# Automation Project
---
Small project to improve my automation skills using selenium and behave
---
## Points of interest:
- Remember install ```behave``` using the following command: ```pip install selenium behave``` if you don't have it  
- To start the robot, you need to use the following command: ```behave``` in your terminal.
- To use the robot you need to set your own url and settings for the page you want to use. Using a config.json file like this:
```json
{
    "url": "www.yoururl.com",
    "correctUser": {
        "username": "yourName",
        "password": "yourPassword*"
    },
    "incorrectUser": {
        "username": "incorrectUsername",
        "password": "incorrectPassword*"
    }
}
```
- The unit test checks the json files shown above. To use it you need to use the following command ```py -m unittest .\unit\test_main.py``` or ```py -m unittest .\unit\test_main.py -v```
---
Thanks for watching my project! Follow me if you want
