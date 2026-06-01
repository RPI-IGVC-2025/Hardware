import smbus2
import time
import math
import struct
import logging

JETSON_DEFAULT_I2C_BUS = 7
DEFAULT_IST8310_ADDR = 0x0E

CNTL_1 = 0x0A
CNTL_2 = 0x0B

GREEN = "\033[32m"
RESET = "\033[0m"


class Compass:
    def __init__(self, i2c_bus=JETSON_DEFAULT_I2C_BUS, address=DEFAULT_IST8310_ADDR, CONFIG_FILEPATH=None, logger=None):
        self._logger = logging.getLogger() if logger is None else logger
        try:
            # init compass
            self._bus = smbus2.SMBus(i2c_bus)
            self._address=address

            self.soft_reset()
            self.normal_mode()
        except Exception as e:
            self._logger.error(f"Error initializing compass: {e}")
            raise e

        self._logger.info(f"{GREEN}IST8310 compass on bus {i2c_bus} with address {address} initialized successfully.{RESET}")

        # get configs
        import yaml

        with open(CONFIG_FILEPATH, "r") as file:
            try:
                data = yaml.safe_load(file)
            except yaml.YAMLError as exception:
                self._logger.error(f"Error parsing YAML file: {exception}")

        self.x_offset = data["offsets"]["x"]
        self.y_offset = data["offsets"]["y"]
        self.z_offset = data["offsets"]["z"]
        self.scale_x = data["scales"]["x"]
        self.scale_y = data["scales"]["y"]
        self.scale_z = data["scales"]["z"]
        self.declination_angle = data["declination_angle"]


    def soft_reset(self):
        try:
            self._bus.write_byte_data(self._address, CNTL_2, 0x01)
            time.sleep(0.01)
        except Exception as e:
            self._logger.warn(f"Error performing soft reset: {e}")
            raise e

    def normal_mode(self):
        try:
            self._bus.write_byte_data(self._address, CNTL_1, 0x01)
            time.sleep(0.01)
        except Exception as e:
            self._logger.warn(f"Error setting normal mode: {e}")
            raise e
        
    def get_heading(self):
        mx, my, mz = self.read_raw()

        if mx is not None:
            rad = math.atan2(my,mx)
            deg = rad * 180.0 / math.pi
            if deg < 0:
                deg+=360
            deg += self.declination_angle
            if deg > 360:
                deg-=360
            elif deg < 0:
                deg += 360
            return deg
        else:
            return None



    def read_raw(self):
        try:
            self._bus.write_byte_data(self._address, CNTL_1, 0x01)
            while True:
                status = self._bus.read_byte_data(self._address, 0x02)
                if status & 0x01:
                    break
                time.sleep(0.005)

            # Read 6 bytes (X_L, X_H, Y_L, Y_H, Z_L, Z_H)
            data = self._bus.read_i2c_block_data(self._address, 0x03, 6)

            # Convert to 16-bit signed integers (Little Endian)
            x, y, z = struct.unpack('<hhh', bytes(data))

            calibrated_x = (x - self.x_offset) * self.scale_x
            calibrated_y = (y - self.y_offset) * self.scale_y
            calibrated_z = (z - self.z_offset) * self.scale_z

            tx = calibrated_y
            ty = -calibrated_x
            tz = calibrated_z

            # Convert to uT (Microteslas) - scale is 0.3 uT/LSB according to IST8310 datasheet
            scale = 0.3
            return tx * scale, ty * scale,tz * scale
        except Exception as e:
            self._logger.warn(f"Error reading compass data: {e}")
            raise e
        
    def cleanup(self):
        try:
            self._bus.close()
        except Exception as e:
            self._logger.warn(f"Error during cleanup: {e}")
            raise e
