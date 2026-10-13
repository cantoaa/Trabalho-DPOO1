from Control.abstractcontrol import Control
from View.view_clinica import ViewClinica
from Model.clinica import Clinica


class ControlClinica(Control):
    def __init__(self, control_geral):
        self.__clinicas = []
        self.__tela = ViewClinica(self)
        self.control_geral = control_geral

    def cadastrar_clinica(self):
        dados = self.__tela.criar_clinica()
        self.__clinicas.append(Clinica(dados["nome"],dados["localizacao"], dados["descricao"]))

    def listar_clinicas(self):
        if(len(self.__clinicas) > 0):
            self.__tela.listar_clinicas(self.__clinicas)
    def excluir_clinica(self):
        if(len(self.__clinicas) > 0):
            index = self.escolher_clinica()
            try:
                del self.__clinicas[index]
            except:
                self.iniciar()

    def escolher_clinica(self):
        if(len(self.__clinicas) > 0):
            clinica = self.__tela.escolher_clinica(self.__clinicas)
            return clinica

    def buscar_clinica(self):
        if(len(self.__clinicas) > 0):
            dados = self.__tela.buscar_clinica()
            for clinica in self.__clinicas:
                if clinica.nome == dados["nome"] and clinica.localizacao == dados["localizacao"]:
                    self.__tela.mostrar_clinica(clinica)
                    return clinica
        return None

    def iniciar(self):
        opcoes = "1.Cadastrar clinica\n2.Excluir clinica\n3.Listar clinicas\n4.Buscar clinica\n0.Sair"
        switch = {1 : self.cadastrar_clinica, 2 : self.excluir_clinica,3 : self.listar_clinicas, 4 : self.buscar_clinica,0 : self.sair}
        self.__tela.mostrar_menu(opcoes, switch)
    def sair(self):
        self.control_geral.iniciar()
