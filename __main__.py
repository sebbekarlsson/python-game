from game.app import App
from game.models.player import Player
from game.controller import Controller

SCALE = 1
WIDTH = 1080 * SCALE
HEIGHT = int(WIDTH / 16 * 9)
app = App(WIDTH, HEIGHT)

player = Player(0, 0, app)
player.add_behavior(Controller)

app.add(player)


app.start()
