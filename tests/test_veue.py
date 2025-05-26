from pywsl import get_venue_attendance

def test_get_venue_attendance_2024():
    df = get_venue_attendance("2024")
    assert not df.empty, "Venue attendance DataFrame should not be empty"
    expected_columns = [
        "Stadium", "Club", "Capacity", "Total Attendance",
        "Avg Attendance", "Matches", "Sold Out", "% Capacity Filled", "Season"
    ]
    for col in expected_columns:
        assert col in df.columns, f"Missing expected column: {col}"