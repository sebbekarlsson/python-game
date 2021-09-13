import pygame
from game.models.drawable import Drawable
from game.models.actor import Actor

class App(Drawable):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.actors = []
        self.screen = pygame.display.set_mode([self.width, self.height])

    def update(self):
        for actor in self.actors:
            actor.update()

    def draw(self):
        for actor in self.actors:
            actor.draw()

    def add(self, actor: Actor):
        self.actors.append(actor)

    def remove(self, actor: Actor):
        self.actors.remove(actor)

    def start(self):
        pygame.init()


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))

            self.draw()
            self.update()

            pygame.display.flip()

        pygame.quit()
