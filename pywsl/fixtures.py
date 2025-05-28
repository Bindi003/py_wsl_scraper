import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_fixtures():
    url = "https://www.soccerdonna.de/en/womens-super-league/spielplangesamt/wettbewerb_ENG1.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    fixtures = []

    # Find *all* tables inside divs with class 'fl' or 'fr'
    matchday_divs = soup.find_all("div", class_=["fl", "fr"])
    
    for div in matchday_divs:
        table = div.find("table", class_="standard_tabelle")
        if not table:
            continue

        # Get matchday number from the first header cell
        header_row = table.find("tr")
        matchday_text = header_row.find("th").text.strip() if header_row else ""
        matchday = matchday_text.split(".")[0] if "." in matchday_text else "?"

        rows = table.find_all("tr")[1:]  # skip header row
        for row in rows:
            cols = row.find_all("td")
            if len(cols) != 5:
                continue

            date = cols[0].text.strip().split(" - ")[0]
            home = cols[1].text.strip()
            score = cols[2].text.strip()
            away = cols[3].text.strip()

            fixtures.append({
                "Matchday": matchday,
                "Date": date,
                "Home Team": home,
                "Away Team": away,
                "Score": score if ":" in score else ""
            })

    return pd.DataFrame(fixtures)
