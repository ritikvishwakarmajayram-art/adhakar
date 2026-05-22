from weather_api import WeatherAPI
from datetime import datetime
from typing import Dict, Optional
import json

class WeatherDashboard:
    """Weather Dashboard for displaying weather information"""
    
    def __init__(self):
        self.api = WeatherAPI()
        self.current_location = None
        self.current_weather = None
    
    def search_location(self, city: str) -> bool:
        """Search for a location and fetch weather data"""
        print(f"\n🔍 Searching for '{city}'...")
        coords = self.api.get_coordinates(city)
        
        if not coords:
            print(f"❌ Could not find city: {city}")
            return False
        
        self.current_location = coords
        weather_data = self.api.get_weather(coords["latitude"], coords["longitude"])
        
        if not weather_data:
            print("❌ Could not fetch weather data")
            return False
        
        self.current_weather = weather_data
        return True
    
    def display_current_weather(self):
        """Display current weather conditions"""
        if not self.current_location or not self.current_weather:
            print("\n⚠️  No weather data available. Search for a location first.")
            return
        
        loc = self.current_location
        current = self.current_weather["current"]
        
        print("\n" + "="*60)
        print(f"📍 {loc['name']}, {loc['country']}")
        print("="*60)
        
        temp = current["temperature_2m"]
        feels_like = current["apparent_temperature"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        precipitation = current["precipitation"]
        weather_code = current["weather_code"]
        
        description = self.api.get_weather_description(weather_code)
        emoji = self.api.get_weather_emoji(weather_code)
        
        print(f"\n{emoji} {description}")
        print(f"\n🌡️  Temperature: {temp}°C")
        print(f"🤔 Feels Like: {feels_like}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} km/h")
        print(f"🌧️  Precipitation: {precipitation} mm")
    
    def display_hourly_forecast(self, hours: int = 24):
        """Display hourly forecast"""
        if not self.current_weather:
            print("\n⚠️  No weather data available.")
            return
        
        hourly = self.current_weather["hourly"]
        times = hourly["time"][:hours]
        temps = hourly["temperature_2m"][:hours]
        precip = hourly["precipitation"][:hours]
        
        print("\n" + "="*60)
        print("⏰ HOURLY FORECAST (Next 24 Hours)")
        print("="*60)
        print(f"{'Time':<12} {'Temperature':<15} {'Precipitation':<15}")
        print("-"*60)
        
        for i, (time, temp, rain) in enumerate(zip(times, temps, precip)):
            hour = time.split("T")[1][:5]
            print(f"{hour:<12} {temp:>6}°C          {rain:>6} mm")
    
    def display_daily_forecast(self):
        """Display 7-day forecast"""
        if not self.current_weather:
            print("\n⚠️  No weather data available.")
            return
        
        daily = self.current_weather["daily"]
        dates = daily["time"]
        max_temps = daily["temperature_2m_max"]
        min_temps = daily["temperature_2m_min"]
        precip = daily["precipitation_sum"]
        codes = daily["weather_code"]
        
        print("\n" + "="*80)
        print("📅 7-DAY FORECAST")
        print("="*80)
        print(f"{'Date':<12} {'Condition':<20} {'Max':<8} {'Min':<8} {'Precip':<10}")
        print("-"*80)
        
        for date, max_t, min_t, rain, code in zip(dates, max_temps, min_temps, precip, codes):
            emoji = self.api.get_weather_emoji(code)
            description = self.api.get_weather_description(code)
            print(f"{date:<12} {emoji} {description:<16} {max_t:>5}°C   {min_t:>5}°C   {rain:>6} mm")
    
    def display_weather_alerts(self):
        """Display weather alerts"""
        print("\n" + "="*60)
        print("⚠️  WEATHER ALERTS")
        print("="*60)
        print("No alerts available for this location.")
    
    def save_weather_data(self, filename: str = "weather_data.json"):
        """Save current weather data to JSON file"""
        if not self.current_weather or not self.current_location:
            print("❌ No weather data to save.")
            return
        
        data = {
            "location": self.current_location,
            "weather": self.current_weather,
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            print(f"\n✅ Weather data saved to {filename}")
        except Exception as e:
            print(f"\n❌ Error saving weather data: {e}")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("🌤️  WEATHER DASHBOARD")
        print("="*60)
        print("1. Search for a city")
        print("2. Display current weather")
        print("3. Show hourly forecast (24h)")
        print("4. Show 7-day forecast")
        print("5. Weather alerts")
        print("6. Save weather data")
        print("7. Exit")
        print("="*60)
    
    def run(self):
        """Run the weather dashboard"""
        print("\n🌍 Welcome to Weather Dashboard!")
        print("Powered by Open-Meteo API (No API key required)")
        
        while True:
            self.display_menu()
            choice = input("\nChoose an option (1-7): ").strip()
            
            if choice == "1":
                city = input("\nEnter city name: ").strip()
                if city:
                    if self.search_location(city):
                        print(f"\n✅ Found {self.current_location['name']}, {self.current_location['country']}")
                    else:
                        print("❌ Failed to find the city")
            
            elif choice == "2":
                self.display_current_weather()
            
            elif choice == "3":
                self.display_hourly_forecast()
            
            elif choice == "4":
                self.display_daily_forecast()
            
            elif choice == "5":
                self.display_weather_alerts()
            
            elif choice == "6":
                self.save_weather_data()
            
            elif choice == "7":
                print("\n👋 Thank you for using Weather Dashboard!")
                break
            
            else:
                print("\n❌ Invalid option. Please choose 1-7.")

def main():
    """Entry point"""
    dashboard = WeatherDashboard()
    dashboard.run()

if __name__ == "__main__":
    main()
