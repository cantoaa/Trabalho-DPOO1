
class Clinica:
    def __init__(self, nome : str, localizacao : str, descricao : str):
        if(isinstance(nome, str) & isinstance(localizacao, str) & isinstance(descricao,str)):
            self.__nome = nome
            self.__localizacao = localizacao
            self.__descricao  = descricao
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

