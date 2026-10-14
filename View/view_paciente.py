
class ViewPaciente:
    def __init__(self, control_paciente):
        self.control_paciente = control_paciente

    def mostrar_menu(self):
        while True:
            print("------------Menu Paciente-------------")
            print("1. Cadastrar Paciente")
            print("2. Listar Pacientes")
            print("3. Buscar Paciente")
            print("4. Alterar Paciente")
            print("0. Voltar ao Menu Principal")
            opcao = int(input("Escolha uma opção: "))
            switch = {1 : self.control_paciente.cadastrar_paciente, 2 : self.control_paciente.listar_pacientes, 3 : self.control_paciente.buscar_paciente, 4 : self.control_paciente.alterar_paciente,0 : self.control_paciente.sair}             
            try:
                switch[opcao]()
            except ValueError:
                print("Opção inválida. Tente novamente.")

    def cadastrar_paciente(self):
        print("------------Cadastrar Paciente-------------")
        nome = input("Digite o nome do paciente: ")
        celular = int(input("Digite o celular do paciente: "))
        cpf = int(input("Digite o CPF do paciente: "))
        idade = int(input("Digite a idade do paciente: "))
        return [nome, celular, cpf, idade]

    def listar_pacientes(self, pacientes):
        if(len(pacientes) > 1):
            for i in range(len(pacientes)):
                print(f"{i}.Nome: {pacientes[i].nome}, Celular: {pacientes[i].celular}, CPF: {pacientes[i].cpf}, Idade: {pacientes[0].idade}")
        else: 
            print(f"{0}.Nome: {pacientes[0].nome}, Celular: {pacientes[0].celular}, CPF: {pacientes[0].cpf}, Idade: {pacientes[0].idade}")
    def escolher_paciente(self, pacientes):
        self.listar_pacientes(pacientes)
        opcao = int(input("Escolha o paciente pelo número correspondente: ")) 
        if opcao >= 0 and opcao < len(pacientes):
            return opcao
        else:
            print("Paciente não encontrado.")
        return None
    def buscar_paciente(self):
        cpf = int(input("Digite o CPF do paciente: "))
        return cpf
    def mostrar_paciente(self, paciente):
        print(f"Paciente encontrado: Nome: {paciente.nome}, Celular: {paciente.celular}, CPF: {paciente.cpf}, Idade: {paciente.idade}")
