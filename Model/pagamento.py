from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def __init__(self, valor : int, data : tuple):
        if(isinstance(valor, int) and valor >= 0 and isinstance(data, tuple) and len(data) == 3):
            self.__valor = valor
            self.__data = data
        else:
            raise ValueError("Os valores enviados como parametros para o construtor de Pagamento tem tipos diferentes dos requisitados")

    @property
    def valor(self) -> int:
        return self.__valor
    @property
    def data(self) -> tuple:
        return self.__data

    @valor.setter
    def valor(self, valor : int):
        if(isinstance(valor, int)):
            self.__valor = valor
    @data.setter
    def data(self, data : tuple):
        if(isinstance(data, tuple) and len(data) == 3):
            self.__data = data

class Dinheiro(Pagamento):
    def __init__(self, valor : int, data : tuple):
        super().__init__(valor, data)

class Pix(Pagamento):
    def __init__(self, valor : int, data : tuple, cpf : int):
        super().__init__(valor, data)
        if(isinstance(cpf, int)):
            self.__cpf = cpf
        else:
            raise ValueError("O CPF do pagador deve ser um numero inteiro")

    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf : int):
        if(isinstance(cpf, int)):
            self.__cpf = cpf

class CartaoCredito(Pagamento):
    def __init__(self, valor : int, data : tuple, numero_cartao : int, bandeira : str):
        super().__init__(valor, data)
        if(isinstance(numero_cartao, int) and isinstance(bandeira, str)):
            self.__numero_cartao = numero_cartao
            self.__bandeira = bandeira
        else:
            raise ValueError("O numero do cartao deve ser inteiro e a bandeira deve ser texto")

    @property
    def numero_cartao(self) -> int:
        return self.__numero_cartao
    @property
    def bandeira(self) -> str:
        return self.__bandeira

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao : int):
        if(isinstance(numero_cartao, int)):
            self.__numero_cartao = numero_cartao
    @bandeira.setter
    def bandeira(self, bandeira : str):
        if(isinstance(bandeira, str)):
            self.__bandeira = bandeira
