class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data.get("name")
        self.location = data.get("location", [])
        self.product_cart = data.get("products", {})
