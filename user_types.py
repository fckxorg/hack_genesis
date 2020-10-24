from typing import Tuple, List

class UserData:
    def __init__(self, age: int, interests: List[str], source: bool, education: int, income: int):
        self.age = age
        self.interests = interests
        self.source = source
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