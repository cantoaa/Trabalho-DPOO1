from Control.abstractcontrol import Control
from View.view_clinica import ViewClinica
from Model.clinica import Clinica
from DAO.clinicaDAO import ClinicaDAO


class ControlClinica(Control):
    def __init__(self, control_geral):
        self.__clinicaDAO = ClinicaDAO()
        self.__tela = ViewClinica(self)
        self.control_geral = control_geral

    @property
    def clinicas(self):
        return list(self.__clinicaDAO.get_all())

    def cadastrar_clinica(self):
        dados = self.__tela.criar_clinica()
        if(self.__clinicaDAO.get(dados["nome"]) != None):
            print("Ja existe uma clinica com esse nome")
            return None
        self.__clinicaDAO.add(Clinica(dados["nome"],dados["localizacao"], dados["descricao"], [dados["horario1"],dados["horario2"]]))

    def listar_clinicas(self):
        if(len(self.clinicas) > 0):
            self.__tela.listar_clinicas(self.clinicas)
    def excluir_clinica(self):
        if(len(self.clinicas) > 0):
            index = self.escolher_clinica()
            if(index != None):
                self.__clinicaDAO.remove(self.clinicas[index].nome)

    def escolher_clinica(self):
        if(len(self.clinicas) > 0):
            clinica = self.__tela.escolher_clinica(self.clinicas)
            return clinica
    def alterar_clinica(self):
        index = self.escolher_clinica()
        if(index == None):
            return None
        clinica = self.clinicas[index]
        dados = self.__tela.criar_clinica()
        self.__clinicaDAO.remove(clinica.nome)
        self.__clinicaDAO.add(Clinica(dados["nome"],dados["localizacao"],dados["descricao"], [dados["horario1"], dados["horario2"]]))
    def buscar_clinica(self):
        if(len(self.clinicas) > 0):
            dados = self.__tela.buscar_clinica()
            clinica = self.__clinicaDAO.get(dados["nome"])
            if(clinica != None and clinica.localizacao == dados["localizacao"]):
                self.__tela.mostrar_clinica(clinica)
                return clinica
        return None

    def iniciar(self):
        opcoes = "1.Cadastrar clinica\n2.Excluir clinica\n3.Listar clinicas\n4.Buscar clinica\n5.Alterar clinica\n0.Sair(Voltar para o menu principal)"
        switch = {1 : self.cadastrar_clinica, 2 : self.excluir_clinica,3 : self.listar_clinicas, 4 : self.buscar_clinica, 5 : self.alterar_clinica,0 : self.sair}
        self.__tela.mostrar_menu(opcoes, switch)
    def sair(self):
        self.control_geral.iniciar()
