# widgets.py file by hirnlosen
# Description: widgets library


# Importing required modules
import time


# Battery widget class description
class Battery_widget():
    
# Widget initialization
    def __init__(self, buffer):
        self.buf = buffer
        self.ox = 0
        self.oy = 0
        self.value = '--%'
        self.width = 8*len(self.value)
        self.height = 8

# Setting new location of the widget
    def set_location(self, origin_x, origin_y):
        self.ox = origin_x
        self.oy = origin_y
    
# Updating widget in the buffer
    def update(self):
        self._get_current_level()
        self.buf.fill_rect(self.ox, self.oy, self.width, self.height, 0)
        self.buf.text(self.value, self.ox, self.oy)
        
# Getting current battery level
# No realization for now, just showes not available
    def _get_current_level(self):
        self.value = 'NA%'
        self.width = 8*len(self.value)


# Wifi widget class description
class Wifi_widget():

# Widget initialization
    def __init__(self, buffer):
        self.buf = buffer
        self.ox = 0
        self.oy = 0
        self.state = 1
        self.width = 7
        self.height = 8
        
# Setting new location of the widget
    def set_location(self, origin_x, origin_y):
        self.ox = origin_x
        self.oy = origin_y

# Updating widget apperance depending on its current state
    def update(self):
        self.buf.fill_rect(self.ox, self.oy, self.width, self.height, 0)
        if self.state == 0:
            self._disabled()
        elif self.state == 1:
            self._not_connected()
        elif self.state == 2:
            self._connected()
        elif self.state == 3:
            self._connecting(0)
        elif self.state == 4:
            self._connecting(1)
        elif self.state == 5:
            self._connecting(2)
        elif self.state == 6:
            self._connecting(3)
        elif self.state == 7:
            self._connecting(4)

# Hidding wifi icon
    def _disabled(self):
        self.buf.fill_rect(self.ox, self.oy, self.width, self.height, 0)
        self.width = 0    

    def _not_connected(self):
        self.buf.line(self.ox, self.oy, self.ox+6, self.oy+6, 1)
        self.buf.line(self.ox, self.oy+6, self.ox+6, self.oy, 1)
        self.width = 7

# Drawing connected wifi icon
    def _connected(self):
        for i in range (0, 3+1):
            self.buf.hline(self.ox+i, self.oy+2*i, 7-2*i, 1)
        self.width = 7

# Drawing connecting wifi icons
    def _connecting(self, pose):
        if pose == 0:
            self.state = 4
        if pose == 1:
            self.buf.hline(self.ox+3, self.oy+1, 7, 1)
            self.state = 5
        elif pose == 2:
            self.buf.hline(self.ox+3, self.oy+1, 7, 1)
            self.buf.hline(self.ox+2, self.oy+3, 5, 1)
            self.state = 6
        elif pose == 3:
            self.buf.hline(self.ox+3, self.oy+1, 7, 1)
            self.buf.hline(self.ox+2, self.oy+3, 5, 1)
            self.buf.hline(self.ox+1, self.oy+5, 3, 1)
            self.state = 7
        elif pose == 4:
            self.buf.hline(self.ox+3, self.oy+1, 7, 1)
            self.buf.hline(self.ox+2, self.oy+3, 5, 1)
            self.buf.hline(self.ox+1, self.oy+5, 3, 1)
            self.buf.hline(self.ox, self.oy+7, 1, 1)
            self.state = 3
        self.width = 7


# Time widget class description
class Time_widget():

# Widget initialization
    def __init__(self, buffer):
        self.buf = buffer
        self.ox = 0
        self.oy = 0
        self.value = '--:--'
        self.width = 8*len(self.value)
        self.height = 8

# Setting new location of the widget
    def set_location(self, origin_x, origin_y):
        self.ox = origin_x
        self.oy = origin_y

# Updating widget in the buffer
    def update(self):
        self._get_current_time()
        self.buf.fill_rect(self.ox, self.oy, self.width, self.height, 0)
        self.buf.text(self.value, self.ox, self.oy)

# Updating widget value with current time
    def _get_current_time(self):
        current_time = time.localtime(time.time())
        #self.value = "{3:02d}:{4:02d}:{5:02d}".format(*current_time)
        self.value = "{3:02d}:{4:02d}".format(*current_time)
        self.width = 8*len(self.value)
        self.height = 8
        