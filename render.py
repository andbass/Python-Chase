
import math
import pygame as pg
import pymunk as pm

from pymunk import Vec2d

def flip(vec, screen):
    return Vec2d(vec.x, screen.get_height() - vec.y)

def draw(screen, cam_pos, space, world, car_info):
    screen.fill((0, 0, 0))

    world_height = len(world)

    for y, row in enumerate(world):
        for x, image in enumerate(row):
            space_pos = Vec2d(x, world_height - y) * image.get_size() - cam_pos
            
            screen.blit(image, flip(space_pos, screen).int_tuple)

    for car, info in car_info.items():
        body = car.body

        rotated_image = pg.transform.rotate(info.image, math.degrees(body.angle) + 180)

        rect = rotated_image.get_rect()
        rect.center = flip(body.position - cam_pos, screen).int_tuple

        screen.blit(rotated_image, rect)
 
    pg.display.flip()
