from sprite import Sprite
from pygame import Vector2


class Entity:
    sprite: Sprite
    pos: Vector2

    def __init__(self, sprite_name: str, x: int, y: int):
        self.sprite = Sprite(sprite_name)
        self.pos = Vector2(x, y)
        print("Sprite has been created with the name: " + sprite_name)