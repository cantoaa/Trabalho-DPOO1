from Model.paciente import Paciente
from View.view_paciente import ViewPaciente
from Control.abstractcontrol import Control

class ControlPaciente(Control):
    def __init__(self, control_geral):
        self.__pacientes = []
        self.__tela = ViewPaciente(self)
        self.control_geral = control_geral

    def cadastrar_paciente(self):
        dados = self.__tela.cadastrar_paciente()
        self.__pacientes.append(Paciente(dados[0],dados[1],dados[2]))
    def listar_pacientes(self):
        if(len(self.__pacientes) > 0):
            self.__tela.listar_pacientes(self.__pacientes)
    def excluir_paciente(self):
        if(len(self.__pacientes) > 0):
            paciente = self.escolher_paciente()
            self.__pacientes.remove(paciente)
    def iniciar(self):
        self.__tela.mostrar_menu()
    def sair(self):
        self.control_geral.iniciar()

    def escolher_paciente(self):
        if(len(self.__pacientes) > 0):
            paciente = self.__pacientes[self.__tela.escolher_paciente(self.__pacientes)]
            return paciente

    def buscar_paciente(self):
        if(len(self.__pacientes) > 0):
            cpf = self.__tela.buscar_paciente()
            for paciente in self.__pacientes:
                if paciente.cpf == cpf:
                    self.__tela.mostrar_paciente(paciente)
                    return paciente
        return None
