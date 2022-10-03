from typing import Set

from macmahon.game import Game
from macmahon.player import Player


class Standings:
    def __init__(self, players: Set[Player], games: Set[Game]):
        self.players = {player.player_id: player for player in players}
        self.games = games

    def get_played_games(self, player_id: str) -> Set[Game]:
        return {game for game in self.games if game.has_played(player_id)}

    def points_x2(self, player_id: str) -> int:
        return sum(g.get_points_x2(player_id) for g in self.get_played_games(player_id))

    def score_x2(self, player_id: str) -> int:
        sp = self.players[player_id]
        return sp.start_mm_score_x2 + self.points_x2(player_id)

    def sos_x2(self, player_id: str) -> int:
        return sum(
            self.score_x2(game.get_opponent_id(player_id))
            for game in self.get_played_games(player_id)
        )

    def sodos_x2(self, player_id: str) -> int:
        return sum(
            self.score_x2(game.get_opponent_id(player_id))
            for game in self.get_played_games(player_id)
            if game.get_points_x2(player_id) == 2
        )

    def sosos_x2(self, player_id: str) -> int:
        return sum(
            self.sos_x2(game.get_opponent_id(player_id))
            for game in self.get_played_games(player_id)
        )

    def sort_players_by(self, *keys: str):
        def sort_by_criteria(player: Player):
            return [getattr(self, key)(player.player_id) for key in keys]

        return sorted(self.players.values(), key=sort_by_criteria, reverse=True)
