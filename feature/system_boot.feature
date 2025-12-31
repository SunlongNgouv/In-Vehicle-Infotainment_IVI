Feature: IVI System Boot
  The IVI system must boot reliably and expose core services after startup.

  Background:
    Given the IVI system is powered off

  Scenario: Cold boot succeeds and home screen becomes available
    When the system is powered on
    Then the home screen should be available
    And the system state should be "ON"

  Scenario: Boot time is within acceptable threshold
    When the system is powered on
    Then the boot time should be less than 30 seconds

  Scenario: Power cycle resets transient states
    Given Bluetooth is enabled
    And media is playing
    When the system is powered off
    And the system is powered on
    Then Bluetooth should be disabled
    And media should not be playing

  Scenario: Boot fails if battery voltage is too low
    Given the battery voltage is 10.5 volts
    When the system is powered on
    Then the boot should fail with error "LOW_VOLTAGE"

  Scenario Outline: Boot behavior depends on battery voltage
    Given the battery voltage is <voltage> volts
    When the system is powered on
    Then the boot result should be "<result>"

    Examples:
      | voltage | result      |
      | 12.6    | SUCCESS     |
      | 11.8    | SUCCESS     |
      | 10.9    | LOW_VOLTAGE |
