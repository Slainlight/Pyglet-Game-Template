from pyglet.window import key
import fullscreen as fs
import statetest
import state1
import parent
import var

def graphics():
    if var.state == 0:
        # Rainbow test
        statetest.graphics()
        pass
    if var.state == 1:
        # Mario test
        state1.graphics()
        pass
    pass


def update(dt):
    fs.update(dt)

    # Debug
    if var.debug == True:
        if var.keys[key._0]:
           var.state = 0
        elif var.keys[key._1]:
           var.state = 1
        
    if var.state == 0:
        statetest.update(dt)
        pass
    if var.state == 1:
        state1.update(dt)
        pass
    pass
