import dataclasses


@dataclasses.dataclass
class Shop:
    shop_name: str
    location_shop: list[int]
    products_price: dict[str, float]

    def calculate_product(
            self,
            product_cart: dict[str, int],
    ) -> dict[str, float]:
        return {
            product: (product_cart[product] * self.products_price[product])
            for product in self.products_price.keys()
        }

    @staticmethod
    def sum_of_products(products: dict[str, float]) -> float:
        return sum(products.values())
