from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int | float],
            money: int | float,
            car: dict,
            fuel_price: float | float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.location_home = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price
        self.text_cost_products = ""

    def position(self, ox: int | float, oy: int | float) -> None:
        self.location = [ox, oy]

    def cost_fuel(self, ox: int | float, oy: int | float) -> float | int:
        distance = sqrt(((ox - self.location[0]) ** 2
                         + (oy - self.location[1]) ** 2)) * 2
        cost_fuel = (distance * self.car["fuel_consumption"]
                     / 100 * self.fuel_price)
        return round(cost_fuel, 2)

    def cost_products(self, price_products: dict) -> float | int:
        cost_products = 0.0
        self.text_cost_products = ""
#
        for key, value in (self.product_cart).items():

            price = price_products.get(key)
            cost_type_product = round(price * value, 2)
            cost_products += cost_type_product
            self.text_cost_products += (f"{value} {key}s for "
                                f"{cost_type_product} dollars\n")

        self.text_cost_products += (f"Total cost "
                                    f"is {cost_products} dollars")
        return round(cost_products, 2)
