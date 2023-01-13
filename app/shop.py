from app.info import get_information
from app.customers import Customer


class Shop:

    def __init__(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            setattr(self, key, value)


def create_class_instance_shops_list() -> list:
    shops_list = get_information()["shops"]
    shops_class_list = []
    for shop in shops_list:
        shops_class_list.append(Shop(shop))
    return shops_class_list


def count_travel_for_customer(customer: Customer, shop: Shop) -> float | int:
    fuel_price = get_information()["FUEL_PRICE"]
    distance_x = shop.location[0] - customer.location[0]
    distance_y = shop.location[1] - customer.location[1]
    distance_to_shop = (distance_x ** 2 + distance_y ** 2) ** (1 / 2)
    travel_cost = distance_to_shop * \
        customer.car_fuel_consumption_per_km * fuel_price
    return travel_cost


def count_shop_visit_cost(customer: Customer, shop: Shop) -> dict:
    cost = {"products": 0}
    for key, value in customer.product_cart.items():
        cost[key] = value * shop.products[key]
        cost["products"] += cost[key]
    cost["travel_cost"] = count_travel_for_customer(customer, shop)
    final_cost = cost["products"] + (cost["travel_cost"] * 2)
    final_cost = round(final_cost * 100) / 100
    cost["final_cost"] = final_cost
    return cost


def create_shop_dict(customer: Customer, shop: Shop) -> dict:
    shop_dict = {}
    shop_dict.update(count_shop_visit_cost(customer, shop))
    shop_dict["name"] = shop.name
    shop_dict["location"] = shop.location
    return shop_dict


def find_cheapest_shop(shops_cost: list, shops: list) -> dict:
    cheapest_shop = {}
    for i in range(len(shops_cost)):
        if shops_cost[i] == min(shops_cost):
            cheapest_shop = shops[i]
            cheapest_shop["cost"] = shops_cost[i]
            break
    return cheapest_shop
