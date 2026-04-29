class Product:
    def __init__(self, name: str, number: int | float) -> None:
        self.name = name
        self.number = number

    def __mul__(self, other: Product) -> int | float:
        res = self.number * other.number
        return int(res) if res.is_integer() else res
