from game.models.drawable import Drawable

# Rack upp handen om ni kan skjuta nu,
# annars sag till sa hjalper jag dig

class Actor(Drawable):

    def __init__(self, x, y, app, *args, **kwargs):
        Drawable.__init__(self, *args, **kwargs, x=x, y=y)
        self.app = app
        self.behaviors = []
        self.color = (255, 255, 255)
        self.speed = 1
        self.direction = 0
        self.width = 32
        self.height = 32

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_color(self, r, g, b):
        self.color = (r, g, b)

    def update(self):
        for behavior in self.behaviors:
            behavior.update()

    def is_colliding(self, actor_class):
        actors = self.app.actors
        w = self.get_width()
        h = self.get_height()

        for actor in actors:
            if not isinstance(actor, actor_class):
                continue

            aw = actor.get_width()
            ah = actor.get_height()

            if self.x + w >= actor.x and self.x <= actor.x + aw:
                if self.y + h >= actor.y and self.y <= actor.y + ah:
                    return True

        return False

    def add_behavior(self, behavior_class):
        self.behaviors.append(behavior_class(self))
