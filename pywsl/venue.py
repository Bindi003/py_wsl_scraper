import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_venue_attendance(season: str = "2024"):
    url = "https://www.soccerdonna.de/en/womens-super-league/besucherzahlen/wettbewerb_ENG1.html"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "saison_id": season
    }

    response = requests.post(url, data=data, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"id": "spieler"})

    if not table:
        print("⚠️ Could not find venue table.")
        return pd.DataFrame()

    rows = table.find_all("tr")[1:]
    data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 8:
            club_info = cols[1].get_text(separator="|", strip=True).split("|")
            stadium = club_info[0]
            club = club_info[1]

        
            try:
                data.append({
                    "Club": club,
                    "Stadium": stadium,
                    "Capacity": int(cols[2].text.strip().replace(".", "").replace(",", "")),
                    "Total Attendance": int(cols[3].text.strip().replace(".", "").replace(",", "")),
                    "Avg Attendance": int(cols[4].text.strip().replace(".", "").replace(",", "")),
                    "Matches": int(cols[5].text.strip()),
                    "Sold Out": int(cols[6].text.strip()),
                    "% Capacity Filled": cols[7].text.strip()
                })
            except:
                continue

    df = pd.DataFrame(data)
    df["Season"] = season
    return df

