from Model.atendimento import Atendimento
from View.view_atendimento import ViewAtendimento
from Control.abstractcontrol import Control



class ControlAtendimento(Control):
    def __init__(self, control_geral):
        self.__atendimentos = []
        self.__tela = ViewAtendimento(self)
        self.control_geral = control_geral

    @property
    def atendimentos(self):
        return self.__atendimentos

    def cadastrar_atendimento(self):
        dados = self.__tela.cadastrar_atendimento() 
        if(dados["horario1"] < 24 & dados["horario1"] >= 0 & dados["horario2"] < 24 & dados["horario2"] >= 0 & dados["horario1"] < dados["horario2"]):
            raise ValueError("Tentou-se inserir uma faixa de horario inexistente")
        try:
            atendimento = Atendimento(dados["clinica"], dados["paciente"], dados["profissional"], dados["data"], dados["horario1"], dados["horario2"], dados["tipo"], dados["valor"])
            self.__atendimentos.append(atendimento)
        except:
            raise ValueError("Erro ao criar o atendimento, por favor verifique os tipos dos parametros")
        self.__atendimentos.append(atendimento)
    def mostrar_atendimentos(self):
        if(len(self.__atendimentos) > 0):
            self.__tela.listar_atendimentos()
    def escolher_atendimento(self):
        if(len(self.__atendimentos) > 0):
            return self.__tela.escolher_atendimento(self.__atendimentos)
    def iniciar(self):
        opcoes = "1. Mostrar Atendimentos\n2.Cadastrar Atendimento\n3.Excluir Atendimento\n4.Alterar Atendimento\n5. Listar atendimentos\n0.Sair(Voltar ao menu principal)"
        switch = {0 : self.sair, 1 : self.mostrar_atendimentos, 2 : self.cadastrar_atendimento, 3 : self.excluir_atendimento, 4:self.alterar_atendimento, 5 : self.mostrar_atendimentos,0 : self.sair}
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
        prof = control_geral.control_profissional.buscar_profissional()
        self.__atendimentos[index].profissional = prof

    def adicionar_procedimento(self):
        atendimento = self.__tela.escolher_atendimento()
        proced = self.control_geral.control_procedimento.escolher_procedimento()
        self.__atendimentos[atendimento].procedimentos.append(self.control_geral.control_procedimento.procedimentos[proced])
    def excluir_atendimento(self):
        if(len(self.__atendimentos) > 0):
            del self.__atendimentos[self.__tela.escolher_atendimento()]
