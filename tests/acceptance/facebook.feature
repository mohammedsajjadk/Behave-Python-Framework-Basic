Feature: Facebook's Home Page and Cookie Page
  As a User
  I want to check the Home Page and Cookie Page of Facebook
  So that I can sign up or login

  Scenario: User checks fields and navigation of facebook home page
    Given the User navigates to the homepage
    When the User is on the "home_page"
    Then the User can see "facebook" icon
    And the User clicks "Cookies" link
    And the User is on the "cookies_page"

  Scenario: User checks the cookie text and navigation links
    Given the User navigates to the cookiepage
    When the User can see cookie text
    Then the User can see 4 navigation links