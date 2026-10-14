
class ViewGeral:
    def __init__(self, control_geral):
        self.control_geral = control_geral

    def mostrar_menu(self):
        while True:
            print("---------------Menu Geral------------------")
            print("1 - Atendimentos\n2- Pacientes\n3- Profissionais\n4- Procedimentos\n5- Clinicas \n0-Sair")
            switch = int(input("Escolha uma opcao: "))
            iniciar = {0 : self.control_geral.sair, 1 : self.control_geral.control_atendimento.iniciar, 2:self.control_geral.control_paciente.iniciar, 3:self.control_geral.control_profissional.iniciar, 4:self.control_geral.control_procedimento.iniciar, 5:self.control_geral.control_clinica.iniciar}
            try:
                iniciar[switch]()
            except ValueError:
                print("Opcao invalida, tente novamente") 
                
