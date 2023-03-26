Feature: Pool Test Scenarios
  Scenario: Pool-Create-Extend-Rename-Delete
    Given Create Pool
    When Extend Pool
    And Rename Pool
    Then Delete Pool

  Scenario: Pool-Delete
    Given Delete Pool

  Scenario: Pool-Rename
    Given Rename Pool
