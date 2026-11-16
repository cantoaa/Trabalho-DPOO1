from Model.atendimento import Atendimento
from View.view_atendimento import ViewAtendimento
from Control.abstractcontrol import Control
from DAO.atendimentoDAO import AtendimentoDAO



class ControlAtendimento(Control):
    def __init__(self, control_geral):
        self.__atendimentoDAO = AtendimentoDAO()
        self.__tela = ViewAtendimento(self)
        self.control_geral = control_geral

    @property
    def atendimentos(self):
        return self.__atendimentos

    def cadastrar_atendimento(self):
        dados = self.__tela.cadastrar_atendimento() 
        if(dados["horario1"] < 24 and dados["horario1"] >= 0 and dados["horario2"] < 24 and dados["horario2"] >= 0 and dados["horario1"] < dados["horario2"]):
            if(dados["paciente"].idade >= 18):
                atendimento = Atendimento(dados["clinica"], dados["paciente"], dados["profissional"], dados["data"], [dados["horario1"], dados["horario2"]], dados["tipo"], dados["valor"], dados["index"])
                self.__atendimentoDAO.add(atendimento)
            else:
                raise ValueError("O paciente não tem idade suficiente.")
        else:
            raise ValueError("Tentou-se inserir uma faixa de horario inexistente")
    def mostrar_atendimentos(self):
        if(len(self.__atendimentos) > 0):
            self.__tela.listar_atendimentos(self.__atendimentoDAO.get_all())
    def escolher_atendimento(self):
        if(len(self.__atendimentos) > 0):
            return self.__tela.escolher_atendimento(self.__atendimentoDAO.get_all())
    def iniciar(self):
        opcoes = "1. Mostrar Atendimentos\n2.Cadastrar Atendimento\n3.Excluir Atendimento\n4.Alterar Atendimento\n5. Listar atendimentos\n6. Mostrar procedimentos realizados\n7.Mostrar atendimento mais caro e o mais barato\n0.Sair(Voltar ao menu principal)"
        switch = {0 : self.sair, 1 : self.mostrar_atendimentos, 2 : self.cadastrar_atendimento, 3 : self.excluir_atendimento, 4:self.alterar_atendimento, 5 : self.mostrar_atendimentos, 6 : self.mostrar_procedimentos, 7 : self.atendimento_mais_carobarato,0 : self.sair}
        self.__tela.mostrar_menu(opcoes,switch)
    def sair(self):
        self.control_geral.iniciar()
    def alterar_atendimento(self):
        if(len(self.__atendimentos) > 0):
            opcoes = "1.Atribuir procedimento\n2.Mudar profissional\n0.Sair(voltar ao menu de atendimentos)"
            switch = {0 : self.sair, 1 : self.adicionar_procedimento, 2 : self.alterar_profatendimento}
            self.__tela.mostrar_menu(opcoes, switch)

    def alterar_profatendimento(self):
        index = self.escolher_atendimento()
        prof = self.control_geral.control_profissional.buscar_profissional()
        atendimento = self.__atendimentoDAO.get(index)
        atendimento.profissional = prof
        self.__atendimentoDAO.update(index, atendimento)

    def adicionar_procedimento(self):
        atendimentoindex = self.__tela.escolher_atendimento(self.__atendimentos)
        proced = self.control_geral.control_procedimento.escolher_procedimento()
        atendimento = self.__atendimentoDAO.get(atendimentoindex)
        atendimento.procedimentos.append(self.control_geral.control_procedimento.procedimentos[proced])
        atendimento.valor(self.__atendimentos[atendimento].valor + self.__atendimentos[atendimento].procedimentos[-1].custo)
        self.__atendimentoDAO.update(atendimentoindex, atendimento)
    def mostrar_procedimentos(self):
        index = self.escolher_atendimento()
        self.__tela.mostrar_procedimentos(self.__atendimentoDAO.get(index))
    #def mostrar_clinica_mais_atend(self):
    #    for atendimento in self.__atendimentos:
    #        clinicas = []
    #        if(atendimento.clinica not in clinicas):
    #            clinicas.append()
    # Depois implementar
    def atendimento_mais_carobarato(self):
        atendimento_anterior = 0
        atendimento_caro = 0
        atendimento_barato = 0
        for atendimento in self.__atendimentos:
            if(atendimento.valor >= atendimento_anterior):
                atendimento_caro = atendimento
            atendimento_anterior = atendimento.valor
        atendimento_anterior = self.__atendimentos[0].valor
        for atendimento in self.__atendimentos:
            if(atendimento.valor <= atendimento_anterior):
                atendimento_barato = atendimento
            atendimento_anterior = atendimento.valor
        self.__tela.mostrar_atendimento(atendimento_caro)
        self.__tela.mostrar_atendimento(atendimento_barato)
    def excluir_atendimento(self):
        index = self.escolher_atendimento()
        self.__atendimentoDAO.remove(index)
