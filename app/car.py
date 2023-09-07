from typing import List, Union
# from customer import Customer
from shop import Shop
import math


def distance_calculation(point_custom: List[Union[int, float]], point_shop: List[Union[int, float]]) -> float:
    # hypotenuse = math.sqrt((point_shop[0] - point_custom[0]) ** 2 + (point_shop[1] - point_custom[1]) ** 2)
    return math.hypot(point_shop[0] - point_custom[0], point_shop[1] - point_custom[1])

# def get_directions(list_customers: List[Customer], list_shop: List[Shop]) -> List[dict]:
#     list_directions = []
#     for work_customer in list_customers:
#         for work_shop in list_shop:
#
#             work_dict = {"customer": work_customer.name, "shop": work_shop.name,
#                          "distance": distance_calculation(work_shop.location, work_customer.location)}
#
#             list_directions.append(work_dict)
#
#     return list_directions


def get_min_distance_shop(location_customers: list, list_shop: List[Shop]) -> dict:
    min_distance = 0
    nearest_shop = {}
    for index, work_shop in enumerate(list_shop):
        if index == 0:
            shop_distance = distance_calculation(location_customers, work_shop.location)
            min_distance = shop_distance
            # nearest_shop = {"shop": work_shop.name, "min_distance": min_distance}
            nearest_shop = {"shop": work_shop, "min_distance": min_distance}

        else:
            shop_distance = distance_calculation(location_customers, work_shop.location)
            if shop_distance < min_distance:
                min_distance = shop_distance
                # nearest_shop = {"shop": work_shop.name, "min_distance": min_distance}
                nearest_shop = {"shop": work_shop, "min_distance": min_distance}
    return nearest_shop


def get_list_nearest_shops(location_customers_l: list, list_shop_l: List[Shop]) -> List[dict]:
    list_nearest_shop = []
    for work_shop_l in list_shop_l:
        nearest_shop_l = {
            "shop": work_shop_l,
            "distance": distance_calculation(location_customers_l, work_shop_l.location)
        }
        list_nearest_shop.append(nearest_shop_l)
    return list_nearest_shop

