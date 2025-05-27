# py_wsl_scraper

[![PyPI version](https://img.shields.io/pypi/v/py-wsl-scraper.svg)](https://pypi.org/project/py-wsl-scraper/)

<p align="center">
  <img src="images/pywsl-banner.jpg" alt="py-wsl-scraper logo" width="300"/>
</p>

**py_wsl_scraper** is a Python package for scraping Women's Super League (WSL) football data. It provides tools to retrieve league tables, fixtures, top scorers, squad market valuations, and venue attendances.

## Why This Matters

While there are several Python packages for scraping football data, most are focused exclusively on men's leagues. Access to structured, reliable data for women's football is still limited and fragmented.

**py-wsl-scraper** helps fill this gap by targeting the [Women's Super League (WSL)](https://www.soccerdonna.de/) using Soccerdonna — a specialist data source affiliated with Transfermarkt that provides deeper coverage of the women’s game.

This package supports researchers, analysts, and developers who want to build inclusive tools, run analysis, and advocate for visibility and representation in football data.

## Installation


Install via pip:

```bash
pip install py-wsl-scraper
```

Alternatively, clone and install manually:

```bash
git clone https://github.com/yourusername/pywsl.git
cd pywsl
pip install -r requirements.txt

```


## Usage

```python
from pywsl import (
    get_league_table,
    get_fixtures,
    get_top_scorers,
    get_squad_valuations,
    get_venue_attendance
)

# League table
league_df = get_league_table()

# Fixtures
fixtures_df = get_fixtures()

# Top scorers for a season
scorers_df = get_top_scorers("2024")

# Squad market values
squads_df = get_squad_valuations()

# Venue attendance
venues_df = get_venue_attendance("2024")

```

## Modules 

- `league.py` – Scrapes the current league table.
- `fixtures.py` – Scrapes upcoming and past match fixtures.
- `scorers.py` – Scrapes top goal scorers by season.
- `squads.py` – Scrapes squad size, average age, and market values.
- `venues.py` – Scrapes venue data including capacity and attendance.



## Dependencies
- ```pandas```
- ```requests```
- ```beautifulsoup4```
- ```selenium```
- ```webdriver-manager```


## License
MIT License