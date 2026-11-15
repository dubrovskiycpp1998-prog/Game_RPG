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

# ==========================================
# НОВЫЙ НАБЛЮДАТЕЛЬ: ВЫДАЕТСЯ ПРИ ЗАХОДЕ В КАЗИНО
# ==========================================

class CasinoEntryManager:
    def __init__(self):
        self.entry_count = 0
        self.achievement_unlocked = False

    def track_casino_entry(self, data = None):
        """Функция-обработчик события 'casino_entered'"""
        self.entry_count += 1
        
        print(f"\n🎰 [Система Ачивок]: Вы вошли в казино {self.entry_count} раз(а).")
        
        # Проверяем условие выполнения достижения (например, войти в казино 5 раз)
        if self.entry_count >= 2 and not self.achievement_unlocked:
            self.achievement_unlocked = True
            print("\n" + "🏆" * 20)
            print("🏆 ДОСТИЖЕНИЕ РАЗБЛОКИРОВАНО: 'Любитель риска'!")
            print("🏆 Вы посетили казино 2 раза!")
            print("🏆" * 20 + "\n")

# Создаем один глобальный объект менеджера входа в казино
casino_entry_manager = CasinoEntryManager()


# ====================================================================================
# ОБЩИЙ МЕТОД ДЛЯ АЧИВОК (можно использовать для других событий)
# ====================================================================================
class AchievementManager:
    def __init__(self):
        # ==============================
        #Инновация: добавляем счетчик для отслеживания потраченного золота на способности и флаг для ачивки 
        # ==============================
        # Переменная для подсчета общего количества потраченного золота
        self.total_gold_spent = 0
        # Флаг, чтобы ачивка не выдавалась несколько раз подряд
        self.achievement_unlocked_ability = False
        
        # ==============================
        #Инновация: добавляем счетчик посещений казино и флаг для ачивки
        # ==============================
        self.entry_count = 0
        self.achievement_unlocked_casino = False

# ====================================================================================
# ОБРАБОТКА СОБЫТИЯ "СПЕНДИНГ УЛЬТИМЕЙТА" (ПЛАТНОЙ СПОСОБНОСТИ)
# ====================================================================================
    def track_ability_spending(self, data):
        """Функция-обработчик события 'ability_used'"""
        cost = data["cost"]
        hero_name = data["hero_name"]
        
        # Увеличиваем счетчик потраченного золота
        self.total_gold_spent += cost
        print(f"\n📊 [Система Ачивок]: {hero_name} потратил {cost} 🪙 на способность.")
        print(f"📊 [Система Ачивок]: Всего влито золота в ультимейты: {self.total_gold_spent} / 1000 🪙")
        
        # Проверяем условие выполнения достижения (например, потратить 1000 золота)
        if self.total_gold_spent >= 1000 and not self.achievement_unlocked_ability:
            self.achievement_unlocked_ability = True
            print("\n" + "🏆" * 20)
            print("🏆 ДОСТИЖЕНИЕ РАЗБЛОКИРОВАНО: 'Богатый воин'!")
            print("🏆 Вы потратили более 1000 коинов на платные способности в бою!")
            print("🏆" * 20 + "\n")

# ====================================================================================
# ОБРАБОТКА СОБЫТИЯ "ВХОД В КАЗИНО"
# ====================================================================================  
    def track_casino_entry(self, data = None):
        """Функция-обработчик события 'casino_entered'"""
        self.entry_count += 1
        
        print(f"\n🎰 [Система Ачивок]: Вы вошли в казино {self.entry_count} раз(а).")
        
        # Проверяем условие выполнения достижения (например, войти в казино 5 раз)
        if self.entry_count >= 2 and not self.achievement_unlocked_casino:
            self.achievement_unlocked_casino = True
            print("\n" + "🏆" * 20)
            print("🏆 ДОСТИЖЕНИЕ РАЗБЛОКИРОВАНО: 'Любитель риска'!")
            print("🏆 Вы посетили казино 2 раза!")
            print("🏆" * 20 + "\n")

# Создаем один глобальный объект менеджера ачивок
achievement_manager = AchievementManager()