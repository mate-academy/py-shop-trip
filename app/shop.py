from app.info import get_information
from app.customers import Customer


class Shop:

    def __init__(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            setattr(self, key, value)

    @staticmethod
    def find_cheapest_shop(shops_cost: list, shops: list) -> dict:
        cheapest_shop = {}
        for i in range(len(shops_cost)):
            if shops_cost[i] == min(shops_cost):
                cheapest_shop = shops[i]
                cheapest_shop["cost"] = shops_cost[i]
                break
        return cheapest_shop

    def count_shop_visit_cost(self, customer: Customer) -> dict:
        cost = {"products": 0}
        for key, value in customer.product_cart.items():
            cost[key] = value * self.products[key]
            cost["products"] += cost[key]
        cost["travel_cost"] = self.count_travel_for_customer(customer)
        final_cost = cost["products"] + (cost["travel_cost"] * 2)
        final_cost = round(final_cost * 100) / 100
        cost["final_cost"] = final_cost
        return cost

    def count_travel_for_customer(self, customer: Customer) -> float | int:
        fuel_price = get_information()["FUEL_PRICE"]
        distance_x = self.location[0] - customer.location[0]
        distance_y = self.location[1] - customer.location[1]
        distance_to_shop = (distance_x ** 2 + distance_y ** 2) ** (1 / 2)
        travel_cost = distance_to_shop * \
            customer.car_fuel_consumption_per_km * fuel_price
        return travel_cost

    @staticmethod
    def create_class_instance_shops_list() -> list:
        shops_list = get_information()["shops"]
        shops_class_list = []
        for shop in shops_list:
            shops_class_list.append(Shop(shop))
        return shops_class_list

    def create_shop_dict(self, customer: Customer) -> dict:
        shop_dict = {}
        shop_dict.update(self.count_shop_visit_cost(customer))
        shop_dict["name"] = self.name
        shop_dict["location"] = self.location
        return shop_dict
