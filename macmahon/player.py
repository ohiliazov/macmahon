from macmahon.utils import rating_to_rank


class Player:
    def __init__(
        self,
        player_id: str,
        first_name: str,
        last_name: str,
        country: str,
        club: str,
        rating: float,
        start_mm_score_x2: int = 0,
    ):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.club = club
        self.rating = rating
        self.rank = rating_to_rank(rating)
        self.start_mm_score_x2 = start_mm_score_x2

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Player({self})"

    def __eq__(self, other: "Player"):
        return self.player_id == other.player_id

    def __hash__(self):
        return hash((self.player_id, self.first_name, self.last_name, self.country))
