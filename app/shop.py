class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def verify_position(position_cords: list) -> bool:
        if not isinstance(position_cords, list):
            return False
        if not len(position_cords) == 2:
            return False
        if not len([i for i in position_cords if isinstance(i, int)]) == 2:
            return False
        return True

    def calculate_distance(self, your_pos: list) -> float:
        if self.verify_position(your_pos):
            return (
                (self.location[0] - your_pos[0]) ** 2
                + (self.location[1] - your_pos[1]) ** 2
            ) ** 0.5

    def get_full_receipt(self, product_cart: dict) -> dict:
        receipt = {"order": {}}
        total_value = 0
        for product, quantity in product_cart.items():
            if product in self.products.keys():
                value = round(quantity * self.products[product], 2)
                value = int(value) if int(value) == value else value
                product_details = {
                    "quantity": quantity,
                    "price": self.products[product],
                    "value": value,
                }
                receipt["order"][product] = product_details
                total_value += receipt["order"][product]["value"]
        receipt["products_costs"] = total_value
        return receipt
