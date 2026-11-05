class probability_weight:
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def calculate_probability(self, total_weight):
        if total_weight == 0:
            return 0
        return self.weight / total_weight

    def __str__(self):
        return f"Probability Weight: {self.weight}"

    def __repr__(self):
        return f"probability_weight(weight={self.weight})"

    def __eq__(self, other):
        if isinstance(other, probability_weight):
            return self.weight == other.weight
        return False

    def __lt__(self, other):
        if isinstance(other, probability_weight):
            return self.weight < other.weight
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, probability_weight):
            return self.weight <= other.weight
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, probability_weight):
            return self.weight > other.weight
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, probability_weight):
            return self.weight >= other.weight
        return NotImplemented

    def __ne__(self, other):    
        if isinstance(other, probability_weight):
            return self.weight != other.weight
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, probability_weight):
            return probability_weight(self.weight + other.weight)
        return NotImplemented

    def change_weight(self, new_weight):
        self.weight = new_weight
        #if  hero.health < 30:
            #self.weight += 10  # Увеличиваем вес события, если здоровье героя низкое

        #elif hero.health > 70:
            #self.weight -= 5  # Уменьшаем вес события, если здоровье героя высокое

        #elif hero.money_balance < 100:
            #self.weight += 15  # Увеличиваем вес события, если баланс героя низкий

        #elif hero.money_balance > 500:
            #self.weight -= 10  # Уменьшаем вес события, если баланс героя высоки

        #elif hero.health < 50 and hero.money_balance < 200:
            #self.weight += 20  # Увеличиваем вес события, если здоровье и баланс
           

        