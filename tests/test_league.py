from pywsl import get_league_table

def test_get_league_table():
    df = get_league_table()
    assert not df.empty, "League table should not be empty"
    assert "Team" in df.columns, "Expected 'Team' column in league table"