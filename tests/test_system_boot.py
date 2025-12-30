from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers

import pytest

File = 'system_boot.feature'
File_Dir = 'feature'
Base_Dir = Path(__file__).resolve().parent.parent
Feature_File = Base_Dir.joinpath(File_Dir).joinpath(File)
print('Feature file exists or not: ', Feature_File.exists())

scenarios(str(Feature_File))

@given('the IVI system is powered off')
def default_state(ivi_system):
    print('In background state')
    ivi_system.power_off()
    assert ivi_system.power_state == 'OFF'

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()
    assert ivi_system.power_state == 'ON'

@then('the home screen should be available')
def home_screen_available(ivi_system):
    assert ivi_system.is_home_screen_available() is True

@then('the system state should be "ON"')
def system_state(ivi_system):
    assert ivi_system.power_state == 'ON'

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()

@then('the boot time should be less than 30 seconds')
def boot_time(ivi_system):
    assert ivi_system.boot_time_default < 30

#####

@given('Bluetooth is enabled')
def bluetooth_enabled(ivi_system):
    ivi_system.power_on()
    assert ivi_system.power_state == 'ON'
    ivi_system.enable_bluetooth()
    assert ivi_system.bluetooth_enabled is True

@given('media is playing')
def media_is_playing(ivi_system):
    assert ivi_system.is_media_available() == True

@when('the system is powered off')
def system_off(ivi_system):
    ivi_system.power_off()
    assert ivi_system.power_state == 'OFF'

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()
    assert ivi_system.power_state == 'ON'

@then('Bluetooth should be disabled')
def bluetooth_disabled(ivi_system):
    assert ivi_system.bluetooth_enabled is False

@then('media should not be playing')
def media_disabled(ivi_system):
    assert ivi_system.is_media_playing() is False