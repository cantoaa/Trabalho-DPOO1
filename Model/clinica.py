
class Clinica:
    def __init__(self, nome : str, localizacao : str, descricao : str, horario : list = None):
        if(isinstance(nome, str) and isinstance(localizacao, str) and isinstance(descricao,str) and isinstance(horario,list) and len(horario) == 2 and horario[0] >= 0 and horario[0] < 24 and horario[1] > horario[0] and horario[1] < 24):
            self.__nome = nome
            self.__localizacao = localizacao
            self.__descricao  = descricao
            self.__horario = horario
        else:
            raise ValueError("Os valores enviados como parametros para o construtor de Clinica tem tipos diferentes dos requisitados")

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def localizacao(self) -> str:
        return self.__localizacao

    @property
    def descricao(self) -> str:
        return self.__descricao
    @property
    def horario(self) -> list:
        return self.__horario

    @nome.setter
    def nome(self, nome : str):
        if(isinstance(nome,str)):
            self.__nome = nome

    @localizacao.setter
    def localizacao(self, localizacao : str):
        if(isinstance(localizacao,str)):
            self.__localizacao = localizacao

    @descricao.setter
    def descricao(self, descricao : str):
        if(isinstance(descricao,str)):
            self.__descricao = descricao
    @horario.setter
    def horario(self, horario1 : int, horario2 : int):
        if(isinstance(horario1, int) and isinstance(horario2, int)):
            if(horario1 >= 0 and horario1 < 24 and horario2 > horario1 and horario2 < 24):
                self.__horario[0] = horario1
                self.__horario[1] = horario2
