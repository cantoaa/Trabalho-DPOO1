
class ViewClinica:
    def __init__(self, control_clinica):
        self.control_clinica = control_clinica

    def listar_clinicas(self, clinicas):
        if(len(clinicas) > 1):
            for i in range(len(clinicas)):
                print(f"{i}. Nome: {clinicas[i].nome} Localização: {clinicas[i].localizacao} Descrição: {clinicas[i].descricao}")
        else:
            print(f"{0}. Nome: {clinicas[0].nome} Localização: {clinicas[0].localizacao} Descrição: {clinicas[0].descricao}")


    def mostrar_menu(self, opcoes : str, switch : dict):
        while True:
            print("------------------Clinica----------------")
            print(opcoes)
            opcao = int(input("Escolha uma opção: "))
            try:
                switch[opcao]()
            except ValueError:
                print("Opção invalida")

    def buscar_clinica(self):
        dados = {"nome" : "", "localizacao" : ""}
        dados["nome"] = input("Insira o nome da clinica: ")
        dados["localizacao"] = input("Insira a localizacao da clinica: ")
        return dados
    def criar_clinica(self):
        dados = {"nome" : "", "localizacao" : "", "descricao" : ""}
        dados["nome"] = input("Nome da clinica: ")
        dados["localizacao"] = input("Localização da clinica: ")
        dados["descricao"] = input("Descrição da clinica: ")
        return dados
    def escolher_clinica(self, clinicas):
        self.listar_clinicas(clinicas)
        opcao = int(input("Escolha uma clinica pelo seu número: "))
        if(opcao >= 0 and opcao < len(clinicas)):
            return opcao
        else:
            print("Opção invalida")
        return None
    def mostrar_clinica(self, clinica):
        print(f"Clinica encontrada: Nome: {clinica.nome} Localização: {clinica.localizacao} Descrição: {clinica.descricao}")
