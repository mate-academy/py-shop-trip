import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products_provides: dict