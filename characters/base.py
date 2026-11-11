from core.inventory import Inventory

class Hero:
    def __init__(self, name, health, attack_power, who_is_character, money_balance = 300, respect_hero = 50, stamina = 100):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.inventory = Inventory()
        self.who_is_character = who_is_character
        self.money_balance = money_balance
        self.respect = respect_hero
        self.stamina = stamina
      

    # Геттер для безопасного получения здоровья
    @property
    def health(self):
        return self._health

    # Сеттер, который контролирует, чтобы здоровье не падало ниже 0
    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

   
    def get_name(self):
        print("Введите имя персонажа")
        self.name = input("Как вас зовут? ")

    def print_info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Атака: {self.attack_power}")
        print(f"Баланс монет: {self.money_balance}")
        print(f"Уважение: {self.respect}")
        print(f"Выносливость: {self.stamina}")


    def unique_ability(self, other):
        pass  # Метод будет переопределен в подклассах

    def attack(self, target):
        print(f"{self.name} атакует {target.name} и наносит {self.attack_power} урона!")
        target.health -= self.attack_power
        self.money_balance += 50
        self.stamina -= 10
        self.respect += 5


    def get_paid(self):
        self.money_balance -= 500

    def add_item(self, item):
            """Добавляет предмет в инвентарь, если есть место."""
            if len(self.items) < self.max_capacity:
                self.items.append(item)
                print(f"Предмет '{item}' добавлен в инвентарь.")
            else:
                print("Инвентарь полон! Невозможно добавить предмет.")
    
        


class Enemy:
    def __init__(self, name, health, attack_power, who_is_enemy, is_Event_ID = 1):
        self.name = name
        self._health = health
        self.attack_power = attack_power
        self.who_is_enemy = who_is_enemy
        self.is_Event_ID = is_Event_ID

    # Геттер для безопасного получения здоровья
    @property
    def health(self):
        return self._health

    # Сеттер, который контролирует, чтобы здоровье не падало ниже 0
    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value

class Loot:
    def __init__(self, name, gain_xp, is_Loot, cost, is_Event_ID = 2):
        self.name = name
        self.gain_xp = gain_xp
        self.is_Loot = is_Loot
        self.cost = cost
        self.is_Event_ID = is_Event_ID

    def help_hero(self, target):

       target.health += self.gain_xp
       
            
        