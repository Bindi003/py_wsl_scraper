from pywsl.scorers import get_top_scorers
from pywsl.display import display_table

df = get_top_scorers("2024")
display_table(df)
