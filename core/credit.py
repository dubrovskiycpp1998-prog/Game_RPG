from characters.base import Hero


class Credit_Manager: 
    def __init__(self, is_debt=False, initial_debt=150, current_debt=150):
        self.hero = None 
        self.is_debt = is_debt
        self.initial_debt = initial_debt
        self.current_debt = current_debt
       

    def activating_debt(self, hero, amount=150):
        self.hero = hero
        self.is_debt = True
        self.initial_debt = amount
        self.current_debt = amount
        # Начисляем герою кредитные деньги, чтобы он мог откупиться
        self.hero.money_balance += amount 
        print(f"Вы взяли кредит на сумму {amount} золотых!")

    def calculation_debt(self, debt_step):
       if self.is_debt:
            # ИСПРАВЛЕНО: добавили self. перед переменными, иначе Python их не найдет
            # ИСПРАВЛЕНО: убрали +=, так как мы пересчитываем долг с нуля на основе шагов
            self.current_debt = self.initial_debt + debt_step * 0.05 * self.initial_debt

    def get_message(self):
        if self.is_debt: 
            return f"💰 [Менеджер Кредита]: У вас есть долг в размере {self.current_debt:.2f} золотых."
        else:
            return "💰 [Менеджер Кредита]: У вас нет активного долга."

    def pay_debt(self):
        if self.hero.money_balance < self.current_debt:

            print("У вас недостаточно денег, чтобы погасить долг")

        elif self.hero.money_balance > self.current_debt:
            self.hero.money_balance -= self.current_debt
            self.is_debt = False
            self.initial_debt = 0
            self.current_debt = 0
            print ("Ваш долг погашен!")

        else:
            self.hero.money_balance -= self.current_debt
            print("У вас на счету ноль!")





    