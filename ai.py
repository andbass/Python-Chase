
import pygame as pg
from pymunk import Vec2d

ai_cars = []

def register(*infos):
    for info in infos:
        ai_cars.append(info)

def update(target, time):
    for info in ai_cars:
        car = info.car
        
        direction = (target.car.body.position - car.body.position).normalized()
        steer_angle = direction.get_angle_between(Vec2d(1, 0).rotated(car.body.angle))

        if abs(steer_angle) > 0.1:
            info.steer = -steer_angle * 15.0

        distance = car.body.position.get_distance(target.car.body.position)
        info.throttle = min(distance * (time / 75000000) + 0.75, 200)

