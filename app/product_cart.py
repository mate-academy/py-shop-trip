class ProductCart:

    def __init__(self, entries: dict) -> None:
        self.entries = entries

    def get_quantity_products(self, name_product: str) -> int:
        return self.entries.get(name_product, 0)
