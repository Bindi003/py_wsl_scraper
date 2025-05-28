# Tests to make sure get_squad_valuations() returns expected structure
from pywsl import get_squad_valuations

def test_get_squad_valuations():
    df = get_squad_valuations()
    assert not df.empty, "Squad valuations DataFrame should not be empty"

    expected_columns = [
        "Club", "Squad Size", "Avg Age", "Market Value (€)",
        "Avg Value/Player (€)", "Market Value (GBP)", "Avg Value/Player (GBP)"
    ]
    for col in expected_columns:
        assert col in df.columns, f"Missing expected column: {col}"

def test_value_formatting():
    df = get_squad_valuations()
    # Check currency formatting
    assert df["Market Value (GBP)"].str.startswith("£").all(), "Market Value (GBP) should start with £"
    assert df["Avg Value/Player (GBP)"].str.startswith("£").all(), "Avg Value/Player (GBP) should start with £"