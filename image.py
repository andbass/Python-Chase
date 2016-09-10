
import pygame as pg
from pymunk import Vec2d

import os

def load(path, size = None, trans = True):
    image = pg.image.load(path)

    if not size is None:
        if type(size) is tuple:
            image = pg.transform.scale(image, size)
        else:
            image_size = Vec2d(image.get_size())
            image = pg.transform.scale(image, (image_size * size).int_tuple)
        
    if trans:
        image.set_colorkey(image.get_at((0, 0)))
        
    return image.convert()
