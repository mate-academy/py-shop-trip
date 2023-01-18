from app.info import get_shops_list, fuel_price
from app.customers import Customer


class Shop:
    def __init__(self, name: str, location: str, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def find_cheapest_shop(shops_cost: dict, shops: list[dict]) -> dict:
        min_cost = min(shops_cost.values())
        cheapest_shop_name = list(
            filter(lambda x: shops_cost[x] == min_cost, shops_cost))[0]
        cheapest_shop = next(
            shop for shop in shops
            if shop["name"] == cheapest_shop_name
        )
        cheapest_shop["cost"] = min_cost
        return cheapest_shop

    def count_shop_visit_cost(self, customer: Customer) -> dict:
        cost = {"products": 0}
        for product_name, quantity in customer.product_cart.items():
            cost[product_name] = quantity * self.products[product_name]
            cost["products"] += cost[product_name]
        cost["travel_cost"] = self.count_travel_for_customer(customer)
        final_cost = cost["products"] + (cost["travel_cost"] * 2)
        final_cost = round(final_cost * 100) / 100
        cost["final_cost"] = final_cost
        return cost

    def count_travel_for_customer(self, customer: Customer) -> float | int:
        distance_x = self.location[0] - customer.location[0]
        distance_y = self.location[1] - customer.location[1]
        distance_to_shop = (distance_x ** 2 + distance_y ** 2) ** (1 / 2)
        return distance_to_shop * \
            customer.car_fuel_consumption_per_km * fuel_price

    @staticmethod
    def create_class_instance_shops_list() -> list:
        shops_list = get_shops_list()
        shops_class_list = []
        for shop in shops_list:
            shops_class_list.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"]
                )
            )
        return shops_class_list

    def create_shop_dict(self, customer: Customer) -> dict:
        shop_dict = {}
        shop_dict.update(self.count_shop_visit_cost(customer))
        shop_dict["name"] = self.name
        shop_dict["location"] = self.location
        return shop_dict
