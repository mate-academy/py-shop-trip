from app.car import Car
from app.shop import Shop


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money

    def distance_to_shop(self, shops: dict) -> dict:
        side_x = self.location[0]
        side_y = self.location[1]
        distance = {}
        for shop in shops:
            other_x = shops[shop].location[0]
            other_y = shops[shop].location[1]
            distance.update({
                shops[shop].name:
                ((other_x - side_x) ** 2 + (other_y - side_y) ** 2) ** 0.5
            })
        return distance

    def count_price_fuel_and_products(
            self,
            shops: dict[Shop],
            cars: dict[Car]
    ) -> None:
        distance = self.distance_to_shop(shops)
        sum_products = {}
        sum_for_fuel = {}
        for shop in shops:
            all_price = self.product_card_for_shop(
                shops[shop].products["milk"],
                shops[shop].products["bread"],
                shops[shop].products["butter"]
            )
            sum_products.update({shops[shop].name: all_price})

            tank = cars[self.name].price_for_trip_on_car(
                distance[shops[shop].name]
            )

            sum_products[shops[shop].name] += tank
            sum_for_fuel.update({shops[shop].name: tank})

        self.go_from_home(sum_products, sum_for_fuel)

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

    def go_from_home(self, card: dict, fuel: dict) -> None:
        print(f"{self.name} has {self.money} dollars")
        shop = "".join(
            [sum_ for sum_ in card if min(card.values()) == card[sum_]]
        )

        for name, sum_trip in card.items():
            print(f"{self.name}'s trip to the {name} costs {sum_trip}")

        if min(card.values()) > self.money:
            print(f"{self.name} doesn't have enough money"
                  f" to make purchase in any shop")
        else:
            self.money -= fuel[shop]
            print(f"{self.name} rides to {shop}")
            Shop.shops[shop].store_cashier(
                self.name,
                self.product_cart,
                self.money
            )
