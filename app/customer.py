from app.car import Car

from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int | float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def print_money(self) -> None:
        print(self.money)

    def calculates_the_price(
        self,
        list_of_shops: list[Shop],
        fuel_price: float
    ) -> list | bool:
        min_buf_cost = float("inf")
        shop_class = None
        for shop in list_of_shops:
            total_cost = 0
            count_distance = (
                (shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2
            ) ** (1 / 2)
            total_cost += round(count_distance
                                * self.car.fuel_consumption
                                / 100 * fuel_price * 2, 2)
            for key in self.product_cart:
                total_cost += round(self.product_cart[key]
                                    * shop.products[key], 2)
            if total_cost < min_buf_cost:
                min_buf_cost = total_cost
                shop_class = shop
            print(f"{self.name}'s trip to the {shop.name}"
                  f" costs {round(total_cost, 2)}")
        if min_buf_cost > self.money:
            print(f"{self.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            return False
        else:
            print(f"{self.name} rides to {shop_class.name}")
            self.money -= min_buf_cost
            return [self.name, shop_class.name, self.product_cart]
