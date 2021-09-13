from game.models.drawable import Drawable


class Actor(Drawable):

    def __init__(self, x, y, app, *args, **kwargs):
        Drawable.__init__(self, *args, **kwargs, x=x, y=y)
        self.app = app
        self.behaviors = []
        self.color = (255, 255, 255)

    def set_color(self, r, g, b):
        self.color = (r, g, b)

    def update(self):
        for behavior in self.behaviors:
            behavior.update()

    def add_behavior(self, behavior_class):
        self.behaviors.append(behavior_class(self))
