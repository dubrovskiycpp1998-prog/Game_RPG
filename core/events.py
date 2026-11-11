# ==========================================
# ИЗДАТЕЛЬ (Класс менеджера событий)
# ==========================================
class EventManager:
    def __init__(self):
        self._listeners = {}

    def subscribe(self, event_type: str, listener_function):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener_function)

    def notify(self, event_type: str, data=None):
        if event_type in self._listeners:
            for listener in self._listeners[event_type]:
                listener(data)

# ==========================================
# ГЛОБАЛЬНЫЙ ОБЪЕКТ СОБЫТИЙ (Ваш код со скриншота)
# ==========================================
game_events = EventManager()

# ==========================================
# НАБЛЮДАТЕЛИ (Ваши функции со скриншота)
# ==========================================
def on_enemy_slain_give_gold(enemy_data):
    hero = enemy_data["hero"]
    hero.money_balance += 1000
    print(f"💰 [Наблюдатель Экономики]: Замечена смерть врага! Начислено 1000 коинов.")

#def on_enemy_slain_track_stats(enemy_data):
    #gameplay_context = enemy_data["gameplay"]
    #gameplay_context.count_win += 1
    #print(f"📊 [Наблюдатель Статистики]: Счетчик побед обновлен! Теперь побед: {gameplay_context.count_win}")

def on_enemy_slain_play_sound(enemy_data):
    print(f"🎵 [Наблюдатель Звука]: Играет победный трек фанфар!")

# ==========================================
# НОВЫЙ НАБЛЮДАТЕЛЬ: МЕНЕДЖЕР ДОСТИЖЕНИЙ
# ==========================================
class AchievementManager:
    def __init__(self):
        # Переменная для подсчета общего количества потраченного золота
        self.total_gold_spent = 0
        # Флаг, чтобы ачивка не выдавалась несколько раз подряд
        self.achievement_unlocked = False

    def track_ability_spending(self, data):
        """Функция-обработчик события 'ability_used'"""
        cost = data["cost"]
        hero_name = data["hero_name"]
        
        # Увеличиваем счетчик потраченного золота
        self.total_gold_spent += cost
        print(f"\n📊 [Система Ачивок]: {hero_name} потратил {cost} 🪙 на способность.")
        print(f"📊 [Система Ачивок]: Всего влито золота в ультимейты: {self.total_gold_spent} / 1000 🪙")
        
        # Проверяем условие выполнения достижения (например, потратить 1000 золота)
        if self.total_gold_spent >= 1000 and not self.achievement_unlocked:
            self.achievement_unlocked = True
            print("\n" + "🏆" * 20)
            print("🏆 ДОСТИЖЕНИЕ РАЗБЛОКИРОВАНО: 'Богатый воин'!")
            print("🏆 Вы потратили более 1000 коинов на платные способности в бою!")
            print("🏆" * 20 + "\n")

# Создаем один глобальный объект менеджера ачивок
achievement_manager = AchievementManager()

