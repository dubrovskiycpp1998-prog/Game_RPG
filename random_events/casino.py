import random
from core.game_loop import AdventureState
from random_events.base_event import RandomEvent

# =====================================================================
#Случайное Событие Казино
# =====================================================================

# 1. Это само событие, на которое игрок натыкается на карте
class CasinoEncounterEvent(RandomEvent):
    def execute(self, engine):
        print("\n🔍 Среди деревьев вы заметили неоновую вывеску тайного заведения...")
        # Переключаем движок игры на экран казино, который написан ниже
        engine.set_state(CasinoState(engine))


class CasinoState(AdventureState):
    def render(self):
        print("\n🎰=== ДОБРО ПОЖАЛОВАТЬ В КАЗИНО 'ЗОЛОТОЙ ГОБЛИН' ===🎰")
        print(f"Ваш баланс: {self.engine.hero.money_balance} 🪙")
        print("1. Сыграть в Кости (Мини-игра)")
        print("2. Крутануть Напёрстки (Удвоение коинов)")
        print("3. Крутануть Игровой Автомат / Слот-машину (Ставка: 300 🪙)  🔥 NEW!")
        print("4. Сыграть в Блэкджек / 21 (Ставка: 400 🪙)                  🔥 NEW!")
        print("5. Покинуть заведение (Вернуться на карту)")

    def handle_input(self, user_input: str):
        hero = self.engine.hero
# =====================================================================
# ИГРА В КОСТИ
# =====================================================================
        if user_input == "1":
            bet = 200
            if hero.money_balance < bet:
                print("Извините у вас недостаточно денег")
                return
            print("Бросаем кости")

            player_score = random.randint(1,6)
            dealer_score = random.randint(1,6)

            print(f"ВЫ выкинули {player_score} очков дилер выкинул {dealer_score} очков")

            if player_score > dealer_score:
                print("Победа!")
                print(f"Ваша ставка удвоена + {bet * 2}!")
                hero.money_balance += bet * 2 
            elif player_score < dealer_score:
                print(f"Вы проиграли - {bet}")
                hero.money_balance -= bet 
            else:
                print("Ничья") 

            input("\nНажмите Enter, чтобы продолжить...")   
# =====================================================================
# ИГРА В НАПЕРСТКИ
# =====================================================================
        if user_input == "2":
            bet = 200 
            if hero.money_balance < bet:
                print("Извините у вас недостаточно денег")
                return
            print("Угадайте число от 1 до 6")

            guess_number = random.randint(1,10)
            player_choice = input ("Введите число, которое вы думаете загадал дилер")
            if guess_number == player_choice:
                hero.money_balance += bet * 2 
                print("ВЫ угадали, ваша ставка удвоенна")
                print(f"Ваш баланс: {hero.money_balance}!")
            else:
                hero.money_balance -= bet 
                print("К сожалению вы проиграли")
                print(f"Ваш баланс: {hero.money_balance}!")
            input("\nНажмите Enter, чтобы продолжить...")


# =====================================================================
# ИГРОВОЙ АВТОМАТ
# =====================================================================
        if user_input == "3":
            bet = 300 
            if hero.money_balance < bet:
                print("Извините у вас недостаточно денег")
                return
            print("Однорукий бандит")
            hero.money_balance -= bet
            print("\n🎰 Рычаг опущен! Барабаны крутятся...")
            
            # Генерируем три случайных эмодзи-символа
            symbols = ["🍒", "🍊", "🍋", "💎", "7️⃣"]
            reel1 = random.choice(symbols)
            reel2 = random.choice(symbols)
            reel3 = random.choice(symbols)

            print(f"| {reel1} |  {reel2} | {reel3}")

            if reel1 == reel2 == reel3 == "7️⃣":
                print ("Вы выиграли джекпот 5000")
                hero.money_balance += 5000
                print (f"Ваш баланс: {hero.money_balance}")

            elif reel1 == reel2 == reel3:
                print ("ВЫиграш 2000")
                hero.money_balance += 2000
                print (f"Ваш баланс: {hero.money_balance}")

            elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
                print ("ВЫиграш 500")
                hero.money_balance += 500
                print (f"Ваш баланс: {hero.money_balance}")

            else:
                print ("Ничего попробуйте еще раз")
                print (f"Ваш баланс: {hero.money_balance}")

            print (f"Ваш баланс: {hero.money_balance}")
            input("\nНажмите Enter, чтобы продолжить...")

# =====================================================================
# БЛЭКДЖЕК
# =====================================================================            
        if user_input == "4":
            bet = 400 
            if hero.money_balance < bet:
                print("Извините у вас недостаточно денег")
                return
            print("ИГРА БЛЭКДЖЕК")
        
            print("\n🎰 Начинается раздача блэкджек")

            player_score = random.randint(2, 11) + random.randint(2, 11)
            dealer_score = random.randint(2, 11) + random.randint(2, 11)
            print (f"Вы набрали: {player_score}")

            while player_score < 21:
                choice_player = input(" Хотите добрать, если да, нажмите 1, если нет 2").strip()
                if choice_player == "1":
                   player_score += random.randint(2, 11)
                   print (f"Вы набрали: {player_score}")
                else:
                    break

            print ("Итоги раздачи")
            print (f"Вы набрали: {player_score}")

            while dealer_score < 17 and player_score <= 21:
                dealer_score += random.randint(2, 11)
            print (f"Дилер набрал: {dealer_score}")

            if player_score > 21 and dealer_score < 21:
                print ("Перебор, вы проиграли")
                hero.money_balance -= 400
                print (f"Ваш баланс: {hero.money_balance}")
            elif player_score < 21 and dealer_score > 21:
                print ("Дилер перебрал ВЫ выиграли")
                hero.money_balance += 100
                print (f"Ваш баланс: {hero.money_balance}")
            elif player_score < 21 and dealer_score < 21 and player_score > dealer_score:
                print ("Вы набрали больше очков, чем дилер, вы выиграли")
                hero.money_balance += 800
                print (f"Ваш баланс: {hero.money_balance}")
            elif player_score < 21 and dealer_score < 21 and player_score < dealer_score:
                print ("Вы набрали меньше очков, чем дилер, вы проиграли")
                hero.money_balance -= 800
                print (f"Ваш баланс: {hero.money_balance}")

            elif player_score == 21:
                print ("Вы набрали 21 вы выиграли")
                hero.money_balance += 1600
                print (f"Ваш баланс: {hero.money_balance}")

            elif dealer_score == 21:
                print ("Дилер набрал 21 дилер выиграл")
                hero.money_balance -= 1600
                print (f"Ваш баланс: {hero.money_balance}")

            elif player_score == 21 and dealer_score == 21:
                print ("Вы набрали с дилером оба 21!!! ВОТ ЭТО УДАЧА")
                hero.money_balance += 5000
                print (f"Ваш баланс: {hero.money_balance}")

            elif player_score == dealer_score:
                print ("Вы набрали с дилером рдинаковое количество очков")
                hero.money_balance += 2000
                print (f"Ваш баланс: {hero.money_balance}")
            else:
                print (" ЧТо то пошло не так")

        input("\nНажмите Enter, чтобы продолжить...")
                    

# =====================================================================
# ВЫХОД ИЗ КАЗИНО
# =====================================================================

        if user_input == "5":
            print("\nВы выходите из казино на карту.")
            # Динамически импортируем MapState прямо здесь, 
            # чтобы избежать циклической зависимости файлов
            from core.game_loop import MapState
            self.engine.set_state(MapState(self.engine))
            
        else:
            print("⚠️ Неверный ввод! Выберите действие от 1 до 3.")


        
        
        