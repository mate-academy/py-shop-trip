class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to_shop(self, location_shop: list[int]) -> int | float:
        distance = ((self.location[0] - location_shop[0]) ** 2
                    + (self.location[1] - location_shop[1]) ** 2) ** 0.5
        return distance

    def cost_of_products(self, products: dict) -> int | float:
        return sum(
            products.get(product) * quantity
            for product, quantity in self.product_cart.items()
        )

    def cost_trip(self, location_shop: list[int], fuel_price: float) -> float:
        return (2 * self.distance_to_shop(location_shop)
                * fuel_price
                * self.car.get("fuel_consumption")
                / 100)

    def total_cost_products_and_trip(
            self,
            products: dict,
            location_shop: list[int],
            fuel_price: float
    ) -> int | float:
        return (
            self.cost_of_products(products)
            + self.cost_trip(location_shop, fuel_price)
        )
