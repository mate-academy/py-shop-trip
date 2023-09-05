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



def read_data_shops(data_file: str) -> List[dict]:
    pass
