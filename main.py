import pygame
from typing import List
from entity import Entity
from pygame import Vector2
import entity
import random
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 120
pygame.display.set_caption("Banana Soup")

# GLOBAL definitions
FILL_COLOR = (200, 200, 255)
entities: List[Entity] = []
test_entity: Entity
sprint: int
prUpdate: bool
myfont: pygame.font
money: int = 0
distanceX: int
distanceY: int
# runs once at the start of the game
def init():
    global test_entity
    global money
    global blob
    money = 0
    blob = Entity("blob.png", random.randint(40,1240), random.randint(40,680))
    entities.append(blob)
    test_entity = Entity("goodsprite.png", 5, 5)
    entities.append(test_entity)
    pygame.font.init()
    global myfont
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

# runs every frame - game logic
def update():
    global test_entity
    global blob
    global money
    distanceX = test_entity.pos.x - blob.pos.x
    distanceY = test_entity.pos.y - blob.pos.y
    sprint = 1
    prUpdate = False
    # input stuff, move later to ma
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        sprint = 2
    if keys[pygame.K_a]:
        test_entity.pos.x -= 1 * sprint
        prUpdate = True
    if keys[pygame.K_d]:
        test_entity.pos.x += 1 * sprint
        prUpdate = True
    if keys[pygame.K_w]:
        test_entity.pos.y -= 1 * sprint
        prUpdate = True
    if keys[pygame.K_s]:
        test_entity.pos.y += 1 * sprint
        prUpdate = True
    if prUpdate:
         print("Sprite's x: " + str(test_entity.pos.x) + " Sprite's y: " + str(test_entity.pos.y))
         prUpdate = False

    if keys[pygame.K_g]:
        test_entity.pos = blob.pos
    #Pickup Blob
    if abs(distanceX) < 20:
        if abs(distanceY) < 20:
         money += 1
         for x in entities:
            if x == blob:
             blob.pos = Vector2(random.randint(40,1240), random.randint(40,680))

# runs every frame - graphics
def draw():
    WINDOW.fill(FILL_COLOR)
    # start drawing

    for entity in entities:
        WINDOW.blit(entity.sprite.img, entity.pos, entity.sprite.rect)
    global myfont
    textsurface = myfont.render("Blobs: " + str(money), False, (0, 0, 0))
    WINDOW.blit(textsurface,(1080,0))

    # finish drawing
    pygame.display.update()


def main():
    init()
    clock = pygame.time.Clock()
    run = True
    # game loop
    while run:
        clock.tick(FPS)
        # go through each event (user input)
        for event in pygame.event.get():
            # if user try to quit, close game
            if event.type == pygame.QUIT:
                run = False
        update()
        draw()

    pygame.quit()
# stupid python syntax for running main only from main.py
if __name__ == "__main__":
    main()

