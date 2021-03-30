from sprite import Sprite
from pygame import Vector2


class Entity:
    sprite: Sprite
    pos: Vector2

    # temporary test constructor
    def __init__(self):
        self.sprite = Sprite('goodsprite.png')
        self.pos = Vector2(0, 0)
