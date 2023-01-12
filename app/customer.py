from app.shop import Shop
from app.car import Car


class Customer:
    customers = []

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict,
            fuel: float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car, fuel)
        self.count_price_fuel_and_products()

    def distance_to_shop(self) -> dict:
        x_ = self.location[0]
        y_ = self.location[1]
        distance = {}
        for shop in Shop.shops:
            other_x = shop.location[0]
            other_y = shop.location[1]
            distance.update({
                shop.name: ((other_x - x_) ** 2 + (other_y - y_) ** 2) ** 0.5
            })
        return distance

    def count_price_fuel_and_products(self) -> None:
        distance = self.distance_to_shop()
        sum_products = {}
        sum_for_fuel = {}
        for shop in Shop.shops:
            all_price = self.product_card_for_shop(
                shop.products["milk"],
                shop.products["bread"],
                shop.products["butter"]
            )
            sum_products.update({shop.name: all_price})
            tank = self.car.price_for_trip_on_car(distance[shop.name])
            sum_products[shop.name] += tank
            sum_for_fuel.update({shop.name: tank})
        StartTrip(
            self.name,
            self.money,
            sum_products,
            self.product_cart,
            sum_for_fuel
        ).go_from_home()

    def product_card_for_shop(
            self,
            milk: float,
            bread: float,
            butter: float
    ) -> float:
        return sum([
            self.product_cart["milk"] * milk,
            self.product_cart["bread"] * bread,
            self.product_cart["butter"] * butter]
        )


class StartTrip:
    def __init__(
            self,
            name: str,
            money: float,
            card: dict,
            product: dict,
            fuel: dict
    ) -> None:
        self.name = name
        self.money = money
        self.card = card
        self.product = product
        self.fuel = fuel

    def go_from_home(self) -> None:
        print(f"{self.name} has {self.money} dollars")
        key = "".join([key for key in self.card
                       if self.card[key] == min(self.card.values())])

        for name, value in self.card.items():
            print(f"{self.name}'s trip to the {name} costs {value}")

        if min(self.card.values()) > self.money:
            print(f"{self.name} doesn't have enough money"
                  f" to make purchase in any shop")
        else:
            self.money -= self.fuel[key]
            print(f"{self.name} rides to {key}")
            Shop.store_cashier(self.name, key, self.product, self.money)
