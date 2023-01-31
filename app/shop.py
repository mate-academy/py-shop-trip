import dataclasses


@dataclasses.dataclass
class Shop:
    shop_name: str
    shop_location: list[int]
    shop_prices: dict[str, float]

    def calculate_product(
            self,
            product_cart: dict[str, float]
    ) -> dict[str, float]:
        return {
            product: (product_cart[product] * self.shop_prices[product])
            for product in self.shop_prices.keys()
        }

    @staticmethod
    def sum_of_products(products: dict[str, float]) -> float:
        return sum(products.values())
