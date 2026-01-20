from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: int,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def trip_cost_calculation(self, shop: Shop) -> float:
        products_cost = 0
        if self.product_cart.keys() <= shop.products.keys():
            for product, value in self.product_cart.items():
                products_cost += value * shop.products[product]

        distance = (
            ((shop.location[0] - self.location[0]) ** 2)
            + ((shop.location[1] - self.location[1]) ** 2)
        ) ** 0.5
        trip_fuel_count = self.car.fuel_consumption * distance / 100
        trip_fuel_cost = (trip_fuel_count * self.car.fuel_price) * 2

        total_cost = round(products_cost + trip_fuel_cost, 2)

        return total_cost

    def shop_selection(self, shops: list[Shop]) -> Shop:
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {self.trip_cost_calculation(shop)}"
            )

        best_choice = min(
            shops, key=lambda store: self.trip_cost_calculation(store)
        )
        best_cost = self.trip_cost_calculation(best_choice)
        if best_cost <= self.money:
            print(f"{self.name} rides to {best_choice.name}\n")
            return best_choice
        print(
            f"{self.name} doesn't have enough money "
            f"to make a purchase in any shop"
        )

    def after_shopping(self, shop: Shop) -> None:
        print(f"{self.name} rides home")
        print(
            f"{self.name} now has "
            f"{self.money - self.trip_cost_calculation(shop)} dollars\n"
        )
