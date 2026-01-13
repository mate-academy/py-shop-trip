import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cost_product_cart(
            self,
            products_cart: dict[str, int]
    ) -> float:
        cost = 0
        for name_product, amount in products_cart.items():
            cost += self.products[name_product] * amount
        return round(cost, 2)

    def print_receipt(
            self,
            customer_name: str,
            products_cart: dict[str, int]
    ) -> None:
        receipt_lines = [
            f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}",
            f"Thanks, {customer_name}, for your purchase!",
            "You have bought:"
        ]
        for name_product, amount in products_cart.items():
            cost = self.products[name_product] * amount
            if cost == int(cost):
                cost_str = str(int(cost))
            else:
                cost_str = str(cost)
            receipt_lines.append(
                f"{amount} {name_product}s for {cost_str} dollars"
            )
        total_cost = self.calculate_cost_product_cart(products_cart)
        receipt_lines.append(f"Total cost is {total_cost} dollars")
        receipt_lines.append("See you again!\n")
        print("\n".join(receipt_lines))
