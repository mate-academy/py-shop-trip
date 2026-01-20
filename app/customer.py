import json
from pathlib import Path
from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car


def create_customer(customer_data: dict) -> Customer | None:
    try:
        if "car" not in customer_data:
            raise ValueError("Data about a car is missing")

        car_data = customer_data["car"]

        required_car_fields = ["brand", "fuel_consumption"]
        for field in required_car_fields:
            if field not in car_data:
                raise ValueError(f"A required field {field} is missing")

        car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"],
        )

        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car,
        )
        return customer
    except KeyError as e:
        print(f"Error: a required field is missing {e}")
        return None
    except ValueError as e:
        print(f"Validation error {e}")
        return None


def load_customers_from_config() -> list[Customer]:
    config_path = Path(__file__).parent / "config.json"

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

            customers = []
            if "customers" in config:
                for customer_data in config["customers"]:
                    customer = create_customer(customer_data)
                    if customer:
                        customers.append(customer)
            return customers
    except FileNotFoundError:
        print("No config.json file found")
        return []
    except json.decoder.JSONDecodeError:
        print("Decoding error JSON")
        return []
