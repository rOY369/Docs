import abc


class AbstractCommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass
