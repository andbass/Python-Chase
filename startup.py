
import pygame as pg
import pymunk as pm

import image

import os, sys

def get_screen_dim():
    info = pg.display.Info()
    return info.current_w, info.current_h

def prepare_pymunk():
    pass

def initalize():
    space = pm.Space()
    space.damping = 0.07

    screen = pg.display.set_mode(get_screen_dim(), pg.DOUBLEBUF)

    return space, screen
