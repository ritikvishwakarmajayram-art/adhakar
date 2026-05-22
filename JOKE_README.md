# Joke Generator

A fun interactive joke generator that fetches random jokes from an external API!

## Features

### Core Features
- **Random Jokes**: Get jokes from any category
- **Category-Based Jokes**: Choose from 7 different categories
- **Two-Part Jokes**: Get setup + punchline jokes
- **Programming Jokes**: Programmer-specific humor
- **Dark Humor**: Dark jokes for mature audiences
- **Joke History**: Track all jokes you've seen
- **Favorites**: Save your favorite jokes
- **No API Key Required**: Uses free JokeAPI

### Joke Categories
1. **Any** - Random from all categories
2. **General** - General humor
3. **Knock-Knock** - Classic knock-knock jokes
4. **Programming** - Tech and programmer jokes
5. **Dark** - Dark humor
6. **Spooky** - Spooky jokes
7. **Christmas** - Holiday jokes

## Installation

### Requirements
```
python 3.7+
requests
```

### Setup
```bash
pip install requests
```

## Usage

### Run the Joke Generator
```bash
python joke_generator.py
```

### Menu Options
1. **Get Random Joke** - Random joke from any category
2. **Get Joke by Category** - Choose a specific category
3. **Get Two-Part Joke** - Setup and punchline format
4. **Get Programming Joke** - Tech jokes
5. **Get Dark Humor Joke** - Dark jokes
6. **View Available Categories** - See all categories
7. **View Joke History** - See last 10 jokes
8. **View Favorite Jokes** - See saved favorites
9. **Clear Favorites** - Remove all favorites
10. **Exit** - Close application

## API Details

### JokeAPI
- **Base URL**: https://v2.jokeapi.dev/joke
- **Features**:
  - Free to use (no API key required)
  - Multiple joke categories
  - Single and two-part jokes
  - JSON response format
  - Worldwide coverage

## Example Output

```
😂 JOKE:
======================================================================
Why do programmers prefer dark mode?

Because light attracts bugs! 🐛
======================================================================

💾 Save to favorites? (y/n): y
✅ Joke saved to favorites!
```

## File Structure

```
├── joke_api.py           # API client module
├── joke_generator.py     # Main application
└── JOKE_README.md        # Documentation
```

## Features In Detail

### Get Random Joke
Fetch a completely random joke from any category

### Category Selection
Choose from 7 different joke types:
- General humor
- Knock-knock jokes
- Programming jokes
- Dark humor
- Spooky jokes
- Christmas jokes
- Any/All categories

### Two-Part Jokes
Get jokes with a setup and separate delivery for better comedic timing

### Joke History
Automatically tracks the last 10 jokes you've seen with:
- Timestamp
- Category
- Joke text

### Favorites System
Save your favorite jokes with:
- Category information
- Saved timestamp
- Full joke text
- Easy viewing and management

## Example Usage

```python
from joke_api import JokeAPI

# Create API client
api = JokeAPI()

# Get random joke
joke = api.get_random_joke()
print(api.format_joke(joke))

# Get programming joke
prog_joke = api.get_programming_joke()
print(api.format_joke(prog_joke))

# Get two-part joke
two_part = api.get_two_part_joke()
print(api.format_joke(two_part))
```

## Troubleshooting

### No internet connection
- Check your network connection
- Verify API endpoint is accessible

### No jokes returned
- Try a different category
- Check your internet connection
- API might be temporarily unavailable

### Empty history
- History starts empty
- Jokes are added as you fetch them

## Future Enhancements

- [ ] Joke search/filter
- [ ] Export jokes to file
- [ ] Share jokes on social media
- [ ] Rate jokes (funny/not funny)
- [ ] Persistent favorite storage
- [ ] Joke statistics/analytics
- [ ] Random joke of the day
- [ ] Multi-language support
- [ ] Joke ratings from community
- [ ] Offline joke cache

## License

Open source - Feel free to use and modify!

**Created by**: ritikvishwakarmajayram-art

---

**Have fun laughing! 😂**
