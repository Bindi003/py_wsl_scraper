import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_fixtures():
    url = "https://www.soccerdonna.de/en/womens-super-league/spielplangesamt/wettbewerb_ENG1.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="standard_tabelle")
    if not table:
        print("⚠️ Could not find fixtures table.")
        return pd.DataFrame()

    rows = table.find_all("tr")[1:]  # skip header
    fixtures = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        matchday = cols[0].text.strip()
        date = cols[1].text.strip()
        home = cols[2].text.strip()
        away = cols[3].text.strip()
        score = cols[4].text.strip()

        fixtures.append({
            "Matchday": matchday,
            "Date": date,
            "Home Team": home,
            "Away Team": away,
            "Score": score if ":" in score else ""
        })

    return pd.DataFrame(fixtures)
