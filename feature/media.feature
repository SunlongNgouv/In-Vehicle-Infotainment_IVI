Feature: Media Playback
  The IVI media application should support basic playback controls and handle errors gracefully.

  Background:
    Given the IVI system is powered on
    And the media app is opened

  Scenario: Media app loads and shows library
    Then the media library should be visible

  Scenario: Play a track successfully
    Given a track "Drive Time" is available
    When the user selects track "Drive Time"
    And the user presses play
    Then media should be playing
    And the current track should be "Drive Time"

  Scenario: Pause and resume playback
    Given media is playing
#    When the user presses pause
#    Then media should be paused
#    When the user presses play
#    Then media should be playing

#  Scenario: Skip to next track updates the current track
#    Given a playlist exists with tracks:
#      | title       |
#      | Drive Time  |
#      | Night Ride  |
#      | Morning Run |
#    And the current track is "Drive Time"
#    When the user presses next
#    Then the current track should be "Night Ride"
#
#  Scenario: Volume changes within allowed range
#    Given the volume is set to 10
#    When the user sets the volume to 15
#    Then the volume should be 15
#
#  Scenario Outline: Setting invalid volume is rejected
#    When the user sets the volume to <volume>
#    Then the volume change should be rejected with error "INVALID_VOLUME"
#
#    Examples:
#      | volume |
#      | -1     |
#      | 101    |
#      | 999    |
#
#  Scenario: Media playback stops when system powers off
#    Given media is playing
#    When the system is powered off
#    Then media should stop
#    And the media app should be closed
