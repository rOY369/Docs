import abc

from computer import Computer


class AbstractBuilder(metaclass=abc.ABCMeta):
    def new_computer(self):
        self._computer = Computer()

    def get_computer(self):
        return self._computer

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass

    @abc.abstractmethod
    def install_hard_drive(self):
        pass

    @abc.abstractmethod
    def install_video_card(self):
        pass
