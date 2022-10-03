from macmahon.constants import GameResult
from macmahon.game import Game
from macmahon.standings import Standings
from tests.helpers import generate_player


def test_standings():
    player1 = generate_player(player_id="player1", start_mm_score_x2=6)
    player2 = generate_player(player_id="player2", start_mm_score_x2=6)
    player3 = generate_player(player_id="player3", start_mm_score_x2=4)
    player4 = generate_player(player_id="player4", start_mm_score_x2=4)

    games = {
        Game(
            black_player_id="player1",
            white_player_id="player2",
            round_number=0,
            result=GameResult.BLACK_WINS,
        ),
        Game(
            black_player_id="player3",
            white_player_id="player4",
            round_number=0,
            result=GameResult.WHITE_WINS,
        ),
        Game(
            black_player_id="player1",
            white_player_id="player3",
            round_number=1,
            result=GameResult.BLACK_WINS,
        ),
        Game(
            black_player_id="player2",
            white_player_id="player4",
            round_number=1,
            result=GameResult.WHITE_WINS,
        ),
        Game(
            black_player_id="player1",
            white_player_id="player4",
            round_number=2,
            result=GameResult.BLACK_WINS,
        ),
        Game(
            black_player_id="player2",
            white_player_id="player3",
            round_number=2,
            result=GameResult.WHITE_WINS,
        ),
    }

    standings = Standings(
        players={player1, player2, player3, player4},
        games=games,
    )
    assert standings.points_x2("player1") == 6
    assert standings.points_x2("player2") == 0
    assert standings.points_x2("player3") == 2
    assert standings.points_x2("player4") == 4

    assert standings.score_x2("player1") == 12
    assert standings.score_x2("player2") == 6
    assert standings.score_x2("player3") == 6
    assert standings.score_x2("player4") == 8

    assert standings.sos_x2("player1") == 20
    assert standings.sos_x2("player2") == 26
    assert standings.sos_x2("player3") == 26
    assert standings.sos_x2("player4") == 24

    assert standings.sodos_x2("player1") == 20
    assert standings.sodos_x2("player2") == 0
    assert standings.sodos_x2("player3") == 6
    assert standings.sodos_x2("player4") == 12

    assert standings.sosos_x2("player1") == 76
    assert standings.sosos_x2("player2") == 70
    assert standings.sosos_x2("player3") == 70
    assert standings.sosos_x2("player4") == 72

    sorted_players = standings.sort_players_by("score_x2", "sos_x2", "sodos_x2")
    assert sorted_players == [player1, player4, player3, player2]
