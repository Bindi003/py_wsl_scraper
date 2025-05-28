# uses selenium as this webpage isnt static
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def get_top_scorers(season="2024"):
    url = "https://www.soccerdonna.de/en/womens-super-league/torschuetzen/wettbewerb_ENG1.html"

    # Set up Chrome WebDriver options for headless browsing (no browser window)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        # Wait until the season dropdown is present in the DOM
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "saison_id")))
        # Use JavaScript to set the season value in the dropdown
        driver.execute_script(f"document.querySelector('select[name=saison_id]').value = '{season}';")
        # Submit the form to load data for the selected season
        driver.execute_script("document.querySelector('form[name=saison]').submit();")
        time.sleep(2)

        # Waiting for the table to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "spieler")))
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Finding scorer table
        table = soup.find("table", {"id": "spieler"})
        # Find all rows within the table body (each row represents a player)
        rows = table.find("tbody").find_all("tr")

        data = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 9:
                continue

            # Extracts name and club from the nested table
            nested_table = cols[1].find("table")
            name = nested_table.find_all("tr")[0].get_text(strip=True)
            club_info = nested_table.find_all("tr")[1].get_text(strip=True)
            club = club_info.split(",")[0].strip()

            data.append({
                "Name": name,
                "Club": club,
                "Age": cols[5].text.strip(),
                "Matches": cols[6].text.strip(),
                "Sub On": cols[7].text.strip(),
                "Sub Off": cols[8].text.strip(),
                "Minutes Played": cols[9].text.strip(),
                "Minutes per Goal": cols[10].text.strip(),
                "Goals": cols[11].text.strip()
            })

        driver.quit()
        return pd.DataFrame(data)

    # Incase it fails to scrape scorers
    except Exception as e:
        print(f" Error while scraping top scorers: {e}")
        driver.quit()
        return pd.DataFrame()
