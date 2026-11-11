from characters.base import Hero
from characters.paidabilitystrategy import PaidShieldSmash
from characters.paidabilitystrategy import PaidBright
from characters.paidabilitystrategy import PaidAlchemicalExplosion


class Knight(Hero):

    def __init__(self, name):
        # Передаем родительскому классу Hero только то, что он ожидает
        super().__init__(name, health=120, attack_power=15, who_is_character=1, money_balance=500, respect_hero=50, stamina=20)
       
        # Создаем уникальный атрибут прочности щита для конкретного Рыцаря
        self.shield_capacity = 50
            
        # Привязываем стратегию платной способности (стоимость, например, 300 коинов)
        self.ability_strategy = PaidShieldSmash(cost=300)

    def unique_ability(self, other):
        if self.ability_strategy:
                # Передаем себя (user=self) и врага (target=other)
                success = self.ability_strategy.use(user=self, target=other)
                if not success:
                    print("⚠️ Способность не была активирована.")
        else:
                print(f"X {self.name} еще не выучил платные способности.")

   
class Stranger(Hero):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=10, who_is_character=2, money_balance=100, respect_hero=30, stamina=60)
        self.is_hidden = True  # Изначально Странник скрыт

        self.is_hidden_capacity = 30
        self.ability_strategy = PaidBright(cost=500)

    # ТЕПЕРЬ МЕТОД ВНУТРИ КЛАССА (добавлен отступ)
    def unique_ability(self, other):
        if self.ability_strategy:
            # Передаем себя (user=self) и врага (target=other)
            success = self.ability_strategy.use(user=self, target=other)
            if not success:
                print("⚠️ Способность не была активирована.")
        else:
            print(f"X {self.name} еще не выучил платные способности.")

    

class Witcher(Hero):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30, who_is_character=3, money_balance=300, respect_hero=70, stamina=40)
        # Инициализируем запас магической силы внутри персонажа

        self.magic_power_capacity = 50 

        self.ability_strategy = PaidAlchemicalExplosion(cost=1000)

    # ТЕПЕРЬ МЕТОД ВНУТРИ КЛАССА (добавлен отступ)
    def unique_ability(self, other):
        if self.ability_strategy:
            # Передаем себя (user=self) и врага (target=other)
            success = self.ability_strategy.use(user=self, target=other)
            if not success:
                print("⚠️ Способность не была активирована.")
        else:
            print(f"X {self.name} еще не выучил платные способности.")
