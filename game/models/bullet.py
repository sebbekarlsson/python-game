from game.models.actor import Actor
import game


import pygame
import math


class Bullet(Actor):

    def __init__(self, *args, **kwargs):
        Actor.__init__(self, *args, **kwargs)
        self.set_color(255, 255, 255)

    def update(self):
        r = math.radians(self.get_direction())
        self.x += math.cos(r) * self.get_speed()
        self.y += math.sin(r) * self.get_speed()

        window_w = self.app.width
        window_h = self.app.height

        if self.x < 0 or self.x > window_w or self.y < 0 or self.y > window_h:
            self.app.remove(self)


    def draw(self):
        pygame.draw.circle(
            self.app.screen,
            self.color,
            (self.x, self.y),
            8
        )
