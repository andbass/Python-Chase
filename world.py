
# 0 grass

# 1 straight up down
# 2 straight left right

# 3 up right
# 4 up left

# 5 down right
# 6 down left

# 7 quad

# b blank
# w wall

import pymunk as pm

import render

from pymunk import Vec2d

def load(screen, text, space, tileset):
    world = []
    split_text = [line.strip() for line in text.split('\n')]

    height = len(split_text)

    for y, line in enumerate(split_text):
        row = []
        for x, ch in enumerate(line):
            image = tileset[ch]
            row.append(image)

            if ch == 'w':
                tile_size = Vec2d(image.get_size())

                space_pos = Vec2d(x, height - y) * tile_size + (tile_size.x / 2, -tile_size.y / 2)

                wall_body = pm.Body()
                wall_body.position = space_pos

                wall_shape = pm.Poly.create_box(wall_body, size = tile_size)

                space.add(wall_shape)
        
        world.append(row)

    return world
