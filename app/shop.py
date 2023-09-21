from dataclasses import dataclass


@dataclass
class Shop:

    name: str
    location: list
    products: dict

    def __hash__(self) -> int:
        return hash(self.name)
