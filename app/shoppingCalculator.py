from app.customer import Customer
from app.shop import Shop
from typing import List
from math import sqrt
from app.printer import Printer


class ShoppingCalculator:

    def __init__(
            self,
            customer: Customer,
            shops: List[Shop],
            fuel: float
    ) -> None:
        self.customer = customer
        self.shops = shops
        self.fuel = fuel

    def get_road_cost(self, shop: Shop) -> float:
        x_start = self.customer.location[0]
        y_start = self.customer.location[1]
        x_end = shop.location[0]
        y_end = shop.location[1]

        road = sqrt(pow((x_start - x_end), 2) + (pow((y_start - y_end), 2)))
        cost = (road * self.customer.car.fuel_consumption * self.fuel) / 100

        return cost * 2

    def get_shopping_price(self) -> None:

        shop_cost = []
        all_cost = []
        receipts = []

        product_list = self.customer.product_cart
        for shop in self.shops:
            road = self.get_road_cost(shop)
            price = 0
            receipt = []
            shop_list = shop.products
            for product in product_list:
                quantity = product_list[product]
                products_price = shop_list[product] * quantity
                price += products_price
                if products_price % 1 == 0:
                    products_price = int(products_price)
                receipt_line = (f"{product_list[product]} {product}s "
                                f"for {products_price} dollars")
                receipt.append(receipt_line)

            shop_cost.append(price)

            receipts.append(receipt)
            all_cost.append(round(price + road, 2))

        Printer.print_info(receipts, all_cost, shop_cost, self.customer)
