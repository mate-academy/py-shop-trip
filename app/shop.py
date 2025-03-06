import dataclasses


@dataclasses.dataclass()
class Shop:
    name: str
    location: list[int]
    product_cart: dict[str: float]

    def product_cost(self):
        return sum(value for value in self.product_cart.values())

    def shop_distance(self, location):
        a = (self.location[0] + location[0]) ** 2
        b = (self.location[1] + location[1]) ** 2
        return (a + b) ** 0.5


if __name__ == "__main__":
    shop = Shop("Central Shop", [4, 3],
                {
                "milk": 2,
                "bread": 2,
                "butter": 2
            })
    print(shop.shop_distance([1, 1]))