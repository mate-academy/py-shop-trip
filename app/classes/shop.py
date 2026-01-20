import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(
            self,
            customer_name: str,
            customer_cart: dict
    ) -> str:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = (
            f"Date: {date}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought:\n"
        )
        total_sum = 0

        for product, amount in customer_cart.items():
            if product in self.products:
                cost = amount * self.products[product]
                if cost == int(cost):
                    cost = int(cost)
                total_sum += cost
                receipt += f"{amount} {product + 's'} for {cost} dollars\n"

        receipt += (
            f"Total cost is {total_sum} dollars\n"
            "See you again!"
        )
        return receipt
