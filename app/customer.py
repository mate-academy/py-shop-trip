import datetime
import json
from typing import Union, List
from app.shop import Shop
from app.car import get_list_nearest_shops


class Customer:
    name: str
    product_cart: dict
    location: List[Union[int, float]]
    money: float
    car: dict

    cheapest_store: Shop

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[Union[int, float]],
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def load_info_customer(cls, read_data_cs: dict) -> "Customer":
        return cls(
            name=read_data_cs["name"],
            product_cart=read_data_cs["product_cart"],
            location=read_data_cs["location"],
            money=read_data_cs["money"],
            car=read_data_cs["car"]
        )

    def search_right_products(self, shop_visited: Shop) -> List[dict]:
        list_right_products = []
        for product_ct in self.product_cart:
            for products_sp in shop_visited.products:
                if product_ct == products_sp:
                    summ_product = (
                        self.product_cart[product_ct]
                        * shop_visited.products[products_sp]
                    )
                    dict_right_products = {product_ct: summ_product}

                    list_right_products.append(dict_right_products)

        return list_right_products

    def costs_for_all_shop(
            self,
            list_shops: List[dict],
            fuel_price: float
    ) -> dict:
        list_cost_all_shops = {}

        for nearest_s in list_shops:
            nearest_s_distance = nearest_s["distance"]
            cost_fuel = (
                (nearest_s_distance * self.car["fuel_consumption"])
                / 100 * fuel_price * 2
            )
            cost_trip = nearest_s["shop"].customer_trip_sum(self.product_cart)
            result_cost = cost_trip + cost_fuel

            list_cost_all_shops[nearest_s["shop"]] = {
                "result_cost": result_cost,
                "cost_trip": cost_trip,
                "cost_fuel": cost_fuel
            }
        return list_cost_all_shops

    def find_cheapest_store_info(self, info_all_shop: dict) -> dict:
        cheapest_store_info = {}
        min_cost_all_shop = 0
        for index, shop_costs in enumerate(info_all_shop):
            if index == 0:
                min_cost_all_shop = (
                    info_all_shop[shop_costs]["result_cost"]
                )
                self.cheapest_store = shop_costs
                cheapest_store_info = info_all_shop[shop_costs]
            else:
                if min_cost_all_shop > (
                        info_all_shop[shop_costs]["result_cost"]
                ):
                    min_cost_all_shop = (
                        info_all_shop[shop_costs]["result_cost"]
                    )
                    self.cheapest_store = shop_costs
                    cheapest_store_info = info_all_shop[shop_costs]

        return cheapest_store_info

    def customer_shopping(
            self,
            local_shops: List[Shop],
            fuel_price: float
    ) -> str:

        result_part_1 = f"{self.name} has {self.money} dollars\n"

        list_nearest_shops = get_list_nearest_shops(self.location, local_shops)
        costs_for_all_shop = self.costs_for_all_shop(
            list_nearest_shops,
            fuel_price
        )

        result_part_2 = ""
        for cost_sheet in costs_for_all_shop:
            print_name_shop = cost_sheet.name
            print_cost_result = round(
                costs_for_all_shop[cost_sheet]["result_cost"],
                2
            )
            result_part_2 += f"{self.name}'s " \
                             f"trip to the {print_name_shop} " \
                             f"costs {print_cost_result}\n"

        cheapest_store_info = self.find_cheapest_store_info(costs_for_all_shop)

        if cheapest_store_info["result_cost"] > self.money:
            sorry_not_many = f"{self.name} " \
                             f"doesn't have enough money " \
                             f"to make a purchase in any shop"
            result_not_many = result_part_1 + result_part_2 + sorry_not_many
            return result_not_many

        customer_nearest_shop_name = self.cheapest_store.name
        result_part_3 = f"{self.name} " \
                        f"rides to {customer_nearest_shop_name}\n\n"

        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        result_part_4 = f"Date: {now}\n"

        result_part_5 = f"Thanks, {self.name}, " \
                        f"for your purchase!\nYou have bought: \n"
        cost_position_shop = (
            self.cheapest_store.cost_sum_position(self.product_cart)
        )
        for cost_position in cost_position_shop:
            abbreviated_c = round(cost_position_shop[cost_position], 2)
            if abbreviated_c % 1 == 0:
                abbreviated_c = int(abbreviated_c)
            str_cost_position = f"{self.product_cart[cost_position]} " \
                                f"{cost_position}s for " \
                                f"{abbreviated_c} dollars\n"
            result_part_5 += str_cost_position

        sum_cost_trip = (
            self.cheapest_store.customer_trip_sum(self.product_cart)
        )
        result_part_6 = f"Total cost is " \
                        f"{round(sum_cost_trip, 2)} " \
                        f"dollars\nSee you again!\n\n"

        rest_money = self.money - cheapest_store_info["result_cost"]
        result_part_7 = f"{self.name} rides home\n" \
                        f"{self.name} now has " \
                        f"{round(rest_money, 2)} dollars\n"

        result_str = (
            result_part_1 + result_part_2 + result_part_3
            + result_part_4 + result_part_5
            + result_part_6 + result_part_7
        )
        return result_str


def read_from_json(
        data_file: str,
        what_information: str
) -> Union[List[Union[Customer, Shop]], float]:
    with open(data_file, "r") as work_file:
        work_data = json.load(work_file)
        if what_information in work_data:
            test = []
            if isinstance(work_data[what_information], float):
                return work_data[what_information]
            for data in work_data[what_information]:
                test.append(data)
            return test
