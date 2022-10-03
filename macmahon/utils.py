from .constants import GRADE_RANK_MAP


def grade_to_rank(grade: str) -> int:
    return GRADE_RANK_MAP[grade]


def rating_to_rank(rating: float) -> int:
    return int(rating // 100 - 21)


def rank_to_grade(rank: int) -> str:
    return f"{-rank}k" if rank < 0 else f"{rank+1}d"


def rank_to_rating(rank: int) -> float:
    return (rank + 21) * 100


def rating_to_grade(rating: float) -> str:
    return rank_to_grade(rating_to_rank(rating))


def grade_to_rating(grade: str) -> float:
    return rank_to_rating(grade_to_rank(grade))
