from Model.paciente import Paciente
from View.view_paciente import ViewPaciente
from Control.abstractcontrol import Control
from DAO.pacienteDAO import PacienteDAO

class ControlPaciente(Control):
    def __init__(self, control_geral):
        self.__pacienteDAO = PacienteDAO()
        self.__tela = ViewPaciente(self)
        self.control_geral = control_geral

    def cadastrar_paciente(self):
        dados = self.__tela.cadastrar_paciente()
        paciente = Paciente(dados[0],dados[1],dados[2],dados[3])
        self.__pacienteDAO.add(paciente)
    def listar_pacientes(self):
        if(len(self.__pacientes) > 0):
            self.__tela.listar_pacientes(self.__pacienteDAO.get_all())
    def excluir_paciente(self):
        if(len(self.__pacientes) > 0):
            paciente = self.escolher_paciente()
            self.__pacientes.remove(paciente)
    def iniciar(self):
        self.__tela.mostrar_menu()
    def sair(self):
        self.control_geral.iniciar()

    def escolher_paciente(self):
        if(len(self.__pacienteDAO.get_all()) > 0):
            paciente = self.__pacienteDAO.get(self.__tela.escolher_paciente(self.__pacienteDAO.get_all()))
            return paciente

    def buscar_paciente(self):
        if(len(self.__pacientes) > 0):
            cpf = self.__tela.buscar_paciente()
            for paciente in self.__pacienteDAO.get_all():
                if paciente.cpf == cpf:
                    self.__tela.mostrar_paciente(paciente)
                    return paciente
        return None
    def alterar_paciente(self):
        index = self.escolher_paciente()
        dados = self.cadastrar_paciente()
        self.__pacienteDAO.get(index) = Paciente(dados[0],dados[1],dados[2],dados[3])
