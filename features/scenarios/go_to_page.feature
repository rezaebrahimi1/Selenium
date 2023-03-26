Feature: Go to desired User Interface page

  Scenario: Go to Pool page
    Given The user Logged into User Interface
    When Click on "Storage" from side-menu
    And Click on "Pool" from Storage sub-menu
    Then The user is in Pool page