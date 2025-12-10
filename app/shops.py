from app.product_cart import ProductCard
from dataclasses import dataclass
from app.check_if_exist import check_values


@dataclass
class Shops(ProductCard):
    name: str
    location: list

    @classmethod
    def create_list_of_shops(cls, dataset: dict) -> "Shops":
        first_condition = check_values(dataset,
                                       "name",
                                       "location",
                                       "products")
        second_condition = check_values(dataset["products"],
                                        "milk",
                                        "bread",
                                        "butter")
        if first_condition and second_condition:
            return cls(milk=dataset["products"]["milk"],
                       bread=dataset["products"]["bread"],
                       butter=dataset["products"]["butter"],
                       name=dataset["name"],
                       location=dataset["location"])
