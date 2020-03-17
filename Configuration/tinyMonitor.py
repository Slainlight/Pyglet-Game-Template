from pyglet.window import key
from pyglet.gl import *
import pyglet
import parent
import var
import ctypes

from var import window

# Get monitor resolution
display = pyglet.canvas.Display()
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

if screen_width < var.wWidth and screen_height < var.wHeight:
    print("Your monitor is too small!")
    window.close()
    ctypes.windll.user32.MessageBoxW(0, "Your monitor is too small!", "tinyMonitor", 1)
    exit()

# I don't know how I'd get this to work haha
"""
# Must be 16:9
tiny_x = 256
tiny_y = 144
ratio_x = tiny_x/var.wWidth
ratio_y = tiny_y/var.wWidth

# Small monitor support
if screen_width < var.wWidth and screen_height < var.wHeight:
    print("Tiny Support")
    var.wWidth = tiny_x
    var.wHeight = tiny_y
    glScalef(ratio_x,ratio_y,1.0)
    window.set_size(tiny_x, tiny_y)
    pass
"""
