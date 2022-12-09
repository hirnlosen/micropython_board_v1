# main.py file by hirnlosen
# Description: event handler


# Importing required modules
from system import handle_functions

# Debug info
print('\nmain.py | Event loop started')
print('\n')

while True:
    function_name = events.pop(0)
    function_argument = events.pop(0)
    getattr(handle_functions, function_name)(events, system_objects, function_argument)
