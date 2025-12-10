from app.car import CustomerCar
from app.product_cart import ProductCard
from dataclasses import dataclass
from app.check_if_exist import check_values


@dataclass
class Customers(ProductCard, CustomerCar):
    name: str
    location: list
    money: int | float

    @classmethod
    def create_list_of_customers(cls, dataset: dict) -> "Customers":
        first_condition = check_values(dataset,
                                       "name",
                                       "product_cart",
                                       "location",
                                       "money",
                                       "car")
        second_condition = check_values(dataset["product_cart"],
                                        "milk",
                                        "bread",
                                        "butter")
        third_condition = check_values(dataset["car"],
                                       "brand",
                                       "fuel_consumption")
        if first_condition and second_condition and third_condition:
            return cls(brand=dataset["car"]["brand"],
                       fuel_consumption=dataset["car"]["fuel_consumption"],
                       milk=dataset["product_cart"]["milk"],
                       bread=dataset["product_cart"]["bread"],
                       butter=dataset["product_cart"]["butter"],
                       name=dataset["name"],
                       location=dataset["location"],
                       money=dataset["money"])
