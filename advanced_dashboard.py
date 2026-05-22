import requests
from weather_api import WeatherAPI
from datetime import datetime

class AdvancedWeatherDashboard:
    """Advanced weather dashboard with additional features"""
    
    def __init__(self):
        self.api = WeatherAPI()
        self.favorites = []
    
    def add_favorite(self, city: str):
        """Add a city to favorites"""
        coords = self.api.get_coordinates(city)
        if coords:
            self.favorites.append({
                "city": coords["name"],
                "country": coords["country"],
                "latitude": coords["latitude"],
                "longitude": coords["longitude"]
            })
            print(f"✅ Added {coords['name']} to favorites")
        else:
            print(f"❌ Could not add {city} to favorites")
    
    def display_favorites(self):
        """Display favorite locations with current weather"""
        if not self.favorites:
            print("\n⚠️  No favorite locations saved.")
            return
        
        print("\n" + "="*80)
        print("⭐ FAVORITE LOCATIONS")
        print("="*80)
        
        for fav in self.favorites:
            weather = self.api.get_weather(fav["latitude"], fav["longitude"])
            if weather:
                temp = weather["current"]["temperature_2m"]
                code = weather["current"]["weather_code"]
                description = self.api.get_weather_description(code)
                emoji = self.api.get_weather_emoji(code)
                print(f"{emoji} {fav['city']}, {fav['country']:<20} {temp:>5}°C  {description}")
    
    def compare_weather(self, city1: str, city2: str):
        """Compare weather between two cities"""
        print(f"\n📊 Comparing weather between {city1} and {city2}...")
        
        coords1 = self.api.get_coordinates(city1)
        coords2 = self.api.get_coordinates(city2)
        
        if not coords1 or not coords2:
            print("❌ Could not find one or both cities")
            return
        
        weather1 = self.api.get_weather(coords1["latitude"], coords1["longitude"])
        weather2 = self.api.get_weather(coords2["latitude"], coords2["longitude"])
        
        if not weather1 or not weather2:
            print("❌ Could not fetch weather data")
            return
        
        print("\n" + "="*80)
        print(f"{'Metric':<30} {city1:<25} {city2:<25}")
        print("="*80)
        
        temp1 = weather1["current"]["temperature_2m"]
        temp2 = weather2["current"]["temperature_2m"]
        print(f"{'Temperature':<30} {temp1:>10}°C           {temp2:>10}°C")
        
        humid1 = weather1["current"]["relative_humidity_2m"]
        humid2 = weather2["current"]["relative_humidity_2m"]
        print(f"{'Humidity':<30} {humid1:>10}%            {humid2:>10}%")
        
        wind1 = weather1["current"]["wind_speed_10m"]
        wind2 = weather2["current"]["wind_speed_10m"]
        print(f"{'Wind Speed':<30} {wind1:>10} km/h        {wind2:>10} km/h")
        
        code1 = weather1["current"]["weather_code"]
        code2 = weather2["current"]["weather_code"]
        desc1 = self.api.get_weather_description(code1)
        desc2 = self.api.get_weather_description(code2)
        print(f"{'Condition':<30} {desc1:<25} {desc2:<25}")
