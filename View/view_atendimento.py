

class ViewAtendimento:
    def __init__(self, control_atendimento):
        self.control_atendimento = control_atendimento

    def listar_atendimentos(self, atendimentos):
        if(len(atendimentos) > 1):
            for i in range(len(atendimentos)):
                print(f"{i}. Clinica: {atendimentos[i].clinica.nome}, Paciente: {atendimentos[i].paciente.nome}, Profissional: {atendimentos[i].profissional.nome}, Data: {atendimentos[i].data}, Horário: {atendimentos[i].horario}, Tipo: {atendimentos[i].tipo}, Valor: {atendimentos[i].valor}")
        else:
            print(f"{i}. Clinica: {atendimentos[i].clinica.nome}, Paciente: {atendimentos[0].paciente.nome}, Profissional: {atendimentos[0].profissional.nome}, Data: {atendimentos[0].data}, Horário: {atendimentos[0].horario}, Tipo: {atendimentos[0].tipo}, Valor: {atendimentos[0].valor}")
    def mostrar_menu(self, opcoes : str, switch : dict):
        while True:
            print(opcoes)
            opcao = int(input("Escolha uma opcao: "))
            sw = switch
            try:
                sw[opcao]()
            except ValueError:
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
        dados = {"horario1" : 0, "horario2" : 0, "data" : (0,0,0), "clinica" : None, "paciente" : None, "profissional" : None, "tipo" : "", "valor" : 0}
        control_geral = self.control_atendimento.control_geral
        dados["horario1"] = int(input("Digite o horario inicial do atendimento: "))
        dados["horario2"] = int(input("Digite o horario final do atendimento: "))
        dados["data"] = (int(input("Digite o dia do atendimento: ")), int(input("Digite o mes do atendimento: ")), int(input("Digite o ano do atendimento: ")))
        dados["clinica"] = control_geral.control_clinica.buscar_clinica()
        dados["paciente"] = control_geral.control_paciente.buscar_paciente()
        dados["profissional"] = control_geral.control_profissional.buscar_profissional()
        dados["tipo"] = input("Digite o tipo do atendimento: ")
        dados["valor"] = int(input("Digite o valor do atendimento: "))
        return dados
