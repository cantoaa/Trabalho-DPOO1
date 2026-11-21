from DAO.AbstractDAO import AbstractDAO
from Model.clinica import Clinica

class ClinicaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('clinicas.pkl')

    def add(self, clinica : Clinica):
        if(isinstance(clinica, Clinica)):
            super().add(clinica.nome, clinica)

    def get(self, key : str):
        if(isinstance(key,str)):
            return super().get(key)

    def remove(self, key : str):
        if(isinstance(key,str)):
            return super().remove(key)
