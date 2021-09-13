from game.models.behavior import Behavior
import random

class AI(Behavior):

    def __init__(self, *args, **kwargs):
        Behavior.__init__(self, *args, **kwargs)

        self.directions = [0, 180, 90, 270]
        self.current_direction = 0
        self.goal_x = 0
        self.goal_y = 0

    def decide_next_move(self):
        self.goal_x = random.randint(0, self.actor.app.width)
        self.goal_y = random.randint(0, self.actor.app.height)

    def should_change_goal(self):
        return random.randint(0, 1000) == 0

    def should_shoot(self):
        return random.randint(0, 600) == 0

    def update(self):
        if self.should_change_goal():
            self.decide_next_move()

        if self.actor.x < self.goal_x:
            self.actor.x += self.actor.get_speed()
            self.actor.set_direction(0)
        if self.actor.x > self.goal_x:
            self.actor.x -= self.actor.get_speed()
            self.actor.set_direction(180)

        if self.actor.y < self.goal_y:
            self.actor.y += self.actor.get_speed()
            self.actor.set_direction(270)
        if self.actor.y > self.goal_y:
            self.actor.y -= self.actor.get_speed()
            self.actor.set_direction(90)

        if self.should_shoot():
            self.actor.shoot()
