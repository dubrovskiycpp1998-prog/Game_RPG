#Игроку преддлагается мини игра, чтобы открыть сундук с сокровищами. 
# В случае успеха игрок получает случайное количество золота, 
# в случае неудачи теряет здоровье.
# Нужно угадать слово, которое загадал компьютер. 
# Выводится слово пропущенными буквами
# Игрок вводит целевое слово. 
# Если игрок угадывает слово, он получает случайное количество золота.

################################################################################################################################
from random_events.base_event import RandomEvent
import random
################################################################################################################################

class TreasureEvent(RandomEvent):
    def execute(self, engine):

        return super().execute(engine)
    
    def render(self):
        print("\nВы нашли сундук")
        print("В нем модет содержаться нечто инетересное")
        print("Однако, чтобы его открыть нужно разгадать головоломку - угадать слово")
        print("ЧТобы сыграть нажмите 1")
        print("Чтобы выйти нажмите 2")

    def handle_input(self, user_input: str):
        hero = self.engine.hero
        if user_input == "1":
            words_for_guessing = ("poker", "treasure")
            max_attempts = 3
            attempts = 0
            guess_word =random.choice(words_for_guessing)
            # Собираем слово с пропущенными буквами (скрываем ~50% букв)
            masked_chars = [
                "_" if random.random() < 0.5 else char 
                for char in guess_word
            ]
            # Защита на случай, если не скрылась ни одна буква
            if "_" not in masked_chars:
                masked_chars[random.randrange(len(guess_word))] = "_"
            
            print_word = "".join(masked_chars)
            while attempts < max_attempts:
                print(f"\nЗагаданное слово: {print_word}")
                print(f"Осталось попыток: {max_attempts - attempts}")
                player_word = input("Введите слово, которое загадал сундук: ").strip().lower()

                if player_word == guess_word:
                    print("Вы угадали!!! Сундук открыт!")
                    # Здесь можно добавить выдачу награды игроку
                    # механика генерации случайного предмета
                    # Механика складывания предмета в инвентарь
                    break
                else:
                    attempts += 1
                    print("Неверно!")
            else:
                print(f"Попытки закончились! Замок заклинило. Было загадано слово: {guess_word}")
                
        elif user_input == "2":
            print("\nВы бросили сундук.")
            # Динамически импортируем MapState прямо здесь, 
            # чтобы избежать циклической зависимости файлов
            from core.game_loop import MapState
            self.engine.set_state(MapState(self.engine))
            
        else:
            print("⚠️ Неверный ввод! Выберите действие от 1 до 2.")
        
