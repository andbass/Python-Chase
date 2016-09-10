#!/usr/bin/env python3

'''
The main gameloop is stored here
'''

import math, os, sys

import pygame as pg
pg.init()

import pymunk as pm

from pymunk import Vec2d
from random import randint

import startup
import game
import world as world_module
import image
import render
import ai

TILE_SIZE = (350, 350)

COP_COLLISION_TYPE = 1
PLAYER_COLLISION_TYPE = 2

def reset(car_info, space):
    game.clear_cars(car_info, space)

    player = game.create_car(
            space, 
            car_info,

            image.load('img/car6.png', size = 0.52),

            pos = (1200, 2000), 
            angle = 0,

            speed = 15,
            accel = 0.01,

            color = (0, 255, 0),
            collision_type = PLAYER_COLLISION_TYPE
    )

    enemy = game.create_car(
            space, 
            car_info,

            image.load('img/cop2.png', size = 0.6),

            pos = (1200, 1500), 
            angle = 0,

            speed = 15,
            accel = 0.01,

            color = (255, 0, 0),
            collision_type = COP_COLLISION_TYPE
    )
    
    ai.register(enemy)

    return player, enemy

def change_skin(car, skin_number, space):
    img_str = "img/car" + str(skin_number) + ".png"
    img = image.load(img_str, size = 0.52)

    car.change_skin(img, space)

def main():
    space, screen = startup.initalize()
    screen_size = Vec2d((screen.get_width(), screen.get_height()))

    car_info = {}

    tileset = {
        '0': image.load('img/grass.png', size = TILE_SIZE),

        '1': image.load('img/road/roadNS.tga', size = TILE_SIZE),
        '2': image.load('img/road/roadEW.tga', size = TILE_SIZE),
        '3': image.load('img/road/roadNW.tga', size = TILE_SIZE),
        '4': image.load('img/road/roadNE.tga', size = TILE_SIZE),
        '5': image.load('img/road/roadSE.tga', size = TILE_SIZE),
        '6': image.load('img/road/roadSW.tga', size = TILE_SIZE),
        '7': image.load('img/road/roadNEWS.tga', size = TILE_SIZE),
        'b': image.load('img/road/roadPLAZA.tga', size = TILE_SIZE),

        'w': image.load('img/wall.tga', size = TILE_SIZE),
    }

    with open('terrain.txt') as terrain_file:
        terrain_text = terrain_file.read()

    world = world_module.load(screen, terrain_text, space, tileset)

    player, enemy = reset(car_info, space)
    #game.delete_car(enemy, car_info, space)

    running = True
    clock = pg.time.Clock() 
    reset_time = pg.time.get_ticks()

    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        cam_pos = player.car.body.position - screen_size / 2
        render.draw(screen, cam_pos, space, world, car_info)

        keys = pg.key.get_pressed()

        if keys[pg.K_r]:
            player, enemy = reset(car_info, space)
            reset_time = pg.time.get_ticks()

        if keys[pg.K_UP]:
            player.throttle += 0.1

        if keys[pg.K_DOWN]:
            player.throttle -= 0.1

        player.throttle *= 0.9

        if keys[pg.K_LEFT]:
            player.steer += 1.0

        if keys[pg.K_RIGHT]:
            player.steer -= 1.0 

        player.steer *= 0.9

        ai.update(player, time = pg.time.get_ticks() - reset_time)
        game.physics_update(space, car_info)

        space.step(1.0 / 30.0)
        clock.tick(30)

    pg.quit() 

if __name__ == "__main__": main()
