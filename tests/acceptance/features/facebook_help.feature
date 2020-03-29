@facebook-help
Feature: Facebook's Home Page and Cookie Page
  As a User
  I want to check the Home Page and Cookie Page of Facebook
  So that I can sign up or login

  Background: Navigating to Help Page
    Given the User navigates to the "help page"

  @regression
  Scenario: User checks fields and navigation of facebook home page
    Then the User can see the Questions Text

  @smoke
  Scenario: User checks the navigation bar
    Then the User can see the following:
      | Navigation bar         |
      | Using Facebook         |
      | Managing Your Account  |
      | Privacy and Safety     |
      | Policies and Reporting |
