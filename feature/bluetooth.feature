#Feature: Bluetooth Pairing & Connectivity
#  Bluetooth should pair/connect reliably and enforce correct state rules.
#
#  Background:
#    Given the IVI system is powered on
#    And the Bluetooth settings screen is opened
#
#  Scenario: Enable Bluetooth successfully
#    Given Bluetooth is disabled
#    When the user enables Bluetooth
#    Then Bluetooth should be enabled
#
#  Scenario: Discover nearby devices when Bluetooth is enabled
#    Given Bluetooth is enabled
#    And device discovery is started
#    Then the list of discovered devices should include:
#      | name          |
#      | SunlongPhone  |
#      | TestHeadset   |
#
#  Scenario: Pair with a device successfully
#    Given Bluetooth is enabled
#    And a device named "SunlongPhone" is discoverable
#    When the user selects device "SunlongPhone"
#    And the user confirms pairing
#    Then the device "SunlongPhone" should be paired
#    And the connection status for "SunlongPhone" should be "CONNECTED"
#
#  Scenario: Pairing fails when PIN is incorrect
#    Given Bluetooth is enabled
#    And a device named "SunlongPhone" is discoverable
#    When the user selects device "SunlongPhone"
#    And the user enters PIN "0000"
#    Then pairing should fail with error "INVALID_PIN"
#    And the device "SunlongPhone" should not be paired
#
#  Scenario: Do not allow pairing when Bluetooth is disabled
#    Given Bluetooth is disabled
#    When the user selects device "SunlongPhone"
#    Then the action should fail with error "BLUETOOTH_OFF"
#
#  Scenario Outline: Auto-connect behavior for known devices
#    Given Bluetooth is enabled
#    And the device "<device>" is paired
#    When the system is powered off
#    And the system is powered on
#    Then the connection status for "<device>" should be "<status>"
#
#    Examples:
#      | device        | status       |
#      | SunlongPhone  | CONNECTED    |
#      | TestHeadset   | DISCONNECTED |
