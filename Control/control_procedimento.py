from Control.abstractcontrol import Control
from View.view_procedimento import ViewProcedimento
from Model.procedimento import Procedimento


class ControlProcedimento(Control):
    def __init__(self, control_geral):
        self.__procedimentos = []
        self.__tela = ViewProcedimento(self)
        self.control_geral = control_geral

    @property
    def procedimentos(self):
        return self.__procedimentos

    def criar_procedimento(self):
        dados = self.__tela.criar_procedimento()
        self.__procedimentos.append(Procedimento(dados[0], dados[1], self.control_geral.control_profissional.buscar_profissional()))
        return dados

    def mostrar_procedimentos(self):
        if(len(self.__procedimentos) > 0):
            self.__tela.listar_procedimentos(self.__procedimentos)
    def escolher_procedimento(self):
        if(len(self.__procedimentos) > 0):
            opcao = self.__tela.escolher_procedimento(self.__procedimentos)
            return opcao

    def alterar_procedimento(self):
        if(len(self.__procedimentos) > 0):
            index = self.escolher_procedimento()
            dados = self.__tela.alterar_procedimento()
            self.__procedimentos[index] = Procedimento(dados[0], dados[1], self.control_geral.control_profissional.buscar_profissional())

    def excluir_procedimento(self):
        if(len(self.__procedimentos) > 0):
            index = self.escolher_procedimento()
            del self.__procedimentos[index]

    def iniciar(self):
        opcoes = "1.Cadastrar procedimento\n2.Alterar procedimento\n3.Excluir procedimento\n4. Listar procedimentos\n0.Sair"
        switch = {0 : self.sair, 1 : self.criar_procedimento, 2 : self.alterar_procedimento, 3 : self.excluir_procedimento, 4: self.mostrar_procedimentos, 0 : self.sair}
        self.__tela.mostrar_menu(opcoes, switch)

    def sair(self):
        self.control_geral.iniciar()
