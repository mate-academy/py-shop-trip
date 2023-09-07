import datetime
import json
from typing import Union, List
from shop import Shop
from car import get_min_distance_shop, get_list_nearest_shops


class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def __init__(self, name, product_cart, location, money, car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __get__(self, instance, owner) -> list:
        pass

    @classmethod
    def load_info_customer(cls, read_data_cs: dict) -> "Customer":
        return cls(
            name=read_data_cs["name"],
            product_cart=read_data_cs["product_cart"],
            location=read_data_cs["location"],
            money=read_data_cs["money"],
            car=read_data_cs["car"]
        )

#   поиск совпадений товаров и если есть сумма их преобретений
    def search_right_products(self, shop_visited: Shop) -> List[dict]:
        list_right_products = []
        for product_ct in self.product_cart:
            for products_sp in shop_visited.products:
                if product_ct == products_sp:
                    summ_product = self.product_cart[product_ct] * shop_visited.products[products_sp]
                    dict_right_products = {product_ct: summ_product}

                    list_right_products.append(dict_right_products)

        return list_right_products

    def customer_shopping(self, local_shops: List[Shop], fuel_price) -> str:

        customer_nearest_shop = get_min_distance_shop(self.location, local_shops)
        list_nearest_shops = get_list_nearest_shops(self.location, local_shops)

        result_part_1 = f"{self.name} has {self.money} dollars\n"

        result_part_2 = ""

        for nearest_s in list_nearest_shops:
            nearest_s_shop = nearest_s["shop"].name
            nearest_s_distance = nearest_s["distance"]
            cost_fuel = (nearest_s_distance * self.car["fuel_consumption"])/100 * fuel_price * 2
            cost_trip = nearest_s["shop"].customer_trip_sum(self.product_cart)
            result_cost = cost_trip + cost_fuel
            result_part_2 += f"{self.name}'s trip to the {nearest_s_shop} costs {result_cost}\n"

        customer_nearest_shop_name = customer_nearest_shop["shop"].name
        result_part_3 = f"Bob rides to {customer_nearest_shop_name}\n\n"

        now = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        result_part_4 = f"Date: {now}\n"

        result_part_5 = f"Thanks, {self.name}, for your purchase!\nYou have bought:\n"
        cost_position_shop = customer_nearest_shop["shop"].cost_sum_position(self.product_cart)
        for cost_position in cost_position_shop:
            str_cost_position = f"{self.product_cart[cost_position]} {cost_position} for {cost_position_shop[cost_position]} dollars\n"
            result_part_5 += str_cost_position

        sum_cost_trip = customer_nearest_shop["shop"].customer_trip_sum(self.product_cart)
        result_part_6 = f"Total cost is {sum_cost_trip} dollars\nSee you again!\n\n"

        rest_money = self.money - sum_cost_trip - ((customer_nearest_shop["min_distance"] * self.car["fuel_consumption"]) / 100 * fuel_price * 2)
        result_part_7 = f"Bob rides home\n{self.name} now has {rest_money} dollars\n"

        result_str = result_part_1 + result_part_2 + result_part_3 + result_part_4 + result_part_5 + result_part_6 + result_part_7
        return result_str


def read_from_json(data_file: str, what_information: str) -> Union[List[Union[Customer, Shop]], float]:
    with open(data_file, "r") as work_file:
        work_data = json.load(work_file)
        if what_information in work_data:
            test = []
            if isinstance(work_data[what_information], float):
                return work_data[what_information]
            for data in work_data[what_information]:
                test.append(data)
            return test
