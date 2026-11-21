from DAO.AbstractDAO import AbstractDAO
from Model.procedimento import Procedimento

class ProcedimentoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('procedimentos.pkl')

    def add(self, procedimento : Procedimento):
        if(isinstance(procedimento, Procedimento)):
            super().add(procedimento.descricao, procedimento)

    def get(self, key : str):
        if(isinstance(key,str)):
            return super().get(key)

    def remove(self, key : str):
        if(isinstance(key,str)):
            return super().remove(key)
