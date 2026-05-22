from character import Character
import random

class Enemy(Character):
    """Enemy class for combat"""
    
    def __init__(self, name, enemy_type, level=1):
        super().__init__(name, enemy_type, level)
        self.experience_reward = level * 50
        self.loot = []
    
    def random_attack(self, player):
        """Enemy performs a random attack"""
        if random.random() < 0.3:  # 30% chance to heal
            if self.character_class == "Prana-Vaidya":
                self.heal()
        else:
            damage = self.attack_enemy(player)
            return damage
        return 0

class Goblin(Enemy):
    def __init__(self, level=1):
        super().__init__(f"Goblin Lvl{level}", "Goblin", level)
        self.attack = 5 + level
        self.defense = 2
        self.max_hp = 30 + level * 10
        self.hp = self.max_hp
        self.experience_reward = level * 30

class Orc(Enemy):
    def __init__(self, level=1):
        super().__init__(f"Orc Lvl{level}", "Orc", level)
        self.attack = 12 + level
        self.defense = 4
        self.max_hp = 60 + level * 15
        self.hp = self.max_hp
        self.experience_reward = level * 60

class Dragon(Enemy):
    def __init__(self, level=1):
        super().__init__(f"Dragon Lvl{level}", "Dragon", level)
        self.attack = 20 + level * 2
        self.defense = 8
        self.max_hp = 150 + level * 30
        self.hp = self.max_hp
        self.experience_reward = level * 150
