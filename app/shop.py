from dataclasses import dataclass


class Customer:
    pass


@dataclass
class Shop:
    name: str
    location: tuple
    products: dict

    def __hash__(self) -> int:
        return hash(self.name)

    def calculate_price(self, customer: Customer,
                        do_print: bool = False) -> float:
        bill = 0
        for product in customer.product_cart:
            price = self.products[product]
            amount = customer.product_cart[product]
            cost = price * amount
            bill += cost
            if do_print:
                print(
                    f"{amount} {product}{'s' if amount > 1 else ''} for "
                    f"{int(cost) if int(cost) == cost else round(cost, 2)}"
                    f" dollars"
                )
        return bill

    def buy_products(self, customer: Customer) -> float:
        from datetime import datetime

        purchase_time = datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S")
        print(f"{purchase_time}")

        print(f"Thanks, {customer.name}, "
              f"for your purchase!\nYou have bought: ")

        bill = self.calculate_price(customer, do_print=True)

        print(f"Total cost is {round(bill, 2)} dollars\nSee you again!\n")
        return bill
