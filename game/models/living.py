from game.models.actor import Actor


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
