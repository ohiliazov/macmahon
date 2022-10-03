from enum import Enum

GRADE_RANK_MAP = {
    "30k": -30,
    "29k": -29,
    "28k": -28,
    "27k": -27,
    "26k": -26,
    "25k": -25,
    "24k": -24,
    "23k": -23,
    "22k": -22,
    "21k": -21,
    "20k": -20,
    "19k": -19,
    "18k": -18,
    "17k": -17,
    "16k": -16,
    "15k": -15,
    "14k": -14,
    "13k": -13,
    "12k": -12,
    "11k": -11,
    "10k": -10,
    "9k": -9,
    "8k": -8,
    "7k": -7,
    "6k": -6,
    "5k": -5,
    "4k": -4,
    "3k": -3,
    "2k": -2,
    "1k": -1,
    "1d": 0,
    "2d": 1,
    "3d": 2,
    "4d": 3,
    "5d": 4,
    "6d": 5,
    "7d": 6,
    "1p": 6,
    "2p": 6,
    "3p": 6,
    "8d": 7,
    "4p": 7,
    "5p": 7,
    "6p": 7,
    "9d": 8,
    "7p": 8,
    "8p": 8,
    "9p": 8,
}


class GameResult(str, Enum):
    UNKNOWN = "unknown"
    WHITE_WINS = "white_wins"
    BLACK_WINS = "black_wins"
    DRAW = "draw"


class PairingMode(str, Enum):
    """
    If set to CROSS the first player will be seeded with middle.
    If set to FOLD the first player will be seeded with last.
    If set to ADJACENT the first player will be seeded with second, third with fourth etc.
    """

    CROSS = "cross"
    FOLD = "fold"
    ADJACENT = "adjacent"


class DrawUpDownMode(str, Enum):
    """
    If set to TOP the first player will be prioritised to be drawn up/down.
    If set to MIDDLE the middle player will be prioritised to drawn up/down.
    If set to BOTTOM the last player will be prioritised to drawn up/down.
    """

    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
