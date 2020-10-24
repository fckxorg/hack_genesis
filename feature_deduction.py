from typing import Tuple
from user_types import UserData
import user_types as ut

# Risk level
LOW_RISK = 0
HIGH_RISK = 1

# Assets
SHARES = 0
BONDS = 1
STRUCTURED = 2

# Investment term
SHORT = 0
MEDIUM = 1
LONG = 2


def deduce_risk_level(user: UserData) -> int:
    if user.age == ut.RETIRED:
        return LOW_RISK
    elif user.age == ut.EASY_MONEY:
        return HIGH_RISK
    else:
        if user.family == ut.MARRIED:
            return LOW_RISK
        else:
            return HIGH_RISK


def deduce_investment_range(user: UserData) -> int:
    return 0


def deduce_investment_term(user: UserData) -> int:
    if user.age == ut.YOUNG:
        return MEDIUM
    elif user.age == ut.EASY_MONEY:
        return SHORT
    elif user.age == ut.MIDDLE_AGED:
        if user.income == ut.INC_130:
            return SHORT
        else:
            return LONG
    else:  # user.age == ut.RETIRED
        return LONG


def deduce_assets(user: UserData) -> Tuple[int, int]:
    return (0, 1)
