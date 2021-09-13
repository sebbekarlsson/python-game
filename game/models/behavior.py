import abc

class Behavior(abc.ABC):

    def __init__(self, options: dict = {}):
        self.options = options

    @abc.abstractmethod
    def update(self):
        pass
