from Model.paciente import Paciente
from View.view_paciente import ViewPaciente
from Control.abstractcontrol import Control
from DAO.pacienteDAO import PacienteDAO

class ControlPaciente(Control):
    def __init__(self, control_geral):
        self.__pacienteDAO = PacienteDAO()
        self.__tela = ViewPaciente(self)
        self.control_geral = control_geral

    @property
    def pacientes(self):
        return list(self.__pacienteDAO.get_all())

    def cadastrar_paciente(self):
        dados = self.__tela.cadastrar_paciente()
        paciente = Paciente(dados[0],dados[1],dados[2],dados[3])
        self.__pacienteDAO.add(paciente)
    def listar_pacientes(self):
        if(len(self.pacientes) > 0):
            self.__tela.listar_pacientes(self.pacientes)
    def excluir_paciente(self):
        if(len(self.pacientes) > 0):
            paciente = self.escolher_paciente()
            if(paciente != None):
                self.__pacienteDAO.remove(paciente.cpf)
    def iniciar(self):
        self.__tela.mostrar_menu()
    def sair(self):
        self.control_geral.iniciar()

    def escolher_paciente(self):
        pacientes = self.pacientes
        if(len(pacientes) > 0):
            index = self.__tela.escolher_paciente(pacientes)
            if(index != None):
                return pacientes[index]
        return None

    def buscar_paciente(self):
        if(len(self.pacientes) > 0):
            cpf = self.__tela.buscar_paciente()
            paciente = self.__pacienteDAO.get(cpf)
            if(paciente != None):
                self.__tela.mostrar_paciente(paciente)
                return paciente
        return None
    def alterar_paciente(self):
        paciente = self.escolher_paciente()
        if(paciente != None):
            dados = self.__tela.cadastrar_paciente()
            self.__pacienteDAO.remove(paciente.cpf)
            self.__pacienteDAO.add(Paciente(dados[0],dados[1],dados[2],dados[3]))
