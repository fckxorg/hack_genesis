from typing import Tuple
import typing
import src.user_types as ut
import src.feature_deduction as fd
import glob
import random
from src.user_types import IntermediateRepresentation
from json import loads


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
    else:  # Workaround because my architecture is falling apart, lol
        return path


def get_age_dependent_path(user: IntermediateRepresentation, folder: str, extension: str) -> str:
    path = folder
    if user.age == ut.YOUNG:
        path += "/young"
    elif user.age == ut.EASY_MONEY:
        path += "/easy_money_seekers"
    elif user.age == ut.MIDDLE_AGED:
        path += "/middle-aged"
    elif user.age == ut.ELDER:
        path += "/elder"

    return path + extension


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


def get_product_from_category(user: IntermediateRepresentation, category: int) -> dict:
    products = glob.glob("assets/cards/info/" +
                         product_category_to_name(category) + "/*.json")

    # Rather sophisticated data science algorithm
    product = random.choice(products)
    return loads(load_asset(product))


def get_product_cards(user: IntermediateRepresentation) -> Tuple[dict, dict, dict]:
    leftover_category = list(
        (set((fd.BONDS, fd.STRUCTURED, fd.SHARES)) - set(user.assets)))[0]
    cat_args = (user.assets[0], user.assets[1], leftover_category)

    return [get_product_from_category(user, x) for x in cat_args]


def get_investment_descriptions(user: IntermediateRepresentation) -> Tuple[str, str]:
    return (get_investment_description_path(user.assets[0], user.education), get_investment_description_path(user.assets[1], user.education))


def get_motivation(user: IntermediateRepresentation) -> str:
    return 'assets/' + get_age_dependent_path(user, "motivation", ".txt")


def get_slogan(user: IntermediateRepresentation) -> str:
    return 'assets/' + get_age_dependent_path(user, "slogans", ".txt")


def get_main_picture(user: IntermediateRepresentation) -> str:
    return '../img/' + get_age_dependent_path(user, "main_picture", ".png")


def get_infographics(user: IntermediateRepresentation) -> str:
    return '../img/' + get_age_dependent_path(user, "infographics", ".png")


def get_icon_path(category: int):
    return "../img/icons/" + product_category_to_name(category) + ".svg"


def get_icons(user: IntermediateRepresentation) -> list:
    return [get_icon_path(user.assets[0]), get_icon_path(user.assets[1])]


def get_trading_type(user: IntermediateRepresentation) -> str:
    if user.account_type == fd.INVEST:
        return "assets/trading_types/iia.txt"
    elif user.account_type == fd.BROKERAGE:
        return "assets/trading_types/broker.txt"
