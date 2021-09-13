from game.models.living import Living
import pygame


class Enemy(Living):

    def __init__(self, *args, **kwargs):
        Living.__init__(self, *args, **kwargs)
        self.set_color(255, 0, 0)


    def update(self):
        pass


    def draw(self):
        pygame.draw.circle(
            self.app.screen,
            self.color,
            (self.x, self.y),
            32
        )
