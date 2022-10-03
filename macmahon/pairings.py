import networkx as nx
from typing import Set

from macmahon.game import Game
from macmahon.player import Player


class Pairings:
    def __init__(self, players: Set[Player], games: Set[Game], parameters):
        self.players = players
        self.games = games

    def run(self) -> Set[Game]:
        graph = nx.Graph()
        print(graph)
        for i, player1 in self.players:
            print(i, player1)

        games = set()
        return games
