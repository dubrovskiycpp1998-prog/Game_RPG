from characters.base import Loot

class Potion(Loot):
    def __init__(self, name):
        super().__init__(name, gain_xp = 10, is_Loot = 1, cost = 2000)


class Magic_Ball(Loot):
    def __init__(self, name):
            super().__init__(name, gain_xp = 5, is_Loot = 1, cost = 1000)



    
    