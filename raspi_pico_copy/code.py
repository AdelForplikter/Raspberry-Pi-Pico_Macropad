import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from adafruit_st7735r import ST7735R
import displayio
import terminalio
from adafruit_display_text import label

import rotaryio


import board, busio, digitalio
mosi_pin = board.GP11
clk_pin = board.GP10
reset_pin = board.GP17
cs_pin = board.GP18
dc_pin = board.GP16




rotPin1 = board.GP2
rotPin2 = board.GP3
'''
rotEnc1 = digitalio.DigitalInOut(rotPin1)
rotEnc1.direction = digitalio.Direction.INPUT
rotEnc1.pull = digitalio.Pull.DOWN

rotEnc2 = digitalio.DigitalInOut(rotPin2)
rotEnc2.direction = digitalio.Direction.INPUT
rotEnc2.pull = digitalio.Pull.DOWN
'''
enc = rotaryio.IncrementalEncoder(rotPin1, rotPin2,1)
last_position = None


btn1_pin = board.GP9
btn2_pin = board.GP8
btn3_pin = board.GP7
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21



btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
#print(usb_hid.devices)
#print(usb_hid)

#---------------------------------------
displayio.release_displays()

spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)

display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

display = ST7735R(display_bus, width=128, height=160, bgr = True)

bitmap = displayio.OnDiskBitmap("/0.bmp")
group = displayio.Group()
display.show(group)


tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
group.append(tile_grid)
#------------------------------



while True:
    position = enc.position
    if last_position == None or position != last_position:
        print(position)
    last_position = position

    
    
    if btn1.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)
    if btn2.value:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.1)
    if btn3.value:
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.F10)
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.F11)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.F12)
        time.sleep(0.1)
    time.sleep(0.1)
