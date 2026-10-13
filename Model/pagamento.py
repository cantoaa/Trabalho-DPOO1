from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def __init__(self,valor : int):
        self.__valor = valor

    @property
    @abstractmethod
    def valor(self):
        return self.__valor

    @valor.setter
    @abstractmethod
    def valor(self, valor : int):
        self.__valor = valor

class Dinheiro(Pagamento):
    def __init__(self, valor : int):
        super().__init__(valor)

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self,valor : int):
        self.__valor = valor

class Pix(Pagamento):
    def __init__(self, valor : int, cpf : int):
        super().__init__(valor)
        self.__cpf = cpf

    @property
    def valor(self):
        return self.__valor

    @property
    def cpf(self):
        return self.__cpf

    @valor.setter
    def valor(self, valor : int):
        self.__valor = valor

    @cpf.setter
    def cpf(self, cpf : int):
        self.__cpf = cpf

class CartaoCredito(Pagamento):
    def __init__(self, valor : int, numero_cartao : int, bandeira : str):
        super().__init__(valor)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def valor(self):
        return self.__valor

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @valor.setter
    def valor(self, valor : int):
        self.__valor = valor

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao : int):
        self.__numero_cartao = numero_cartao

    @bandeira.setter
    def bandeira(self, bandeira : str):
        self.__bandeira = bandeira
