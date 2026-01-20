import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict
