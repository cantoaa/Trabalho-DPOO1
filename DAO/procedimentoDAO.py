
from AbstractDAO import AbstractDAO
from Model.procedimento import Procedimento

class PacienteDAO(AbstractDAO):
    def __init__(self):
        super().__init__('procedimentos.pkl')

    def add(self, procedimento : Procedimento):
        if(isinstance(procedimento, Procedimento)):
            super().add(procedimento.cpf, procedimento)

    def get(self, key : int):
        if(isinstance(key,int)):
            return super().get(key)

    def remove(self, key : int):
        if(isinstance(key,int)):
            return super().remove(key)
