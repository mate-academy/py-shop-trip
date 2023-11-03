class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict,
            fuel_price: float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.location_home = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price
        self.text_cost_products = ""

    def position(self, ox: int, oy: int) -> None:
        self.location = [ox, oy]

    def cost_fuel(self, ox: int, oy: int) -> float:
        distance = (((ox - self.location[0]) ** 2
                     + (oy - self.location[1]) ** 2) ** 0.5)
        cost_fuel = (distance * self.car["fuel_consumption"]
                     / 100 * self.fuel_price)
        return cost_fuel

    def cost_products(self, price_products: dict) -> float:
        cost_products = 0
        self.text_cost_products = ""
        for key, value in (self.product_cart).items():

            price = price_products.get(key)
            cost_type_product = price * value
            self.text_cost_products += (f"{value} {key} "
                                        f"for {cost_type_product} dollars\n")
            cost_products += cost_type_product

        self.text_cost_products += f"Total cost is {cost_products} dollars"
        return cost_products
