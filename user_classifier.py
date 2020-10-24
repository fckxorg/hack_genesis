# Class for input data

class UserData:
    def __init__(self, age: int, interests: list, source: bool, education: int, income: int):
        self.age = age
        self.interests = interests
        self.source = source
        self.education = education
        self.income = income

class IntermediateRepresentation:
    def __init__(self):
        pass

def get_intermediate_representation(user: UserData):
    pass 
 