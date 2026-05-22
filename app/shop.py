class Shop:
    def __init__(self, name: str, location: tuple, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cost(self, shopping_list: dict) -> float:
        total = 0
        for item, quantity in shopping_list.items():
            if item in self.products:
                price = self.products[item]
                total += price * quantity
        return total
