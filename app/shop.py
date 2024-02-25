class Shop:

    def __init__(
            self, name: str, location: list[int], products_price: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products_price = products_price

    def __str__(self) -> str:
        return (f"Store name: {self.name}, "
                f"location: {self.location}, "
                f"products price list: {self.products_price}")

    @staticmethod
    def convert_to_int(number: int | float) -> int | float:
        if number == int(number):
            return int(number)
        return number
