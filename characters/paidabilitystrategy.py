from abc import ABC, abstractmethod
import random
# 1. Обязательно импортируйте game_events в этот файл в самый верх:
from core.events import game_events

class PaidAbilityStrategy(ABC):
    def __init__(self, cost: int):
        self.cost = cost  # Стоимость в золоте

    @abstractmethod
    def use(self, user, target) -> bool:
        pass

class PaidShieldSmash(PaidAbilityStrategy):
    """Платная суперспособность Рыцаря: Щит + Золото"""
    def use(self, user, target) -> bool:
        # 1. Проверяем золото
        if user.money_balance < self.cost:
            print(f"❌ Недостаточно средств! Требуется {self.cost} 🪙, ваш баланс: {user.money_balance} 🪙.")
            return False

        # 2. Проверяем щит (логика с вашего скриншота)
        if user.shield_capacity < 10:
            print(f"❌ {user.name} пытается закрыться щитом, но он сломан!")
            return False

        # 3. Списываем ресурсы
        user.money_balance -= self.cost
        user.shield_capacity -= 10
        
        # 4. Применяем эффекты Рыцаря (из вашего кода)
        heal_amount = 20
        damage_amount = 5   # Можно увеличить, раз способность теперь платная!
        
        user.health += heal_amount
        target.health -= damage_amount

        # 👇 ГЕНЕРИРУЕМ СОБЫТИЕ ПЕРЕД ВЫХОДОМ ИЗ МЕТОДА!
        # Собираем данные, которые ждет наш AchievementManager (cost и hero_name)
        event_data = {
            "cost": self.cost,
            "hero_name": user.name
        }
        # Оповещаем всех подписчиков события "ability_used"
        game_events.notify("ability_used", data=event_data)

        # 5. Выводим текст в консоль
        print(f"💰 [Платная способность] Потрачено {self.cost} 🪙 на активацию механизма щита.")
        print(f"🛡️ {user.name} использует уникальную способность: Щит!")
        print(f"❤️ Восстановлено +{heal_amount} здоровья (Текущее: {user.health}).")
        print(f"🛡️ Оставшаяся прочность щита: {user.shield_capacity}")
        return True

class PaidBright(PaidAbilityStrategy):
    """Платная суперспособность Странника: Щит + Золото"""
    def use(self, user, target) -> bool:
              # 1. Проверяем золото
        if user.money_balance < self.cost:
            print(f"❌ Недостаточно средств! Требуется {self.cost} 🪙, ваш баланс: {user.money_balance} 🪙.")
            return False
        if user.is_hidden_capacity < 10:
            print(f"❌ {user.name} вы не можете применить сверхспособность укрытие!")
            return False

        # 3. Списываем ресурсы
        user.money_balance -= self.cost
        user.is_hidden_capacity -= 10
        target.health -= 40
        user.health += 20

        # 👇 ГЕНЕРИРУЕМ СОБЫТИЕ ПЕРЕД ВЫХОДОМ ИЗ МЕТОДА!
        # Собираем данные, которые ждет наш AchievementManager (cost и hero_name)
        event_data = {
            "cost": self.cost,
            "hero_name": user.name
        }
        # Оповещаем всех подписчиков события "ability_used"
        game_events.notify("ability_used", data=event_data)
        
        print(f"💰 [Платная способность] {user.name} швыряет горсть из {self.cost} коинов в глаза {target.name}!")
        print(f"✨ {target.name} дезориентирован ослепительным блеском и теряет 30 HP! {user.name} исцеляется на 15 HP.")
        return True

class PaidAlchemicalExplosion(PaidAbilityStrategy):
    """Суперспособность Ведьмака: Платная алхимическая бомба"""
    def use(self, user, target) -> bool:
        # 1. Проверяем баланс
        if user.money_balance < self.cost:
            print(f"❌ Недостаточно средств! Требуется {self.cost} 🪙, ваш баланс: {user.money_balance} 🪙.")
            return False
        if user.magic_power_capacity < 10:
            print(f"❌ {user.name} вы не можете применить сверхспособность алхимия!")
            return False

        # 3. Списываем ресурсы
        user.money_balance -= self.cost
        damage: int = random.randint(40, 70)
        target.health -= damage

        # 👇 ГЕНЕРИРУЕМ СОБЫТИЕ ПЕРЕД ВЫХОДОМ ИЗ МЕТОДА!
        # Собираем данные, которые ждет наш AchievementManager (cost и hero_name)
        event_data = {
            "cost": self.cost,
            "hero_name": user.name
        }
        # Оповещаем всех подписчиков события "ability_used"
        game_events.notify("ability_used", data=event_data)

        print(f"💰 [Платная способность] {user.name} покупает редкие ингредиенты прямо во время боя за {self.cost} 🪙!")
        print(f"🔥 Бомба взрывается, нанося {target.name} {damage} урона!")
        return True
