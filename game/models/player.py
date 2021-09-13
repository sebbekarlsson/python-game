from game.models.living import Living
from game.models.actor import Actor
import pygame


class Player(Living):

    def __init__(self, *args, **kwargs):
        Living.__init__(self, *args, **kwargs)
        self.set_color(255, 255, 255)


    def update(self):
        Actor.update(self)

    def draw(self):
        pygame.draw.circle(
            self.app.screen,
            self.color,
            (self.x, self.y),
            32
        )
