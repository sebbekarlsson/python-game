from game.models.living import Living
from game.models.actor import Actor
from game.models.bullet import Bullet
import pygame


class Enemy(Living):

    def __init__(self, *args, **kwargs):
        Living.__init__(self, *args, **kwargs)
        self.set_color(255, 0, 0)


    # Rack upp handen nar ni ser meddelandet
    def update(self):
       Actor.update(self)

       if self.is_colliding(Bullet):
           print("Enemy touched a bullet!")


    def draw(self):
        pygame.draw.circle(
            self.app.screen,
            self.color,
            (self.x, self.y),
            32
        )
