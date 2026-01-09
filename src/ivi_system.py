from datetime import time
from enum import Enum
import pytest

class MediaState(Enum):
    PLAYING = "Playing"
    PAUSED = "Paused"
    STOPPED = "Stopped"

class PowerState(Enum):
    ON = "ON"
    OFF = "OFF"

class TrackDriveTime(Enum):
    ON = "ON"
    OFF = "OFF"
    RUN = "RUN"

class IVISystem:
    def __init__(self):
        self.power_state = PowerState.OFF

        self.bluetooth_enabled = False
        self.max_boot_time = 30
        self.boot_time = self.max_boot_time - 1

        self.media_ready = False
        #self.media_playing_enabled = False
        self.media_library_visible = False
        self.media_state = MediaState.STOPPED

        self.battery_voltage = 0
        self.engine_start_volt = 12
        self.engine_boot = False

        self.drive_time_mode_available = TrackDriveTime.OFF
        self.drive_time_mode_run = TrackDriveTime.OFF
        self.drive_time_state = TrackDriveTime.OFF

        self.current_driving_time = time(0,0)
        self.rush_hours = [(time(6,0),time(10,0)), (time(15,0),time(19,0))]

# action
    def power_on(self):
        self.power_state = PowerState.ON
        self.media_ready = True

    def power_off(self):
        self.power_state = PowerState.OFF
        self.bluetooth_enabled = False
        self.engine_boot = False

        self.media_ready = False
        self.media_library_visible = False
        #self.media_playing_enabled = False
        self.media_state = MediaState.STOPPED

        self.drive_time_mode_available = TrackDriveTime.OFF
        self.drive_time_state = TrackDriveTime.OFF
        self.drive_time_run = TrackDriveTime.OFF

    def boot_time_defaul(self):
        if self.power_state != PowerState.ON:
            raise RuntimeError("System must be ON")
        else:
            return self.boot_time_default

    def enable_bluetooth(self):
        if self.power_state != PowerState.ON:
            raise RuntimeError("System must be ON")
        self.bluetooth_enabled = True

    def enable_media_library(self):
        if self.power_state != PowerState.ON:
            raise RuntimeError("System must be ON")
        elif not self.media_ready:   # assume media is automatically opened after it is ready
            raise RuntimeError("Media is not ready yet")
        else:
            self.media_library_visible = True

    # @pytest.mark.xfail('Deprecated value! Please use control_media_playback()')
    # def enable_media_playing(self):
    #     if self.media_library_visible != True:
    #         raise RuntimeError("Media library is not ready yet")
    #     else:
    #
    #         self.media_playing_enabled = True
    #         self.media_state = MediaState.PLAYING

    def control_media_playback(self, action:str):
        self.last_media_action = action.lower()
        if self.media_library_visible != True:
            raise RuntimeError("Media library is not ready yet")

        if action == 'play':
            if self.media_state in [MediaState.STOPPED, MediaState.PAUSED]:
                self.media_state = MediaState.PLAYING

        elif action == 'pause':
            if self.media_state == MediaState.PLAYING:
                self.media_state = MediaState.PAUSED

        else:
            raise RuntimeError("Invalid action")
            print (f"Unsupported media action: {action}")

    def enable_media_drive_time(self):
        if not self.media_library_visible:
            raise RuntimeError("Media library is not ready yet")
        elif not self.drive_time_state:
            raise RuntimeError("Drive Time mode is not ready yet")
        else:
            self.media_playing_enabled = True
            self.media_state = MediaState.PLAYING
            self.drive_time_state = TrackDriveTime.ON

    def set_battery_volt_now(self, volt:float):
        self.battery_voltage = volt

    def enable_boot_engine(self):
        if self.power_state != PowerState.ON:
            raise RuntimeError("System must be ON")
        elif self.battery_voltage <= self.engine_start_volt:
            raise RuntimeError("LOW_VOLTAGE")
        else:
            self.engine_boot = True

    def set_driving_time(self, hour, minute):
        self.current_driving_time = time(hour, minute)

    def set_drive_time_mode(self):
        if self.power_state != PowerState.ON:
            raise RuntimeError("System must be ON")
        elif self.engine_boot != True:
            raise RuntimeError("Engine is not ready yet")
        elif self.is_rush_hour() != True:
            raise RuntimeError("Not in rush hours")
        else:
            self.drive_time_mode_available = TrackDriveTime.ON

    def enable_drive_time_mode(self):
        if self.drive_time_mode_available != TrackDriveTime.ON:
            raise RuntimeError("'Drive Time' mode is not available at this time")
        else:
            self.drive_time_state = TrackDriveTime.ON

    def run_drive_time_mode(self):
        if self.drive_time_state != TrackDriveTime.ON:
            raise RuntimeError("Please select track 'Drive Time' mode to proceed")
        else:
            self.drive_time_run = TrackDriveTime.RUN

# query
    def is_home_screen_available(self):
        return self.power_state == PowerState.ON

    def is_rush_hour(self):
        return any(start <= self.current_driving_time <= end for start, end in self.rush_hours)


if __name__ == "__main__":
    system = IVISystem()
    # system.set_driving_time(hour=12, minute=30)
    # print(system.current_driving_time)
    # print(system.is_rush_hour())
    system.power_on()
    system.enable_media_library()
    system.control_media_playback('play')
    print(system.media_state)





