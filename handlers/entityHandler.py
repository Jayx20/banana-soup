from entity import Entity
from pygame import Vector2
from typing import List
from handlers.logHandler import LogHandler
import random


class EntityHandler:
    entity: Entity
    entityList: List[Entity] = []

    # adds entity to handler and returns a reference to it
    def add(self, image: str, x: int, y: int):
        new_entity = Entity(image, x, y)
        self.entityList.append(new_entity)
        return new_entity

    def multi_add(self, image: str, amount: int):
        self.entityList = []
        for x in range(amount):
            new_entity = Entity(image, random.randint(40,1240), random.randint(40,680))
            self.entityList.append(new_entity)
            LogHandler.log(new_entity.pos,2)


