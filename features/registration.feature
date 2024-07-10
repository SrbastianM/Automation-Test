Feature: Registration Functionally

    Scenario: Register one user successfull (username & email)
        Given the browser is launched
        When the user navigates to the website
        Then the home page should be visible
        When the user clicks on the signup button page
        Then the New User signup should be visible
        When user fill in the name and email address with:
            | Name  | John Doe         |
            | Email | jhon@example.com |
        And the user clicks the signup button
        Then the the ENTER ACCOUNT should be visible
        When the user fills in the account information with:
            | Title         | Mr               |
            | Name          | John Doe         |
            | Email         | jhon@example.com |
            | Password      | *******          |
            | Date of birth | 01/01/1990       |
        Then the ADDRESS INFORMATION section should be visible
        When the user fills in the address information with:
            | First Name    | John        |
            | Last Name     | Doe         |
            | Company       | Example Inc |
            | Address       | 123 Main 5t |
            | Country       | USA         |
            | State         | CA          |
            | City          | Los Angeles |
            | Zipcode       | 90001       |
            | Mobile Number | 123789      |
        And the user clicks the Create Account button
        Then the "Account Created!" message should be visible
        And the account should be created successfully

    Scenario: Register one user unssuccesfully
        Given the user is launched
        When the user clicks on the signup button
        Then the enter account information should be visible
        When the user fills in the account information with:
            | Title         | (Leave Empty)    |
            | Name          | John Doe         |
            | Email         | john@example.com |
            | Password      | *******          |
            | Date of birth | 01/01/1990       |
        And the user clicks the Create Account button
        Then the alert "PLEASE FILL OUT THIS FIELD" is visible
        And the account registration should fail