from random_events.base_event import RandomEvent

class HealingShrineEvent(RandomEvent):
    def execute(self, engine):
        hero = engine.hero
        heal_amount = 30
        hero.health += heal_amount
        print("\n✨=========================================✨")
        print(f"🤠 Вы нашли древний Алтарь Жизни!")
        print(f"Благословение восстанавливает {hero.name} +{heal_amount} HP.")
        print(f"Ваше текущее здоровье: {hero.health} HP.")
        print("✨=========================================✨")
        input("\nНажмите Enter, чтобы продолжить путь...")
        # Так как этот стейт не менялся (мы остались на карте), 
        # нам не нужно вызывать engine.set_state(), игрок просто продолжит идти

    def get_weight(self, hero):
        """
        
        Метод для получения веса события. По умолчанию возвращает 0.5.
        """
        weight = 0.5
        # Если здоровье героя ниже 30, увеличиваем вероятность события
        if hero.health < 30:
            weight += 0.5  # Увеличиваем вес события, если здоровье героя низкое
        # Если здоровье героя выше 80, уменьшаем вероятность события
        elif hero.health > 80:
            weight -= 0.2  # Уменьшаем вес события, если здоровье героя высокое
        elif hero.health < 50:
            weight += 0.3  # Увеличиваем вес события, если здоровье героя очень низкое
       
        return weight
    
        
    