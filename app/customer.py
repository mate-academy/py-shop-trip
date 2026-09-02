from app.shop import Shop
import math


class Customer:
    def __init__(self, data: dict, fuel_price: int | float) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = data["car"]
        self.fuel_price_of_1_l = fuel_price
        self.cheapest_shop_for_customer = None
        self.ho_location = self.location.copy()

    def how_much_money(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def full_price_in_shop(self, shop: Shop) -> float | int:
        result = 0
        for key in self.product_cart.keys():
            result += self.product_cart[key] * shop.products[key]
        return round(result, 2)

    def full_price_of_trip(self, shop: Shop) -> int | float:
        price_of_product = self.full_price_in_shop(shop)
        km_to_shop = math.sqrt((shop.location[0] - self.ho_location[0]) ** 2
                               + (shop.location[1] - self.ho_location[1]) ** 2)
        fuel_needed = km_to_shop / 100 * self.car["fuel_consumption"]
        fuel_cost = fuel_needed * self.fuel_price_of_1_l
        result = price_of_product + fuel_cost * 2
        return round(result, 2)

    def cheapest_shop(self, shop: list[Shop]) -> str:
        dict_of_shops = {}
        for i in range(len(shop)):
            dict_of_shops[shop[i].name] = self.full_price_of_trip(shop[i])
        sorted_dict = dict(sorted(dict_of_shops.items(),
                                  key=lambda item: item[1]))
        shop_name_cheap = next(iter(sorted_dict))
        for shops in shop:
            if shops.name == shop_name_cheap:
                self.cheapest_shop_for_customer = shops
                break
        self.location = self.cheapest_shop_for_customer.location.copy()
        return f"{self.name} rides to {shop_name_cheap}"

    def have_money_for_product(self) -> bool:
        how_much_need_money_for_shop = (
            self.full_price_of_trip(self.cheapest_shop_for_customer))
        if self.money < how_much_need_money_for_shop:
            return False
        return True

    def how_money_have_after_shopping(self, shop: Shop) -> int:
        money_now = self.money - self.full_price_of_trip(shop)
        return round(money_now, 2)
