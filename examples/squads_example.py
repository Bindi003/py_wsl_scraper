from pywsl.squads import get_squad_valuations
from pywsl.display import display_table

df = get_squad_valuations()
display_table(df)
