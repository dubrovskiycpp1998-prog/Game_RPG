import random
from core.game_loop import AdventureState
from random_events.base_event import RandomEvent
from core.game_loop import MapState

class RobberyMeetEvent (AdventureState, RandomEvent):
    def __init__(self, engine, robbery = None, robbery_get_health = 0):
            super().__init__(engine)
            self.robbery = robbery
            self.robbery_get_health = robbery_get_health
            robbery_get_health = random.randint(10,40)
            
            print("-" * 40)
    
    def execute(self, engine):
        """Этот метод вызовется автоматически при выборе из random.choice"""
        # Генерируем случайного врага с помощью вашего фабричного метода
        self.robbery = engine.factory_choose_robbery()
        # Если враг не передан (при генерации в массиве), мы выберем его позже в execute
        
        print(f"\n⚔️ Блуждая по лесу вы напоролись на разбойника, он предлагает вам выбор или отдать 500 монет или сражаться !")

        print("-" * 40)
        
        # Переключаем экран игры на этот конкретный бой
        engine.set_state(self)

    def render(self):
        print("\nВыберите действие:")
        print("Нажмите 1, чтобы откупитсья")
        print("Нажмите 2, чтобы сражаться")

    def handle_input(self, user_input: str):
        hero = self.engine.hero
        robbery_get_health = random.randint(10,40)

        if user_input == "1" and hero.money_balance >= 500:
            hero.money_balance -= 500
            print("\nВЫ отдали разбойнику 500 монет")
            print(f"Ваш баланс: {hero.money_balance}")

        if user_input == "2":
            hero.health -= robbery_get_health
            print("\nВы сражаетесь с разбойника, ему удается ранить вас")
            print(f"Ваше здоровье = {hero.health}")

        if user_input == "1" and hero.money_balance <= 500:
            print("\nВЫ не можете отдать разбойнику 500 монет, ваш баланс меньше!")
            print("Разбойник наносит вам двойной урон")
            hero.health -= 2*robbery_get_health
            print(f"Ваше здоровье = {hero.health}")
            

        # Проверка: выжил ли герой после удара разбойника?
        if hero.health <= 0:
            # Герой погиб. Останавливаем движок приключений. 
            # Класс Gameplay это увидит и переключит экран на GameOver
            self.engine.stop()
            return  

        input("\nНажмите Enter, чтобы продолжить путь...")
        self.engine.set_state(MapState(self.engine))
        return




    
    