from Control.control_paciente import ControlPaciente
from Control.control_profissional import ControlProfissional
from Control.control_procedimento import ControlProcedimento
from Control.control_clinica import ControlClinica
from Control.control_atendimento import ControlAtendimento
from Control.abstractcontrol import Control
from View.view_geral import ViewGeral

class ControlGeral(Control):
    def __init__(self):
        self.control_atendimento = ControlAtendimento(self)
        self.control_procedimento = ControlProcedimento(self)
        self.control_clinica = ControlClinica(self)
        self.control_paciente = ControlPaciente(self)
        self.control_profissional = ControlProfissional(self)
        self.tela = ViewGeral(self)

    def sair(self):
        exit()
    def iniciar(self):
        self.tela.mostrar_menu()
