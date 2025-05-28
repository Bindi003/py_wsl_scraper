import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_league_table():
    url = "https://www.soccerdonna.de/en/womens-super-league/tabelle/wettbewerb_ENG1.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="standard_tabelle")
    rows = table.find_all("tr")[1:]  # skipping header

    data = []
    for row in rows:
        cols = [td.text.strip() for td in row.find_all("td")]
        if len(cols) != 10:  # skipping rows without full data
            continue

        # fomats goal data
        goals = cols[7].split(":")
        goals_for = int(goals[0])
        goals_against = int(goals[1])

        # appends data to team data list
        team_data = {
            "Position": cols[0],
            "Team": cols[2],
            "Matches": int(cols[3]),
            "Wins": int(cols[4]),
            "Draws": int(cols[5]),
            "Losses": int(cols[6]),
            "Goals For": goals_for,
            "Goals Against": goals_against,
            "Goal Difference": int(cols[8]),
            "Points": int(cols[9]),
        }
        data.append(team_data)

    return pd.DataFrame(data)
