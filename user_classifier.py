import feature_deduction as fd
from user_types import UserData, IntermediateRepresentation


def get_intermediate_representation(user: UserData) -> IntermediateRepresentation:
    risk_level = fd.deduce_risk_level(user)
    assets = fd.deduce_assets(user)
    investment_term = fd.deduce_investment_term(user)
    account_type = fd.deduce_account_type(user)

    return IntermediateRepresentation(risk_level, assets, user.income, investment_term, account_type, user.source, user.interests)
