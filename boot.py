# boot.py file by hirnlosen
# System initialization


# Importing required modules
from machine import Pin, I2C
import gc, network, json, framebuf
from drivers.ssd1306_mod import SSD1306_I2C
from system import widgets


# Debug info
print('\nboot.py | Starting system initialization... ', end = '')


# Startup garbage collector
gc.collect()


# System objects dictionary initialization
system_objects = {}


# Loading system config file
file = open('/configs/system_config.json', 'r')
system_objects.update({'system_config': json.load(file)})
file.close()
del file


# Loading device specific config file
file = open('/configs/device_config.json', 'r')
system_objects.update({'device_config': json.load(file)})
file.close()
del file


# Leds initialization
leds = {}
for key, value in system_objects['device_config']['leds'].items():
    leds[key] = Pin(value, Pin.OUT)
    leds[key].off()
system_objects.update({'leds': leds})
del leds
#system_objects.update({'leds': Pin(system_objects['device_config']['leds']['led1'], Pin.OUT)})
#system_objects['leds']['led1'].off()


# Buttons initialization
buttons = {}
for key, value in system_objects['device_config']['buttons'].items():
    buttons[key] = Pin(value, Pin.IN)
system_objects.update({'buttons': buttons})
del buttons


# Making access point object and turning it off 
system_objects.update({'access_point': network.WLAN(network.AP_IF)})
system_objects['access_point'].active(False)


# Making wifi object and turning it off
system_objects.update({'wifi': network.WLAN(network.STA_IF)})
system_objects['wifi'].active(False)


# Making OLED display object
system_objects.update({'screen': SSD1306_I2C(system_objects['device_config']['display']['width'],
                                             system_objects['device_config']['display']['height'],
                                             I2C(scl=Pin(system_objects['device_config']['display']['scl']),
                                             sda=Pin(system_objects['device_config']['display']['sda'])))})


# Creating top bar buffer and adding to system objects dictionary
buffer_top = framebuf.FrameBuffer(bytearray(system_objects['device_config']['display']['width']*system_objects['device_config']['display']['top_bar_height']),
                                            system_objects['device_config']['display']['width'],
                                            system_objects['device_config']['display']['top_bar_height'],
                                            framebuf.MONO_VLSB)
system_objects.update({'buffer_top': buffer_top})
del buffer_top


# Creating main screen buffer and adding to system objects dictionary
buffer_main = framebuf.FrameBuffer(bytearray(system_objects['device_config']['display']['width']*(system_objects['device_config']['display']['height']-system_objects['device_config']['display']['top_bar_height'])),
                                             system_objects['device_config']['display']['width'],
                                             system_objects['device_config']['display']['height']-system_objects['device_config']['display']['top_bar_height'],
                                             framebuf.MONO_VLSB)
system_objects.update({'buffer_main': buffer_main})
del buffer_main


# Creating widgets array
system_objects.update({'widgets': [widgets.Time_widget(system_objects['buffer_top']), widgets.Wifi_widget(system_objects['buffer_top']), widgets.Battery_widget(system_objects['buffer_top'])]})


# Initialising events array
events = ['buffer_top_update', 0, 'screen_update', 0]

# Debug info
print('Done')