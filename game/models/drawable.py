import abc


class Drawable(abc.ABC):


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def update(self):
        pass


    @abc.abstractmethod
    def draw(self):
        pass
