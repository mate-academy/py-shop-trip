from typing import List


class Shop:
    name: str
    location: List[int]
    products: dict

    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __get__(self, instance, owner) -> list:
        pass

    @classmethod
    def load_info_shop(cls, read_data_sh: dict) -> "Shop":
        return cls(
            name=read_data_sh["name"],
            location=read_data_sh["location"],
            products=read_data_sh["products"]
        )
