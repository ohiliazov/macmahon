from pydantic import BaseModel, conint, root_validator
from .constants import PairingMode, DrawUpDownMode


class McMahonSettings(BaseModel):
    """
    If lower_mm_bar is set to -20 all players from 30k to 20k will start with 0 McMahon group
    If upper_mm_bar is set to 0 all players from 1d to 9p will start in the same McMahon group

    mm_dense defines the presence of gaps between McMahon groups.
        If mm_dense set to True, there is only one point gap between each McMahon group
        If mm_dense set to False, McMahon group difference is equal to rank difference between players
    """

    lower_mm_bar: conint(ge=-20, le=8) = -20
    upper_mm_bar: conint(ge=-20, le=8) = 8
    mm_dense: bool = True

    @root_validator
    def assert_mm_bars(cls, values: dict):
        assert values["lower_mm_bar"] <= values["upper_mm_bar"]


class HandicapSettings(BaseModel):
    """
    handicap_bar defines the rank, above which handicap is not used.
    Example:
        player 1 has rank of 3d
        player 2 has rank of 5k
        handicap_bar is set to 0 [equal to 1d]
        Then the handicap will be 5 instead of 7

    handicap_correction defines the amount of handicap deduction
    Example:
        player 1 has rank of 3d
        player 2 has rank of 5k
        handicap_correction is set to -3
        Then the handicap will be 4 instead of 7

    handicap_max defines the maximum handicap
    Example:
        player 1 has rank of 3d
        player 2 has rank of 5k
        handicap_max is set to 3
        Then the handicap will be 3 instead of 7

    The rules order: handicap_bar -> handicap_correction -> handicap_max
    """

    handicap_bar: conint(ge=-20, le=8) = 8
    handicap_correction: conint(ge=-9, le=9) = 0
    handicap_max: conint(ge=0, le=9) = 0


class SeedingSettings(BaseModel):
    pairing_mode: PairingMode = "cross"
    draw_up_mode: DrawUpDownMode = "middle"
    draw_down_mode: DrawUpDownMode = "middle"
