from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers

import pytest

File = 'system_boot.feature'
File_Dir = 'feature'
Base_Dir = Path(__file__).resolve().parent.parent
Feature_File = Base_Dir.joinpath(File_Dir).joinpath(File)
print('Feature file exists or not: ', Feature_File.exists())

scenarios(str(Feature_File))

#1 ---------- Home Screen ----------

@given('the IVI system is powered off')
def default_state(ivi_system):
    print('In background state')
    ivi_system.power_off()
    assert ivi_system.power_state == 'OFF'

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()

@then('the home screen should be available')
def home_screen_available(ivi_system):
    assert ivi_system.is_home_screen_available() is True

@then('the system state should be "ON"')
def system_state(ivi_system):
    assert ivi_system.power_state == 'ON'

#2 ---------- Boot time ----------

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()

@then('the boot time should be less than 30 seconds')
def boot_time(ivi_system):
    assert ivi_system.boot_time < 30

#3 ---------- Bluetooth + media ----------

@given('Bluetooth is enabled')
def bluetooth_enabled(ivi_system):
    ivi_system.power_on()
    assert ivi_system.power_state == 'ON'
    ivi_system.enable_bluetooth()
    assert ivi_system.bluetooth_enabled is True

@given('media is playing')
def media_is_playing(ivi_system):
    ivi_system.enable_media_library()
    ivi_system.enable_media_playing()
    assert ivi_system.media_playing_enabled is True

@when('the system is powered off')
def system_off(ivi_system):
    ivi_system.power_off()

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()

@then('Bluetooth should be disabled')
def bluetooth_disabled(ivi_system):
    assert ivi_system.bluetooth_enabled is False

@then('media should not be playing')
def media_disabled(ivi_system):
    assert ivi_system.media_playing_enabled is False

#4 ---------- Battery / engine boot ----------

@given('the battery voltage is 10.5 volts')
def battery_state(ivi_system):
    ivi_system.battery_volt_default = 10.5

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()

@then('the boot should fail with error "LOW_VOLTAGE"')
def engine_boot(ivi_system):
    with pytest.raises(RuntimeError) as excinfo:
        ivi_system.enable_boot_engine()
    assert str(excinfo.value) == "LOW_VOLTAGE"

#5 ---------- Battery / engine boot (scenario outline) ----------

@given(parsers.parse('the battery voltage is {voltage} volts'), target_fixture = 'battery_boot')
def battery_state(ivi_system, voltage):
    return ivi_system.battery_volt_default + float(voltage)

@when('the system is powered on')
def system_on(ivi_system):
    ivi_system.power_on()

@then(parsers.parse('the boot result should be "{result}"'))
def engine_boot(ivi_system, battery_boot, result):
    with pytest.raises(RuntimeError) as excinfo:
        assert ivi_system.enable_boot_engine() == result
    print(str(excinfo.value))