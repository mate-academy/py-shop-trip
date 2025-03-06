import dataclasses


@dataclasses.dataclass()
class Shop:
    name: str
    location: list[int]
    product_cart: dict[str: float]

    def shop_distance(self, location: list[float, float]) -> float:
        a_distance = (self.location[0] + location[0]) ** 2
        b_distance = (self.location[1] + location[1]) ** 2
        return (a_distance + b_distance) ** 0.5
