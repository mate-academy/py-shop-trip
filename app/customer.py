from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 prod_cart: dict[str, int],
                 location: list[int],
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.prod_cart = prod_cart
        self.home = location
        self.location = location
        self.money = money
        self.car = car

    def check_price_to_shop(self, shop: Shop, fuel_price: float) -> float:

        shopping_cost = shop.check_prices(self.prod_cart)
        trip_cost = self.car.calc_trip_cost(
            self.location,
            shop.location,
            fuel_price)

        return round(trip_cost + shopping_cost, 2)

    def choose_shop(self,
                    shops: list[Shop],
                    fuel_price: float) -> tuple[Shop | None, str]:

        shopping_cost = {}
        text = f"{self.name} has {self.money} dollars\n"

        for shop in shops:
            shopping_cost[shop] = self.check_price_to_shop(shop, fuel_price)
            text = (f"{text}{self.name}'s trip to the {shop.name} "
                    f"costs {shopping_cost[shop]}\n")

        shop = min(shopping_cost, key=shopping_cost.get)
        if self.money < shopping_cost[shop]:
            return None, (f"{text}{self.name} doesn't have enough"
                          f" money to make a purchase in any shop")
        text = f"{text}{self.name} rides to {shop.name}\n"
        self.money -= shopping_cost[shop]
        self.location = shop.location
        return shop, text

    def drives_home(self) -> str:
        text = f"{self.name} rides home\n"
        text = f"{text}{self.name} now has {self.money} dollars\n"
        self.location = self.home
        return text
