from datetime import time

class IVISystem:
    def __init__(self):
        self.power_state = "OFF"

        self.bluetooth_enabled = False
        self.max_boot_time = 30
        self.boot_time = self.max_boot_time - 1

        self.media_ready = False
        self.media_playing_enabled = False
        self.media_library_visible = False

        self.battery_volt_default = 0
        self.engine_start_volt = 12
        self.engine_boot = False

        self.drive_time_mode_available = False
        self.drive_time_mode_enabled = False
        self.drive_time_mode_run = False

        self.current_driving_time = time(0,0)
        self.rush_hours = [(time(6,0),time(10,0)), (time(15,0),time(19,0))]

# action
    def power_on(self):
        self.power_state = "ON"
        self.media_ready = True

    def power_off(self):
        self.power_state = "OFF"
        self.bluetooth_enabled = False
        self.media_ready = False
        self.media_library_visible = False
        self.media_playing_enabled = False

    def boot_time_defaul(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        else:
            return self.boot_time_default

    def enable_bluetooth(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        self.bluetooth_enabled = True

    def enable_media_library(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        elif not self.media_ready:   # assume media is automatically opened after it is ready
            raise RuntimeError("Media is not ready yet")
        else:
            self.media_library_visible = True
        return True

    def enable_media_playing(self):
        if self.media_library_visible != True:
            raise RuntimeError("Media library is not ready yet")
        else:
            self.media_playing_enabled = True
        return True

    def enable_boot_engine(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        elif self.battery_volt_default < self.engine_start_volt:
            raise RuntimeError("LOW_VOLTAGE")
        else:
            self.engine_boot = True

    def set_driving_time(self, hour, minute):
        self.current_driving_time = time(hour, minute)

    def set_drive_time_mode(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        elif self.engine_boot != True:
            raise RuntimeError("Engine is not ready yet")
        elif self.is_rush_hour() != True:
            raise RuntimeError("Not in rush hours")
        else:
            self.drive_time_mode_available = True

    def enable_drive_time_mode(self):
        if self.is_drive_time_mode_available() != True:
            raise RuntimeError("'Drive Time' mode is not available at this time")
        else:
            self.drive_time_mode_enabled = True
        return True

    def run_drive_time_mode(self):
        if self.drive_time_mode_enabled != True:
            raise RuntimeError("Please select track 'Drive Time' mode to proceed")
        else:
            self.drive_time_mode_run = True

# query
    def is_home_screen_available(self):
        return self.power_state == "ON"

    def is_rush_hour(self):
        return any(start <= self.current_driving_time <= end for start, end in self.rush_hours)

    def is_drive_time_mode_available(self):
        return self.drive_time_mode_available

if __name__ == "__main__":
    system = IVISystem()
    system.set_driving_time(hour=12, minute=30)
    print(system.current_driving_time)
    print(system.is_rush_hour())




