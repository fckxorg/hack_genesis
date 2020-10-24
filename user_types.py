from typing import Tuple, List

# Correct values
# Age -- 0 (young), 1 (middle) or 2 (retired)
# Interest -- Whatever
# Source -- whatever
# Education -- whatever
# Income -- whatever

# Age
YOUNG = 0
EASY_MONEY = 1
MIDDLE_AGED = 2
ELDER = 3

# Interests -- whatever

# Family
SINGLE = False
MARRIED = True

# Source
CONTEXT_ADS = False
SEARCH_ENGINE = True

# Education
HIGH = 2
AVERAGE = 1
LOW = 0

# Income
INC_0_20 = 0
INC_20_70 = 1
INC_70_130 = 2
INC_130 = 3


class UserData:
    def __init__(self, age: int, interest: str, source: bool, family: bool, education: int, income: int):
        self.age = age
        self.interest = interest
        self.source = source
        self.family = family
        self.education = education
        self.income = income


class IntermediateRepresentation:
    def __init__(self, age: int, education: int, risk_level: int, assets: Tuple[int, int], income: int, investment_term: int, account_type: int, source: bool, interest: str):
        self.age = age
        self.education = education
        self.risk_level = risk_level
        self.assets = assets
        self.income = income
        self.investment_term = investment_term
        self.account_type = account_type
        self.source = source
        self.interest = interest


class PageSettings:
    def __init__(self, motivation: str, investment_descriptions: Tuple[str, str], slogan: str, trading_type: str):
        self.motivation = motivation
        self.investment_descriptions = investment_descriptions
        self.slogan = slogan
        self.trading_type = trading_type
