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
RETIRED = 3

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
    def __init__(self, age: int, interests: List[str], source: bool, family: bool, education: int, income: int):
        self.age = age
        self.interests = interests
        self.source = source
        self.family = family
        self.education = education
        self.income = income

class IntermediateRepresentation:
    def __init__(self, risk_level: int, assets: List[str], investment_range: int, investment_term: int, source: bool, interests: Tuple[int, int]):
        self.risk_level = risk_level
        self.assets = assets
        self.investment_range = investment_range
        self.investment_term = investment_term
        self.source = source
        self.interests = interests

        pass