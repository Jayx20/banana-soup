import pygame
from typing import List

from entity import Entity

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption("Banana Soup")

# GLOBAL definitions
FILL_COLOR = (200, 200, 255)
entities: List[Entity] = []
test_entity: Entity


# runs once at the start of the game
def init():
    global test_entity
    test_entity = Entity("goodsprite.png", 5, 5)
    entities.append(test_entity)

    # create joe and add him to the game like an epic boss
    joe = Entity("goodsprite.png", 10, 10)
    entities.append(joe)


# runs every frame - game logic
def update():
    global test_entity
    print('test entity pos is '+str(test_entity.pos))

    # input stuff, move later to make this less terrible / in the way
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        test_entity.pos.x -= 1
    if keys[pygame.K_d]:
        test_entity.pos.x += 1
    if keys[pygame.K_w]:
        test_entity.pos.y -= 1
    if keys[pygame.K_s]:
        test_entity.pos.y += 1


# runs every frame - graphics
def draw():
    WINDOW.fill(FILL_COLOR)
    # start drawing

    for entity in entities:
        WINDOW.blit(entity.sprite.img, entity.pos, entity.sprite.rect)

    # finish drawing
    pygame.display.update()


def main():
    init()
    clock = pygame.time.Clock()
    run = True
    # game loop
    while run:
        clock.tick(60)
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

