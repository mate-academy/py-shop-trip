from app.trip.get_data import get_data
from app.shop.shop import Shop


def get_list_of_shops() -> list[Shop]:
    """Get a list of available shops"""
    shop_list = get_data()["shops"]
    return [Shop(shop) for shop in shop_list]
