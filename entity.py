from sprite import Sprite
from pygame import Vector2
from handlers.logHandler import LogHandler

class Entity:
    sprite: Sprite
    pos: Vector2

    # Entity creation
    def __init__(self, sprite_name: str, x: int, y: int):
        self.sprite = Sprite(sprite_name)
        self.pos = Vector2(x, y)
        LogHandler.log("Entity: " + sprite_name + " has been created with the position of: " + str(self.pos), 1)