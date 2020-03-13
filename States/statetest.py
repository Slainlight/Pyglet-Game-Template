import pyglet
import parent
from var import window
import var

#Rainbow test
quad = pyglet.graphics.vertex_list(4,
    ('v2i', (0, 0,  var.wWidth, 0, var.wWidth, var.wHeight, 0, var.wHeight)),
    ('c3B', (0, 0, 255, 255, 0, 0, 255, 255, 0,  0, 255, 0)))

def graphics():
    quad.draw(pyglet.gl.GL_QUADS)
    pass

def update(dt):
    pass
    
