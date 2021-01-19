import abc


class AbstractShipper(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, order):
        pass


class FedEx(AbstractShipper):
    def calculate(self, order):
        return 3.00


class UPS(AbstractShipper):
    def calculate(self, order):
        return 4.00


class Postal(AbstractShipper):
    def calculate(self, order):
        return 4.00
