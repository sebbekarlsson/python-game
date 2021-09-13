from game.models.behavior import Behavior
import pygame

class Controller(Behavior):

    def __init__(self, actor):
        self.actor = actor

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.actor.x += 1
        if keys[pygame.K_LEFT]:
            self.actor.x -= 1
        if keys[pygame.K_UP]:
            self.actor.y -= 1
        if keys[pygame.K_DOWN]:
            self.actor.y += 1
