from typing import Tuple
from src.user_types import UserData
import src.user_types as ut
from src.deduction import Deductor

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

# Account type
BROKERAGE = 0
INVEST = 1

deds = {
    'assets': Deductor(),
}

deds['assets'].add_rule((lambda user : user.age == ut.ELDER or user.age == ut.MIDDLE_AGED), (BONDS, STRUCTURED))
deds['assets'].add_rule((lambda user : user.age == ut.YOUNG and user.income == ut.INC_130), (BONDS, STRUCTURED))
deds['assets'].add_rule((lambda user : user.age == ut.YOUNG and user.income == ut.INC_70_130), (BONDS, SHARES))
deds['assets'].set_fallback((SHARES, BONDS))




def deduce_risk_level(user: UserData) -> int:
    if user.age == ut.ELDER:
        return LOW_RISK
    elif user.age == ut.EASY_MONEY:
        return HIGH_RISK
    else:
        if user.family == ut.MARRIED:
            return LOW_RISK
        else:
            return HIGH_RISK


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
    # if user.age == ut.ELDER or user.age == ut.MIDDLE_AGED:
    #     return (BONDS, STRUCTURED)
    # elif user.age == ut.EASY_MONEY:
    #     return (SHARES, BONDS)
    # else:  # user.age == ut.YOUNG
    #     if user.income == ut.INC_130:
    #         return (BONDS, STRUCTURED)
    #     elif user.income == ut.INC_70_130:
    #         return (BONDS, SHARES)
    #     else:
    #         return (SHARES, BONDS)
    return deds['assets'](user)

def deduce_account_type(user: UserData) -> int:
    if user.age == ut.YOUNG:
        if user.income == ut.INC_70_130 or user.income == ut.INC_130:
            return INVEST
        else:
            return BROKERAGE
    elif user.age == ut.EASY_MONEY:
        return BROKERAGE
    else:
        return INVEST
