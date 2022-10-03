from .constants import GameResult
from typing import Set

from .exceptions import GameException
from .helpers import black_points_x2, white_points_x2


class Game:
    def __init__(
        self,
        black_player_id: str,
        white_player_id: str,
        round_number: int,
        *,
        handicap: int = 0,
        result: GameResult = GameResult.UNKNOWN,
    ):
        self.black_player_id = black_player_id
        self.white_player_id = white_player_id
        self.round_number = round_number

        self.handicap = handicap
        self.result = result

    def __str__(self):
        return f"{self.round_number}-{self.black_player_id}-{self.white_player_id}"

    def __repr__(self):
        return f"Game({self})"

    @property
    def player_ids(self) -> Set[str]:
        return {self.black_player_id, self.white_player_id}

    def has_played(self, player_id: str) -> bool:
        return player_id in self.player_ids

    def get_opponent_id(self, player_id: str) -> str:
        if player_id == self.black_player_id:
            return self.white_player_id
        if player_id == self.white_player_id:
            return self.black_player_id
        raise GameException(f"Player({player_id}) did not played in the game!")

    def get_points_x2(self, player_id: str) -> int:
        if player_id == self.black_player_id:
            return black_points_x2(self.result)
        if player_id == self.white_player_id:
            return white_points_x2(self.result)
        raise GameException(f"Player({player_id}) did not played in the game!")
