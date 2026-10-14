from Model.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome : str, celular : int, cpf : int, idade : int):
        if(isinstance(nome,str) and isinstance(celular,int) and isinstance(cpf,int) and isinstance(idade,int)):
            self.__nome = nome
            self.__celular = celular
            self.__cpf = cpf
            self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def celular(self):
        return self.__celular
    @property
    def cpf(self):
        return self.__cpf
    @property
    def idade(self):
        return self.__idade
    
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
    @idade.setter
    def idade(self, idade : int):
        if(isinstance(idade, int)):
            self.__idade = idade
