class Anton:
#     location = "Новосибирск"  # public static
#     # __location = "Секрет" # private static
#     def __init__(self, rost=1, ves=2): # __magic__
#         self.height = rost # public dynamic
#         self.__weight = ves  # private dynamic
#         self.otkuda = Anton.location
#     def __zdarova(self):
#         pass
#     def sdarova(self):
#         pass
#
# chelovek = Anton(10)
# chelovek2 = Anton(15)
# print(chelovek.height)
# print(chelovek.location)
class Human:
    default_name = 'human'
    default_age = 18
    def __init__(self, imya: str = default_name, vozrast: int = default_age):
        self.name = imya
        self.age = vozrast
        self.__money = 10200
        self.__house = None

    def __make_deal(self,dom):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True
        else:
            return False
    def buy_house(self,dom):
        if self.__make_deal(dom):
            dom.owner = self.name
            self.__house = dom
            return "Купили, по кайфу."
        else:
            return f"Денег не хватило, нужно ещё {dom.final_price() - self.__money}"

class House:
    def __init__(self):
        self.price = 50000
        self.skidka = randint(5, 25)
    def final_price(self):
        return self.__price - self.__price * (self.__skidka / 100)





