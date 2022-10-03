import pytest

from macmahon.utils import (
    rating_to_rank,
    rank_to_rating,
    grade_to_rank,
    rank_to_grade,
    rating_to_grade,
    grade_to_rating,
)


@pytest.mark.parametrize(
    "rating,rank",
    [
        (100, -20),
        (200, -19),
        (2050, -1),
        (2100, 0),
        (2900, 8),
    ],
)
def test_rating_to_rank(rating, rank):
    assert rating_to_rank(rating) == rank


@pytest.mark.parametrize(
    "rank,rating",
    [
        (-20, 100),
        (-19, 200),
        (-1, 2000),
        (0, 2100),
        (8, 2900),
    ],
)
def test_rank_to_rating(rank, rating):
    assert rank_to_rating(rank) == rating


@pytest.mark.parametrize(
    "grade,rank",
    [
        ("20k", -20),
        ("19k", -19),
        ("1k", -1),
        ("1d", 0),
        ("9d", 8),
        ("4p", 7),
    ],
)
def test_grade_to_rank(grade, rank):
    assert grade_to_rank(grade) == rank


@pytest.mark.parametrize(
    "rank, grade",
    [
        (-20, "20k"),
        (-19, "19k"),
        (-1, "1k"),
        (0, "1d"),
        (8, "9d"),
    ],
)
def test_rank_to_grade(rank, grade):
    assert rank_to_grade(rank) == grade


@pytest.mark.parametrize(
    "rating,grade",
    [
        (100, "20k"),
        (200, "19k"),
        (2050, "1k"),
        (2100, "1d"),
        (2900, "9d"),
    ],
)
def test_rating_to_grade(rating, grade):
    assert rating_to_grade(rating) == grade


@pytest.mark.parametrize(
    "grade,rating",
    [
        ("20k", 100),
        ("19k", 200),
        ("1k", 2000),
        ("1d", 2100),
        ("9d", 2900),
        ("4p", 2800),
    ],
)
def test_grade_to_rating(grade, rating):
    assert grade_to_rating(grade) == rating
