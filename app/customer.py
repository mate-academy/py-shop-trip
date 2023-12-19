from __future__ import annotations

from app.shop import Shop


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:

        self._name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.product_cost = sum(cost for cost in self.product_cart.values())

    def find_distance(
            self,
            shop: Shop
    ) -> float:

        x_distance = abs(self.location[0] - shop.location[0])
        y_distance = abs(self.location[1] - shop.location[1])

        return round(((x_distance ** 2) + (y_distance ** 2)) ** (1 / 2), 2)

    def chose_shop(
            self,
            shop_list: list[Shop],
            fuel_price: float
    ):
        print(f"{self._name} has {self.money} dollars")

        chipest_shop_name = None
        chipest_shop_price = None

        for shop in shop_list:
            trip_cost = round(
                (fuel_price
                 * self.find_distance(shop)
                 * self.car["fuel_consumption"]
                 + self.product_cost), 2
            )
            print(f"{self._name}'s trip to the {shop._name} costs {trip_cost}")

            if not chipest_shop_price:
                chipest_shop_price = trip_cost
                chipest_shop_name = shop._name
            if chipest_shop_price > trip_cost:
                chipest_shop_price = trip_cost
                chipest_shop_name = shop._name

        if self.money > chipest_shop_price:
            print(f"{self._name} rides to {chipest_shop_name}")
        else:
            print(f"{self._name} doesn't have enough money to make a purchase in any shop")

# 1.попробовать переписать иниты кастомера и магазина на приём словарей
# 2. допистаь метод уезжания из магазина

