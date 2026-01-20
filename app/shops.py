import dataclasses


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    def __repr__(self) -> None:
        return self.name
