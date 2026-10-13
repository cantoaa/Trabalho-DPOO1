from Model.profissional import Profissional


class Procedimento:
    def __init__(self, descricao : str, custo : int, profissional : Profissional):
        if(isinstance(descricao,str) & isinstance(custo,int) & isinstance(profissional, Profissional)):
            self.__descricao = descricao
            self.__custo = custo
            self.__profissional = profissional

    @property
    def descricao(self):
        return self.__descricao
    @property 
    def custo(self):
        return self.__custo
    @property
    def profissional(self):
        return self.__profissional
    
    @descricao.setter
    def descricao(self, descricao : str):
        if(isinstance(descricao,str)):
            self.__descricao = descricao
    @custo.setter
    def custo(self, custo : int):
        if(isinstance(custo,int)):
            self__custo = custo
    @profissional.setter
    def profissional(self, profissional : Profissional):
        if(isinstance(profissional, Profissional)):
            self.__profissional = profissional
