class Character:
    """Base character class for RPG game"""
    
    def __init__(self, name, character_class, level=1):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.hp = 100
        self.max_hp = 100
        self.mana = 50
        self.max_mana = 50
        self.attack = 10
        self.defense = 5
        self.experience = 0
        
    def heal(self):
        """Heal the character based on their class"""
        heal_amount = 30
        if self.character_class == "Prana-Vaidya":
            heal_amount = 50
        # Add limit to prevent spamming
        self.hp = min(self.hp + heal_amount, self.max_hp)
        return heal_amount
    
    def take_damage(self, damage):
        """Take damage, reduced by defense"""
        actual_damage = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage
    
    def attack_enemy(self, enemy):
        """Attack an enemy"""
        damage = self.attack + (self.level * 2)
        actual_damage = enemy.take_damage(damage)
        return actual_damage
    
    def level_up(self):
        """Increase level and stats"""
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.max_mana += 10
        self.mana = self.max_mana
        self.attack += 5
        self.defense += 2
    
    def is_alive(self):
        """Check if character is alive"""
        return self.hp > 0
    
    def __str__(self):
        return f"{self.name} (Lvl {self.level} {self.character_class}) - HP: {self.hp}/{self.max_hp}"
