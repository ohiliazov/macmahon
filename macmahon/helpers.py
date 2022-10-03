from macmahon.constants import GameResult


def black_points_x2(result: GameResult):
    if result is result.BLACK_WINS:
        return 2
    if result is result.DRAW:
        return 1
    return 0


def white_points_x2(result: GameResult):
    if result is result.WHITE_WINS:
        return 2
    if result is result.DRAW:
        return 1
    return 0
