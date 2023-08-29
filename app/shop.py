from datetime import datetime


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def calculate_purchase_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
        return total_cost

    def purchase_products(
            self,
            customer_name: str,
            product_cart: dict
    ) -> None:
        receipt = Receipt(self.name, customer_name)
        for product, quantity in product_cart.items():
            if product in self.products:
                price_per_unit = self.products[product]
                receipt.add_item(product, quantity, price_per_unit)

        receipt.print_receipt()


class Receipt:
    def __init__(
            self,
            shop_name: str,
            customer_name: str
    ) -> None:
        self.shop_name = shop_name
        self.customer_name = customer_name
        self.items = []

    def add_item(
            self,
            product: str,
            quantity: str,
            price_per_unit: float
    ) -> None:
        self.items.append((product, quantity, price_per_unit))

    def print_receipt(self) -> None:
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.customer_name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, quantity, price_per_unit in self.items:
            cost = quantity * price_per_unit
            total_cost += cost
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
