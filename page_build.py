from typing import Tuple
import typing
import user_types as ut
import feature_deduction as fd
import glob
import random
from user_types import IntermediateRepresentation


def load_asset_by_path(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()

    except FileNotFoundError:
        print("Unable to load asset file", path)

    except PermissionError:
        print("Do not have permission to open file", path)

    return str()


def load_asset(path):
    if type(path) is str:
        return load_asset_by_path(path)
    elif type(path) is tuple:
        return tuple(map(load_asset_by_path, path))


def get_age_dependent_path(user: IntermediateRepresentation, folder: str) -> str:
    if user.age == ut.YOUNG:
        return "assets/" + folder + "/young.txt"
    elif user.age == ut.EASY_MONEY:
        return "assets/" + folder + "/easy_money_seekers.txt"
    elif user.age == ut.MIDDLE_AGED:
        return "assets/" + folder + "/middle-aged.txt"
    elif user.age == ut.ELDER:
        return "assets/" + folder + "/elder.txt"


def get_investment_description_path(asset_type: int, education: int):
    path = "assets/investments_descriptions/"

    if education == ut.HIGH:
        path += "good_education_"
    else:
        path += "poor_education_"

    return path + product_category_to_name(asset_type) + ".txt"


def product_category_to_name(product_class: int) -> str:
    if product_class == fd.SHARES:
        return "shares"
    elif product_class == fd.STRUCTURED:
        return "structural_products"
    elif product_class == fd.BONDS:
        return "obligations"


def get_product_from_category(user: IntermediateRepresentation, category: int) -> str:
    products = glob.glob("assets/cards/info/" +
                         product_category_to_name(category) + "/*.json")

    # Rather sophisticated data science algorithm
    return random.choice(products)


def get_product_cards(user: IntermediateRepresentation) -> Tuple[str, str, str]:
    leftover_category = (set((fd.BONDS, fd.STRUCTURED, fd.SHARES)) - set(user.assets))[0] 
    cat_args = (user.assets[0], user.assets[1], leftover_category)

    return tuple([get_product_from_category(x, user) for x in cat_args])


def get_investment_descriptions(user: IntermediateRepresentation) -> Tuple[str, str]:
    return (get_investment_description_path(user.assets[0], user.education), get_investment_description_path(user.assets[1], user.education))


def get_motivation(user: IntermediateRepresentation) -> str:
    return get_age_dependent_path(user, "motivation")


def get_slogan(user: IntermediateRepresentation) -> str:
    return get_age_dependent_path(user, "slogans")


def get_trading_type(user: IntermediateRepresentation) -> str:
    if user.account_type == fd.INVEST:
        return "assets/trading_types/iia.txt"
    elif user.account_type == fd.BROKERAGE:
        return "assets/trading_types/broker.txt"
