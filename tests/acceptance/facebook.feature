Feature: Facebook's Home Page and Cookie Page
  As a User
  I want to check the Home Page and Cookie Page of Facebook
  So that I can sign up or login

  Scenario:
    Given the User navigates to the homepage
    When the User is on the "home_page"
    Then the User can see "facebook" icon
    And the User clicks "Cookies" link
    And the User is on the "cookies_page"

  Scenario: Cookie Page
    Given the User navigates to the cookiepage
    When the User can see cookie text