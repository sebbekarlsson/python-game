from game.models.behavior import Behavior
import pygame

class Controller(Behavior):

    def __init__(self, *args, **kwargs):
        Behavior.__init__(self, *args, **kwargs)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.actor.x += 1
            self.actor.set_direction(0)
        if keys[pygame.K_LEFT]:
            self.actor.x -= 1
            self.actor.set_direction(180)
        if keys[pygame.K_UP]:
            self.actor.y -= 1
            self.actor.set_direction(270)
        if keys[pygame.K_DOWN]:
            self.actor.y += 1
            self.actor.set_direction(90)
        if keys[pygame.K_SPACE]:
            self.actor.shoot()
