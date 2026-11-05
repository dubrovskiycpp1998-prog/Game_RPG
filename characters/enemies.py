from characters.base import Enemy

class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name, health=50, attack_power=5, who_is_enemy=1)
        
    # МЕТОД ВЫНЕСЕН ИЗ __init__ И ПЕРЕИМЕНОВАН В attack
    def attack(self, target):
        print(f"{self.name} атакует {target.name} и наносит {self.attack_power} урона!")
        target.health -= self.attack_power

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=25, who_is_enemy=2)
        
    # МЕТОД ВЫНЕСЕН ИЗ __init__ И ПЕРЕИМЕНОВАН В attack
    def attack(self, target):
        print(f"{self.name} изрыгает пламя на {target.name} и наносит {self.attack_power} урона!")
        target.health -= self.attack_power

class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, who_is_enemy=3)
        
    # МЕТОД ВЫНЕСЕН ИЗ __init__ И ПЕРЕИМЕНОВАН В attack
    def attack(self, target):
        print(f"{self.name} наносит удар по {target.name} и наносит {self.attack_power} урона!")
        target.health -= self.attack_power