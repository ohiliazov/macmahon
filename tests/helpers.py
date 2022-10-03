import uuid
import faker
from macmahon.constants import GRADE_RANK_MAP
from macmahon.player import Player

fake = faker.Faker()


def generate_player_id() -> str:
    return str(uuid.uuid4())


def generate_first_name() -> str:
    return fake.first_name()


def generate_last_name() -> str:
    return fake.last_name()


def generate_rating() -> int:
    return fake.random_int(100, 2900)


def generate_grade() -> str:
    return fake.random_element(list(GRADE_RANK_MAP))


def generate_country() -> str:
    return fake.country_code()


def generate_club() -> str:
    return fake.city()


def generate_player(player_id: str = None, start_mm_score_x2: int = 0) -> Player:
    if player_id is None:
        player_id = generate_player_id()
    return Player(
        player_id=player_id,
        first_name=generate_first_name(),
        last_name=generate_last_name(),
        country=generate_country(),
        club=generate_club(),
        rating=generate_rating(),
        start_mm_score_x2=start_mm_score_x2,
    )
