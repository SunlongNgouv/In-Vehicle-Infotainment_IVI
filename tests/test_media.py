from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path
from ivi_qa_framework.src.ivi_system import IVISystem

import pytest

File = 'media.feature'
File_Dir = 'feature'
Base_Dir = Path(__file__).resolve().parent.parent
Feature_File = Base_Dir.joinpath(File_Dir, File)
print('Feature File exists: ', Feature_File.exists())

# scenarios(str(Feature_File))
#
# @given('the IVI system is powered on')
# def system_on(ivi_system):
#     print('In background state')
#     ivi_system.power_on()
#     assert ivi_system.power_state == 'ON'

# @given('the media app is opened')
# def media_enable(ivi_system):
#     ivi_system.enable_media_library()
#
# #### 1
# @then('the media library should be visible')
# def media_visible(ivi_system):
#     assert ivi_system.media_library_visible == True

#
# @given('a track "Drive Time" is available')
# def drive_time_enabled(ivi_system):
#     ivi_system.power_on()
#     ivi_system.enable_boot_engine()
#     ivi_system.set_driving_time(8,0)  # rush hours typically is at 6-10 a.m. and 3-7 p.m. for 'Driver Time' mode to be available
#     assert ivi_system.is_driving_time_available() is True
#
# @when('the user selects track "Drive Time"')
# def drive_time_selected(ivi_system):
#     ivi_system.enable_drive_time_mode()
#     assert ivi_system.drive_time_mode_enabled is True
#
# @when('the user presses play')
# def media_selected(ivi_system):
#     ivi_system.enable_media_playing()
#
# @then('media should be playing')
# def media_played(ivi_system):
#     assert ivi_system.media_playing_enabled is True
#
# @then('the current track should be "Drive Time"')
