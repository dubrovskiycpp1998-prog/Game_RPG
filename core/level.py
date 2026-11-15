#Generate Level and require for the Level Up
#class Level:
#Hero in begin of the game is level 1, and can be leveled up to level 10. 
# Each level up requires a certain amount of experience points (XP). 
# The XP required for each level is as follows:
################################################################################################
################################################################################################

#Level 1: 0 XP (starting level)    
#Level 2: 100 XP
#Level 3: 300 XP
#Level 4: 600 XP
#Level 5: 1000 XP
#Level 6: 1500 XP
#Level 7: 2100 XP
#Level 8: 2800 XP
#Level 9: 3600 XP
#Level 10: 4500 XP
################################################################################################
#############################################################################################################################################################################################

#Xp required for each level up is calculated using the formula: 
#XP_required = 100 * (level - 1) * level / 2
################################################################################################
#############################################################################################################################################################################################

#XP depends on the level of the hero, and the hero can gain XP by 
#defeating enemies, completing quests, 
#or performing other actions in the game.
################################################################################################
#############################################################################################################################################################################################

#For def __init__:
#    self.level = level
#    self.hash_map_level = hash_map_level
#    self.XP_hero = XP_hero
#    self.XP_required_for_next_level = XP_required_for_next_level
#    self.is_level_up = False
#    self.is_max_level = False
#    hash_map_level = {
#        "Level_01": 0,
#        "Level_02": 100,
#        "Level_03": 300,
#        "Level_04": 600,
#        "Level_05": 1000,
#        "Level_06": 1500,
#        "Level_07": 2100,
#        "Level_08": 2800,
#        "Level_09": 3600,
#        "Level_10": 4500
#    }
################################################################################################
#############################################################################################################################################################################################

#def calculated_XP_required_for_next_level(self):
#    self.XP_required_for_next_level = 100 * (self.level - 1) * self.level / 2

#def check_level_up(self):   
#   if self.XP_hero >= self.XP_required_for_next_level:
#    self.is_level_up = True

#def level_up(self):
#   if check_level_up(self):
#    self.level += 1
   
