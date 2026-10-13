from Model.pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome : str, celular : int, cpf : int, especialidade : str, rp : str):
        if(isinstance(nome,str) & isinstance(celular,int) & isinstance(cpf, int) & isinstance(especialidade,str) & isinstance(rp, str)):
            self.__nome = nome
            self.__celular = celular
            self.__cpf = cpf
            self.__especialidade = especialidade
            self.__rp = rp #registro profissional

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
    def especialidade(self):
        return self.__especialidade

    @property
    def rp(self):
        return self.__rp

    @nome.setter
    def nome(self, nome : str):
        if(isinstance(nome,str)):
            self.__nome = nome

    @celular.setter
    def celular(self, celular : int):
        if(isinstance(celular,int)):
            self.__celular = celular

    @cpf.setter
    def cpf(self, cpf : int):
        if(isinstance(cpf,int)):
            self.__cpf = cpf

    @especialidade.setter
    def especialidade(self, especialidade : str):
        if(isinstance(especialidade,str)):
            self.__especialidade = especialidade
    @rp.setter
    def rp(self, rp : str):
        if(isinstance(rp,str)):
            self.__rp = rp
    
