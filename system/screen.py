# Device 1 screen.py file by Hirnlosen
# Description:
# *

# Making display object
# screen = Display(config['display']['width'], config['display']['height'], I2C(scl=Pin(5), sda=Pin(4)))

# Adding module to boot
# from system.screen import Display

from drivers.ssd1306 import SSD1306_I2C

class Display(SSD1306_I2C):
    def __init__(self, width, height, i2c):
        self.width = width
        self.height = height
        self.i2c = i2c
        super().__init__(width, height, i2c)
        
    def update(self):
        self.show()
    
    def selector(self, line_number):
        self.fill_rect(0, (line_number - 1) * 8, self.width, 8, 1)


