from core.credit import Credit_Manager
class Calculation_Step:
     
    def __init__(self, global_step, debt_step):
        self.global_step = global_step
        self.debt_step = debt_step
        self.credit_manager = Credit_Manager(is_debt=False, initial_debt=150, current_debt=150)

    def update_step(self, engine):
        self.global_step == 0
        self.global_step += 1

       # Если у игрока в движке активирован долг
        if engine.credit.is_debt:
            self.debt_step += 1
            # Пересчитываем долг в менеджере кредитов, передавая текущий шаг долга
            engine.credit.calculation_debt(self.debt_step)
        else:
            self.debt_step = 0 # Сбрасываем шаги долга, если кредита нет

    def print_steps(self):
        print(f"Текущий глобальный шаг: {self.global_step}")
        print(f"Текущий шаг долга: {self.debt_step}")

    def print_credit_info(self, engine):
        if engine.credit.is_debt:
            print(f"💰 [Менеджер Кредита]: У вас есть долг в размере {engine.credit.current_debt:.2f} золотых.")
        else:
            print("💰 [Менеджер Кредита]: У вас нет активного долга.")

    def print_credit_info(self, engine, is_debt):
        if is_debt:
                print(f"💰 [Менеджер Кредита]: У вас есть долг в размере {engine.credit.current_debt:.2f} золотых.")
        else:
                print("💰 [Менеджер Кредита]: У вас нет активного долга.")


    

    