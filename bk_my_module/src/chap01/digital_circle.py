from abc import ABCMeta, abstractmethod


class DigitalCircle(metaclass=ABCMeta):
    @abstractmethod
    def clock(self, i):
        pass
