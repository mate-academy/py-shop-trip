from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, int | float]

    def cost_of_products(
            self,
            customer_curt: dict[str, int]
    ) -> dict[str, float | int]:
        return {
            key: self.products[key] * value
            for key, value in customer_curt.items()
        }
