from Model.clinica import Clinica
from Model.paciente import Paciente
from Model.profissional import Profissional
from Model.procedimento import Procedimento


class Atendimento:
    def __init__(self, clinica : Clinica, paciente : Paciente, profissional : Profissional, data : tuple, horario : list, tipo : str, valor : int):
        if(isinstance(clinica, Clinica) and isinstance(paciente, Paciente) and isinstance(profissional, Profissional) and isinstance(data, tuple) and isinstance(horario,list) and len(horario) == 2 and horario[0] < 24 and horario[0] >= 0 and horario[1] < 24 and horario[1] >= 0 and horario[0] < horario[1] and isinstance(tipo,str) and isinstance(valor,int)):
            self.__clinica = clinica
            self.__paciente = paciente
            self.__profissional = profissional
            self.__data = data
            self.__horario = horario
            self.__tipo = tipo
            self.__valor = valor
            self.__procedimentos = []
        else:
            raise ValueError("Os valores enviados como parametros para o construtor de Clinica tem tipos diferentes dos requisitados")

    @property
    def clinica(self) -> Clinica:
        return self.__clinica
    @property 
    def paciente(self) -> Paciente:
        return self.__paciente
    @property
    def profissional(self) -> Profissional:
        return self.__profissional
    @property
    def data(self) -> tuple:
        return self.__data
    @property
    def horario(self) -> list:
        return self.__horario
    @property
    def tipo(self) -> str:
        return self.__tipo
    @property
    def valor(self) -> int:
        return self.__valor
    @property
    def procedimentos(self):
        return self.__procedimentos

    @clinica.setter
    def clinica(self, clinica : Clinica):
        self.__clinica = clinica
    @paciente.setter
    def paciente(self, paciente : Paciente):
        self.__paciente = paciente
    @profissional.setter
    def profissional(self, profissional : Profissional):
        self.__profissional = profissional
    @data.setter
    def data(self, data : tuple):
        self.__data = data
    @horario.setter
    def horario(self, horario : list):
        if(len(horario) == 2 & horario[0] < 24 & horario[0] >= 0 & horario[1] < 24 & horario[1] >= 0 & horario[0] < horario[1]):
            self.__horario = horario
        else:
            raise ValueError("Tentou-se inserir uma faixa de horario inexistente")
