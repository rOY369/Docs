import abc


class MyABC(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_something(self):
        pass

    @abc.abstractproperty
    def some_property(self):
        pass


class MyConcreteClass(MyABC):
    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        self._myprop *= 2 + value

    @property
    def some_property(self):
        return self._myprop


myObject = MyConcreteClass(4)
myObject.do_something(3)
print(myObject.some_property)


class BadClass(MyABC):
    pass


bcObject = BadClass()
