import pyglet
import directories
import assets
from pyglet.window import key

# Window
caption = "Colors"
#icon = pyglet.image.load("Assets/mario.png")
wWidth, wHeight = 1280, 720

window = pyglet.window.Window(wWidth,wHeight)
window.set_caption(caption)
window.set_icon(assets.icon)

# Keyboard
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Batches
background = pyglet.graphics.Batch()

# Where player resides & things player collides with
ground = pyglet.graphics.Batch()

foreground = pyglet.graphics.Batch()

# Global Variables
state = 1
debug = True

# Fullscreen
timeSinceLastF = 1
fKeyEligiblity = True
