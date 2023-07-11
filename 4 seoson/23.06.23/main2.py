class Bankomat:
    def __init__(self, balance):
        self.__balance = balance
        self.__online_balance = balance
        self.__history = list()
        self.__limit = 4000000
        self.__current_pincode = 0

    def get_money(self, card, money):
        if self.__check_balance() and self.__check_limit(money):
            if card.withdraw_money(money):
                self.__balance -= money
                self.__online_balance += money * 1.01
                self.__history.append([card.get_card_number(),-money])
                print(f"{money} mablag' yechib oldiz")
        elif not self.__check_limit(money):
            print(f"Bankomatddan maximum {self.__limit} mablag' olish mumkin")
        else:
            print("Bankomatdda mablag' yetarli emas")

    def get_card_info(self, card):
        self.__current_pincode = input("Enter pincode: ")
        if card.check_pincode(self.__current_pincode):
            b = True
            while b:
                i = int(input(f"""
                1. Info
                2. Change pincode
                3. Get money
                4. Add money
                5. History
                6. Exit
                >>>"""))
                if i == 6:
                    exit()

                match i:
                    case 1:
                        card.show_info()
                    case 2:
                        card.change_pincode(self.__current_pincode, int(input("Enter new pincode: "))),
                    case 3:
                        self.get_money(card, int(input("Enter money: ")))
                    case 4:
                        self.add_money(card, int(input("Enter money: ")))
                    case 5:
                        print(self.__history)
        else:
            print("Error pincode")
            self.get_card_info(card)
    def add_money(self, card, money):
        if self.__online_balance>money*0.99:
            self.__online_balance-=money*0.99
            card.add_moneycard(money*0.99)
            self.__history.append([card.get_card_number(),+money])
    def __check_balance(self):
        return True if self.__limit <= self.__balance else False

    def __check_limit(self, money):
        return True if self.__limit >= money else False

    def show_info(self):
        if self.__check_balance():
            print("Bankomat is working )")
        else:
            print("Bankomat isn't working (")


class Card:
    def __init__(self, balance, card_number, card_type, pincode):
        self.__balance = balance
        self.__card_number = card_number
        self.__card_type = card_type
        self.__pincode = pincode

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

    def show_info(self):
        print(f"{self.__card_number} hisob raqamida {self.__balance} mablag' mavjud")

    def change_pincode(self, pincode, new_pincode):
        if self.__pincode == pincode:
            self.__pincode = new_pincode
        else:
            print("Pincode not valid")

    def check_pincode(self, pincode):
        return True if self.__pincode == pincode else False
    def add_moneycard(self,money):
        self.__balance+=money


card = Card(10000000, "986025698523", "humo", "1234")
bankomat = Bankomat(10000000)
bankomat.get_card_info(card)
