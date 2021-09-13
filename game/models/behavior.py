import abc

class Behavior(abc.ABC):

    def __init__(self, actor, options: dict = {}):
        self.actor = actor
        self.options = options

    @abc.abstractmethod
    def update(self):
        pass
