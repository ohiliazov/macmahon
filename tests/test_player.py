from tests.helpers import generate_player


def test_player():
    p1 = generate_player()
    p2 = generate_player()
    p3 = generate_player()

    assert p1 != p2
    assert p1 != p3
    assert p2 != p3

    p2.player_id = p1.player_id
    assert p1 == p2
    assert p1 != p3
    assert p2 != p3
