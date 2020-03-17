from pyglet.window import key
from pyglet.gl import *
import pyglet
import parent
import var

from var import window

# Get monitor resolution
display = pyglet.canvas.Display()
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

# Can Fullscreen? is 16:9?
canFS = False
if screen_width//16 == screen_height//9:
    canFS = True

# Side note, removed decimal point for the sake of 1768 x 992! oml

def update(dt):
    if canFS:
        var.timeSinceLastF += dt
        if var.keys[key.LSHIFT] and var.keys[key.F] and var.timeSinceLastF > 0.5:

            if(not window.fullscreen):
                wRatio = screen_width/window.width
                glScalef(wRatio,screen_height/window.height,1.0)
                window.set_fullscreen(True)
                var.timeSinceLastF = 0
                
            elif(window.fullscreen):
                glScalef(var.wWidth/screen_width,var.wHeight/screen_height,1.0)
                window.set_fullscreen(False)
                var.timeSinceLastF = 0
