from Model.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome : str, celular : int, cpf : int):
        if(isinstance(nome,str) & isinstance(celular,int) & isinstance(cpf,int)):
            self.__nome = nome
            self.__celular = celular
            self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    @property
    def celular(self):
        return self.__celular
    @property
    def cpf(self):
        return self.__cpf
    
    @nome.setter
    def nome(self, nome : str):
        if isinstance(nome,str):
            self.__nome = nome

    @celular.setter
    def celular(self, celular:int):
        if isinstance(celular, int):
            self.__celular = celular
    @cpf.setter
    def cpf(self, cpf : int):
        if(isinstance(cpf, int)):
            self.__cpf = cpf

