Feature: Registration Functionally

    Scenario: Register one user successfull (username & email)
        Given the browser is launched
        When the user navigates to the website
        Then the home page should be visible
        When the user clicks on the signup link page
        Then the subtitle "New User Signup!" should be visible
        When user fill in the name and email address fields
        And the user clicks the signup button
        Then the "Enter Account Information" should be visible
        When the user fills in the account information fields
        Then the ADDRESS INFORMATION section should be visible
        When the user fills the address information fields
        And the user clicks the Create Account button
        Then the "Account Created!" message should be visible
        And the account should be created successfully

    Scenario: Register one user unssuccesfully
        Given the browser is launched
        When the user navigates to the website
        Then the home page should be visible
        When the user clicks on the signup link page
        Then the subtitle "New User Signup!" should be visible
        When user fill name field only
        And the user clicks the signup button
        Then the account registration should fail
