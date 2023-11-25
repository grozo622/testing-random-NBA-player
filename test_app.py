from app import random_nba_player, get_player_info

def test_random_nba_player():
    players = ["Stephen Curry", "Lebron James", "Damian Lillard"]
    result = random_nba_player()
    assert result in players

def test_get_player_info():
    # You may need to customize this test based on the actual behavior of get_player_info
    player_name = "Stephen Curry"
    player_image, player_stats = get_player_info(player_name)
    assert player_image is not None
    assert player_stats is not None
