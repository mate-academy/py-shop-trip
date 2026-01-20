from dataclasses import dataclass
from .car import Car
from .shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: tuple
    money: float
    car: Car
    home_location: tuple = None

    def total_product_cost(self, shop: Shop) -> float:
        total_cost = 0
        for product , quantity in self.product_cart.items():
            if product in shop.products:
                total_cost += shop.products[product] * quantity
            else:
                return 0.0
        return total_cost

    def total_trip_cost(
            self,
            shop_position: tuple,
            fuel_price: float,
    ) -> float:
        distance = (((self.location[0] - shop_position[0]) ** 2)
                    + (self.location[1] - shop_position[1]) ** 2) ** 0.5
        liters_one_way = distance * (self.car.fuel_consumption / 100)
        cost_one_way = liters_one_way * fuel_price
        total_cost = cost_one_way * 2
        return total_cost

    def go_shopping(self, shops: list[Shop], fuel_price: float) -> None:

        print(f"{self.name} has {self.money:.0f} dollars")
        min_total_cost = float("inf")
        best_shop = None

        for shop in shops:
            product_cost = self.total_product_cost(shop)
            if product_cost == 0.0:
                continue
            trip_cost = self.total_trip_cost(shop.location, fuel_price)
            total_trip_cost = product_cost + trip_cost

            formatted_cost = f"{total_trip_cost:.2f}"
            print(f"{self.name}'s trip to "
                  f"the {shop.name} costs {formatted_cost}")

            if total_trip_cost < min_total_cost:
                min_total_cost = total_trip_cost
                best_shop = shop

        if not best_shop:
            return

        if self.money >= min_total_cost:
            print(f"{self.name} rides to {best_shop.name}\n")
            self.home_location = self.location
            self.location = best_shop.location

            product_cost_only = self.total_product_cost(best_shop)
            best_shop.print_receipt(
                self.name, self.product_cart, product_cost_only
            )

            self.money -= min_total_cost

            print(f"{self.name} rides home")
            self.location = self.home_location
            print(f"{self.name} now has {self.money:.2f} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in any shop")
