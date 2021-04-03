import pygame
from entity import Entity
from pygame import Vector2
import random
from handlers.entityHandler import EntityHandler
from handlers.inputHandler import InputHandler
from handlers.logHandler import LogHandler
from player import Player

# Constants / Pygame stuff
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 120
pygame.display.set_caption("Banana Soup")

# GLOBAL definitions
FILL_COLOR = (200, 200, 255)  # Background color
myfont: pygame.font  # Fontz
entities: EntityHandler  # List of active entities
test_entity: Player  # Test entity (The guy you use to walk around)
input: InputHandler
log: LogHandler
sprint: int  # Sprint
money: int = 0  # Money or blob value


# runs once at the start of the game
def init():
    global test_entity, money, myfont, entities, input, log
    log = LogHandler.log
    entities = EntityHandler()
    input = InputHandler()
    money = 0
    entities.multi_add("blob.png", 10)
    test_entity = entities.add("tiddies.png", 5, 5)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)


# runs every frame - game logic
def update():
    global test_entity, money, sprint, LogHandler

    player_movement = input.get_player_movement()
    if (player_movement.x != 0 or player_movement.y != 0):
        test_entity.pos += player_movement
        # print player position, for debugging
        log("Sprite's x: " + str(test_entity.pos.x) + " Sprite's y: " + str(test_entity.pos.y),2)

    # Pickup Blob
    for entity in entities.entityList:
        # Make sure not player
        if entity != test_entity:
            distance_x = test_entity.pos.x - entity.pos.x # Get x to compare later
            distance_y = test_entity.pos.y - entity.pos.y # Get y to compare later
            if abs(distance_x) < 20:
                if abs(distance_y) < 20:
                    randnum = random.randint(1,100)
                    if randnum > 90:
                        money = 20

                    money += 1
                    entity.pos = Vector2(random.randint(40, 1240), random.randint(40, 680))


# runs every frame - graphics
def draw():
    WINDOW.fill(FILL_COLOR)
    # start drawing
    for entity in entities.entityList:
        WINDOW.blit(entity.sprite.img, entity.pos, entity.sprite.rect)

    # draw money thing
    text_surface = myfont.render("Blobs: " + str(money), False, (0, 0, 0))
    WINDOW.blit(text_surface, (WIDTH - 220, 0))

    if money == 21:
        text_surface = myfont.render("WHATS 9 + 10!??!?! " + str(money), False, (0, 0, 0))
        WINDOW.blit(text_surface, (69,69))

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
