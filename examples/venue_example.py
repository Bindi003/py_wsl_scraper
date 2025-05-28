from pywsl.venue import get_venue_attendance
from pywsl.display import display_table

df = get_venue_attendance("2024")
display_table(df)
