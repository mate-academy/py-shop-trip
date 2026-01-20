from typing import List


class Shop:
    name: str
    location: List[int]
    products: dict

    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def load_info_shop(cls, read_data_sh: dict) -> "Shop":
        return cls(
            name=read_data_sh["name"],
            location=read_data_sh["location"],
            products=read_data_sh["products"]
        )

    def customer_trip_sum(self, purchase_registry: dict) -> float:
        result_trip_sum = 0
        for product_tr in purchase_registry:
            if product_tr in self.products:
                result_trip_sum += (
                    self.products[product_tr]
                    * purchase_registry[product_tr]
                )
        return result_trip_sum

    def cost_sum_position(self, purchase_registry: dict) -> dict:
        list_position = {}
        for product_tr in purchase_registry:
            if product_tr in self.products:
                list_position[product_tr] = (
                    self.products[product_tr]
                    * purchase_registry[product_tr]
                )
        return list_position
