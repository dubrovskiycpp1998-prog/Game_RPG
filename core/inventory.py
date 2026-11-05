from secrets import choice


class Inventory():
    def __init__(self):
        self.items = {}  # Список предметов в инвентаре
        self.max_capacity = 10  # Максимальная вместимость инвентаря

    def list_items(self):
        """Выводит список всех предметов и их количество."""
        if self.items:
            print("Предметы в инвентаре:")
            # Перебираем хеш-таблицу парами: Название и Количество
            for name, count in self.items.items():
                print(f"- {name}: {count} шт.")
        else:
            print("Инвентарь пуст.")

    def add_item(self, item):
        """Добавляет предмет в хеш-таблицу, если есть место."""
        
        # Проверяем вместимость. len(self.items) считает количество УНИКАЛЬНЫХ видов предметов
        if len(self.items) < self.max_capacity or item.name in self.items:
            
            # Магия хеш-таблицы: берем текущее количество по имени предмета (если его нет — вернет 0)
            # и прибавляем 1. Записываем обратно в словарь.
            self.items[item.name] = self.items.get(item.name, 0) + 1
            
            # Печатаем КРАСИВОЕ имя предмета (item.name вместо самого объекта)
            print(f"Предмет '{item.name}' добавлен в инвентарь.")
        else:
            print("Инвентарь полон! Невозможно добавить предмет.")

    def remove_item(self, item):
        """Удаляет одну единицу предмета из хеш-таблицы."""
        if item in self.items:
            # Уменьшаем количество на 1
            self.items[item] -= 1
            
            # КРИТИЧЕСКИ ВАЖНО: если количество стало 0, полностью удаляем ключ из словаря!
            if self.items[item] <= 0:
                del self.items[item]
                
            print(f"Предмет '{item}' удален из инвентаря.")
        else:
            print(f"Предмет '{item}' не найден в инвентаре.")

    def use_item(self):
        """Использует предмет, если он есть в инвентаре."""
        # Здесь можно добавить логику применения предмета
        self.list_items()
        try:
            user_choice = int(input("Какой предмет использовать?: "))
        except ValueError:
            print("⚠️ Пожалуйста, введите корректное число!")
            return
        if user_choice < 1 or user_choice > len(self.items):
            print("⚠️ Неверный выбор предмета!")
            return
        selected_key = list(self.items.keys())[user_choice - 1]

        print(f"Вы использовали предмет: {selected_key}")
        self.remove_item(selected_key)  # После использования удаляем предмет
        

    
