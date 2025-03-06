import dataclasses


@dataclasses.dataclass()
class Shop:
    name: str
    location: list[int]
    product_cart: dict[str: float]

    def shop_distance(self, location: list[float, float]) -> float:
        a_distance = (location[0] - self.location[0]) ** 2
        b_distance = (location[1] - self.location[1]) ** 2
        return (a_distance + b_distance) ** 0.5
