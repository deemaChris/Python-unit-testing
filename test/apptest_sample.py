from src.appsample import add_entry


def test_add_entry():
    records = add_entry([], "Alice", "alice@inwonder.land", "Alice Wonderland")
    assert records == [{"username": "Alice", "email": "alice@inwonder.land", "displayName": "Alice Wonderland"}]