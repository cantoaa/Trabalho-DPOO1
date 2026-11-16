from AbstractDAO import AbstractDAO
from Model.paciente import Paciente

class PacienteDAO(AbstractDAO):
    def __init__(self):
        super().__init__('pacientes.pkl')

    def add(self, paciente : Paciente):
        if(isinstance(paciente, Paciente)):
            super().add(paciente.cpf, paciente)

    def get(self, key : int):
        if(isinstance(key,int)):
            return super().get(key)

    def remove(self, key : int):
        if(isinstance(key,int)):
            return super().remove(key)

