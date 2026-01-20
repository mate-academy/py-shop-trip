import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list[float]
    products: dict
