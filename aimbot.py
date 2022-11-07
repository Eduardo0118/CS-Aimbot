import keyboard

from ctypes import *

def move_mousey(y):
    windll.user32.mouse_event(
        c_uint(0x0001),
        c_uint(0),
        c_uint(y),
        c_uint(0),
        c_uint(0)
    )
 
 
def move_mousex(x):
    windll.user32.mouse_event(
        c_uint(0x0001),
        c_uint(x),
        c_uint(0),
        c_uint(0),
        c_uint(0)
    )

def Aimbot(x, y):
    if keyboard.is_pressed('c'):
        if x != 0:
            move_mousex(int(x * 2))

        if y != 0:
            move_mousey(int(y * 2))