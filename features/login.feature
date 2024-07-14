Feature: Login Functionally
   Scenario:  Login successful (user & password)
      Given the browser is launched
      When the user navigates to the website
      Then the home page should be visible
      When the user clicks on the signup link page
      Then the subtitle "Login to your account" should be visible
      When user fill in the email and password fields
      And the user clicks the Login button
      Then the "Logout" message should be visible
      And the account should be logged in successfully


   Scenario: Login unsuccessful (user & password)
      Given the browser is launched
      When the user navigates to the website
      Then the home page should be visible
      When the user clicks on the signup link page
      Then the subtitle "Login to your account" should be visible
      When user fill with wrong information the email and password fields
      Then the "Your email or password is incorrect!" message should be visible
      And the account should not be logged in successfully