import json
from typing import Any


class DataLoader:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        self._data: dict[str, Any] = {}
        self._fuel_price: float = 0.0
        self._customers: list[dict[str, Any]] = []
        self._shops: list[dict[str, Any]] = []

        self._load_data()

    @property
    def fuel_price(self) -> float:
        return self._fuel_price

    @property
    def customers(self) -> list[dict[str, Any]]:
        return self._customers

    @property
    def shops(self) -> list[dict[str, Any]]:
        return self._shops

    def _validate_fuel_price(self) -> None:
        if "FUEL_PRICE" not in self._data:
            raise KeyError("No FUEL_PRICE provided")

        fuel_price = self._data["FUEL_PRICE"]

        if not isinstance(fuel_price, (int, float)):
            raise ValueError("'customers' must be a list")

        if fuel_price < 0:
            raise ValueError("FUEL_PRICE must be a number >= 0")

        self._fuel_price = fuel_price

    def _validate_customer_list(self) -> None:
        if "customers" not in self._data:
            raise KeyError("'customers' list not provided")

        customers = self._data["customers"]

        if not isinstance(customers, list):
            raise ValueError("'customers' must be a list")

        self._customers = customers

    def _validate_shop_list(self) -> None:
        if "shops" not in self._data:
            raise KeyError("'shops' list not provided")

        shops = self._data["shops"]

        if not isinstance(shops, list):
            raise ValueError("'shops' must be a list")

        self._shops = shops

    def _extract_data(self) -> None:
        self._validate_fuel_price()
        self._validate_customer_list()
        self._validate_shop_list()

    def _load_data(self) -> None:
        with open(self._file_path, "r") as file:
            self._data = json.load(file)
        self._extract_data()
