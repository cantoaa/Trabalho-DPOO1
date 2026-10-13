from Control.abstractcontrol import Control
from View.view_profissional import ViewProfissional
from Model.profissional import Profissional

class ControlProfissional(Control):
    def __init__(self, control_geral):
        self.__profissionais = []
        self.__tela = ViewProfissional(self)
        self.control_geral = control_geral

    def cadastrar_profissional(self):
        dados = self.__tela.criar_profissional()
        self.__profissionais.append(Profissional(dados[0], dados[1], dados[2], dados[3], dados[4]))
        return dados

    def escolher_profissional(self):
        if(len(self.__profissionais) > 0):
            profissional = self.__profissionais[self.__tela.escolher_profissional(self.__profissionais)]
            return profissional

    def buscar_profissional(self):
        if(len(self.__profissionais) > 0):
            cpf = self.__tela.buscar_profissional()
            for profissional in self.__profissionais:
                if profissional.cpf == cpf:
                    self.__tela.mostrar_profissional(profissional)
                    return profissional 
        return None

    def excluir_profissional(self):
        if(len(self.__profissionais) > 0):
            self.__profissionais.remove(self.escolher_profissional())

    def listar_profissionais(self):
        if(len(self.__profissionais) > 0):
            self.__tela.listar_profissionais(self.__profissionais)

    def iniciar(self):
        opcoes = "1.Cadastrar profissional\n2.Buscar profissional\n3.Excluir profissional\n4.Listar Profissionais\n0.Sair"
        switch = {1 : self.cadastrar_profissional, 2 : self.buscar_profissional, 3 : self.excluir_profissional, 4 : self.listar_profissionais, 0 : self.sair}
        self.__tela.mostrar_menu(opcoes, switch)
    def sair(self):
        self.control_geral.iniciar()
