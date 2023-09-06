from typing import List, Union
from customer import Customer
from shop import Shop
import math


def distance_calculation(point_custom: List[Union[int, float]], point_shop: List[Union[int, float]]) -> float:
    return math.hypot(point_shop[0] - point_custom[0], point_shop[1] - point_custom[1])


def get_directions(list_customers: List[Customer], list_shop: List[Shop]) -> List[dict]:
    list_directions = []
    for work_customer in list_customers:
        for work_shop in list_shop:

            work_dict = {"customer": work_customer.name, "shop": work_shop.name,
                         "distance": distance_calculation(work_shop.location, work_customer.location)}

            list_directions.append(work_dict)

    return list_directions
