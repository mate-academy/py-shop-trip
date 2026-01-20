from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def print_customer_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calc_distance(self, shop: Shop) -> float:
        return ((self.location[0] - shop.location[0]) ** 2
                + (self.location[1] - shop.location[1]) ** 2) ** 0.5

    def calc_trip_cost(self, fuel_price: float, shop: Shop) -> float:
        distance = self.calc_distance(shop)
        fuel_consumption = self.car.calc_fuel_consumption(distance)
        return (fuel_consumption * fuel_price) * 2

    def find_cheapest_shop(
            self,
            fuel_price: float,
            shops: list[Shop]
    ) -> tuple[None | Shop, float, float]:
        cheapest_shop = None
        min_products_cost = None
        min_total_cost = float("inf")

        for shop in shops:
            trip_cost = self.calc_trip_cost(fuel_price, shop)
            products_cost = shop.calc_products_cost(self.product_cart)
            total_cost = trip_cost + products_cost
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {round(total_cost, 2)}")

            if total_cost <= self.money and total_cost < min_total_cost:
                cheapest_shop = shop
                min_products_cost = products_cost
                min_total_cost = total_cost

        return cheapest_shop, min_total_cost, min_products_cost

    def make_purchase(
            self,
            shop: Shop,
            total_cost: float,
            products_cost: float
    ) -> None:
        print(f"{self.name} rides to {shop.name}")
        shop.print_receipt(self.name, self.product_cart, products_cost)
        self.money -= total_cost
        print(f"{self.name} rides home\n"
              f"{self.name} now has {round(self.money, 2)} dollars\n")

    def go_shopping(self, fuel_price: float, shops: list[Shop]) -> None:
        self.print_customer_info()
        (
            cheapest_shop,
            min_total_cost,
            products_cost
        ) = self.find_cheapest_shop(fuel_price, shops)

        if cheapest_shop:
            self.make_purchase(cheapest_shop, min_total_cost, products_cost)
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
