from Control.abstractcontrol import Control
from View.view_procedimento import ViewProcedimento
from Model.procedimento import Procedimento
from DAO.procedimentoDAO import ProcedimentoDAO


class ControlProcedimento(Control):
    def __init__(self, control_geral):
        self.__procedimentoDAO = ProcedimentoDAO()
        self.__tela = ViewProcedimento(self)
        self.control_geral = control_geral

    @property
    def procedimentos(self):
        return list(self.__procedimentoDAO.get_all())

    def criar_procedimento(self):
        dados = self.__tela.criar_procedimento()
        profissional = self.control_geral.control_profissional.buscar_profissional()
        if(profissional == None):
            print("O procedimento não foi criado, profissional não encontrado")
            return None
        if(self.__procedimentoDAO.get(dados[0]) != None):
            print("Ja existe um procedimento com essa descrição")
            return None
        try:
            self.__procedimentoDAO.add(Procedimento(dados[0], dados[1], profissional))
        except:
            print("O procedimento não foi criado, verifique os valores enviados")
        return dados

    def mostrar_procedimentos(self):
        if(len(self.procedimentos) > 0):
            self.__tela.listar_procedimentos(self.procedimentos)
    def escolher_procedimento(self):
        if(len(self.procedimentos) > 0):
            opcao = self.__tela.escolher_procedimento(self.procedimentos)
            return opcao

    def alterar_procedimento(self):
        if(len(self.procedimentos) > 0):
            index = self.escolher_procedimento()
            if(index == None):
                return None
            procedimento = self.procedimentos[index]
            dados = self.__tela.alterar_procedimento()
            profissional = self.control_geral.control_profissional.buscar_profissional()
            if(profissional == None):
                print("O procedimento não foi alterado, profissional não encontrado")
                return None
            self.__procedimentoDAO.remove(procedimento.descricao)
            self.__procedimentoDAO.add(Procedimento(dados[0], dados[1], profissional))

    def excluir_procedimento(self):
        if(len(self.procedimentos) > 0):
            index = self.escolher_procedimento()
            if(index != None):
                self.__procedimentoDAO.remove(self.procedimentos[index].descricao)

    def iniciar(self):
        opcoes = "1.Cadastrar procedimento\n2.Alterar procedimento\n3.Excluir procedimento\n4. Listar procedimentos\n5.Mostrar procedimento mais caro e mais barato\n0.Sair(Voltar ao menu principal)"
        switch = {0 : self.sair, 1 : self.criar_procedimento, 2 : self.alterar_procedimento, 3 : self.excluir_procedimento, 4: self.mostrar_procedimentos, 5 : self.proced_mais_carobarato}
        self.__tela.mostrar_menu(opcoes, switch)
    def proced_mais_carobarato(self):
        procedimentos = self.procedimentos
        if(len(procedimentos) > 0):
            proced_caro = procedimentos[0]
            proced_barato = procedimentos[0]
            for proced in procedimentos:
                if(proced.custo > proced_caro.custo):
                    proced_caro = proced
                if(proced.custo < proced_barato.custo):
                    proced_barato = proced
            self.__tela.mostrar_procedimento(proced_caro)
            self.__tela.mostrar_procedimento(proced_barato)
    def sair(self):
        self.control_geral.iniciar()
