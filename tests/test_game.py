import pytest

from macmahon.constants import GameResult
from macmahon.exceptions import GameException
from macmahon.game import Game


def test_game():
    game = Game(
        "player1",
        "player2",
        0,
        handicap=3,
        result=GameResult.WHITE_WINS,
    )
    assert game.player_ids == {"player1", "player2"}

    assert game.has_played("player1")
    assert game.has_played("player2")
    assert not game.has_played("player3")

    assert game.get_opponent_id("player1") == "player2"
    assert game.get_opponent_id("player2") == "player1"

    with pytest.raises(GameException):
        game.get_opponent_id("player3")
