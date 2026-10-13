from abc import ABC, abstractmethod

class Control(ABC):

    @abstractmethod
    def iniciar(self):
        pass
    @abstractmethod
    def sair(self):
        pass
