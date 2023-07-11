class Bankomat:
    def __init__(self, balance):
        self.__balance = balance
        self.__online_balance = balance
        self.__history = dict()
        self.__limit = 4000000

    def get_money(self, card, money):
        if self.__check(money):
            if card.withdraw_money(money):
                self.__balance -= money
                self.__online_balance += money * 1.01
                self.__history[card.get_card_number()] = money
                print(f"{money} mablag' yechib oldiz")
        elif self.__limit < money:
            print(f"Bankomatddan maximum {self.__limit} mablag' olish mumkin")
        else:
            print("Bankomatdda mablag' yetarli emas")

    def __check(self, money):
        return True if self.__limit < self.__balance and self.__limit >= money else False

    def show_info(self):
        if self.__check(0):
            print("Bankomat is working )")
        else:
            print("Bankomat isn't working (")


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
bankomat = Bankomat(1000000)
bankomat.get_money(card, 2000000)
match i:
    case