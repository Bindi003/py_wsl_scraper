from pywsl import get_fixtures

def test_get_fixtures():
    df = get_fixtures()
    assert not df.empty
    assert "Date" in df.columns 