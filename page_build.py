from typing import Tuple
import typing
import user_types as ut
import feature_deduction as fd
from user_types import IntermediateRepresentation


@typing.overload
def load_asset(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()

    except FileNotFoundError:
        print("Unable to load asset file", path)

    except PermissionError:
        print("Do not have permission to open file", path)

    return str()


@typing.overload
def load_asset(paths: Tuple[str, str]) -> Tuple[str, str]:
    return (load_asset(paths[0]), load_asset(paths[1]))


def get_age_dependent_path(user: IntermediateRepresentation, folder: str) -> str:
    if user.age == ut.YOUNG:
        return "assets/" + folder + "/young.txt"
    elif user.age == ut.EASY_MONEY:
        return "assets/" + folder + "/easy_money_seekers.txt"
    elif user.age == ut.MIDDLE_AGED:
        return "assets/" + folder + "/middle-aged.txt"
    elif user.age == ut.ELDER:
        return "assets/" + folder + "/elder.txt"


def get_investment_description_path(asset_type: int, knowledge: int):
    path = "assets/investment_descriptions/"

    if knowledge == ut.HIGH:
        path += "good_education_"
    else:
        path += "poor_education_"

    if asset_type == fd.BONDS:
        return path + "obligations.txt"
    elif asset_type == fd.SHARES:
        return path + "shares.txt"
    else:
        return path + "structural_products.txt"


def get_investment_descriptions(user: IntermediateRepresentation) -> Tuple[str, str]:
    return (get_investment_description_path(user.assets[0], user.knowledge), get_investment_description_path(user.assets[1], user.knowledge))


def get_motivation(user: IntermediateRepresentation) -> str:
    return get_age_dependent_path(user, "motivation")


def get_slogan(user: IntermediateRepresentation) -> str:
    return get_age_dependent_path(user, "slogan")


def get_trading_type(user: IntermediateRepresentation) -> str:
    if user.account_type == fd.INVEST:
        return "assets/trading_types/iia.txt"
    elif user.account_type == fd.BROKERAGE:
        return "assets/trading_types/broker.txt"
