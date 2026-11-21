from Model.pagamento import Dinheiro, Pix, CartaoCredito

class ViewAtendimento:
    def __init__(self, control_atendimento):
        self.control_atendimento = control_atendimento

    def listar_atendimentos(self, atendimentos):
        if(len(atendimentos) > 1):
            for i in range(len(atendimentos)):
                print(f"{i}. Clinica: {atendimentos[i].clinica.nome}, Paciente: {atendimentos[i].paciente.nome}, Profissional: {atendimentos[i].profissional.nome}, Data: {atendimentos[i].data}, Horário: {atendimentos[i].horario}, Tipo: {atendimentos[i].tipo}, Valor: {atendimentos[i].valor}")
        else:
            print(f"{0}. Clinica: {atendimentos[0].clinica.nome}, Paciente: {atendimentos[0].paciente.nome}, Profissional: {atendimentos[0].profissional.nome}, Data: {atendimentos[0].data}, Horário: {atendimentos[0].horario}, Tipo: {atendimentos[0].tipo}, Valor: {atendimentos[0].valor}")
    def mostrar_menu(self, opcoes : str, switch : dict):
        while True:
            print("---------------Atendimentos-----------------")
            print(opcoes)
            sw = switch
            try:
                opcao = int(input("Escolha uma opcao: "))
                sw[opcao]()
            except (ValueError, KeyError):
                print("Opcao invalida.")
    def escolher_atendimento(self, atendimentos):
        self.listar_atendimentos(atendimentos)
        opcao = int(input("Escolha um atendimento(Numero): "))
        if(opcao >= 0 and opcao < len(atendimentos)):
            return opcao
    def adicionar_procedimento(self):
        print("------------Adicionar procedimento-------------")
        self.control_atendimento.adicionar_procedimento()
    def cadastrar_atendimento(self):
        print("------------Cadastrar atendimento-------------")
        dados = {"index" : 0, "horario1" : 0, "horario2" : 0, "data" : (0,0,0), "clinica" : None, "paciente" : None, "profissional" : None, "tipo" : "", "valor" : 0}
        control_geral = self.control_atendimento.control_geral
        dados["index"] = int(input("Digite o codigo do atendimento: "))
        dados["horario1"] = int(input("Digite o horario inicial do atendimento: "))
        dados["horario2"] = int(input("Digite o horario final do atendimento: "))
        dados["clinica"] = control_geral.control_clinica.buscar_clinica()
        if(dados["clinica"] == None):
            print("Clinica não encontrada.")
            return None
        if(dados["horario1"] < dados["clinica"].horario[0] or dados["horario1"] > dados["clinica"].horario[1] or dados["horario2"] > dados["clinica"].horario[1] or dados["horario2"] < dados["clinica"].horario[0]):
            print("Não é possivel realizar o atendimento, pois não está no horario de atendimento da clinica.")
            return None
        dados["data"] = (int(input("Digite o dia do atendimento: ")), int(input("Digite o mes do atendimento: ")), int(input("Digite o ano do atendimento: ")))
        dados["paciente"] = control_geral.control_paciente.buscar_paciente()
        if(dados["paciente"] == None):
            print("Paciente não encontrado.")
            return None
        if(dados["paciente"].idade < 18):
            print("Não é possivel um paciente menor de 18 anos fazer um atendimento.")
            return None
        dados["profissional"] = control_geral.control_profissional.buscar_profissional()
        if(dados["profissional"] == None):
            print("Profissional não encontrado.")
            return None
        dados["tipo"] = input("Digite o tipo do atendimento: ")
        dados["valor"] = int(input("Digite o valor do atendimento: "))
        return dados
    def mostrar_procedimentos(self, atendimento):
        procedimentos = atendimento.procedimentos
        for procedimento in procedimentos:
            print(f"Descrição: {procedimento.descricao} Custo: {procedimento.custo} Profissional(Nome): {procedimento.profissional.nome}")
    def mostrar_atendimento(self, atendimento):
        print(f"Clinica: {atendimento.clinica.nome}, Paciente: {atendimento.paciente.nome}, Profissional: {atendimento.profissional.nome}, Data: {atendimento.data}, Horário: {atendimento.horario}, Tipo: {atendimento.tipo}, Valor: {atendimento.valor}")
    def realizar_pagamento(self, atendimento):
        print("------------Realizar pagamento-------------")
        print(f"Valor a pagar: {atendimento.valor} Data do atendimento: {atendimento.data}")
        dados = {"modalidade" : 0, "data" : (0,0,0), "cpf" : 0, "numero_cartao" : 0, "bandeira" : ""}
        dados["modalidade"] = int(input("Modalidade do pagamento (1.Dinheiro 2.PIX 3.Cartão de crédito): "))
        if(dados["modalidade"] not in [1, 2, 3]):
            print("Modalidade de pagamento invalida.")
            return None
        dados["data"] = (int(input("Digite o dia do pagamento: ")), int(input("Digite o mes do pagamento: ")), int(input("Digite o ano do pagamento: ")))
        if(dados["modalidade"] == 2):
            dados["cpf"] = int(input("Digite o CPF do pagador: "))
        elif(dados["modalidade"] == 3):
            dados["numero_cartao"] = int(input("Digite o numero do cartão: "))
            dados["bandeira"] = input("Digite a bandeira do cartão: ")
        return dados
    def mostrar_pagamento(self, pagamento):
        if(isinstance(pagamento, Dinheiro)):
            print(f"Pagamento em Dinheiro, Valor: {pagamento.valor}, Data: {pagamento.data}")
        elif(isinstance(pagamento, Pix)):
            print(f"Pagamento via PIX, Valor: {pagamento.valor}, Data: {pagamento.data}, CPF do pagador: {pagamento.cpf}")
        elif(isinstance(pagamento, CartaoCredito)):
            print(f"Pagamento no Cartão de crédito, Valor: {pagamento.valor}, Data: {pagamento.data}, Numero do cartão: {pagamento.numero_cartao}, Bandeira: {pagamento.bandeira}")
