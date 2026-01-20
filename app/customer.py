from __future__ import annotations

from app.shop import Shop


class Customer:
    def __init__(
            self,
            custom_info: dict
    ) -> None:
        self.name = custom_info["name"]
        self.product_cart = custom_info["product_cart"]
        self.location = custom_info["location"]
        self.money = custom_info["money"]
        self.car = custom_info["car"]

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cheaper_shop(self, shops: list[Shop], fuel_price: float) -> None:
        shop_dict = {}
        for shop in shops:
            fuel_cost = ((((shop["location"][0] - self.location[0]) ** 2 + (
                shop["location"][1] - self.location[1]) ** 2)
                ** 0.5) * fuel_price * self.car[
                "fuel_consumption"] / 100)
            sum_of_the_product = 0
            for product in self.product_cart:
                sum_of_the_product += (
                    shop["products"][product] * self.product_cart[product])
            sum_of_the_trip = round(fuel_cost * 2 + sum_of_the_product, 2)
            print(f"{self.name}'s trip "
                  f"to the {shop['name']} costs {sum_of_the_trip}")
            shop_dict[sum_of_the_trip] = shop
        if self.money > min(shop_dict):
            print(f"{self.name} rides to {shop_dict[min(shop_dict)]['name']}")
            self.print_info(shop_dict[min(shop_dict)], min(shop_dict))
            return None
        print(f"{self.name} doesn't have enough money "
              f"to make a purchase in any shop")

    def print_info(self, shop: dict, all_cost: float) -> None:
        # {datetime.today().now().strftime('%d/%m/%Y %H:%M:%S')}
        print(f"\nDate: 04/01/2021 12:33:41\n"
              f"Thanks, {self.name}, for your purchase!\n"
              f"You have bought:")
        total_cost = 0
        for product in self.product_cart:
            product_cost = (
                self.product_cart[product] * shop["products"][product])
            total_cost += product_cost
            calcul_product_cost = (int(product_cost)
                                   if product_cost == int(product_cost)
                                   else product_cost)
            print(
                f"{self.product_cart[product]} {product}s "
                f"for {calcul_product_cost} "
                f"dollars")
        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!")
        self.money -= all_cost
        print(f"\n{self.name} rides home\n"
              f"{self.name} now has {round(self.money, 2)} dollars\n")
