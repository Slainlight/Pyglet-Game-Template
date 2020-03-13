import pyglet
from pyglet.gl import *
import directories as d
from var import window
import var
import states

@window.event
def on_draw():
    window.clear()
    states.graphics()

def update(dt):
    states.update(dt)

glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

pyglet.clock.schedule_interval(update, 1/240.0)
pyglet.app.run()
 
