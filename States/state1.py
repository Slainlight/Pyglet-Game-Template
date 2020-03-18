from pyglet.window import key
from pyglet.gl import *
import parent
import pyglet

from var import window
import directories
import assets
import var

# Rainbow test
quad = pyglet.graphics.vertex_list(4,
    ('v2i', (0, 0,  var.wWidth, 0, var.wWidth, var.wHeight, 0, var.wHeight)),
    ('c3B', (0, 0, 255, 255, 0, 0, 255, 255, 0,  0, 255, 0)))

# Mario Sprite
mario = pyglet.sprite.Sprite(assets.mario_img)
mario.scale = 20

# Luigi Sprite
luigi = pyglet.sprite.Sprite(assets.luigi_img)
luigi.scale = 20
luigi.scale_x = -1
luigi.x = mario.width*2+50

def aaoff():
    glEnable(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

def graphics():
    quad.draw(pyglet.gl.GL_QUADS)
    aaoff()
    luigi.draw()
    aaoff()
    mario.draw()
    pass

def update(dt):
    if var.keys[key.RIGHT]:
        mario.x+= 200*dt
    if var.keys[key.LEFT]:
        mario.x+= 200*-dt
    if var.keys[key.UP]:
        mario.y+= 200*dt
    if var.keys[key.DOWN]:
        mario.y-= 200*dt
    pass
    
