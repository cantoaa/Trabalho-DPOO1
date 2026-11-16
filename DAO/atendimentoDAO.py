from AbstractDAO import AbstractDAO
from Model.atendimento import Atendimento

class AtendimentoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento : Atendimento):
        if(isinstance(atendimento, Atendimento)):
            super().add(paciente.cpf, paciente)

    def get(self, key : int):
        if(isinstance(key,int)):
            return super().get(key)

    def remove(self, key : int):
        if(isinstance(key,int)):
            return super().remove(key)
