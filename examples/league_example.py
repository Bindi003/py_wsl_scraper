from pywsl.league import get_league_table
from pywsl.display import display_table

df = get_league_table()
display_table(df)
