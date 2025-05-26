from pywsl import get_top_scorers

def test_get_top_scorers_2024():
    df = get_top_scorers("2024")
    assert not df.empty, "Top scorers DataFrame should not be empty"
    expected_columns = [
        "Name", "Club", "Age", "Matches", "Sub On", "Sub Off",
        "Minutes Played", "Minutes per Goal", "Goals"
    ]
    for col in expected_columns:
        assert col in df.columns, f"Expected column '{col}' in top scorers DataFrame"