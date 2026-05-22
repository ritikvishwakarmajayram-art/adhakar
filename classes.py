from character import Character

class Warrior(Character):
    """Warrior class - High attack and defense"""
    def __init__(self, name, level=1):
        super().__init__(name, "Warrior", level)
        self.attack = 15
        self.defense = 8
        self.max_hp = 150
        self.hp = 150

class Mage(Character):
    """Mage class - High mana and spell damage"""
    def __init__(self, name, level=1):
        super().__init__(name, "Mage", level)
        self.attack = 8
        self.defense = 3
        self.max_mana = 100
        self.mana = 100
        self.max_hp = 80
        self.hp = 80
    
    def cast_spell(self, spell_name, mana_cost, damage):
        """Cast a spell if enough mana"""
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            return damage
        return 0

class PranaVaidya(Character):
    """Prana-Vaidya class - Healer with enhanced healing"""
    def __init__(self, name, level=1):
        super().__init__(name, "Prana-Vaidya", level)
        self.attack = 6
        self.defense = 4
        self.max_hp = 90
        self.hp = 90
    
    def heal(self):
        """Enhanced healing for Prana-Vaidya"""
        heal_amount = 50
        self.hp = min(self.hp + heal_amount, self.max_hp)
        return heal_amount
    
    def heal_ally(self, ally):
        """Heal an ally"""
        heal_amount = 40
        ally.hp = min(ally.hp + heal_amount, ally.max_hp)
        return heal_amount

class Rogue(Character):
    """Rogue class - High speed and critical hits"""
    def __init__(self, name, level=1):
        super().__init__(name, "Rogue", level)
        self.attack = 12
        self.defense = 4
        self.max_hp = 100
        self.hp = 100
        self.critical_chance = 0.25
    
    def critical_strike(self, enemy):
        """Perform a critical strike"""
        import random
        if random.random() < self.critical_chance:
            damage = self.attack * 2 + (self.level * 3)
            return enemy.take_damage(damage)
        return enemy.take_damage(self.attack)
