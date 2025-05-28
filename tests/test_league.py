# Tests to make sure get_league_table() returns expected structure
from pywsl import get_league_table

def test_get_league_table():
    df = get_league_table()
    assert not df.empty
    assert "Position" in df.columns
    assert "Team" in df.columns
    assert "Matches" in df.columns
    assert "Wins" in df.columns
    assert "Draws" in df.columns
    assert "Losses" in df.columns
    assert "Goals For" in df.columns
    assert "Goals Against" in df.columns
    assert "Goal Difference" in df.columns
    assert "Points" in df.columns