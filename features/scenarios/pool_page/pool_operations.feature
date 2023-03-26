Feature: Pool Page Operations

  Scenario: Pool Creation
    Given The user is in Pool page
    When Click on "Create" button
    And Enter Pool Name: "Pool-Name"
    And Select Optimize Pool for: "Performance/Capacity"
    And Select Recommended RAID Mode: "RAID-Mode"
    And Select Type of Disk Drive: "Disk-Type"
    And Select Recommended Disk Number: "Disk-Number"
    And Select disks: "automatically/manually"
    And Enable cache: "True/False"
    And Click on Create button in Pool Creation modal
    Then Storage Pool "Pool-Name" should be created successfully


  Scenario: Delete Pool
    Given The user is in Pool page
    When Select desired Pool in Pool Configuration table: "Pool-Name"
    And Click on Delete button in Pool page
    And Press Delete button in confirmation message
    Then The Pool should be deleted successfully: "Pool-Name"


  Scenario: Rename Pool
    Given The user is in Pool page
    When Select desired Pool in Pool Configuration table: "Pool-Name"
    And Click on Rename button in Pool page
    And Enter new Pool name: "Pool-New-Name"
    And Press Rename button
    Then Pool "Pool-Name" should be renamed successfully to "Pool-New-Name"


  Scenario: Pool Extension
    Given The user is in Pool page
    When Select desired Pool in Pool Configuration table: "Pool-Name"
    And Click on Extend button in Pool page
    And Select Disk Number: "Disk-Number" in Pool Extension modal
    And Select disks: "automatically/manually"
    And Click on Extend button in Pool Extension modal
    Then Number of disks should be shown correctly in Pool Configuration table for pool: "Pool-Name"
