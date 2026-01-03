from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path
from ivi_qa_framework.src.ivi_system import *

import pytest

File = 'media.feature'
File_Dir = 'feature'
Base_Dir = Path(__file__).resolve().parent.parent
Feature_File = Base_Dir.joinpath(File_Dir, File)
print('Feature File exists: ', Feature_File.exists())

scenarios(str(Feature_File))

@given('the IVI system is powered on')
def system_on(ivi_system):
    print('In background state')
    ivi_system.power_on()
    assert ivi_system.power_state == PowerState.ON

@given('the media app is opened')
def media_enable(ivi_system):
    ivi_system.enable_media_library()

#1 ---------- Media app loads and shows library ----------
@then('the media library should be visible')
def media_visible(ivi_system):
    assert ivi_system.media_library_visible == True

#2 ---------- Play a track successfully ----------

@given('a track "Drive Time" is available')
def drive_time_enabled(ivi_system):
    ivi_system.power_on()
    ivi_system.set_battery_volt_now(12.5)
    ivi_system.enable_boot_engine()
    ivi_system.set_driving_time(8,0)  # rush hours typically is at 6-10 a.m. and 3-7 p.m. for 'Driver Time' mode to be available
    ivi_system.is_rush_hour()
    ivi_system.set_drive_time_mode()
    assert ivi_system.drive_time_mode_available == TrackDriveTime.ON

@when('the user selects track "Drive Time"')
def drive_time_selected(ivi_system):
    ivi_system.enable_drive_time_mode()
    ivi_system.run_drive_time_mode()

@when('the user presses play')
def media_selected(ivi_system):
    ivi_system.enable_media_library()
    ivi_system.enable_media_drive_time()

@then('media should be playing')
def media_played(ivi_system):
    assert ivi_system.media_playing_enabled is True

@then('the current track should be "Drive Time"')
def current_track(ivi_system):
    assert ivi_system.track_drive_time == 'Drive Time'

#3 ---------- PPause and resume playback ----------
@given('media is playing')
def media_played(ivi_system):
    ivi_system.power_on()
    ivi_system.enable_media_library()
    ivi_system.enable_media_playing()
    assert ivi_system.media_playing_enabled is True
#
# @when('the user presses pause')
#
#
# @then('media should be paused')
# @then('the user presses play')
# @then('media should be playing')