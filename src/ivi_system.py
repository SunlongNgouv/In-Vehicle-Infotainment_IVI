class IVISystem:
    def __init__(self):
        self.power_state = "OFF"
        self.bluetooth_enabled = False
        self.media_ready = False
        self.max_boot_time = 30
        self.boot_time_default = self.max_boot_time - 1
        self.media_playing = False
        self.battery_volt_default = 0
        self.engine_start = 12
        self.engine_boot = False

# action
    def power_on(self):
        self.power_state = "ON"
        self.media_ready = True

    def power_off(self):
        self.power_state = "OFF"
        self.bluetooth_enabled = False
        self.media_ready = False
        self.media_playing = False

    def boot_time_defaul(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        else:
            return self.boot_time_default

    def enable_bluetooth(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        self.bluetooth_enabled = True

    def enable_media_playing(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        elif not self.media_ready:
            raise RuntimeError("Media is not ready yet")
        else:
            self.media_playing = True

    def enable_boot_engine(self):
        if self.power_state != "ON":
            raise RuntimeError("System must be ON")
        elif self.battery_volt_default < self.engine_start:
            raise RuntimeError("LOW_VOLTAGE")
        else:
            self.engine_boot = True

# query
    def is_home_screen_available(self):
        return self.power_state == "ON"

    def is_media_available(self):
        return self.media_ready

    def is_media_playing(self):
        return self.media_playing




