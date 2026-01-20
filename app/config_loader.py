import json
import pathlib
from typing import Any
from .car import Car
from .customer import Customer
from .shop import Shop
from .helper_fuctions import ConfigError, validate_location


def parse_car(car: dict[str, Any]) -> Car:
    fuel_consumption_raw = car.get("fuel_consumption")
    if fuel_consumption_raw is None:
        raise ConfigError("car fuel_consumption is missing")
    try:
        fuel_consumption = float(fuel_consumption_raw)
    except ValueError:
        raise ConfigError("car fuel_consumption is invalid")

    brand = car.get("brand")
    if brand is None:
        raise ConfigError("car brand name is missing")

    return Car(
        brand=brand,
        fuel_consumption=fuel_consumption,
    )


def parse_shop(shop: dict[str, Any]) -> Shop:
    if "name" not in shop or not shop["name"]:
        raise ConfigError("Shop name is required")

    location = shop.get("location")
    location = validate_location(location, shop["name"])

    return Shop(
        name=shop.get("name"),
        location=tuple(location),
        products=shop.get("products"),
    )


def parse_customer(customer: dict[str, Any]) -> Customer:
    money_raw = customer.get("money")
    if money_raw is None:
        raise ConfigError("Customer money is missing")
    try:
        money = float(money_raw)
    except (ValueError, TypeError):
        raise ConfigError("Customer money is invalid")

    car_data = customer.get("car")
    if car_data is None:
        raise ConfigError("Customer car is missing")

    name = customer.get("name")
    if name is None:
        raise ConfigError("Customer name is missing")

    location = customer.get("location")
    location = validate_location(location, name)

    products_cart = customer.get("product_cart")

    return Customer(
        name=name,
        product_cart=products_cart,
        location=tuple(location),
        money=money,
        car=parse_car(car_data),
    )


def load_config_data(file_path: str) -> dict[str, Any]:
    config_path = pathlib.Path(__file__).parent.parent / file_path
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found.")
    except json.JSONDecodeError:
        raise ConfigError(f"File {file_path} contains invalid json.")

    try:
        if "FUEL_PRICE" not in config_data:
            raise ConfigError("fuel_price is required")
        fuel_price_raw = config_data["FUEL_PRICE"]
        try:
            fuel_price = float(fuel_price_raw)
        except (ValueError, TypeError):
            raise ConfigError("fuel_price is invalid")

        shops = []
        if "shops" not in config_data:
            raise ConfigError("shops is required")
        for shop_data in config_data["shops"]:
            shop = parse_shop(shop_data)
            shops.append(shop)

        customers = []
        if "customers" not in config_data:
            raise ConfigError("customers is required")
        for customer_data in config_data["customers"]:
            customer = parse_customer(customer_data)
            customers.append(customer)

    except (KeyError, TypeError) as e:
        raise ConfigError(
            f"Configuration structure error (KeyError/TypeError): "
            f"{e}. Check configuration structure (e.g., missing 'shops', "
            f"'customers' key or incorrect type)."
        )

    return {
        "fuel_price": fuel_price,
        "shops": shops,
        "customers": customers
    }
