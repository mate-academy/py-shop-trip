import json
from typing import Union, List
from shop import Shop


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
