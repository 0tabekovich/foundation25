class Bankomat:
    def __init__(self, balance):
        self.__balance = balance
        self.__online_balance = balance
        self.__history = dict()
        self.__limit = 4000000

    def get_money(self, card, money):
        if self.__check():
            if card.withdraw_money(money):
                self.__balance -= money
                self.__online_balance += money*1.01
                self.__history[card.get_card_number()] = money
                print(f"{money} so'm mablag' yechildi")

        else:
            print("Bankomatdda mablag' yetarli emas")

    def __check(self):
        return True if self.__limit < self.__balance else False


class Card:
    def __init__(self, balance, card_number, card_type):
        self.__balance = balance
        self.__card_number = card_number
        self.__card_type = card_type

    def withdraw_money(self, money):
        money *= 1.01
        if self.__check_balance(money):
            self.__balance -= money
            return True
        else:
            print("Hisobingizda mablag' yetarli emas")
            return False

    def __check_balance(self, money):
        return True if money <= self.__balance else False

    def get_card_number(self):
        return self.__card_number

card = Card(1000000, "986025698523", "humo")
