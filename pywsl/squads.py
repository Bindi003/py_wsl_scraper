import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_squad_valuations():
    url = "https://www.soccerdonna.de/en/womens-super-league/startseite/wettbewerb_ENG1.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    eur_to_gbp = 0.86  # ✅ static exchange rate

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", class_="standard_tabelle")
    if not table:
        print("⚠️ Squad valuation table not found.")
        return pd.DataFrame()

    rows = table.find_all("tr")[1:]
    data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 6:
            continue
        try:
            total_eur = float(cols[4].text.strip().replace(".", "").replace("€", "").replace(",", "."))
            avg_eur = float(cols[5].text.strip().replace(".", "").replace("€", "").replace(",", "."))
            data.append({
                "Club": cols[1].text.strip(),
                "Squad Size": int(cols[2].text.strip()),
                "Avg Age": float(cols[3].text.strip().replace(",", ".")),
                "Market Value (€)": f"{total_eur:,.0f} €",
                "Avg Value/Player (€)": f"{avg_eur:,.0f} €",
                "Market Value (GBP)": f"£{(total_eur * eur_to_gbp):,.0f}",
                "Avg Value/Player (GBP)": f"£{(avg_eur * eur_to_gbp):,.0f}"
            })
        except:
            continue

    return pd.DataFrame(data)
