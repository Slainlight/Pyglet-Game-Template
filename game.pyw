from pyglet.gl import *
import directories as d
from var import window

import pyglet

import states
import var


@window.event
def on_draw():
    window.clear()
    states.graphics()

def update(dt):
    states.update(dt)

pyglet.clock.schedule_interval(update, 1/240.0)
pyglet.app.run()
 
