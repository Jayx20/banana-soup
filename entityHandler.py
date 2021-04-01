from entity import Entity
from pygame import Vector2
from typing import List
import random


class EntityHandler:
    entity: Entity
    entityList: List[Entity] = []
    def add(self, image: str, x: int, y: int):
        newEntity = Entity(image, x, y)
        self.entityList = []
        self.entityList.append(newEntity)
        print(newEntity.pos)
    def position(self, entity: Entity, pos: Vector2):
        for e in self.entityList:
            if(e == entity):
                e.pos = pos
    def multiAdd(self, image: str, amount: int):
        self.entityList = []
        for x in range(amount):
            newEntity = Entity(image, random.randint(40,1240), random.randint(40,680))
            self.entityList.append(newEntity)
            print(newEntity.pos)


