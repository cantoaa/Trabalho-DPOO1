
from AbstractDAO import AbstractDAO
from Model.profissional import Profissional

class ProfissionalDAO(AbstractDAO):
    def __init__(self):
        super().__init__('profissionais.pkl')

    def add(self, profissional : Profissional):
        if(isinstance(profissional, Profissional)):
            super().add(profissional.cpf, profissional)

    def get(self, key : int):
        if(isinstance(key,int)):
            return super().get(key)

    def remove(self, key : int):
        if(isinstance(key,int)):
            return super().remove(key)
