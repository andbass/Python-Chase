
import pymunk as pm
from pymunk import Vec2d

import ai

class CarInfo(object):
    def __init__(self, speed, accel, image, car):
        self.speed = speed
        self.accel = accel

        self.car = car
        self.image = image
        
        self.steer = 0
        self.throttle = 0
        self.health = 1.0 
    
    @property
    def body(self):
        return self.car.body
    
    def change_skin(self, image, space):
        self.image = image
        space.remove(self.car, self.body)

        self.car = pm.Poly.create_box(self.body, size = self.image.get_size())

        space.add(self.car, self.body)

def calc_accel_factor(info):
    return info.accel + min(info.car.body.velocity.length * info.accel, 1)

def create_car(space, car_info, image, pos, angle, speed, accel, color, collision_type = 0):
    body = pm.Body(0.2, 50)

    shape = pm.Poly.create_box(body, size = Vec2d(image.get_size()))
    shape.color = color
    shape.collision_type = collision_type

    body.position = pos 
    body.angle = angle

    info = CarInfo(speed, accel, image, shape)
    car_info[shape] = info

    space.add(body, shape)

    return info

def physics_update(space, car_info):
    for car, info in car_info.items():
        speed = info.speed * calc_accel_factor(info)
        
        car.body.apply_impulse(Vec2d(speed * info.throttle, 0).rotated(car.body.angle))

        if car.body.velocity.length > 175:
            car.body.angular_velocity = info.steer

        info.steer *= 0.9
        if abs(info.steer) < 0.01:
            info.steer = 0

def clear_cars(car_info, space):
    for car, info in car_info.items():
        space.remove(car, car.body)

    car_info.clear()

def delete_car(info, car_info, space):
    space.remove(info.car, info.car.body)
    del car_info[info.car]
