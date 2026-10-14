
class ViewProcedimento:
    def __init__(self, controlador_procedimento):
        self.controlador_procedimento = controlador_procedimento

    def criar_procedimento(self):
        print("Criando procedimento:")
        dados0 = input("Descrição do procedimento: ")
        dados1 = int(input("Custo do procedimento: "))
        return [dados0,dados1]

    def alterar_procedimento(self):
        print("Alterando procedimento:")
        dados1 = input("Descrição do procedimento: ")
        dados2 = int(input("Novo custo do procedimento: "))
        return [dados1, dados2]
    def mostrar_menu(self, opcoes : str, switch : dict):
        while True:
            print("-------------Procedimento---------------")
            print(opcoes)
            opcao = int(input("Escolha uma opcao: "))
            sw = switch
            try:
                sw[opcao]()
            except ValueError:
                print("Opcao invalida.")
    def listar_procedimentos(self, procedimentos):
        if(len(procedimentos) > 1):
            for i in range(len(procedimentos)):
                print(f"{i}. Descrição:{procedimentos[i].descricao} Custo: {procedimentos[i].custo} Profissional Responsavel(nome):{procedimentos[i].profissional.nome}")
        else:
            print(f"{0}. Descrição:{procedimentos[0].descricao} Custo: {procedimentos[0].custo} Profissional Responsavel(nome):{procedimentos[0].profissional.nome}")
    def escolher_procedimento(self, procedimentos):
        self.listar_procedimentos(procedimentos)
        opcao = int(input("Escolha um procedimento(numero): "))
        if(opcao >= 0 and opcao < len(procedimentos)):
            return opcao
    def mostrar_procedimento(self, procedimento):
        print(f"Descrição:{procedimento.descricao} Custo: {procedimento.custo} Profissional Responsavel(nome):{procedimento.profissional.nome}")
