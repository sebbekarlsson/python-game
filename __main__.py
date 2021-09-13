from game.app import App
from game.models.player import Player
from game.models.enemy import Enemy
from game.controller import Controller
from game.ai import AI

SCALE = 1
WIDTH = 1080 * SCALE
HEIGHT = int(WIDTH / 16 * 9)
app = App(WIDTH, HEIGHT)

player = Player(WIDTH / 2, HEIGHT / 2, app)
player.add_behavior(Controller)
app.add(player)

enemy = Enemy(WIDTH / 2, HEIGHT - 100, app)
enemy.add_behavior(AI)
app.add(enemy)


app.start()
