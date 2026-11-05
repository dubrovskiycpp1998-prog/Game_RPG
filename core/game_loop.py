from abc import ABC, abstractmethod
import random

# Ваши оригинальные импорты персонажей и лута
from characters.enemies import Goblin, Dragon, Troll
from characters.loot import Potion, Magic_Ball

# В самом верху core/game_loop.py добавьте импорт объекта событий
from core.events import game_events

# В начало файла core/game_loop.py не забудьте импортировать базовый класс событий
from random_events.base_event import RandomEvent


# =====================================================================
# БАЗОВЫЙ КЛАСС ДЛЯ СОСТОЯНИЙ ВНУТРИ ПОХОДА (Карта / Бой / Лут)
# =====================================================================
class AdventureState(ABC):
    def __init__(self, engine):
        self.engine = engine  # Ссылка на GameEngine, где хранится герой

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_input(self, user_input: str):
        pass


# =====================================================================
# СОСТОЯНИЕ: КАРТА (Генератор случайных событий)
# =====================================================================
class MapState(AdventureState):
    def render(self):
        # Если герой погиб по какой-то причине на карте — завершаем поход
        if self.engine.hero.health <= 0:
            self.engine.stop()
            return

        print("\n=== КАРТА МИРА ===")
        print("Вы исследуете локацию. Что делаете?")
        print("1. Идти вперед (Случайное событие)")
        print("2. Завершить поход и вернуться в Таверну")

    def handle_input(self, user_input: str):
        if user_input == "1":
            # Ленивый импорт событий из папки random_events, чтобы не было круговых импортов
            from random_events.casino import CasinoEncounterEvent
            from random_events.shrine import HealingShrineEvent
            from random_events.robbery import RobberyMeetEvent
            
            # Собираем ВСЕ события игры в один красивый массив объектов!
            possible_events = [
                BattleState(self.engine),      # Передаем движок, execute сам создаст врага
                LootState(self.engine),        # execute сам создаст предмет лута
                CasinoEncounterEvent(),        # Наше событие казино
                HealingShrineEvent(),          # Наш текстовый алтарь исцеления
                RobberyMeetEvent(self.engine)             # Встреча с разбойником
            ]
            
            # Выбираем абсолютно любое событие по одному правилу
            chosen_event = random.choice(possible_events)
            
            # Запускаем полиморфный метод execute!
            chosen_event.execute(self.engine)
                
        elif user_input == "2":
            print("\nВы решили вернуться в таверну...")
            self.engine.stop()  # Выходим из движка приключений назад в Gameplay
        else:
            print("⚠️ Неверный ввод. Выберите 1 или 2.")


# =====================================================================
# СОСТОЯНИЕ: РЕЖИМ БОЯ (Ваша боевая логика, перенесенная в стейт)
# =====================================================================
class BattleState(AdventureState, RandomEvent):
    def __init__(self, engine, enemy = None):
        super().__init__(engine)
        self.enemy = enemy
        self.round_number = 1
        print("-" * 40)

    def execute(self, engine):
        """Этот метод вызовется автоматически при выборе из random.choice"""
        # Генерируем случайного врага с помощью вашего фабричного метода
        self.enemy = engine.factory_choose_enemy()
        # Если враг не передан (при генерации в массиве), мы выберем его позже в execute
        
        print(f"\n⚔️ Начинается бой! Вашему герою противостоит {self.enemy.name}!")
        print("-" * 40)
        
        # Переключаем экран игры на этот конкретный бой
        engine.set_state(self)


    def render(self):
        print(f"\n--- Раунд {self.round_number} ---")
        print(f"[{self.engine.hero.name}] Здоровье: {self.engine.hero.health}")
        print(f"[{self.enemy.name}] Здоровье: {self.enemy.health}")
        print(f"Ваш баланс: {self.engine.hero.money_balance} 🪙")
        print("-" * 20)
        print("Выберите действие:")
        print("1. Атаковать")
        print("2. Использовать уникальную способность")
        print("3. Откупиться от врага (стоимость: 500 коинов)")

    def handle_input(self, user_input: str):
        hero = self.engine.hero
        
        # 1. ХОД ГЕРОЯ
        if user_input == "1":
            hero.attack(self.enemy)
        elif user_input == "2":
            hero.unique_ability(self.enemy)
        elif user_input == "3":
            # Вызываем ваш метод откупа (убедитесь, что внутри него списывается 500 коинов)
            hero.get_paid()  
            print(f"🤝 Вы откупились от {self.enemy.name}. Возвращение на карту.")
            self.engine.set_state(MapState(self.engine))
            return
        else:
            print("⚠️ Неверный ввод! Пожалуйста, выберите 1, 2 или 3.")
            return

        # Проверка: умер ли враг после удара героя?
        # ... внутри метода handle_input класса BattleState, когда враг повержен:
        if self.enemy.health <= 0:
            print(f"\n🎉 {self.enemy.name} повержен!")
            
            # Собираем данные, которые нужны нашим наблюдателям для работы
            event_data = {
                "hero": self.engine.hero,
                "enemy": self.enemy,
                #"gameplay": self.engine.gameplay_context # передаем контекст для счетчика побед
            }
            
            # Срабатывает магия Наблюдателя — одной строчкой уведомляем все системы!
            game_events.notify("enemy_death", data=event_data)
            
            input("\nНажмите Enter, чтобы продолжить путь...")
            self.engine.set_state(MapState(self.engine))
            return

        # 2. ХОД ВРАГА
        print()
        self.enemy.attack(hero)

        # Проверка: выжил ли герой после удара врага?
        if hero.health <= 0:
            # Герой погиб. Останавливаем движок приключений. 
            # Класс Gameplay это увидит и переключит экран на GameOver
            self.engine.stop()
            return

        self.round_number += 1


# =====================================================================
# СОСТОЯНИЕ: СИСТЕМА ЛУТА (Покупка найденного предмета)
# =====================================================================
class LootState(AdventureState, RandomEvent):
    def __init__(self, engine, loot = None):
        super().__init__(engine)
        self.loot = loot

    def execute(self, engine):
        """Этот метод вызовется автоматически при выборе из random.choice"""
        
        # Генерируем случайный лут с помощью вашего фабричного метода
        self.loot = engine.factory_choose_loot()
        
        
        # Переключаем экран игры на этот магазин лута
        engine.set_state(self)    

    def render(self):
        print(f"\n✨ Вы нашли предмет: {self.loot.name}!")
        print(f"Его цена: {self.loot.cost} коинов")
        print(f"Ваш баланс: {self.engine.hero.money_balance} 🪙")
        print("-" * 20)
        print("1. Купить предмет")
        print("2. Продолжить без покупки")

    def handle_input(self, user_input: str):
        hero = self.engine.hero
        
        if user_input == "1":
            # У вас в коде было условие > 2000, но правильнее проверять по цене самого лута:
            if hero.money_balance >= self.loot.cost:
                print("\n Вы успешно купили предмет!")
                hero.money_balance -= self.loot.cost
                print("Вы хотите сразу применить предмет или положить в инвентарь?")
                print("1. Применить")
                print("2. Положить в инвентарь")
                user_choice = input("Выберите действие: ").strip()
                if user_choice == "1":
                    self.loot.help_hero(hero) # Передаем объект героя для применения эффекта
                elif user_choice == "2":
                    hero.inventory.add_item(self.loot)
                print(f"Ваш баланс после покупки: {hero.money_balance}")
            else:
                print("\n❌ У вас недостаточно средств для покупки!")
            
            input("\nНажмите Enter, чтобы продолжить...")
            self.engine.set_state(MapState(self.engine))
            
        elif user_input == "2":
            print("Вы прошли мимо предмета.")
            input("\nНажмите Enter, чтобы продолжить...")
            self.engine.set_state(MapState(self.engine))
        else:
            print("⚠️ Неверный ввод! Выберите 1 или 2.")


# =====================================================================
# ОБНОВЛЕННЫЙ ДВИЖОК GAME_LOOP (Менеджер состояний приключения)
# =====================================================================
class GameEngine:
    def __init__(self, hero):
        self.hero = hero
        self._is_running = True
        # Каждый поход начинается с исследования карты мира
        self._state = MapState(self)

    def set_state(self, new_state: AdventureState):
        self._state = new_state

    def stop(self):
        """Выход из игрового цикла похода."""
        self._is_running = False

    # ВАШИ ФАБРИЧНЫЕ МЕТОДЫ ГЕНЕРАЦИИ
    def factory_choose_enemy(self):
        who_is_enemy = random.choice([1, 2, 3])
        if who_is_enemy == 1: return Goblin("Гоблин")
        elif who_is_enemy == 2: return Dragon("Дракон")
        return Troll("Тролль")

    def factory_choose_loot(self):
        is_loot = random.choice([1, 2])
        if is_loot == 1: return Potion("Зелье")
        return Magic_Ball("Магический шар")

    # Добавьте этот метод внутрь вашего класса GameEngine:
    def factory_choose_casino(self):
        # Просто пишем красивый текст в консоль перед входом
        print("\n🔍 Среди деревьев вы заметили вывеску тайного заведения...")
        return None # Нам не нужно возвращать объект, так как CasinoState всё сделает сам
    def factory_choose_robbery(self):
        # Просто пишем красивый текст в консоль перед входом
        print("\n🔍 Глубоко в лесу, cреди деревьев кто то прятался...")
        return None # Нам не нужно возвращать объект, так как CasinoState всё сделает сам


    def run(self):
        # Запускаем внутренний цикл приключений (пока мы не вызвали self.stop())
        while self._is_running:
            self._state.render()
            if not self._is_running:
                break
            
            user_input = input("\nВведите номер действия: ").strip()
            self._state.handle_input(user_input)
