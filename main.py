import pygame

WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Banana Soup")


def main():
    run = True
    # game loop
    while(run):
        # go through each event (user input)
        for event in pygame.event.get():
            # if user try to quit, close game
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


# stupid python syntax for running main only from main.py
if __name__ == "__main__":
    main()

