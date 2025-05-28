# tests to make sure the get_fixtures does display the following
from pywsl import get_fixtures

def test_get_fixtures():
    df = get_fixtures()
    assert not df.empty
    assert "Date" in df.columns 
    assert "Home Team" in df.columns
    assert "Away Team" in df.columns
    assert "Score" in df.columns