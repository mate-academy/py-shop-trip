import math


class Shop:
    def __init__(
            self,
            name: str,
            location: tuple[int, int],
            products: dict[str, float]
    ) -> None:

        self._name = name
        self._location = location
        self._products = products

    def __hash__(self) -> int:
        return hash(self._name)

    def __eq__(self, other: "Shop") -> bool:
        return isinstance(other, Shop) and self._name == other.name

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> tuple[int, int]:
        return self._location

    @property
    def products(self) -> dict[str, int | float]:
        return self._products

    def products_cost(self, customers_product_cart: dict[str, int]) -> float:
        total = 0
        for product in customers_product_cart:
            try:
                product_price = self._products[product]
            except KeyError:
                print(f"This store does not have '{product}'.")
                continue
            number_of_products = customers_product_cart[product]
            total += product_price * number_of_products
        return total

    def distance_to_shop(self, customer_location: tuple[int, int]) -> float:
        distance = math.sqrt(
            (self.location[0] - customer_location[0]) ** 2
            + (self.location[1] - customer_location[1]) ** 2
        )
        return distance
