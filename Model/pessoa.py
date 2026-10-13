from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome : str, celular : int, cpf : int):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    
    @property
    @abstractmethod
    def nome(self):
        pass

    @property
    @abstractmethod
    def celular(self):
        pass

    @property
    @abstractmethod
    def cpf(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self,nome : str):
        pass

    @celular.setter
    @abstractmethod
    def celular(self, celular : int):
        pass

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf : int):
        pass
    
