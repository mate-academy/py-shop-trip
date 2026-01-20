import math
import datetime

from app.functions_to_interact_with_config import (
    get_file_config, get_file_dict
)


class Customer:
    def __init__(self, my_dict: dict) -> None:

        for key in my_dict:
            setattr(self, key, my_dict[key])

    def calculate_trip_fuel(self, shops: dict, fuel_price: dict) -> dict:
        dict_with_fuel_prices = {}
        for shop in shops.values():
            dx = shop.location[0] - self.location[0]
            dy = shop.location[1] - self.location[1]
            distance = math.hypot(dx, dy)
            trip_fuel_cost = (
                fuel_price["FUEL_PRICE"]
                * (self.car["fuel_consumption"]
                    * (distance / 100))
            )
            dict_with_fuel_prices[shop.name] = trip_fuel_cost

        return dict_with_fuel_prices

    def calculate_trip_products(
            self,
            shops: dict,
    ) -> dict:
        result_dict = {}
        for shop, values in shops.items():
            spent_money = {}
            for product, quantity in self.product_cart.items():
                spent_money[product] = (
                    quantity * shops[shop].products[product]
                )
            result_dict[values.name] = spent_money

        return result_dict

    @staticmethod
    def calc_sum_price_products_only(dict_with_product_prices: dict) -> dict:
        result_dict = {}
        for shop, value in dict_with_product_prices.items():
            sum_price = 0
            for product, money in value.items():
                sum_price += money
            result_dict[shop] = sum_price

        return result_dict

    @staticmethod
    def calc_sum_price_with_fuel(
            dict_with_product_prices: dict,
            dict_with_fuel_prices: dict
    ) -> dict:
        result_dict = {}
        for shop, value in dict_with_product_prices.items():
            sum_price = 0
            for product, money in value.items():
                sum_price += money
            sum_price += dict_with_fuel_prices[shop] * 2
            result_dict[shop] = sum_price
        return result_dict

    @staticmethod
    def calc_cheapest(dict_sum_with_fuel: dict) -> dict:
        min_key = min(dict_sum_with_fuel, key=dict_sum_with_fuel.get)
        return {min_key: dict_sum_with_fuel[min_key]}

    def receipt(self,
                dict_with_spent_money: dict,
                store_we_go_to: str,
                ) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for shop, value in dict_with_spent_money.items():
            if shop == store_we_go_to:
                for product, cost in value.items():
                    rounded_cost = round(cost, 2)

                    if rounded_cost == int(rounded_cost):
                        cost_str = str(int(rounded_cost))
                    else:
                        cost_str = f"{rounded_cost:.1f}"

                    print(
                        f"{self.product_cart[product]} "
                        f"{product}s for {cost_str} dollars"
                    )

        sum_price = (
            self.calc_sum_price_products_only
            (dict_with_spent_money)
            [store_we_go_to]
        )
        print(f"Total cost is {sum_price} dollars")
        print("See you again!")


customers_config = get_file_config("customers")
customers_dict = get_file_dict(customers_config, "customers")
customers = {}

for name, info in customers_dict.items():
    customers[name] = Customer(info)
