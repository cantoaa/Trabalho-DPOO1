from Control.abstractcontrol import Control
from View.view_profissional import ViewProfissional
from Model.profissional import Profissional
from DAO.profissionalDAO import ProfissionalDAO

class ControlProfissional(Control):
    def __init__(self, control_geral):
        self.__profissionalDAO = ProfissionalDAO()
        self.__tela = ViewProfissional(self)
        self.control_geral = control_geral

    @property
    def profissionais(self):
        return list(self.__profissionalDAO.get_all())

    def cadastrar_profissional(self):
        dados = self.__tela.criar_profissional()
        self.__profissionalDAO.add(Profissional(dados[0], dados[1], dados[2], dados[3], dados[4]))
        return dados

    def escolher_profissional(self):
        profissionais = self.profissionais
        if(len(profissionais) > 0):
            index = self.__tela.escolher_profissional(profissionais)
            if(index != None):
                return profissionais[index]
        return None

    def buscar_profissional(self):
        if(len(self.profissionais) > 0):
            cpf = self.__tela.buscar_profissional()
            profissional = self.__profissionalDAO.get(cpf)
            if(profissional != None):
                self.__tela.mostrar_profissional(profissional)
                return profissional
        return None

    def excluir_profissional(self):
        if(len(self.profissionais) > 0):
            profissional = self.escolher_profissional()
            if(profissional != None):
                self.__profissionalDAO.remove(profissional.cpf)

    def listar_profissionais(self):
        if(len(self.profissionais) > 0):
            self.__tela.listar_profissionais(self.profissionais)

    def iniciar(self):
        opcoes = "1.Cadastrar profissional\n2.Buscar profissional\n3.Excluir profissional\n4.Listar Profissionais\n0.Sair(Voltar para o menu principal)"
        switch = {1 : self.cadastrar_profissional, 2 : self.buscar_profissional, 3 : self.excluir_profissional, 4 : self.listar_profissionais, 0 : self.sair}
        self.__tela.mostrar_menu(opcoes, switch)
    def sair(self):
        self.control_geral.iniciar()
