import abc
from abstract_observer import AbstractObserver


class AbstractSubject(metaclass=abc.ABCMeta):

    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbstractObserver):
            raise TypeError("Observer not derived from Abstract Observer")
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value:
                observer.update(value)
            else:
                observer.update()
