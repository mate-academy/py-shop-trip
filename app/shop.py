import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def get_price_of_cart(self, cart: dict) -> dict:
        def format_number(num: int) -> int | float:
            if isinstance(num, float) and num != int(num):
                return round(num, 2)
            return int(num)

        calculated_prices = {
            product_name: format_number(
                product_count * self.products.get(product_name, 0)
            )
            for product_name, product_count in cart.items()
        }
        return {
            "full_amount": sum(calculated_prices.values()),
            "detailed": calculated_prices,
        }
