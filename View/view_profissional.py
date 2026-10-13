
class ViewProfissional:
    def __init__(self, control_profissional):
        self.control_profissional = control_profissional

    def listar_profissionais(self, profissionais): 
        if(len(profissionais) > 1):
            for i in range(len(profissionais)):
                print(f"{i}. Nome: {profissionais[i].nome}, Especialidade: {profissionais[i].especialidade}, CPF: {profissionais[i].cpf}, Celular: {profissionais[i].celular}, Registro Profissional: {profissionais[i].rp}")
        else:
            print(f"{0}. Nome: {profissionais[0].nome}, Especialidade: {profissionais[0].especialidade}, CPF: {profissionais[0].cpf}, Celular: {profissionais[0].celular}, Registro Profissional: {profissionais[0].rp}")


    def mostrar_menu(self, opcoes : str, switch : dict):
        while True:
            print(opcoes)
            opcao = int(input("Escolha uma opcao: "))
            sw = switch
            try:
                sw[opcao]()
            except ValueError:
                print("Opcao invalida.")

    def criar_profissional(self):
        print("------------Cadastrar profissional-------------")
        nome = input("Digite o nome do profissional: ")
        celular = int(input("Digite o celular do profissional: "))
        cpf = int(input("Digite o CPF do profissional: "))
        especialidade = input("Digite a especialidade do profissional: ")
        rp = input("Digite o registro profissional do profissional: ")
        return [nome, celular, cpf, especialidade, rp]

    def escolher_profissional(self, profissionais):
        self.listar_profissionais(profissionais)
        opcao = int(input("Escolha um profissional(Numero): "))
        if opcao >= 0 and opcao < len(profissionais):
            return opcao

    def buscar_profissional(self):
        cpf = int(input("Digite o CPF do profissional: "))
        return cpf

    def mostrar_profissional(self, profissional):
        print(f"Profissional encontrado: Nome: {profissional.nome}, Especialidade: {profissional.especialidade}, CPF: {profissional.cpf}, Celular: {profissional.celular}, Registro Profissional: {profissional.rp}")
