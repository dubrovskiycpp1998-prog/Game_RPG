from abc import ABC, abstractmethod
import characters.heroes
from core.game_loop import GameEngine  # Импортируем обновленный движок похода
# Добавляем импорт объекта событий и функций в самый верх core/gameplay.py
from core.events import game_events, on_enemy_slain_give_gold, on_enemy_slain_play_sound
from core.events import game_events, achievement_manager
from core.inventory import Inventory  # Импортируем класс Inventory

# =====================================================================
# БАЗОВЫЙ КЛАСС ГЛОБАЛЬНЫХ СОСТОЯНИЙ ИГРЫ (Верхний уровень)
# =====================================================================
class GameplayState(ABC):
    def __init__(self, gameplay):
        self.gameplay = gameplay

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_input(self, user_input: str):
        pass


# --- СОСТОЯНИЕ: ВЫБОР ПЕРСОНАЖА ---
class CharacterSelectionState(GameplayState):
    def render(self):
        print("\n=== ВЫБОР ПЕРСОНАЖА ===")
        print("1. Рыцарь")
        print("2. Странник")
        print("3. Ведьмак")

    def handle_input(self, user_input: str):
        if user_input == "1":
            self.gameplay.hero = characters.heroes.Knight("Рыцарь")
        elif user_input == "2":
            self.gameplay.hero = characters.heroes.Stranger("Странник")
        elif user_input == "3":
            self.gameplay.hero = characters.heroes.Witcher("Ведьмак")
        else:
            print("⚠️ Неверный ввод! Пожалуйста, введите цифру от 1 до 3.")
            return

        print(f"\nВы выбрали класс: {self.gameplay.hero.name}!")
        self.gameplay.hero.get_name()  # Запрашиваем имя у игрока
        self.gameplay.hero.print_info()
        self.gameplay.count_win = 0  # Сбрасываем победы у нового персонажа
        
        # Сразу отправляем нового героя в его первое приключение!
        self.gameplay.start_adventure()


# --- СОСТОЯНИЕ: ПРОСМОТР И ИСПОЛЬЗОВАНИЕ ИНВЕНТАРЯ ---
class InventoryState(GameplayState):
    def render(self):
        hero = self.gameplay.hero

        print("ЗДЕСЬ БУДЕТ ВАШ ИНВЕНТАРЬ")
        print("Нажмите 1, для просмотра списка инвентаря")
        print("Нажмите 2, чтобы использовать инвентарь")
        print("Нажмите 3, чтобы удалить инвентарь")
        print("Нажмите 4, чтобы вернуться в таверну")


    def handle_input(self, user_input: str):
        if user_input == "1":
            self.gameplay.hero.inventory.print_information()
            return  # Возвращаемся к выбору действия после просмотра инвентаря
        elif user_input == "2":
            self.gameplay.hero.inventory.use_item()  # Передаем первый предмет из инвентаря
            self.gameplay.hero.inventory.help_hero()  # Передаем первый предмет из инвентаря, чтобы использовать метод help_hero с конкретным предметом
            return  # Возвращаемся к выбору действия после просмотра инвентаря
        elif user_input == "3": 
            self.gameplay.hero.inventory.remove_item()
            return  # Возвращаемся к выбору действия после удаления предмета
        elif user_input == "4":
            self.gameplay.set_state(TavernState(self.gameplay))
        else:
            print("⚠️ Неверный ввод! Пожалуйста, выберите от 1 до 4.")
            return

# --- СОСТОЯНИЕ: ТАВЕРНА (ОТДЫХ И ВЫБОР ДАЛЬНЕЙШЕГО ПУТИ) ---
class TavernState(GameplayState):
    def render(self):
        hero = self.gameplay.hero
        
        # Ваша логика восстановления характеристик при отдыхе в таверне
        if isinstance(hero, characters.heroes.Knight):
            hero.health = 120
            hero.shield_capacity = 50
        elif isinstance(hero, characters.heroes.Stranger):
            hero.health = 80
            hero.is_hidden_capacity = 30
        elif isinstance(hero, characters.heroes.Witcher):
            hero.health = 100
            hero.magic_power_capacity = 50
            
        print(f"\n🎒 {hero.name} отдохнул в таверне, восстановил силы и ресурсы!")
        print(f"--- Количество побед в этом походе: {self.gameplay.count_win} ---")
        print("\nЧто вы хотите сделать?")
        print("1. Продолжить поход текущим героем (следующее событие)")
        print("2. Начать сначала (создать нового героя)")
        print("3. Просмотреть инвентарь")
        print("4. Выйти из игры")

    def handle_input(self, user_input: str):
        if user_input == "1":
            # Снова отправляем этого же героя в приключения
            self.gameplay.start_adventure()
        elif user_input == "2":
            # Переключаемся обратно на экран выбора персонажа
            self.gameplay.set_state(CharacterSelectionState(self.gameplay))
        elif user_input == "3":
            # Переключаемся на экран инвентаря
            self.gameplay.set_state(InventoryState(self.gameplay))
        elif user_input == "4":
            print("\nСпасибо за игру! До встречи в таверне. 👋")
            self.gameplay.stop()
        else:
            print("⚠️ Неверный ввод! Пожалуйста, выберите от 1 до 4.")


# --- СОСТОЯНИЕ: ПОРАЖЕНИЕ (КОНЕЦ ИГРЫ) ---
class GameOverState(GameplayState):
    def render(self):
        print("\n" + "="*30)
        print("🪦 ПОРАЖЕНИЕ... Ваш герой пал в бою.")
        print("="*30)
        print(f"--- Итоговое количество побед: {self.gameplay.count_win} ---")
        print("\nЧто вы хотите сделать?")
        print("1. Начать сначала (создать нового героя)")
        print("2. Выйти из игры")

    def handle_input(self, user_input: str):
        if user_input == "1":
            self.gameplay.set_state(CharacterSelectionState(self.gameplay))
        elif user_input == "2":
            print("\nСпасибо за игру! До встречи в таверне. 👋")
            self.gameplay.stop()
        else:
            print("⚠️ Неверный ввод! Пожалуйста, выберите 1 или 2.")


# =====================================================================
# ОБНОВЛЕННЫЙ КЛАСС GAMEPLAY (Центральный менеджер всей игры)
# =====================================================================
class Gameplay:
    def __init__(self):
        self.hero = None
        self.count_win = 0
        self._is_running = True
        # Игра всегда начинается с выбора персонажа
        self._state = CharacterSelectionState(self)

        # 👇 ВОТ СЮДА ВСТАВЛЯЕМ ПОДПИСКУ ПРИ ИНИЦИАЛИЗАЦИИ ИГРЫ
        game_events.subscribe("enemy_death", on_enemy_slain_give_gold)
        #game_events.subscribe("enemy_death", on_enemy_slain_track_stats)
        game_events.subscribe("enemy_death", on_enemy_slain_play_sound)
        # 👇 ПОДПИСЫВАЕМ СИСТЕМУ АЧИВОК НА НОВОЕ СОБЫТИЕ
        game_events.subscribe("ability_used", achievement_manager.track_ability_spending)

    def set_state(self, new_state: GameplayState):
        """Метод смены глобальных экранов."""
        self._state = new_state

    def stop(self):
        self._is_running = False

    def start_adventure(self):
        """Запуск под-движка для походов (Карта/Бой/Лут)"""
        # Передаем героя во внутренний движок GameEngine (бывший Game_Loop)
        adventure_engine = GameEngine(self.hero)
        adventure_engine.run()
        
        # Сюда код вернется, как только внутри приключения сработает engine.stop()
        # Проверяем состояние героя после возвращения из похода
        if self.hero.health > 0:
            self.count_win += 1
            print("\n🎉 ПОБЕДА! Вы успешно завершили этап похода!")
            self.set_state(TavernState(self))
        else:
            self.set_state(GameOverState(self))

    def start_game(self):
        """Главный жизненный цикл приложения."""
        print("Добро пожаловать в игру!")
        while self._is_running:
            self._state.render()
            if not self._is_running:
                break
            choice = input("Введите номер действия: ").strip()
            self._state.handle_input(choice)
