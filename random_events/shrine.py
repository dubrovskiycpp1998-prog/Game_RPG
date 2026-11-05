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
