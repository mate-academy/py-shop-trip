import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: tuple
    products: dict
