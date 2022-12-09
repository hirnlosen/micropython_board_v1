# handle_functions.py file by hirnlosen
# Description: event handler functions list


# Importing required modules
import ntptime


def screen_update(events, sys_obj, arg):
    
    sys_obj['screen'].fill_rect(0, 0, sys_obj['device_config']['display']['width'], sys_obj['device_config']['display']['top_bar_height'], 0)
    sys_obj['screen'].blit(sys_obj['buffer_top'], 0, 0)
    sys_obj['screen'].show()
    
    events.append('screen_update')
    events.append(0)

def buffer_top_update(events, sys_obj, arg):
    
    for item in sys_obj['widgets']:
        item.update()
    
    x_loc = 0
    for item in sys_obj['widgets']:
        item.set_location(x_loc, 0)
        x_loc += item.width + 2
        
    sys_obj['widgets'][-1].set_location(sys_obj['device_config']['display']['width']-sys_obj['widgets'][-1].width, 0)
    
    events.append('buffer_top_update')
    events.append(0)

def buffer_main_update(events, sys_obj, arg):
    print('Not available')

def buttons_click(events, sys_obj, arg):
    print('Not available')

def leds_switch(arg):
    print('Not available')

def time_update_from_internet(events, sys_obj, arg):
    ntptime.settime()

# def wifi_check(events, sys_obj, arg):
#     if sys_obj['system_config']['wifi']['enabled'] == True 

def wifi_enable(events, sys_obj, arg):
    sys_obj['wifi'].active(True)
    sys_obj['system_config']['wifi']['enabled'] = True
    events.append('wifi_connect&0')
    
def wifi_disable(events, sys_obj, arg):
    sys_obj['wifi'].active(False)
    sys_obj['system_config']['wifi']['enabled'] = False
    
def wifi_connect(events, sys_obj, arg):
    print('Not available')
    
def wifi_add_new(events, sys_obj, arg):
    print('Not available')