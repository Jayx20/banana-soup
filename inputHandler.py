import pygame


class InputHandler:
    
    # Get a Vector2 for how the player should move
    def get_player_movement(self):
        # input stuff, move later to ma
        keys = pygame.key.get_pressed()
        sprint = 1
        movement = pygame.Vector2()
        if keys[pygame.K_LSHIFT]:
            sprint += 1
        if keys[pygame.K_a]:
            movement.x -= 1 * sprint
        if keys[pygame.K_d]:
            movement.x += 1 * sprint
        if keys[pygame.K_w]:
            movement.y -= 1 * sprint
        if keys[pygame.K_s]:
            movement.y += 1 * sprint

        return movement