@facebook
Feature: Facebook's Home Page and Cookie Page
  As a User
  I want to check the Home Page and Cookie Page of Facebook
  So that I can sign up or login

  @smoke
  Scenario: User checks fields and navigation of facebook home page
    Given the User navigates to the "home page"
    When the User is on the "home_page"
    Then the User can see "facebook" icon
    And the User clicks "Cookies" link
    And the User is on the "cookies_page"

  @regression
  Scenario: User checks the cookie text and navigation links
    Given the User navigates to the "cookies page"
    When the User can see cookie text
    Then the User can see 4 navigation links

  @smoke
    @regression
  Scenario Outline: User checks the presence of email and password field in various pages
    Given the User navigates to the "<Page>"
    When the User can see "facebook" icon
    Then the User can see "email" textbox
    And the User can see "password" textbox
    Examples:
      | Page          |
      | home page     |
      | location page |