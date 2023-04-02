import requests
class User:
    def __init__(self, im="", fam="", pas="", log=""):
        self.__data = requests.get(" https://api.randomdatatools.ru/").json()
        self.login = self.__data["login"] if not log else log
        self.__password = self.__data["password"] if not pas else pas
        self.imya = self.__data["firstname"] if not im else im
        self.familiya = self.__data["lastname"] if not fam else fam
        self.podpiski = []
        self.podpischiki = []

