import datetime


class Shop:
    def __init__(self, name: str, location: str, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def is_products(self, products: dict) -> bool | int:
        total_cost = 0
        for product, count in products.items():
            if product not in self.products:
                return False
            total_cost += count * self.products.get(product)
        return total_cost

    def calculate_total_cost(self, product: str, count: int) -> float | int:
        unit_price = self.products.get(product, 0)
        total_cost = count * unit_price
        formatted_cost = (
            int(total_cost) if total_cost.is_integer() else total_cost
        )
        return formatted_cost

    def get_receipt(self, products: dict, name: str) -> tuple:
        current_date = datetime.datetime.now()
        string_of_products = "\n".join(
            (
                f"{count} {product}s for "
                f"{self.calculate_total_cost(product, count)} dollars"
            )
            for product, count in products.items()
        )
        total_cost = sum(
            [
                count * self.products.get(product)
                for product, count in products.items()
            ]
        )
        receipt = (
            "Date: {}\n"
            "Thanks, {}, for your purchase!\n"
            "You have bought:\n"
            "{}\n"
            "Total cost is {} dollars\n"
            "See you again!\n"
        ).format(
            current_date.strftime("%d/%m/%Y %H:%M:%S"),
            name,
            string_of_products,
            total_cost
        )

        return receipt, total_cost
