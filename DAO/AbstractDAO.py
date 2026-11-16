from abc import ABC, abstractmethod
import pickle

class AbstractDAO(ABC):
    def __init__(self, datasource=''):
        self.__cache = {}
        self.__datasource
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickel.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def update(self, key, obj):
        try:
            if self.__cache[key] != None:
                self.__cache[key] = obj
                self.__dump()
        except KeyError:
            return None

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()
