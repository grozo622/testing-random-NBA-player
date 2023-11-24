from app import random_nba_player


def test_random_nba_player():
    assert "Stephen Curry" or "Lebron James" or "Damian Lillard" in random_nba_player()
