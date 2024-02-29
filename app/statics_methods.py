import json


class Method:

    @staticmethod
    def open_file(file_name: str) -> dict:
        """Open file only for reading."""
        with open(file_name, "r") as j_son:
            data = json.load(j_son)
        return data

    @staticmethod
    def transform_in_plural(data: list[str]) -> list:
        """Transform in plural the list of string data."""
        return [element + "s" for element in data]

    @staticmethod
    def cost_of_trip(
            distance: int | float,
            fuel_cons: int | float,
            fuel_cost: int | float
    ) -> int | float:
        """Return the cost of trip from Home to shop."""
        return (fuel_cons * (distance * 0.01)) * fuel_cost

    @staticmethod
    def check_money(
            customer_cart: dict,
            shop_price: dict
    ) -> int | float:
        """Return the sum of purchase considering the
           card of customer and price in shop."""
        return sum(
            customer_cart[element] * shop_price[element]
            for element in customer_cart
        )
