import datetime
from app.shop import Shop
from app.car import Car
from app.point import Point


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: Point,
        money: int | float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def check_shops(
            self, shops: list[Shop],
            fuel_price: int | float
    ) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        shops_costs = {}
        for shop in shops:
            distance = self.location.distance_to_point(shop.location)
            total_cost = round(
                (
                    (
                        shop.price_of_products_set(self.product_cart)
                        + self.car.cost_of_way(fuel_price, distance) * 2
                    )
                ),
                2,
            )
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
            shops_costs[total_cost] = shop

        value = min(shops_costs.keys())
        matching_shop = shops_costs[value]
        self.is_enought_money(value, matching_shop)

    def print_bill(self, shop: Shop) -> None:
        current_date = datetime.datetime.now()
        date_time = current_date.strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"Date: {date_time}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought: \n"
            f"{self.product_cart['milk']} milks "
            f"for {self.product_cart['milk'] * shop.products['milk']} "
            "dollars\n"
            f"{self.product_cart['bread']} breads "
            f"for {self.product_cart['bread'] * shop.products['bread']} "
            "dollars\n"
            f"{self.product_cart['butter']} butters "
            f"for {self.product_cart['butter'] * shop.products['butter']} "
            "dollars\n"
            f"Total cost is {shop.price_of_products_set(self.product_cart)} "
            "dollars\n"
            f"See you again!\n"
        )

    def is_enought_money(self, trip_cost: int | float, shop: Shop) -> None:
        if self.money >= trip_cost:
            print(f"{self.name} rides to {shop.name}\n")
            self.location = shop.location
            self.print_bill(shop)
            print(f"{self.name} rides home")
            self.money = self.money - trip_cost
            print(f"{self.name} now has {self.money} dollars\n")
        else:
            print(
                f"{self.name} doesn't have enough "
                "money to make a purchase in any shop"
            )
