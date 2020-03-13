from pyglet import image
import os
import sys

base = os.getcwd() + "\\Assets\\"

"""
def dirConvert(dirStr):
    newStrs = dirStr.split("\\")
    newStr = ""
    for string in newStrs:
        newStr += string + "/"
        pass

    return newStr[0:len(newStr)-1]
"""

mario_img = image.load(base + 'mario.png')
