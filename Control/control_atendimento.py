from Model.atendimento import Atendimento
from Model.pagamento import Dinheiro, Pix, CartaoCredito
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
        return list(self.__atendimentoDAO.get_all())

    def cadastrar_atendimento(self):
        dados = self.__tela.cadastrar_atendimento()
        if(dados == None):
            return None
        if(self.__atendimentoDAO.get(dados["index"]) != None):
            print("Ja existe um atendimento com esse codigo.")
            return None
        if(dados["horario1"] < 24 and dados["horario1"] >= 0 and dados["horario2"] < 24 and dados["horario2"] >= 0 and dados["horario1"] < dados["horario2"]):
            if(dados["paciente"].idade >= 18):
                atendimento = Atendimento(dados["clinica"], dados["paciente"], dados["profissional"], dados["data"], [dados["horario1"], dados["horario2"]], dados["tipo"], dados["valor"], dados["index"])
                self.__atendimentoDAO.add(atendimento)
            else:
                raise ValueError("O paciente não tem idade suficiente.")
        else:
            raise ValueError("Tentou-se inserir uma faixa de horario inexistente")
    def mostrar_atendimentos(self):
        if(len(self.atendimentos) > 0):
            self.__tela.listar_atendimentos(self.atendimentos)
    def escolher_atendimento(self):
        atendimentos = self.atendimentos
        if(len(atendimentos) > 0):
            opcao = self.__tela.escolher_atendimento(atendimentos)
            if(opcao != None):
                return atendimentos[opcao].index
        return None
    def iniciar(self):
        opcoes = "1. Mostrar Atendimentos\n2.Cadastrar Atendimento\n3.Excluir Atendimento\n4.Alterar Atendimento\n5. Listar atendimentos\n6. Mostrar procedimentos realizados\n7.Mostrar atendimento mais caro e o mais barato\n8.Realizar pagamento\n9.Mostrar pagamento\n0.Sair(Voltar ao menu principal)"
        switch = {0 : self.sair, 1 : self.mostrar_atendimentos, 2 : self.cadastrar_atendimento, 3 : self.excluir_atendimento, 4:self.alterar_atendimento, 5 : self.mostrar_atendimentos, 6 : self.mostrar_procedimentos, 7 : self.atendimento_mais_carobarato, 8 : self.realizar_pagamento, 9 : self.mostrar_pagamento}
        self.__tela.mostrar_menu(opcoes,switch)
    def sair(self):
        self.control_geral.iniciar()
    def alterar_atendimento(self):
        if(len(self.atendimentos) > 0):
            opcoes = "1.Atribuir procedimento\n2.Mudar profissional\n0.Sair(voltar ao menu de atendimentos)"
            switch = {0 : self.iniciar, 1 : self.adicionar_procedimento, 2 : self.alterar_profatendimento}
            self.__tela.mostrar_menu(opcoes, switch)

    def alterar_profatendimento(self):
        index = self.escolher_atendimento()
        if(index == None):
            return None
        prof = self.control_geral.control_profissional.buscar_profissional()
        if(prof == None):
            return None
        atendimento = self.__atendimentoDAO.get(index)
        atendimento.profissional = prof
        self.__atendimentoDAO.update(index, atendimento)

    def adicionar_procedimento(self):
        index = self.escolher_atendimento()
        if(index == None):
            return None
        proced = self.control_geral.control_procedimento.escolher_procedimento()
        if(proced == None):
            return None
        atendimento = self.__atendimentoDAO.get(index)
        if(atendimento.pagamento != None):
            print("Atendimento ja pago, não é possivel adicionar procedimentos.")
            return None
        procedimento = self.control_geral.control_procedimento.procedimentos[proced]
        atendimento.procedimentos.append(procedimento)
        atendimento.valor = atendimento.valor + procedimento.custo
        self.__atendimentoDAO.update(index, atendimento)
    def mostrar_procedimentos(self):
        index = self.escolher_atendimento()
        if(index != None):
            self.__tela.mostrar_procedimentos(self.__atendimentoDAO.get(index))
    #def mostrar_clinica_mais_atend(self):
    #    for atendimento in self.__atendimentos:
    #        clinicas = []
    #        if(atendimento.clinica not in clinicas):
    #            clinicas.append()
    # Depois implementar
    def atendimento_mais_carobarato(self):
        atendimentos = self.atendimentos
        if(len(atendimentos) > 0):
            atendimento_caro = atendimentos[0]
            atendimento_barato = atendimentos[0]
            for atendimento in atendimentos:
                if(atendimento.valor > atendimento_caro.valor):
                    atendimento_caro = atendimento
                if(atendimento.valor < atendimento_barato.valor):
                    atendimento_barato = atendimento
            self.__tela.mostrar_atendimento(atendimento_caro)
            self.__tela.mostrar_atendimento(atendimento_barato)
    def excluir_atendimento(self):
        index = self.escolher_atendimento()
        if(index != None):
            self.__atendimentoDAO.remove(index)

    def data_ate_atendimento(self, data_pagamento : tuple, data_atendimento : tuple):
        return (data_pagamento[2], data_pagamento[1], data_pagamento[0]) <= (data_atendimento[2], data_atendimento[1], data_atendimento[0])

    def realizar_pagamento(self):
        index = self.escolher_atendimento()
        if(index == None):
            return None
        atendimento = self.__atendimentoDAO.get(index)
        if(atendimento.pagamento != None):
            print("Esse atendimento ja foi pago.")
            return None
        dados = self.__tela.realizar_pagamento(atendimento)
        if(dados == None):
            return None
        if(not self.data_ate_atendimento(dados["data"], atendimento.data)):
            print("Não é possivel realizar o pagamento, os pagamentos devem ser realizados até a data do atendimento.")
            return None
        if(dados["modalidade"] == 1):
            pagamento = Dinheiro(atendimento.valor, dados["data"])
        elif(dados["modalidade"] == 2):
            pagamento = Pix(atendimento.valor, dados["data"], dados["cpf"])
        else:
            pagamento = CartaoCredito(atendimento.valor, dados["data"], dados["numero_cartao"], dados["bandeira"])
        atendimento.pagamento = pagamento
        self.__atendimentoDAO.update(index, atendimento)
        print("Pagamento realizado com sucesso.")

    def mostrar_pagamento(self):
        index = self.escolher_atendimento()
        if(index == None):
            return None
        atendimento = self.__atendimentoDAO.get(index)
        if(atendimento.pagamento == None):
            print("Esse atendimento ainda não foi pago.")
        else:
            self.__tela.mostrar_pagamento(atendimento.pagamento)
