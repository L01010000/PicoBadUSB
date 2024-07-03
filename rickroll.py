import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(1)

kbd.send(Keycode.WINDOWS)
kbd.release_all()
layout.write("ter")

time.sleep(1)  

kbd.send(Keycode.ENTER)
kbd.release_all()

time.sleep(1)  

layout.write("xdg-open https://www.youtube.com/watch?v=dQw4w9WgXcQ")

kbd.send(Keycode.ENTER)
kbd.release_all()
