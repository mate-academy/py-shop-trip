import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def receipt(self, customer: object) -> str:
        date = datetime.datetime.now()
        receipt = (f"\nDate: {date.strftime('%d/%m/%Y %H:%M:%S')}"
                   f"\nThanks, {customer.name}, for your purchase!"
                   f"\nYou have bought: \n")

        total_cost = 0
        for product in customer.products_cart:
            price_of_products = (
                customer.products_cart[product]
                * self.products[product]
            )
            total_cost += price_of_products

            receipt += (f"{customer.products_cart[product]} {product}s for "
                        f"{price_of_products} dollars\n")

        receipt += (f"Total cost is {total_cost} dollars"
                    f"\nSee you again!\n")

        return receipt
