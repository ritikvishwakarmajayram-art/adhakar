import random
from classes import Warrior, Mage, PranaVaidya, Rogue
from enemy import Goblin, Orc, Dragon

class Game:
    """Main game engine"""
    
    def __init__(self):
        self.player = None
        self.current_enemy = None
        self.game_over = False
        self.turn = 0
    
    def create_character(self):
        """Create a new character"""
        print("\n=== Character Creation ===")
        name = input("Enter your character name: ")
        
        print("\nChoose your class:")
        print("1. Warrior - High HP and Defense")
        print("2. Mage - High Mana and Spell Damage")
        print("3. Prana-Vaidya - Healer with Enhanced Healing")
        print("4. Rogue - High Attack and Critical Chance")
        
        choice = input("Enter class number (1-4): ").strip()
        
        if choice == "1":
            self.player = Warrior(name)
        elif choice == "2":
            self.player = Mage(name)
        elif choice == "3":
            self.player = PranaVaidya(name)
        elif choice == "4":
            self.player = Rogue(name)
        else:
            print("Invalid choice! Defaulting to Warrior.")
            self.player = Warrior(name)
        
        print(f"\nWelcome, {self.player}!\n")
    
    def spawn_enemy(self):
        """Spawn a random enemy"""
        enemy_level = max(1, self.player.level + random.randint(-1, 1))
        enemy_type = random.choice([Goblin, Orc, Dragon])
        self.current_enemy = enemy_type(enemy_level)
        print(f"\nA wild {self.current_enemy} appears!\n")
    
    def display_status(self):
        """Display player and enemy status"""
        print(f"\n--- Turn {self.turn} ---")
        print(f"Player: {self.player}")
        print(f"Enemy:  {self.current_enemy}")
    
    def player_turn(self):
        """Handle player's turn in combat"""
        print("\nYour turn!")
        print("1. Attack")
        print("2. Heal")
        print("3. Run Away")
        
        choice = input("Choose action (1-3): ").strip()
        
        if choice == "1":
            damage = self.player.attack_enemy(self.current_enemy)
            print(f"You deal {damage} damage!")
        elif choice == "2":
            heal_amount = self.player.heal()
            print(f"You heal {heal_amount} HP!")
        elif choice == "3":
            if random.random() < 0.5:
                print("You successfully escaped!")
                return "escape"
            else:
                print("Failed to escape!")
        else:
            print("Invalid action!")
    
    def enemy_turn(self):
        """Handle enemy's turn in combat"""
        damage = self.current_enemy.attack_enemy(self.player)
        print(f"\nEnemy deals {damage} damage!")
    
    def battle(self):
        """Main battle loop"""
        self.spawn_enemy()
        self.turn = 0
        
        while self.player.is_alive() and self.current_enemy.is_alive():
            self.turn += 1
            self.display_status()
            
            result = self.player_turn()
            if result == "escape":
                return "escape"
            
            if not self.current_enemy.is_alive():
                print(f"\n✓ You defeated {self.current_enemy.name}!")
                self.player.experience += self.current_enemy.experience_reward
                print(f"Gained {self.current_enemy.experience_reward} experience!")
                
                # Level up if experience threshold reached
                if self.player.experience >= self.player.level * 100:
                    self.player.level_up()
                    print(f"✨ LEVEL UP! You are now level {self.player.level}!")
                return "victory"
            
            self.enemy_turn()
            
            if not self.player.is_alive():
                print(f"\n✗ You were defeated by {self.current_enemy.name}...")
                return "defeat"
        
        return "draw"
    
    def main_menu(self):
        """Main game menu"""
        print("\n" + "="*40)
        print("     ADHAKAR - RPG ADVENTURE GAME")
        print("="*40)
        print("1. New Game")
        print("2. Exit")
        
        choice = input("\nChoose option (1-2): ").strip()
        
        if choice == "1":
            self.create_character()
            self.game_loop()
        elif choice == "2":
            print("\nThanks for playing!")
            self.game_over = True
        else:
            print("Invalid choice!")
    
    def game_loop(self):
        """Main game loop"""
        while not self.game_over and self.player.is_alive():
            print("\n" + "="*40)
            print("1. Search for Battle")
            print("2. Rest (Restore HP/Mana)")
            print("3. View Status")
            print("4. Quit")
            
            choice = input("\nChoose action (1-4): ").strip()
            
            if choice == "1":
                result = self.battle()
                if result == "defeat":
                    self.game_over = True
            elif choice == "2":
                self.player.hp = self.player.max_hp
                self.player.mana = self.player.max_mana
                print("\n✓ You rest and restore your health and mana!")
            elif choice == "3":
                print(f"\n{self.player}")
                print(f"Mana: {self.player.mana}/{self.player.max_mana}")
                print(f"Experience: {self.player.experience}")
            elif choice == "4":
                print(f"\nFinal Stats: {self.player}")
                print("Thanks for playing!")
                self.game_over = True
            else:
                print("Invalid choice!")

def main():
    """Entry point"""
    game = Game()
    while not game.game_over:
        game.main_menu()

if __name__ == "__main__":
    main()
