# Weather Dashboard

A comprehensive weather dashboard application that fetches real-time weather data from the **Open-Meteo API** (free, no API key required).

## Features

### Core Features
- **Current Weather**: Real-time temperature, humidity, wind speed, and precipitation
- **Hourly Forecast**: 24-hour weather forecast with temperature and precipitation
- **7-Day Forecast**: Extended forecast with daily highs, lows, and conditions
- **Location Search**: Find any city worldwide and get weather data
- **Weather Descriptions**: Human-readable weather conditions with emojis
- **Data Export**: Save weather data to JSON files

### Advanced Features
- **Favorite Locations**: Save and quickly view favorite cities
- **Weather Comparison**: Compare weather between two cities side-by-side
- **Multiple Location Support**: Track multiple cities at once

## Installation

### Requirements
- python 3.7+
- requests

### Setup
```bash
pip install -r requirements.txt
```

## Usage

### Basic Weather Dashboard
```bash
python weather_dashboard.py
```

### Menu Options
1. **Search for a city** - Enter city name to fetch weather
2. **Display current weather** - Show real-time conditions
3. **Show hourly forecast** - 24-hour forecast view
4. **Show 7-day forecast** - Weekly forecast
5. **Weather alerts** - Display available alerts
6. **Save weather data** - Export to JSON file
7. **Exit** - Close the application

## API Details

### Open-Meteo API
- **Endpoint**: https://api.open-meteo.com/v1/forecast
- **Geocoding**: https://geocoding-api.open-meteo.com/v1/search
- **Features**:
  - Free to use (no API key required)
  - Accurate global weather data
  - Historical and forecast data

## File Structure

```
├── weather_api.py              # API client and weather utilities
├── weather_dashboard.py        # Main dashboard UI
├── advanced_dashboard.py       # Advanced features
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## License

Open source - Feel free to use and modify!

**Created by**: ritikvishwakarmajayram-art
