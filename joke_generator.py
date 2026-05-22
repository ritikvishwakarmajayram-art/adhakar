from joke_api import JokeAPI
import time

class JokeGenerator:
    """Interactive Joke Generator Application"""
    
    def __init__(self):
        self.api = JokeAPI()
        self.joke_history = []
        self.favorite_jokes = []
    
    def display_welcome(self):
        """Display welcome message"""
        print("\n" + "="*70)
        print("😂 WELCOME TO THE RANDOM JOKE GENERATOR 😂")
        print("="*70)
        print("Get random jokes from multiple categories!")
        print("Powered by JokeAPI (https://jokeapi.dev)")
        print("="*70)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*70)
        print("📋 MAIN MENU")
        print("="*70)
        print("1.  Get Random Joke (Any Category)")
        print("2.  Get Joke by Category")
        print("3.  Get Two-Part Joke (Setup + Punchline)")
        print("4.  Get Programming Joke")
        print("5.  Get Dark Humor Joke")
        print("6.  View Available Categories")
        print("7.  View Joke History")
        print("8.  View Favorite Jokes")
        print("9.  Clear Favorites")
        print("10. Exit")
        print("="*70)
    
    def display_categories(self):
        """Display available joke categories"""
        categories = self.api.get_available_types()
        
        print("\n" + "="*70)
        print("📂 AVAILABLE JOKE CATEGORIES")
        print("="*70)
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        print("="*70)
    
    def get_random_joke(self):
        """Get and display a random joke"""
        print("\n⏳ Fetching a joke for you...")
        joke_data = self.api.get_random_joke()
        
        if joke_data:
            self._display_and_save_joke(joke_data)
        else:
            print("❌ Failed to fetch joke. Please try again.")
    
    def get_joke_by_category(self):
        """Get joke from specific category"""
        self.display_categories()
        
        try:
            choice = int(input("\nEnter category number (1-7): ").strip())
            categories = self.api.get_available_types()
            
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                print(f"\n⏳ Fetching a {category} joke...")
                joke_data = self.api.get_joke_by_type(category)
                
                if joke_data:
                    self._display_and_save_joke(joke_data)
                else:
                    print(f"❌ Failed to fetch {category} joke.")
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    def get_two_part_joke(self):
        """Get a two-part joke"""
        print("\n⏳ Fetching a two-part joke for you...")
        joke_data = self.api.get_two_part_joke()
        
        if joke_data:
            self._display_and_save_joke(joke_data)
        else:
            print("❌ Failed to fetch two-part joke.")
    
    def get_programming_joke(self):
        """Get programming joke"""
        print("\n⏳ Fetching a programming joke...")
        joke_data = self.api.get_programming_joke()
        
        if joke_data:
            self._display_and_save_joke(joke_data)
        else:
            print("❌ Failed to fetch programming joke.")
    
    def get_dark_joke(self):
        """Get dark humor joke"""
        print("\n⏳ Fetching a dark humor joke...")
        joke_data = self.api.get_dark_joke()
        
        if joke_data:
            self._display_and_save_joke(joke_data)
        else:
            print("❌ Failed to fetch dark humor joke.")
    
    def _display_and_save_joke(self, joke_data):
        """Display joke and save to history"""
        joke_text = self.api.format_joke(joke_data)
        
        print("\n" + "="*70)
        print("😂 JOKE:")
        print("="*70)
        print(joke_text)
        print("="*70)
        
        # Save to history
        self.joke_history.append({
            "joke": joke_text,
            "type": joke_data.get("type", "unknown"),
            "category": joke_data.get("category", "Unknown"),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Ask if user wants to save to favorites
        save_favorite = input("\n💾 Save to favorites? (y/n): ").strip().lower()
        if save_favorite == 'y':
            self.favorite_jokes.append({
                "joke": joke_text,
                "category": joke_data.get("category", "Unknown"),
                "saved_at": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            print("✅ Joke saved to favorites!")
    
    def view_joke_history(self):
        """View previous jokes"""
        if not self.joke_history:
            print("\n⚠️  No jokes in history yet.")
            return
        
        print("\n" + "="*70)
        print("📜 JOKE HISTORY (Last 10)")
        print("="*70)
        
        # Show last 10 jokes
        for i, joke_record in enumerate(self.joke_history[-10:], 1):
            print(f"\n{i}. [{joke_record['timestamp']}] {joke_record['category']}")
            print(f"   {joke_record['joke'][:50]}...")
        
        print("\n" + "="*70)
    
    def view_favorite_jokes(self):
        """View favorite jokes"""
        if not self.favorite_jokes:
            print("\n⚠️  No favorite jokes yet.")
            return
        
        print("\n" + "="*70)
        print("⭐ FAVORITE JOKES")
        print("="*70)
        
        for i, joke_record in enumerate(self.favorite_jokes, 1):
            print(f"\n{i}. [{joke_record['category']}] - Saved: {joke_record['saved_at']}")
            print(f"   {joke_record['joke']}")
        
        print("\n" + "="*70)
    
    def clear_favorites(self):
        """Clear all favorite jokes"""
        if not self.favorite_jokes:
            print("\n⚠️  No favorite jokes to clear.")
            return
        
        confirm = input(f"\n⚠️  Clear {len(self.favorite_jokes)} favorite jokes? (yes/no): ").strip().lower()
        if confirm == 'yes':
            self.favorite_jokes = []
            print("✅ Favorites cleared!")
        else:
            print("❌ Cancelled.")
    
    def run(self):
        """Run the joke generator"""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = input("\nChoose an option (1-10): ").strip()
            
            if choice == "1":
                self.get_random_joke()
            elif choice == "2":
                self.get_joke_by_category()
            elif choice == "3":
                self.get_two_part_joke()
            elif choice == "4":
                self.get_programming_joke()
            elif choice == "5":
                self.get_dark_joke()
            elif choice == "6":
                self.display_categories()
            elif choice == "7":
                self.view_joke_history()
            elif choice == "8":
                self.view_favorite_jokes()
            elif choice == "9":
                self.clear_favorites()
            elif choice == "10":
                print("\n👋 Thanks for laughing with us! Goodbye! 😂")
                break
            else:
                print("\n❌ Invalid option. Please choose 1-10.")

def main():
    """Entry point"""
    generator = JokeGenerator()
    generator.run()

if __name__ == "__main__":
    main()
