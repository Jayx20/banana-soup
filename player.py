from sprite import Sprite
from pygame import Vector2
from handlers.logHandler import LogHandler
from entity import Entity

class Player(Entity):
    def __init__(self, sprite_name: str, x: int, y: int):
        super().__init__(sprite_name,x,y)