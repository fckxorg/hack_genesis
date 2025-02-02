from . import feature_deduction as fd
from src.user_types import UserData, IntermediateRepresentation, PageSettings
from json import dumps
import src.page_build as pb


def get_intermediate_representation(user: UserData) -> IntermediateRepresentation:
    risk_level = fd.deduce_risk_level(user)
    assets = fd.deduce_assets(user)
    investment_term = fd.deduce_investment_term(user)
    account_type = fd.deduce_account_type(user)

    return IntermediateRepresentation(user.age, user.education, risk_level, assets, user.income, investment_term, account_type, user.source, user.interest)


def get_page_json(user: IntermediateRepresentation) -> str:
    # It's time to get funktional
    arg_getters = [pb.get_motivation, pb.get_investment_descriptions,
                   pb.get_slogan, pb.get_trading_type, pb.get_product_cards]
    args_paths = [f(user) for f in arg_getters]
    args = map(pb.load_asset, args_paths)

    main_picture = pb.get_main_picture(user)
    infographics = pb.get_infographics(user)
    icons = pb.get_icons(user)

    return dumps(PageSettings(*args, user.account_type, icons, main_picture, infographics).__dict__, ensure_ascii=False)
