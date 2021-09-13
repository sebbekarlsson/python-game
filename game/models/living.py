from game.models.actor import Actor
from game.models.bullet import Bullet

# Rack upp handen om ni kan skjuta nu,
# annars sag till sa hjalper jag dig

class Living(Actor):

    def __init__(self, *args, **kwargs):
        Actor.__init__(self, *args, **kwargs)
        self.attack_damage = 1
        self.health = 100

    def set_attack_damage(self, attack_damage):
        self.attack_damage = attack_damage

    def get_attack_damage(self):
        return self.attack_damage

    def is_dead(self):
        return self.health <= 0

    def take_damage(self, living):
        self.health = max(
            0,
            self.health - living.get_attack_damage()
        )

    def attack(self, living):
        living.take_damage(self)

    def shoot(self):
        bullet = Bullet(self.x, self.y, self.app)
        bullet.set_direction(self.direction)
        self.app.add(bullet)

# Rack upp handen om ni kan skjuta nu,
# annars sag till sa hjalper jag dig
