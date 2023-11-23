from app.utils import calculate_distance, calculate_fuel_cost


class Shop:

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> float:
        return sum(
            self.products[product] * quantity
            for product, quantity in product_cart.items()
        )


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
        self.car = car

    def calc_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance_to_shop = calculate_distance(shop.location, self.location)
        fuel_cost_to_shop = calculate_fuel_cost(
            distance_to_shop, self.car.get("fuel_consumption"), fuel_price
        )
        product_cost = shop.calculate_product_cost(self.product_cart)
        return round(fuel_cost_to_shop * 2 + product_cost, 2)

    def print_check(self, shop: Shop) -> None:
        total_cost = 0
        string_check = "Date: 04/01/2021 12:33:41\n"
        string_check += (f"Thanks, {self.name}, "
                         f"for your purchase!\n"
                         f"You have bought:\n")

        for product, quantity in shop.products.items():
            total_cost += (quantity * self.product_cart.get(product, 0))
            cost_per_item = self.product_cart.get(product, 0) * quantity
            cost_format = (
                f"{cost_per_item:.0f}"
                if float(cost_per_item).is_integer()
                else f"{cost_per_item:.1f}")
            string_check += (f"{self.product_cart.get(product, 0)}"
                             f" {product}s for "
                             f"{cost_format.format(cost_per_item)} dollars\n")

        string_check += (
            f"Total cost is {total_cost:.1f} dollars\n"
            f"See you again!\n"
        )
        print(string_check)

    def ride_home(self) -> None:
        string_ride = f"{self.name} rides home\n"
        string_ride += f"{self.name} now has {self.money} dollars\n"
        print(string_ride)
