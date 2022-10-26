print("Starting")

import board
import time
# import gc

# from micropython import const

# import ulab.numpy as np
# import ulab.numpy.linalg as lg

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB, AnimationModes
# from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

rgb_ext = RGB(pixel_pin=board.A3, num_pixels=22, hue_default=2, sat_default=255, val_default=25, animation_mode=AnimationModes.STATIC_STANDBY)
# media_key_ext = MediaKeys()

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D5, board.D6, board.D7, board.D8,  board.D9)    # try D5 on Feather, keeboar
keyboard.row_pins = (board.A2, board.A1, board.A0, board.SCK, board.MISO)    # try D6 on Feather, keeboar
keyboard.diode_orientation = DiodeOrientation.ROW2COL
keyboard.extensions.append(rgb_ext)
# keyboard.extensions.append(media_key_ext)
keyboard.modules.append(Layers())

# keyboard.debug_enabled = True

""" def distances(base, coords): 
    dist_array = []
    offset_coords = coords - np.array(base)
    for coord in offset_coords:
        dist_array.append(lg.norm(np.array(coord)))
    return dist_array
 """

for ext in keyboard.extensions:
    if type(ext) is RGB:
        rgbobj = ext
        break


def lighter_upper(key, keyboard, *args):
    rgbobj.set_hsv(85, rgbobj.sat_default, 255, rgbmap[args[1]])

def tamper_downer(key, keyboard, *args):
    rgbobj.set_hsv(rgbobj.hue_default, rgbobj.sat_default, rgbobj.val_default, rgbmap[args[1]])

keyboard.keymap = [
    [   KC.HOME,    KC.BSPACE,  KC.KP_SLASH,    KC.KP_ASTERISK, KC.KP_MINUS,
        KC.PGUP,    KC.KP_7,    KC.KP_8,        KC.KP_9,        KC.NO,
        KC.PGDOWN,  KC.KP_4,    KC.KP_5,        KC.KP_6,        KC.KP_PLUS,
        KC.END,     KC.KP_1,    KC.KP_2,        KC.KP_3,        KC.KP_ENTER,
        KC.MO(1),   KC.KP_0,    KC.NO,          KC.KP_DOT,      KC.NO
    ],

    [   KC.TRNS,    KC.DEL,     KC.TRNS,        KC.TRNS,        KC.TRNS,
        KC.TRNS,    KC.F7,      KC.F8,          KC.F9,          KC.TRNS,
        KC.TRNS,    KC.F4,      KC.F5,          KC.F6,          KC.TRNS,
        KC.TRNS,    KC.F1,      KC.F2,          KC.F3,          KC.TRNS,
        KC.TRNS,    KC.F10,     KC.TRNS,        KC.TRNS,        KC.TRNS
    ]
]

for layer in keyboard.keymap:
    for ky in layer:
        ky.after_press_handler(lighter_upper)
        ky.after_release_handler(tamper_downer)

XX = -1

rgbmap = [  # Maps int_coord to Neopixel index
     0,  1,  2,  3,  4,
     8,  7,  6,  5, XX,
     9, 10, 11, 12, 21,
    16, 15, 14, 13, 20,
    17, 18, XX, 19, XX
]

""" rgblocs =  [    # Maps int_coord to physical location; 1u = .75 in = 19.05 mm
    [ 0, 4 ], [   1, 4 ], [  2,  4 ], [ 3, 4 ], [  4,   4 ],
    [ 0, 3 ], [   1, 3 ], [  2,  3 ], [ 3, 3 ], [ XX,  XX ],
    [ 0, 2 ], [   1, 2 ], [  2,  2 ], [ 3, 2 ], [  4, 2.5 ],
    [ 0, 1 ], [   1, 1 ], [  2,  1 ], [ 3, 1 ], [  4, 0.5 ],
    [ 0, 0 ], [ 1.5, 0 ], [ XX, XX ], [ 3, 0 ], [ XX,  XX ]
]

then = time.monotonic_ns()
ds = distances([2,2], rgblocs)
now = time.monotonic_ns()
print(ds)
print(now - then)
 """

rgbobj.effect_static()
# rgbobj.set_hsv_fill(rgbobj.hue_default, rgbobj.sat_default, rgbobj.val_default)
# rgbobj.set_hsv(0, 255, 255, 18)
# print(rgbobj.pixels)
# print(rgbobj.pixels[0][11])
# print(dir(rgbobj))

if __name__ == '__main__': 
    keyboard.go()
